---
title_rus: Гниющие апельсины
difficulty: Medium
leetcode_url: https://leetcode.com/problems/rotting-oranges/
topics:
  - Array
  - Breadth-First Search
  - Matrix
time: O(n+m)
space: O(n+m)
grind75: true
tags:
  - problem
---

## Решение

```python
from typing import List  
from collections import deque  
  
  
class Solution:  
    def orangesRotting(self, grid: List[List[int]]) -> int:  
        rows, cols = len(grid), len(grid[0])  
        queue = deque()  
        fresh = 0  
  
        for r in range(rows):  
            for c in range(cols):  
                if grid[r][c] == 2:  
                    queue.append((r, c, 0))   
elif grid[r][c] == 1:  
                    fresh += 1  
  
        time = 0  
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
  
        while queue:  
            r, c, t = queue.popleft()  
            time = max(time, t)  
            for dr, dc in directions:  
                nr, nc = r + dr, c + dc  
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:  
                    grid[nr][nc] = 2  
                    fresh -= 1  
                    queue.append((nr, nc, t + 1))  
  
        return time if fresh == 0 else -1
```

## 🇺🇸 Условие

You are given an `m x n` `grid` where each cell can have one of three values:

- `0` representing an empty cell,
- `1` representing a fresh orange, or
- `2` representing a rotten orange.

Every minute, any fresh orange that is **4-directionally adjacent** to a rotten orange becomes rotten.

Return _the minimum number of minutes that must elapse until no cell has a fresh orange_. If _this is impossible, return_ `-1`.

## 🇷🇺 Условие

<!-- Место для вставки перевода на русском языке -->

## Примеры

**Example 1:**

![](https://assets.leetcode.com/uploads/2019/02/16/oranges.png)

**Input:** grid = [ [2,1,1],[1,1,0],[0,1,1] ]  
**Output:** 4  

**Example 2:**

**Input:** grid = [ [2,1,1],[0,1,1],[1,0,1] ]  
**Output:** -1  
**Explanation:** The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.  

**Example 3:**

**Input:** grid = [ [0,2] ]  
**Output:** 0  
**Explanation:** Since there are already no fresh oranges at minute 0, the answer is just 0.  

```json
{
  "examples": [
    {
      "input": {
        "grid": [
          [2,1,1],
          [1,1,0],
          [0,1,1]
        ]
      },
      "output": 4
    },
    {
      "input": {
        "grid": [
          [2,1,1],
          [0,1,1],
          [1,0,1]
        ]
      },
      "output": -1
    },
    {
      "input": {
        "grid": [
          [0,2]
        ]
      },
      "output": 0
    }
  ]
}
```

## Ограничения

- $m \equiv grid.length$
- $n \equiv grid[i].length$
- $1 \leq m, n \leq 10$
- `grid[i][j]` is `0`, `1`, or `2`.

## Потребление ресурсов
### ⏱ Time complexity: `O(n+m)`

- `m x n` — размер сетки
- Каждый апельсин обрабатывается максимум один раз

**Итог:** `O(n+m)`

### 🧠 Space complexity: `O(n+m)`

- Очередь может содержать до всех клеток
- Грид можно изменять на месте, не создавая копий

**Итог:** `O(n+m)`

#medium #array #breadth-first-search #matrix
