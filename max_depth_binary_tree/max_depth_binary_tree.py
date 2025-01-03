# 問題: 二分木の最大深さの計算
# 問題文
# 二分木が与えられたとき、その木の最大深さ（ルートノードから最も深いリーフノードまでの距離）を計算する関数を実装してください。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth_with_recursive(root: TreeNode) -> int:
    """
    二分木の最大深さを計算する関数。

    Args:
    root (TreeNode): 二分木のルートノード

    Returns:
    int: 二分木の最大深さ
    """

    if root is None:
        return 0

    left_node = max_depth_with_recursive(root.left)
    right_node = max_depth_with_recursive(root.right)
    return max(left_node, right_node) + 1


def max_depth_with_bfs(root: TreeNode) -> int:
    """
    二分木の最大深さを計算する関数。

    Args:
    root (TreeNode): 二分木のルートノード

    Returns:
    int: 二分木の最大深さ
    """

    if root is None:
        return 0

    # キューを初期化し、スタート地点と距離0を格納
    queue = [root]
    depth = 0

    while queue:
        current_level = len(queue)
        for _ in range(current_level):
            node = queue.pop()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        depth += 1
    return depth


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print(max_depth_with_recursive(root))
    print(max_depth_with_bfs(root))
