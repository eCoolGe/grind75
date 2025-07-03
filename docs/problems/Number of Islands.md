---
title_rus: Количество островов
difficulty: Medium
leetcode_url: https://leetcode.com/problems/number-of-islands/
topics:
- Array
- Depth-First Search
- Breadth-First Search
- Union Find
- Matrix
time: O(n*m)
space: O(n*m)
grind75: true
tags:
- Array
- Breadth-First Search
- Depth-First Search
- Matrix
- Medium
- Union Find
- problem
---
## Решение

```python
from typing import List  
  
  
class Solution:  
    def numIslands(self, grid: List[List[str]]) -> int:  
        if not grid:  
            return 0  
  
        rows, cols = len(grid), len(grid[0])  
        count = 0  
  
        def dfs(r, c):  
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != '1':  
                return  
            grid[r][c] = '0'  
            dfs(r + 1, c)  
            dfs(r - 1, c)  
            dfs(r, c + 1)  
            dfs(r, c - 1)  
  
        for m in range(rows):  
            for n in range(cols):  
                if grid[m][n] == '1':  
                    dfs(m, n)  
                    count += 1  
  
        return count
```

> [!INFO]  
> **🇷🇺 Название:** Количество островов  
> **LeetCode:** [number-of-islands](https://leetcode.com/problems/number-of-islands/)  
> **Временная сложность:** O(n*m)  
> **Пространственная сложность:** O(n*m)  



## 🇺🇸 Условие

Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return _the number of islands_.

An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

## 🇷🇺 Условие

<!-- Место для вставки перевода на русском языке -->

## Примеры

**Example 1:**

**Input:** grid = [  
  ["1","1","1","1","0"],  
  ["1","1","0","1","0"],  
  ["1","1","0","0","0"],  
  ["0","0","0","0","0"]  
]  
**Output:** 1  

**Example 2:**

**Input:** grid = [  
  ["1","1","0","0","0"],  
  ["1","1","0","0","0"],  
  ["0","0","1","0","0"],  
  ["0","0","0","1","1"]  
]  
**Output:** 3  

```json
{
  "examples": [
    {
      "input": {
        "grid": [
          ["1","1","1","1","0"],
          ["1","1","0","1","0"],
          ["1","1","0","0","0"],
          ["0","0","0","0","0"]
        ]
      },
      "output": 1
    },
    {
      "input": {
        "grid": [
          ["1","1","0","0","0"],
          ["1","1","0","0","0"],
          ["0","0","1","0","0"],
          ["0","0","0","1","1"]
        ]
      },
      "output": 3
    }
  ]
}
```

## Ограничения

- `m == grid.length`
- `n == grid[i].length`
- $1 \leq m, n \leq 300$
- `grid[i][j]` is `'0'` or `'1'`.

## Потребление ресурсов
### ⏱ Time complexity: `O(n*m)`

- Каждая ячейка посещается **ровно один раз**

**Итог:** `O(n*m)`

### 🧠 Space complexity: `O(n*m)`

- В худшем случае (всё земля) стек рекурсии = `O(n * m)`

**Итог:** `O(n*m)`

#medium #array #depth-first-search #breadth-first-search #union-find #matrix
