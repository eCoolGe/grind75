---
title_rus: Мажоритарный элемент
difficulty: Easy
leetcode_url: https://leetcode.com/problems/majority-element/
topics:
- Array
- Hash Table
- Divide and Conquer
- Sorting
- Counting
time: O(n)
space: O(1)
grind75: true
tags:
- Array
- Counting
- Divide and Conquer
- Easy
- Hash Table
- Sorting
- problem
---

> [!INFO]  
> **🇷🇺 Название:** Мажоритарный элемент  
> **LeetCode:** [majority-element](https://leetcode.com/problems/majority-element/)  
> **Временная сложность:** O(n)  
> **Пространственная сложность:** O(1)  

## Решение

```python
from typing import List  
  
  
class Solution:  
    def majorityElement(self, nums: List[int]) -> int:  
        count = 0  
        candidate = None  
  
        for num in nums:  
            if count == 0:  
                candidate = num  
            if num == candidate:  
                count += 1  
            else:  
                count -= 1
                
        return candidate
```

## 🇺🇸 Условие

Given an array `nums` of size `n`, return _the majority element_.

The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

## 🇷🇺 Условие

<!-- Место для вставки перевода на русском языке -->

## Примеры

**Example 1:**

**Input:** nums = [3,2,3]  
**Output:** 3  

**Example 2:**

**Input:** nums = [2,2,1,1,1,2,2]  
**Output:** 2  

```json
{
  "examples": [
    {
      "input": {
        "nums": [3,2,3]
      },
      "output": 3
    },
    {
      "input": {
        "nums": [2,2,1,1,1,2,2]
      },
      "output": 2
    }
  ]
}
```

## Ограничения

- `n == nums.length`
- $1 \leq n \leq 5 * 10^4$
- $-10^9 \leq nums[i] \leq 10^9$

## Потребление ресурсов
### ⏱ Time complexity: `O(n)`

- Используется **алгоритм Бойера–Мура (Boyer–Moore Voting Algorithm)**.
- Один проход по массиву `nums`, без вложенных циклов или сортировки.

**Итог:** `O(n)`

### 🧠 Space complexity: `O(1)`

- Алгоритм работает в **константной памяти**, без использования дополнительных структур данных.
- Только две переменные: `candidate` и `count`.

**Итог:** `O(1)`

#easy #array #hash-table #divide-and-conquer #sorting #counting
