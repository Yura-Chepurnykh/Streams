#!/usr/bin/env python3

from sln import bottom_up

import sys

def main():
    if (len(sys.argv) != 3):
        print("Error: Usage <lcs> <string #1> <string #2>", file = sys.stderr)
        return 1

    lcs : str = bottom_up(sys.argv[1], sys.argv[2])

    print(f"lcs: {lcs}, length: {len(lcs)}")

    return 0

if __name__ == "__main__":
    sys.exit(main())
