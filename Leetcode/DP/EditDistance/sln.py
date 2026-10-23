def brute_force(source : str, destination : str) -> int:
    s_idx : int = len(source) - 1
    d_idx : int = len(destination) - 1
    return brute_force_helper(source, destination, s_idx, d_idx, True, "")

def brute_force_helper(
    source : str,
    destination : str,
    src_idx : int,
    dest_idx : int,
    is_last : bool,
    indent : str
) -> int:
    print(indent + ("└── " if is_last else "├── ") +
        (str(source[0:src_idx + 1]) if source[0:src_idx + 1] else "empty")  + ", " +
        (str(destination[0:dest_idx + 1] if destination[0:dest_idx + 1] else "empty")
    ))

    if src_idx < 0 or dest_idx < 0:
        return abs(src_idx - dest_idx)

    if source[src_idx] == destination[dest_idx]:
        return brute_force_helper(
            source,
            destination,
            src_idx - 1,
            dest_idx - 1,
            True,
            indent + ("    " if is_last else "│   ")
        )

    input_op : int = brute_force_helper(
        source,
        destination,
        src_idx - 1,
        dest_idx,
        False,
        indent + ("    " if is_last else "│   ")
    ) + 1

    delete_op : int = brute_force_helper(
        source,
        destination,
        src_idx,
        dest_idx - 1,
        False,
        indent + ("    " if is_last else "│   ")
    ) + 1

    replace_op : int = brute_force_helper(
        source,
        destination,
        src_idx - 1,
        dest_idx - 1,
        True,
        indent + ("    " if is_last else "│   ")
    ) + 1

    return min(input_op, delete_op, replace_op)

def bottom_up(source : str, destination : str) -> int:
    expanded_source : str = "#" + source
    expanded_destination : str = "$" + destination

    rows : int = len(expanded_source)
    cols : int = len(expanded_destination)

    dp : list[list[int]] = [[0] * cols for _ in range(rows)]

    # base cases
    for c in range(cols):
        dp[0][c] = c

    for r in range(rows):
        dp[r][0] = r

    for r in range(1, rows):
        for c in range(1, cols):
            if expanded_source[r] == expanded_destination[c]:
                dp[r][c] = dp[r - 1][c - 1]
            else:
                dp[r][c] = min(dp[r - 1][c - 1], dp[r - 1][c], dp[r][c - 1]) + 1

    # debug
    for r in range(rows):
        for c in range(cols):
            print(dp[r][c], end = "")
        print()

    return dp[rows - 1][cols - 1]

def space_optimized_bottom_up(source : str, destination : str) -> int:
    expanded_source : str = "#" + source
    expanded_destination : str = "$" + destination

    rows : int = len(expanded_source)
    cols : int = len(expanded_destination)

    dp : list[int] = [0] * cols

    # base cases
    for c in range(cols):
        dp[c] = c

    for r in range(1, rows):
        prev_prev : int = r

        for c in range(1, cols):
            prev : int = dp[c]
            if expanded_source[r] == expanded_destination[c]:
                dp[c] = dp[c - 1]
            else:
                dp[c] = min(dp[c - 1], dp[c], prev_prev) + 1

            prev_prev = prev

    return dp[cols - 1]

def top_down(source : str, destination : str) -> int:
    expanded_source : str = "#" + source
    expanded_destination : str = "$" + destination

    rows : int = len(expanded_source)
    cols : int = len(expanded_destination)

    arr : list[list[int]] = [[-1] * cols for _ in range(rows)]

    # base cases
    for c in range(cols):
        arr[0][c] = c

    for r in range(rows):
        arr[r][0] = r

    return top_down_helper(expanded_source, expanded_destination, arr, rows - 1, cols - 1)

def top_down_helper(source : str, destination : str, arr : list[list[int]], src_idx : int, dest_idx : int) -> int:
    if src_idx < 0 or dest_idx < 0:
        return abs(src_idx - dest_idx)

    if arr[src_idx][dest_idx] != -1:
        return arr[src_idx][dest_idx]

    if source[src_idx] == destination[dest_idx]:
        return top_down_helper(source, destination, arr, src_idx - 1, dest_idx - 1)

    arr[src_idx][dest_idx] = min(
        top_down_helper(source, destination, arr, src_idx - 1, dest_idx - 1),
        top_down_helper(source, destination, arr, src_idx - 1, dest_idx),
        top_down_helper(source, destination, arr, src_idx, dest_idx - 1),
    ) + 1

    return  arr[src_idx][dest_idx]
