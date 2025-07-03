---
title_rus: Максимальная последовательность единиц
difficulty: Easy
leetcode_url: https://leetcode.com/problems/max-consecutive-ones/
topics:
- Array
time: O(n)
space: O(1)
grind75: false
tags:
- Array
- Easy
- problem
---
## Решение

```python
from typing import List  
  
  
class Solution:  
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:  
        max_count = 0  
        count = 0  
  
        for num in nums:  
            if num == 1:  
                count += 1  
                max_count = max(max_count, count)  
            else:  
                count = 0  
  
        return max_count
```

> [!INFO]  
> **🇷🇺 Название:** Максимальная последовательность единиц  
> **LeetCode:** [max-consecutive-ones](https://leetcode.com/problems/max-consecutive-ones/)  
> **Временная сложность:** O(n)  
> **Пространственная сложность:** O(1)  



## 🇺🇸 Условие

Given a binary array `nums`, return _the maximum number of consecutive_ `1`_'s in the array_.

## 🇷🇺 Условие

<!-- Место для вставки перевода на русском языке -->

## Примеры

**Example 1:**

**Input:** nums = [1,1,0,1,1,1]  
**Output:** 3  
**Explanation:** The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.  

**Example 2:**

**Input:** nums = [1,0,1,1,0,1]  
**Output:** 2  

```json
{
  "examples": [
    {
      "input": {
        "nums": [1,1,0,1,1,1]
      },
      "output": 3
    },
    {
      "input": {
        "nums": [1,0,1,1,0,1]
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

- Проход по массиву выполняется один раз.
- На каждом шаге — фиксированное число операций.

**Итог:** `O(n)`

### 🧠 Space complexity: `O(1)`

- Используются только две переменные-счётчика (`count` и `max_count`).
- Нет дополнительных структур данных.

**Итог:** `O(1)`

#easy #array
