---
title_rus: Первая плохая версия
difficulty: Easy
leetcode_url: https://leetcode.com/problems/first-bad-version/
topics:
  - Binary Search
  - Interactive
time: O(log n)
space: O(1)
grind75: true
tags:
  - problem
---

## Решение

```python
# The isBadVersion API is already defined for you.  
# def isBadVersion(version: int) -> bool:  


class Solution:  
    def firstBadVersion(self, n: int) -> int:  
        first, last = 1, n  
  
        while first < last:  
            center = first + (last - first) // 2  
  
            if not isBadVersion(center):  
                first = center + 1  
            else:  
                last = center  
  
        return first
```

## 🇺🇸 Условие

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have `n` versions `[1, 2, ..., n]` and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API `bool isBadVersion(version)` which returns whether `version` is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

## 🇷🇺 Условие

<!-- Место для вставки перевода на русском языке -->

## Примеры

**Example 1:**

**Input:** n = 5, bad = 4  
**Output:** 4  
**Explanation:**  
call isBadVersion(3) -> false  
call isBadVersion(5) -> true  
call isBadVersion(4) -> true  
Then 4 is the first bad version.  

**Example 2:**

**Input:** n = 1, bad = 1  
**Output:** 1  

```json
{
  "examples": [
    {
      "input": {
        "n": 5,
        "bad": 4
      },
      "output": 4
    },
    {
      "input": {
        "n": 1,
        "bad": 1
      },
      "output": 1
    }
  ]
}
```

## Ограничения

- $1 \leq bad \leq n \leq 2^{31} - 1$

## Потребление ресурсов
### ⏱ Time complexity: `O(log n)`

- Алгоритм использует бинарный поиск по диапазону от 1 до n.
- На каждом шаге сокращает интервал вдвое.
- Максимум `log₂(n)` вызовов `isBadVersion`.

**Итог:** `O(log n)`

### 🧠 Space complexity: `O(1)`

- Используются только несколько переменных (`first`, `last`, `center`).
- Нет дополнительной памяти, зависящей от `n`.

**Итог:** `O(1)`

#easy #binary-search #interactive
