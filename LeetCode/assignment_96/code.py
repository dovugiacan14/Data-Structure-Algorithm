

def unique_binary_tree(n):
    def generate_tree(start, end):
        if start > end:
            return [None]

        all_trees = []
        for i in range(start, end + 1):
            left_trees = generate_tree(start, i - 1)
            right_trees = generate_tree(i + 1, end)

            for left in left_trees:
                for right in right_trees:
                    root = TreeNode(i, left, right)
                    all_trees.append(root)
        return all_trees

    if n == 0:
        return 0
    return len(generate_tree(1, n))


def unique_binary_tree(n):
    """
    :type n: int
    :rtype: int
    """

    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1  # Với 0 hoặc 1 node thì chỉ có 1 cách tạo cây BST

    for nodes in range(2, n + 1):
        for root in range(1, nodes + 1):
            dp[nodes] += dp[root - 1] * dp[nodes - root]

    return dp[n]
