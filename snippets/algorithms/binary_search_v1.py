#!/usr/bin/env python3
"""
二分查找 (Binary Search)

在有序数组中查找目标值，每次将搜索范围缩小一半。
时间复杂度: O(log n), 空间复杂度: O(1)

前提条件：
输入数组必须是已排序的。
"""

from typing import List, Optional


def binary_search(arr: List[int], target: int) -> Optional[int]:
    """
    在有序数组中查找目标值。

    Args:
        arr: 已排序的整数列表（升序）
        target: 要查找的目标值

    Returns:
        目标值的索引，未找到返回 None
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # 防止整数溢出

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return None


if __name__ == "__main__":
    sorted_data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    print(f"数组: {sorted_data}")
    print(f"查找 7: 索引 {binary_search(sorted_data, 7)}")
    print(f"查找 10: {binary_search(sorted_data, 10)}")
    print(f"查找 1: 索引 {binary_search(sorted_data, 1)}")
    print(f"查找 19: 索引 {binary_search(sorted_data, 19)}")
