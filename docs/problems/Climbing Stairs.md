---
title_rus: Поднимаясь по лестнице
difficulty: Easy
leetcode_url: https://leetcode.com/problems/climbing-stairs/
topics:
- Math
- Dynamic Programming
- Memoization
time: O(n)
space: O(1)
grind75: true
tags:
- Dynamic Programming
- Easy
- Math
- Memoization
- problem
---

> [!INFO]  
> **🇷🇺 Название:** Поднимаясь по лестнице  
> **LeetCode:** [climbing-stairs](https://leetcode.com/problems/climbing-stairs/)  
> **Временная сложность:** O(n)  
> **Пространственная сложность:** O(1)  

## Решение

```python
class Solution:  
    def climbStairs(self, n: int) -> int:  
        if n < 2:  
            return n  
  
        a, b = 1, 2  
        for _ in range(3, n + 1):  
            a, b = b, a + b  
        return b
```

## 🇺🇸 Условие

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

## 🇷🇺 Условие

<!-- Место для вставки перевода на русском языке -->

## Примеры

**Example 1:**

**Input:** n = 2  
**Output:** 2  
**Explanation:** There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

**Example 2:**

**Input:** n = 3  
**Output:** 3  
**Explanation:** There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

```json
{
  "examples": [
    {
      "input": {
        "n": 2
      },
      "output": 2
    },
    {
      "input": {
        "n": 3
      },
      "output": 3
    }
  ]
}
```

## Ограничения

- $1 \leq n \leq 45$

## Потребление ресурсов
### ⏱ Time complexity: `O(n)`

- Один цикл от `3` до `n` включительно.
- Каждая итерация — `O(1)`.

**Итог:** `O(n)`

### 🧠 Space complexity: `O(1)`

- Используются только две переменные (`a`, `b`) для хранения предыдущих значений.

**Итог:** `O(1)`

#easy #math #dynamic-programming #memoization
