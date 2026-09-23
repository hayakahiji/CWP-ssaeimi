#!/usr/bin/env python3
from checkmate import checkmate
from sys import argv
def main():
    for filename in argv[1:]:
        try:
            with open(filename, "r") as file:
                board = file.read()

            checkmate(board)

        except (FileNotFoundError, IndexError):
            return
if __name__ == "__main__":
    main()