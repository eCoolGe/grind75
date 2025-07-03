---
title_rus: Самый длинный подмассив из единиц после удаления одного элемента
difficulty: Medium
leetcode_url: https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
topics:
- Array
- Dynamic Programming
- Sliding Window
time: O(n)
space: O(1)
grind75: false
tags:
- Array
- Dynamic Programming
- Medium
- Sliding Window
- problem
---

> [!INFO]  
> **🇷🇺 Название:** Самый длинный подмассив из единиц после удаления одного элемента  
> **LeetCode:** [longest-subarray-of-1s-after-deleting-one-element](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/)  
> **Временная сложность:** O(n)  
> **Пространственная сложность:** O(1)  

## Решение

```python
from typing import List  
  
  
class Solution:  
    def longestSubarray(self, nums: List[int]) -> int:  
        left = 0  
        max_len = 0  
        zero_count = 0  
  
        for right in range(len(nums)):  
            if nums[right] == 0:  
                zero_count += 1  
  
            while zero_count > 1:  
                if nums[left] == 0:  
                    zero_count -= 1  
                left += 1  
  
            max_len = max(max_len, right - left)  
  
        return max_len
```

## 🇺🇸 Условие

Given a binary array `nums`, you should delete one element from it.

Return _the size of the longest non-empty subarray containing only_ `1`_'s in the resulting array_. Return `0` if there is no such subarray.

## 🇷🇺 Условие

<!-- Место для вставки перевода на русском языке -->

## Примеры

**Example 1:**

**Input:** nums = [1,1,0,1]  
**Output:** 3  
**Explanation:** After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.  

**Example 2:**

**Input:** nums = [0,1,1,1,0,1,1,0,1]  
**Output:** 5  
**Explanation:** After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].  

**Example 3:**

**Input:** nums = [1,1,1]  
**Output:** 2  
**Explanation:** You must delete one element.  

```json
{
  "examples": [
    {
      "input": {
        "nums": [1,1,0,1]
      },
      "output": 3
    },
    {
      "input": {
        "nums": [0,1,1,1,0,1,1,0,1]
      },
      "output": 5
    },
    {
      "input": {
        "nums": [1,1,1]
      },
      "output": 2
    }
  ]
}
```

## Ограничения

- $1 \leq nums.length \leq 10^5$
- `nums[i]` is either `0` or `1`.

## Потребление ресурсов
### ⏱ Time complexity: `O(n)`

- Проходим по массиву один раз указателем `right`.
- Указатель `left` сдвигается вперёд максимум столько же раз, сколько `right`.
- Все операции — константные на каждом шаге.

**Итог:** `O(n)`

### 🧠 Space complexity: `O(1)`

- Используется несколько счётчиков и указателей.
- Нет дополнительных структур данных.

**Итог:** `O(1)`

#medium #array #dynamic-programming #sliding-window
