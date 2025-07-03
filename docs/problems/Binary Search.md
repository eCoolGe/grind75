---
title_rus: Бинарный поиск
difficulty: Easy
leetcode_url: https://leetcode.com/problems/binary-search/
topics:
- Array
- Binary Search
time: O(log n)
space: O(1)
grind75: true
tags:
- Array
- Binary Search
- Easy
- problem
---
## Решение

```python
from typing import List


class Solution:  
    def search(self, nums: List[int], target: int) -> int:  
        left = 0  
        right = len(nums) - 1  
  
        while left <= right:  
            middle = left + (right - left) // 2  
  
            if target > nums[middle]:  
                left = middle + 1  
            elif target < nums[middle]:  
                right = middle - 1  
            else:  
                return middle  
        return -1
```

> [!INFO]  
> **🇷🇺 Название:** Бинарный поиск  
> **LeetCode:** [binary-search](https://leetcode.com/problems/binary-search/)  
> **Временная сложность:** O(log n)  
> **Пространственная сложность:** O(1)  



## 🇺🇸 Условие

Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.

You must write an algorithm with `O(log n)` runtime complexity.

## 🇷🇺 Условие

<!-- Место для вставки перевода на русском языке -->

## Примеры

**Example 1:**

**Input:** nums = [-1,0,3,5,9,12], target = 9  
**Output:** 4  
**Explanation:** 9 exists in nums and its index is 4

**Example 2:**

**Input:** nums = [-1,0,3,5,9,12], target = 2  
**Output:** -1  
**Explanation:** 2 does not exist in nums so return -1

```json
{
  "examples": [
    {
      "input": {
        "nums": [-1,0,3,5,9,12],
        "target": 9
      },
      "output": 4
    },
    {
      "input": {
        "nums": [-1,0,3,5,9,12],
        "target": 2
      },
      "output": -1
    }
  ]
}
```

## Ограничения

- $1 \leq nums.length \leq 10^4$
- $-10^4 < nums[i], target < 10^4$
- All the integers in `nums` are **unique**.
- `nums` is sorted in ascending order.

## Потребление ресурсов
### ⏱ Time complexity: `O(log n)`

- На каждом шаге диапазон поиска уменьшается в 2 раза.
- Всего будет максимум `log₂(n)` итераций.

**Итог:** `O(log n)`

### 🧠 Space complexity: `O(1)`

- Используются только 3 переменные: `left`, `right`, `middle`.
- Без рекурсии и дополнительных структур.

**Итог:** `O(1)`

#easy #array #binary-search
