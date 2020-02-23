#!/usr/bin/env python3

from face_compare import compare
from face_compare import compareDir
import sys
import os


def main():
    args = sys.argv
    if os.path.isdir(args[1]) == True and os.path.isfile(args[2]):
        compareDir(args[1], args[2])
    elif os.path.isdir(args[2]) == True and os.path.isfile(args[1]):
        compareDir(args[2], args[1])
    else:
        ValueError("No dir and file pair received!")


if __name__ == '__main__':
    main()
