---
title_rus: Проверка дерева бинарного поиска
difficulty: Medium
leetcode_url: https://leetcode.com/problems/validate-binary-search-tree/
topics:
- Tree
- Depth-First Search
- Binary Search Tree
- Binary Tree
time: O(n)
space: O(h)
grind75: true
tags:
- Binary Search Tree
- Binary Tree
- Depth-First Search
- Medium
- Tree
- problem
---
## Решение

```python
# Definition for a binary tree node.  
# class TreeNode:  
#     def __init__(self, val=0, left=None, right=None):  
#         self.val = val  
#         self.left = left  
#         self.right = right  
from typing import Optional  
  
  
class Solution:  
    def isValidBST(self, root: Optional[TreeNode]) -> bool:  
        def validate(node, low, high):  
            if not node:  
                return True  
            if not (low < node.val < high):  
                return False  
            return (validate(node.left, low, node.val) and  
                    validate(node.right, node.val, high))  
  
        return validate(root, float('-inf'), float('inf'))
```

> [!INFO]  
> **🇷🇺 Название:** Проверка дерева бинарного поиска  
> **LeetCode:** [validate-binary-search-tree](https://leetcode.com/problems/validate-binary-search-tree/)  
> **Временная сложность:** O(n)  
> **Пространственная сложность:** O(h)  



## 🇺🇸 Условие

Given the `root` of a binary tree, return _the length of the **diameter** of the tree_.

The **diameter** of a binary tree is the **length** of the longest path between any two nodes in a tree. This path may or may not pass through the `root`.

The **length** of a path between two nodes is represented by the number of edges between them.

## 🇷🇺 Условие

<!-- Место для вставки перевода на русском языке -->

## Примеры

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/06/diamtree.jpg)

**Input:** root = [1,2,3,4,5]  
**Output:** 3  
**Explanation:** 3 is the length of the path [4,2,1,3] or [5,2,1,3].  

**Example 2:**

**Input:** root = [1,2]  
**Output:** 1  

```json
{
  "examples": [
    {
      "input": {
        "root": [1,2,3,4,5]
      },
      "output": 3
    },
    {
      "input": {
        "root": [1,2]
      },
      "output": 1
    }
  ]
}
```

## Ограничения

- The number of nodes in the tree is in the range $[1, 10^4]$.
- $-2^{31} \leq Node.val \leq 2^{31} - 1$

## Потребление ресурсов
### ⏱ Time complexity: `O(n)`

- Каждый узел посещается **один раз**.
- На каждом шаге — одна проверка диапазона и два рекурсивных вызова.

**Итог:** `O(n)`

### 🧠 Space complexity: `O(h)`

- `h` — высота дерева:
    - `O(log n)` в среднем,
    - `O(n)` в худшем случае (вырожденное дерево).
- Используется стек вызовов рекурсии.

**Итог:** `O(h)`

#medium #tree #depth-first-search #binary-search-tree #binary-tree
