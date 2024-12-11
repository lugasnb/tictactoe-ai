const boardDiv = document.getElementById("board");
const resetButton = document.getElementById("reset");
let gameOver = false;

function renderBoard(board) {
    boardDiv.innerHTML = "";
    board.forEach((cell, index) => {
        const cellDiv = document.createElement("div");
        cellDiv.textContent = cell;

        // Tambahkan warna sesuai isi sel
        if (cell === "X") {
            cellDiv.classList.add("X");
        } else if (cell === "O") {
            cellDiv.classList.add("O");
        }

        if (cell === " " && !gameOver) {
            cellDiv.addEventListener("click", () => makeMove(index));
        }
        boardDiv.appendChild(cellDiv);
    });
}

async function makeMove(position) {
    const response = await fetch("/make_move", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ position })
    });
    const data = await response.json();

    renderBoard(data.board);
    gameOver = data.game_over;

    if (data.game_over) {
        alert(data.winner ? `${data.winner} wins!` : "It's a draw!");
    }
}

async function resetGame() {
    const response = await fetch("/reset", { method: "POST" });
    const data = await response.json();
    gameOver = false;
    renderBoard(data.board);
}

// Jalankan reset saat halaman dimuat
resetGame();

// Tambahkan event listener pada tombol reset
resetButton.addEventListener("click", resetGame);
