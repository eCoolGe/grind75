---
title_rus: Вставить интервал
difficulty: Medium
leetcode_url: https://leetcode.com/problems/insert-interval/
topics:
- Array
time: O(n)
space: O(n)
grind75: true
tags:
- Array
- Medium
- problem
---

> [!INFO]  
> **🇷🇺 Название:** Вставить интервал  
> **LeetCode:** [insert-interval](https://leetcode.com/problems/insert-interval/)  
> **Временная сложность:** O(n)  
> **Пространственная сложность:** O(n)  

## Решение

```python
from typing import List  
  
class Solution:  
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:  
        result = []  
        i = 0
        n = len(intervals)  
  
        # Добавляем интервалы, не пересекающиеся и идущие до newInterval  
        while i < n and intervals[i][1] < newInterval[0]:  
            result.append(intervals[i])  
            i += 1  
  
        # Объединяем пересекающиеся интервалы  
        start, end = newInterval  
        while i < n and intervals[i][0] <= end:  
            start = min(start, intervals[i][0])  
            end = max(end, intervals[i][1])  
            i += 1  
        result.append([start, end])  
  
        # Добавляем оставшиеся интервалы  
        while i < n:  
            result.append(intervals[i])  
            i += 1  
  
        return result
```

## 🇺🇸 Условие

You are given an array of non-overlapping intervals `intervals` where `intervals[i] = [starti, endi]` represent the start and the end of the `ith` interval and `intervals` is sorted in ascending order by `starti`. You are also given an interval `newInterval = [start, end]` that represents the start and end of another interval.

Insert `newInterval` into `intervals` such that `intervals` is still sorted in ascending order by `starti` and `intervals` still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return `intervals` _after the insertion_.

**Note** that you don't need to modify `intervals` in-place. You can make a new array and return it.

## 🇷🇺 Условие

<!-- Место для вставки перевода на русском языке -->

## Примеры

**Example 1:**

**Input:** intervals = [ [1,3],[6,9] ], newInterval = [2,5]  
**Output:** [ [1,5],[6,9] ]  

**Example 2:**

**Input:** intervals = [ [1,2],[3,5],[6,7],[8,10],[12,16] ], newInterval = [4,8]  
**Output:** [ [1,2],[3,10],[12,16] ]  
**Explanation:** Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].  

```json
{
  "examples": [
    {
      "input": {
        "intervals": [
          [1,3],
          [6,9]
        ],
        "newInterval": [2,5]
      },
      "output": [
        [1,5],
        [6,9]
      ]
    },
    {
      "input": {
        "intervals": [
          [1,2],
          [3,5],
          [6,7],
          [8,10],
          [12,16]
        ],
        "newInterval": [4,8]
      },
      "output": [
        [1,2],
        [3,10],
        [12,16]
      ]
    }
  ]
}
```

## Ограничения

- $0 \leq intervals.length \leq 10^4$
- `intervals[i].length == 2`
- $0 \leq start_{i} \leq end_{i} \leq 10^5$
- `intervals` is sorted by $start_{i}$ in **ascending** order.
- `newInterval.length == 2`
- $0 \leq start \leq end \leq 10^5$

## Потребление ресурсов
### ⏱ Time complexity: `O(n)`

- Переменная `n` — длина списка `intervals`.
- Алгоритм проходит по списку **одним проходом** (с индексом `i` от 0 до `n`), каждый элемент рассматривается максимум один раз.
- Все операции внутри циклов — константные (сравнения, обновления переменных, добавление в результат).

**Итог:** `O(n)`

### 🧠 Space complexity: `O(n)`

- Используется список `result` для хранения результата.
- В худшем случае (когда `newInterval` не объединяется ни с каким интервалом) `result` содержит все `n+1` интервалов (включая вставляемый).
- Дополнительные переменные (`start`, `end`, счетчик `i`) занимают константное пространство.

**Итог:** `O(n)`

#medium #array
