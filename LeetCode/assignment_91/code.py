

# Use Brute-Force solution --> Too Long
def decode_ways(s):
    def generate_subsets(start, path):
        if start == len(s):  # when split all string s
            subsets.append(path[:])
            return

        for i in range(start + 1, len(s) + 1):
            # only keep partition has lenght < 2
            if i - start > 2:
                break
            path.append(s[start:i])
            generate_subsets(i, path)
            path.pop()

    subsets = []
    generate_subsets(0, [])

    valid_ways = 0
    valid_string = [str(i) for i in range(1, 27)]
    for ways in subsets:
        if set(ways).issubset(set(valid_string)):
            valid_ways += 1

    return valid_ways


# Use Dynamic-Programing
def decode_ways(s):
    if not s or s[0] == "0":
        return 0

    n = len(s)
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1  # setting base case

    for i in range(2, n + 1):
        one_digit = int(s[i - 1])
        two_digit = int(s[i - 2 : i])

        if 1 <= one_digit <= 9:
            dp[i] += dp[i - 1]

        if 10 <= two_digit <= 26:
            dp[i] += dp[i - 2]
    return dp[n]


s = "11106"
print(decode_ways(s))
