---
title_rus: Порядок уровней прохождения бинарного дерева
difficulty: Medium
leetcode_url: https://leetcode.com/problems/binary-tree-level-order-traversal/
topics:
- Tree
- Breadth-First Search
- Binary Tree
time: O(n)
space: O(w)
grind75: true
tags:
- Binary Tree
- Breadth-First Search
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
from typing import Optional, List  
from collections import deque  


class Solution:  
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:  
        if not root:  
            return []  
  
        result = []  
        queue = deque([root])  
  
        while queue:  
            level = []  
            for _ in range(len(queue)):  
                node = queue.popleft()  
                level.append(node.val)  
                if node.left:  
                    queue.append(node.left)  
                if node.right:  
                    queue.append(node.right)  
            result.append(level)  
  
        return result
```

> [!INFO]  
> **🇷🇺 Название:** Порядок уровней прохождения бинарного дерева  
> **LeetCode:** [binary-tree-level-order-traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)  
> **Временная сложность:** O(n)  
> **Пространственная сложность:** O(w)  



## 🇺🇸 Условие

Given the `root` of a binary tree, return _the level order traversal of its nodes' values_. (i.e., from left to right, level by level).

## 🇷🇺 Условие

<!-- Место для вставки перевода на русском языке -->

## Примеры

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg)

**Input:** root = [3,9,20,null,null,15,7]  
**Output:** [ [3],[9,20],[15,7] ]  

**Example 2:**

**Input:** root = [1]  
**Output:** [ [1] ]  

**Example 3:**

**Input:** root = []  
**Output:** []  

```json
{
  "examples": [
    {
      "input": {
        "root": [3,9,20,null,null,15,7]
      },
      "output": [
        [3],
        [9,20],
        [15,7]
      ]
    },
    {
      "input": {
        "root": [1]
      },
      "output": [
        [1]
      ]
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

- The number of nodes in the tree is in the range `[0, 2000]`.
- $-1000 \leq Node.val \leq 1000$

## Потребление ресурсов
### ⏱ Time complexity: `O(n)`

- `n` — число всех узлов дерева
- Каждый узел:
    - добавляется в очередь один раз
    - извлекается из очереди один раз
    - добавляется в результат один раз

**Итог:** Все операции по узлам — константные, итого `O(n)`

### 🧠 Space complexity: `O(w)`

- `w` — максимальная ширина дерева (макс. число узлов на одном уровне)
- В очереди одновременно находятся только **узлы одного уровня + потомки**

**Итог:** в худшем случае, - если дерево «плоское» (широкое) `w ≈ n/2`, тогда `O(n)`

#medium #tree #breadth-first-search #binary-tree
