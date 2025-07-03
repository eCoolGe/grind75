---
title_rus: Максимальная глубина бинарного дерева
difficulty: Easy
leetcode_url: https://leetcode.com/problems/maximum-depth-of-binary-tree/
topics:
- Tree
- Depth-First Search
- Breadth-First Search
- Binary Tree
time: O(n)
space: O(h)
grind75: true
tags:
- Binary Tree
- Breadth-First Search
- Depth-First Search
- Easy
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:  
        if not root:  
            return 0  
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
```

> [!INFO]  
> **🇷🇺 Название:** Максимальная глубина бинарного дерева  
> **LeetCode:** [maximum-depth-of-binary-tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)  
> **Временная сложность:** O(n)  
> **Пространственная сложность:** O(h)  



## 🇺🇸 Условие

Given the `root` of a binary tree, return _its maximum depth_.

A binary tree's **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.

## 🇷🇺 Условие

<!-- Место для вставки перевода на русском языке -->

## Примеры

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/11/26/tmp-tree.jpg)

**Input:** root = [3,9,20,null,null,15,7]  
**Output:** 3  

**Example 2:**

**Input:** root = [1,null,2]  
**Output:** 2  

```json
{
  "examples": [
    {
      "input": {
        "root": [3,9,20,null,null,15,7]
      },
      "output": 3
    },
    {
      "input": {
        "root": [1,null,2]
      },
      "output": 2
    }
  ]
}
```

## Ограничения

- The number of nodes in the tree is in the range `[0, 104]`.
- $-100 \leq Node.val \leq 100$

## Потребление ресурсов
### ⏱ Time complexity: `O(n)`

- Нужно обойти **все** `n` узлов (каждый только один раз).
- Рекурсивно вызывается `maxDepth` для каждого поддерева.

**Итог:** `O(n)`

### 🧠 Space complexity: `O(h)`

- Используется **стек вызовов рекурсии**, глубина которого равна `h` — высоте дерева.
- В худшем случае (вытянутое дерево) `h = n`, в лучшем (сбалансированное) `h = log n`.

**Итог:** `O(h)`, где `h ≤ n`

#easy #tree #depth-first-search #breadth-first-search #binary-tree
