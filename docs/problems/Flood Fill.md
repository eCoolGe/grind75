---
title_rus: Заливка потоком
difficulty: Easy
leetcode_url: https://leetcode.com/problems/flood-fill/
topics:
- Array
- Depth-First Search
- Breadth-First Search
- Matrix
time: O(n*m)
space: O(n*m)
grind75: true
tags:
- Array
- Breadth-First Search
- Depth-First Search
- Easy
- Matrix
- problem
---
## Решение

```python
from typing import List  
  
  
class Solution:  
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:  
        start_color = image[sr][sc]  
  
        if start_color == color:  
            return image  
  
        stack = [(sr, sc)]  
        rows, cols = len(image), len(image[0])  
  
        while stack:  
            r, c = stack.pop()  
            if (0 <= r < rows) and (0 <= c < cols) and image[r][c] == start_color:  
                image[r][c] = color  
                stack.append((r + 1, c))  
                stack.append((r - 1, c))  
                stack.append((r, c + 1))  
                stack.append((r, c - 1))  
  
        return image
```

> [!INFO]  
> **🇷🇺 Название:** Заливка потоком  
> **LeetCode:** [flood-fill](https://leetcode.com/problems/flood-fill/)  
> **Временная сложность:** O(n*m)  
> **Пространственная сложность:** O(n*m)  



## 🇺🇸 Условие

You are given an image represented by an `m x n` grid of integers `image`, where `image[i][j]` represents the pixel value of the image. You are also given three integers `sr`, `sc`, and `color`. Your task is to perform a **flood fill** on the image starting from the pixel `image[sr][sc]`.

To perform a **flood fill**:

1. Begin with the starting pixel and change its color to `color`.
2. Perform the same process for each pixel that is **directly adjacent** (pixels that share a side with the original pixel, either horizontally or vertically) and shares the **same color** as the starting pixel.
3. Keep **repeating** this process by checking neighboring pixels of the _updated_ pixels and modifying their color if it matches the original color of the starting pixel.
4. The process **stops** when there are **no more** adjacent pixels of the original color to update.

Return the **modified** image after performing the flood fill.

## 🇷🇺 Условие

<!-- Место для вставки перевода на русском языке -->

## Примеры

**Example 1:**

**Input:** image = [ [1,1,1],[1,1,0],[1,0,1] ], sr = 1, sc = 1, color = 2  
**Output:** [ [2,2,2],[2,2,0],[2,0,1] ]  
**Explanation:**
![](https://assets.leetcode.com/uploads/2021/06/01/flood1-grid.jpg)  
From the center of the image with position `(sr, sc) = (1, 1)` (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.  
Note the bottom corner is **not** colored 2, because it is not horizontally or vertically connected to the starting pixel.  

**Example 2:**

**Input:** image = [ [0,0,0],[0,0,0] ], sr = 0, sc = 0, color = 0  
**Output:** [ [0,0,0],[0,0,0] ]  
**Explanation:**  
The starting pixel is already colored with 0, which is the same as the target color. Therefore, no changes are made to the image.  

```json
{
  "examples": [
    {
      "input": {
        "image": [
          [1,1,1],
          [1,1,0],
          [1,0,1]
        ],
        "sr": 1,
        "sc": 1,
        "color": 2
      },
      "output": [
        [2,2,2],
        [2,2,0],
        [2,0,1]
      ]
    },
    {
      "input": {
        "image": [
          [0,0,0],
          [0,0,0]
        ],
        "sr": 0,
        "sc": 0,
        "color": 0
      },
      "output": [
        [0,0,0],
        [0,0,0]
      ]
    }
  ]
}
```

## Ограничения

- $m \equiv image.length$
- $n \equiv image[i].length$
- $1 \leq m, n \leq 50$
- $0 \leq image[i][j], color < 2^{16}$
- $0 \leq sr < m$
- $0 \leq sc < n$

## Потребление ресурсов
### ⏱ Time complexity: `O(n*m)`

- `n × m` — общее количество пикселей в изображении.
- Каждый пиксель обрабатывается **не более одного раза**.
- На каждом шаге:
    - Проверка координат — `O(1)`
    - Сравнение цвета — `O(1)`
    - Перезапись цвета — `O(1)`
    - Добавление до 4 соседей в стек — до 4 операций на пиксель

**Итог:** `O(n*m)`

### 🧠 Space complexity: `O(n*m)`

- Используем стек `stack`, в который могут попасть **все пиксели** (если вся область — одного цвета).
- Других вспомогательных структур нет.
- **Нет риска переполнения системного стека**, как в рекурсивном DFS.

**Итог:**
- **Худшее**: `O(n*m)` — если вся область заливается
- **Среднее/лучшее**: зависит от размеров связной области одного цвета

#easy #array #depth-first-search #breadth-first-search #matrix
