---
title_rus: Разменять монету
difficulty: Medium
leetcode_url: https://leetcode.com/problems/coin-change/
topics:
- Array
- Dynamic Programming
- Breadth-First Search
time: O(n*amount)
space: O(amount)
grind75: true
tags:
- Array
- Breadth-First Search
- Dynamic Programming
- Medium
- problem
---

> [!INFO]  
> **🇷🇺 Название:** Разменять монету  
> **LeetCode:** [coin-change](https://leetcode.com/problems/coin-change/)  
> **Временная сложность:** O(n*amount)  
> **Пространственная сложность:** O(amount)  

## Решение 

```python
from typing import List  
  
  
class Solution:  
    def coinChange(self, coins: List[int], amount: int) -> int:  
        variants = [float("inf")] * (amount + 1)  
        variants[0] = 0  
  
        for coin in coins:  
            for x in range(coin, amount + 1):  
                variants[x] = min(variants[x], variants[x - coin] + 1)  
  
        return variants[amount] if variants[amount] != float('inf') else -1
```

## 🇺🇸 Условие

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return _the fewest number of coins that you need to make up that amount_. If that amount of money cannot be made up by any combination of the coins, return `-1`.

You may assume that you have an infinite number of each kind of coin.

## 🇷🇺 Условие

<!-- Место для вставки перевода на русском языке -->

## Примеры

**Example 1:**

**Input:** coins = [1,2,5], amount = 11  
**Output:** 3  
**Explanation:** 11 = 5 + 5 + 1  

**Example 2:**

**Input:** coins = [2], amount = 3  
**Output:** -1  

**Example 3:**

**Input:** coins = [1], amount = 0  
**Output:** 0  

```json
{
  "examples": [
    {
      "input": {
        "coins": [1,2,5],
        "amount": 11
      },
      "output": 3
    },
    {
      "input": {
        "coins": [2],
        "amount": 3
      },
      "output": -1
    },
    {
      "input": {
        "coins": [1],
        "amount": 0
      },
      "output": 0
    }
  ]
}
```

## Ограничения

- $1 \leq coins.length \leq 12$
- $1 \leq coins[i] \leq 2^{31} - 1$
- $0 \leq amount \leq 10^4$

## Потребление ресурсов
### ⏱ Time complexity: `O(n*amount)`

- Внешний цикл по `coins` длины `n`
- Внутренний цикл по значениям `x = coin .. amount` — максимум `amount` итераций
- На каждой итерации выполняется `min(...)` — O(1)

**Итог:** `O(n*amount)`

### 🧠 Space complexity: `O(amount)`

- Используется один список `variants` длины `amount + 1`
- Дополнительная память не используется

**Итог:** `O(amount)`

#medium #array #dynamic-programming #breadth-first-search
