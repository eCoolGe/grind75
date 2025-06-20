---
title_rus: Лучшее время для покупки и продажи акций
difficulty: Easy
leetcode_url: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
topics:
  - Array
  - Dynamic Programming
time: O(n)
space: O(1)
grind75: true
---

## Решение

```python
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        profit = 0

        for price in prices[1:]:
            if buy_price > price:
                buy_price = price

            profit = max(profit, price - buy_price)

        return profit
```

## 🇺🇸 Условие

You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return _the maximum profit you can achieve from this transaction_. If you cannot achieve any profit, return `0`.

## 🇷🇺 Условие

<!-- Место для вставки перевода на русском языке -->

## Примеры

**Example 1:**

**Input:** prices = [7,1,5,3,6,4]
**Output:** 5
**Explanation:** Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

**Example 2:**

**Input:** prices = [7,6,4,3,1]
**Output:** 0
**Explanation:** In this case, no transactions are done and the max profit = 0.

```json
{
  "examples": [
    {
      "input": {
        "prices": [7,1,5,3,6,4]
      },
      "output": 5
    },
    {
      "input": {
        "prices": [7,6,4,3,1]
      },
      "output": 0
    }
  ]
}
```

## Ограничения

- `1 <= prices.length <= 105`
- `0 <= prices[i] <= 104`

## Потребление ресурсов
### ⏱ Time complexity: `O(n)`

- Один проход по `prices` длины `n`
- Все операции внутри цикла — `O(1)`
- Всего: `O(n)`

### 🧠 Space complexity: `O(1)`

- - Используются только 2 переменные (`buy_price`, `profit`)
- Память не зависит от входных данных
- **Итог**: `O(1)`

#easy #array #dynamic-programming
