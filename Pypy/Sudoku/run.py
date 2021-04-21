#!/usr/bin/python3

import os
import pathlib

def main():
    a = 'Sudoku.py'
    path = pathlib.Path(__file__).parent.absolute()
    a = str(path)+'/'+a
    os.system('echo "running scripts... program launced."; time python3 {}'.format(a))


if __name__ == "__main__":
    main();
