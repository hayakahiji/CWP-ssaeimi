#!/usr/bin/env python3
from checkmate import checkmate
from sys import argv
def main():
    try:
        with open(argv[1], "r") as file:
            board = file.read()

        checkmate(board)

    except (FileNotFoundError, IndexError):
        return
if __name__ == "__main__":
    main()