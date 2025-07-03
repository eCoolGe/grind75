---
title_rus: Диаметр бинарного дерева
difficulty: Easy
leetcode_url: https://leetcode.com/problems/diameter-of-binary-tree/
topics:
- Tree
- Depth-First Search
- Binary Tree
time: O(n)
space: O(h)
grind75: true
tags:
- Binary Tree
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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:  
        self.max_diameter = 0  
  
        def height(node):  
            if not node:  
                return 0  
            left = height(node.left)  
            right = height(node.right)  
            self.max_diameter = max(self.max_diameter, left + right)  
            return max(left, right) + 1  
  
        height(root)  
        return self.max_diameter
```

> [!INFO]  
> **🇷🇺 Название:** Диаметр бинарного дерева  
> **LeetCode:** [diameter-of-binary-tree](https://leetcode.com/problems/diameter-of-binary-tree/)  
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
- $-100 \leq Node.val \leq 100$

## Потребление ресурсов
### ⏱ Time complexity: `O(n)`

- Проходим по каждому узлу один раз.  
- На каждом шаге выполняем фиксированное число операций: вычисление высот, обновление максимума диаметра.

**Итог:** `O(n)`

### 🧠 Space complexity: `O(h)`

- Используется стек вызовов рекурсии глубиной `h` (высота дерева).  
- В худшем случае (вырожденное дерево) `h = n`, в среднем `h = log n`.

**Итог:** `O(h)`

#easy #tree #depth-first-search #binary-tree
