#!/usr/bin/python3
"""N-Queens Puzzle"""
import sys


def is_integer(value):
    """
    Check if a given value is an integer."""
    try:
        int(value)
        return True
    except ValueError:
        return False


def solve_nqueens(N):
    """Solve the N Queens problem and print solutions."""
    def is_safe(board, row, col):
        """Check if it's safe to place a queen at a
        specific position on the board."""
        for i in range(row):
            if board[i][1] == col or \
               board[i][1] - i == col - row or \
               board[i][1] + i == col + row:
                return False
        return True

    def place_queen(board, row):
        """Recursively place queens on the chessboard."""
        if row == N:
            print_solution(board)
            return
        for col in range(N):
            if is_safe(board, row, col):
                board[row] = [row, col]
                place_queen(board, row + 1)

    def print_solution(board):
        """Print the solution in the specified format."""
        print(board)

    if not is_integer(N):
        print("N must be a number")
        sys.exit(1)

    N = int(N)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[-1, -1] for _ in range(N)]

    place_queen(board, 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    solve_nqueens(sys.argv[1])
