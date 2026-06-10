#!/usr/bin/env python3
"""
二叉搜索树 - 三种遍历 (BST Traversal)

实现二叉搜索树的前序、中序、后序遍历。
- 前序遍历: 根 -> 左 -> 右
- 中序遍历: 左 -> 根 -> 右（对 BST 来说结果是升序的）
- 后序遍历: 左 -> 右 -> 根
"""

from typing import Optional, List


class TreeNode:
    """二叉树节点。"""

    def __init__(self, val: int):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None


def preorder(root: Optional[TreeNode]) -> List[int]:
    """前序遍历：根 -> 左 -> 右"""
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)


def inorder(root: Optional[TreeNode]) -> List[int]:
    """中序遍历：左 -> 根 -> 右"""
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


def postorder(root: Optional[TreeNode]) -> List[int]:
    """后序遍历：左 -> 右 -> 根"""
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]


if __name__ == "__main__":
    # 构建二叉树:
    #        4
    #       / \
    #      2   6
    #     / \ / \
    #    1  3 5  7
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)

    print(f"前序遍历: {preorder(root)}")
    print(f"中序遍历: {inorder(root)}")
    print(f"后序遍历: {postorder(root)}")
