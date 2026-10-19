def brute_force(str1 : str, str2 : str) -> str:
    s1 : int = len(str1) - 1
    s2 : int = len(str2) - 1
    result = brute_force_helper(str1, str2, s1, s2, True, "")
    return result[::-1]

def brute_force_helper(
    str1 : str,
    str2 : str,
    s1 : int,
    s2 : int,
    to_right : bool,
    indent : str
) -> str:

    # Pretty print / Debug
    print(indent + ("└── " if to_right else "├── ") +
        (str1[0:s1 + 1] if str1[0:s1 + 1] else "empty") + ", " +
        (str2[0:s2 + 1] if str2[0:s2 + 1] else "empty")
    )

    if s1 < 0 or s2 < 0:
        return ""

    if str1[s1] == str2[s2]:
        return str1[s1] + brute_force_helper(
            str1,
            str2,
            s1 - 1,
            s2 - 1,
            True,
            indent + ("    " if to_right else "│   ")
        )

    left : str = brute_force_helper(
        str1,
        str2,
        s1 - 1,
        s2,
        False,
        indent + ("    " if to_right else "│   ")
    )

    right : str = brute_force_helper(
        str1,
        str2,
        s1,
        s2 - 1,
        True,
        indent + ("    " if to_right else "│   ")
    )

    return max(left, right)

def bottom_up(str1 : str, str2 : str) -> str:
    return recover("#" + str1, "$" + str2, dp(str1, str2), len(str1), len(str2))

def recover(str1 : str, str2 : str, dp : list[list[int]], r : int, c : int) -> str:
    if r < 0 or r > len(str1) or c < 0 or c > len(str2):
        return ""

    if str1[r] == str2[c]:
        return recover(str1, str2, dp, r - 1, c - 1) + str1[r]

    if dp[r - 1][c] > dp[r][c - 1]:
        return recover(str1, str2, dp, r - 1, c)

    return recover(str1, str2, dp, r, c - 1)

def dp(str1 : str, str2 : str) -> list[list[int]]:
    expand1 : str = "#" + str1
    expand2 : str = "$" + str2

    rows : int = len(expand1)
    cols : int = len(expand2)

    dp : list[list[int]] = [[0] * cols for _ in range(rows)]

    for r in range(1, rows):
        for c in range(1, cols):
            if expand1[r] == expand2[c]:
                dp[r][c] = dp[r - 1][c - 1] + 1
            else:
                dp[r][c] = max(dp[r - 1][c], dp[r][c - 1])

    # debug
    #for r in range(rows):
    #    for c in range(cols):
    #        print(dp[r][c], end = " ")
    #    print()

    return dp
