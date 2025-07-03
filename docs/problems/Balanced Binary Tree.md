---
title_rus: Сбалансированное бинарное дерево
difficulty: Easy
leetcode_url: https://leetcode.com/problems/balanced-binary-tree/
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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:  
        return self.height(root) >= 0  
  
    def height(self, root):  
        if root is None:  
            return 0  
        left, right = self.height(root.left), self.height(root.right)  
        if left < 0 or right < 0 or abs(left - right) > 1:  
            return -1  
        return max(left, right) + 1
```

> [!INFO]  
> **🇷🇺 Название:** Сбалансированное бинарное дерево  
> **LeetCode:** [balanced-binary-tree](https://leetcode.com/problems/balanced-binary-tree/)  
> **Временная сложность:** O(n)  
> **Пространственная сложность:** O(h)  



## 🇺🇸 Условие

Given a binary tree, determine if it is **height-balanced**.

## 🇷🇺 Условие

<!-- Место для вставки перевода на русском языке -->

## Примеры

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/06/balance_1.jpg)

**Input:** root = [3,9,20,null,null,15,7]  
**Output:** true  

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/10/06/balance_2.jpg)

**Input:** root = [1,2,2,3,3,null,null,4,4]  
**Output:** false  

**Example 3:**

**Input:** root = []  
**Output:** true  

```json
{
  "examples": [
    {
      "input": {
        "root": [3,9,20,null,null,15,7]
      },
      "output": true
    },
    {
      "input": {
        "root": [1,2,2,3,3,null,null,4,4]
      },
      "output": false
    },
    {
      "input": {
        "root": []
      },
      "output": true
    }
  ]
}
```

## Ограничения

- The number of nodes in the tree is in the range `[0, 5000]`.
- $-10^4 \leq Node.val \leq 10^4$

## Потребление ресурсов
### ⏱ Time complexity: `O(n)`

- Каждый узел обходится **один раз**.
- Для каждого узла рекурсивно вычисляется высота левого и правого поддеревьев.
- Если хотя бы одно несбалансировано, прекращаем обход и возвращаем `-1`.

**Итог:** `O(n)`

### 🧠 Space complexity: `O(h)`

- Используется стек вызовов глубиной `h`, где:
	- `h = log n` для сбалансированного дерева,
	- `h = n` в худшем случае (деградированное дерево, например, список).

**Итог:** `O(h)`

#easy #tree #depth-first-search #binary-tree
