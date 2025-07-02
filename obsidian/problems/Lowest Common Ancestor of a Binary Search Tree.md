---
title_rus: Наименьший общий предок дерева бинарного поиска
difficulty: Medium
leetcode_url: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
topics:
  - Tree
  - Depth-First Search
  - Binary Search Tree
  - Binary Tree
time: O(h)
space: O(1)
grind75: true
tags:
  - problem
---

## Решение

```python
# Definition for a binary tree node.  
# class TreeNode:  
#     def __init__(self, x):  
#         self.val = x  
#         self.left = None  
#         self.right = None  


class Solution:  
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':  
        small = min(p.val, q.val)  
        large = max(p.val, q.val)  
  
        while root:  
            if root.val > large:  
                root = root.left  
            elif root.val < small:  
                root = root.right  
            else:  
                return root  
        return None
```

## 🇺🇸 Условие

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the [definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor): “The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow **a node to be a descendant of itself**).”

## 🇷🇺 Условие

<!-- Место для вставки перевода на русском языке -->

## Примеры

**Example 1:**

![](https://assets.leetcode.com/uploads/2018/12/14/binarysearchtree_improved.png)

**Input:** root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8  
**Output:** 6  
**Explanation:** The LCA of nodes 2 and 8 is 6.  

**Example 2:**

![](https://assets.leetcode.com/uploads/2018/12/14/binarysearchtree_improved.png)

**Input:** root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4  
**Output:** 2  
**Explanation:** The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.  

**Example 3:**

**Input:** root = [2,1], p = 2, q = 1  
**Output:** 2  

```json
{
  "examples": [
    {
      "input": {
        "root": [6,2,8,0,4,7,9,null,null,3,5],
        "p": 2,
        "q": 8
      },
      "output": 6
    },
    {
      "input": {
        "root": [6,2,8,0,4,7,9,null,null,3,5],
        "p": 2,
        "q": 4
      },
      "output": 2
    },
    {
      "input": {
        "root": [2,1],
        "p": 2,
        "q": 1
      },
      "output": 2
    }
  ]
}
```

## Ограничения

- The number of nodes in the tree is in the range $[2, 10^5]$.
- $-10^9 \leq Node.val \leq 10^9$
- All `Node.val` are **unique**.
- `p != q`
- `p` and `q` will exist in the BST.

## Потребление ресурсов
### ⏱ Time complexity: `O(h)`

- В каждом шаге переходим либо влево, либо вправо — как в обычном поиске в BST.
- Этот алгоритм работает **только для BST (двоичного дерева поиска)**.
- `h` — высота дерева:
    - в среднем `O(log n)` (сбалансированное дерево),
    - в худшем `O(n)` (вырожденное дерево — список).

**Итог:** `O(h)`

### 🧠 Space complexity: `O(1)`

- Используется **только один указатель** `root`, меняющийся на месте.
- Нет рекурсии, нет стека, нет дополнительных структур.

**Итог:** `O(1)`

#medium #tree #depth-first-search #binary-search-tree #binary-tree
