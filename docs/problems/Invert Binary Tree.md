---
title_rus: Инвертировать двоичное дерево
difficulty: Easy
leetcode_url: https://leetcode.com/problems/invert-binary-tree/
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:  
        def swipe(node):  
            if not node:  
                return None  
            node.left, node.right = swipe(node.right), swipe(node.left)  
            return node  
  
        swipe(root)  
        return root
```

> [!INFO]  
> **🇷🇺 Название:** Инвертировать двоичное дерево  
> **LeetCode:** [invert-binary-tree](https://leetcode.com/problems/invert-binary-tree/)  
> **Временная сложность:** O(n)  
> **Пространственная сложность:** O(h)  



## 🇺🇸 Условие

Given the `root` of a binary tree, invert the tree, and return _its root_.

## 🇷🇺 Условие

<!-- Место для вставки перевода на русском языке -->

## Примеры

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/03/14/invert1-tree.jpg)

**Input:** root = [4,2,7,1,3,6,9]  
**Output:** [4,7,2,9,6,3,1]  

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/03/14/invert2-tree.jpg)

**Input:** root = [2,1,3]  
**Output:** [2,3,1]  

**Example 3:**

**Input:** root = []  
**Output:** []  

```json
{
  "examples": [
    {
      "input": {
        "root": [4,2,7,1,3,6,9]
      },
      "output": [4,7,2,9,6,3,1]
    },
    {
      "input": {
        "root": [2,1,3]
      },
      "output": [2,3,1]
    },
    {
      "input": {
        "root": []
      },
      "output": []
    }
  ]
}
```

## Ограничения

- The number of nodes in the tree is in the range `[0, 100]`.
- $-100 \leq Node.val \leq 100$

## Потребление ресурсов
### ⏱ Time complexity: `O(n)`

- Проходим каждый узел **ровно один раз**.
- Для каждого узла выполняется:
    - один вызов для левого поддерева,
    - один вызов для правого,
    - одна операция обмена (`swap`).
- Всего `n` узлов = `O(n)` операций.

**Итог:** `O(n)`

### 🧠 Space complexity: `O(h)`

- Используется **рекурсия**, которая занимает стек вызовов глубиной `h`, где:
	- `h = log n` для сбалансированного дерева,
	- `h = n` для деградировавшего в список дерева.

**Итог:** `O(h)`

#easy #tree #depth-first-search #breadth-first-search #binary-tree
