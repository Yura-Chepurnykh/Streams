#!/usr/bin/env python3

import sys
from sln import brute_force
from sln import bottom_up
from sln import space_optimized_bottom_up
from sln import top_down

def main() -> int:
    if len(sys.argv) != 3:
        print("Error: Usage <str1> <str2>", file = sys.stderr)
        return 1

    str1 : str = str(sys.argv[1])
    str2 : str = str(sys.argv[2])

    brute_force_sln : int = brute_force(str1, str2)
    print(f"brute force sln: {brute_force_sln}")

    btm_up : int = bottom_up(str1, str2)
    print(f"bottom up sln: {btm_up}")

    space_btm_up : int = space_optimized_bottom_up(str1, str2)
    print(f"space optimized bottom up sln: {space_btm_up}")

    top_down_sln : int = top_down(str1, str2)
    print(f"top down sln: {top_down_sln}")

    return 0

if __name__ == "__main__":
    sys.exit(main())
