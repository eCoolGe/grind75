---
title_rus: Максимальный подмассив
difficulty: Medium
leetcode_url: https://leetcode.com/problems/maximum-subarray/
topics:
- Array
- Divide and Conquer
- Dynamic Programming
time: O(n)
space: O(1)
grind75: true
tags:
- Array
- Divide and Conquer
- Dynamic Programming
- Medium
- problem
---
## Решение

```python
from typing import List  
  
  
class Solution:  
    def maxSubArray(self, nums: List[int]) -> int:  
        max_sub = cur_sub = nums[0]  
  
        for num in nums[1:]:  
            cur_sub = max(num, cur_sub + num)  
            max_sub = max(max_sub, cur_sub)  
  
        return max_sub
```

> [!INFO]  
> **🇷🇺 Название:** Максимальный подмассив  
> **LeetCode:** [maximum-subarray](https://leetcode.com/problems/maximum-subarray/)  
> **Временная сложность:** O(n)  
> **Пространственная сложность:** O(1)  



## 🇺🇸 Условие

Given an integer array `nums`, find the subarray with the largest sum, and return _its sum_.

## 🇷🇺 Условие

<!-- Место для вставки перевода на русском языке -->

## Примеры

**Example 1:**

**Input:** nums = [-2,1,-3,4,-1,2,1,-5,4]  
**Output:** 6  
**Explanation:** The subarray [4,-1,2,1] has the largest sum 6.  

**Example 2:**

**Input:** nums = [1]  
**Output:** 1  
**Explanation:** The subarray [1] has the largest sum 1.  

**Example 3:**

**Input:** nums = [5,4,-1,7,8]  
**Output:** 23  
**Explanation:** The subarray [5,4,-1,7,8] has the largest sum 23.  

```json
{
  "examples": [
    {
      "input": {
        "nums": [-2,1,-3,4,-1,2,1,-5,4]
      },
      "output": 6
    },
    {
      "input": {
        "nums": [1]
      },
      "output": 1
    },
    {
      "input": {
        "nums": [5,4,-1,7,8]
      },
      "output": 23
    }
  ]
}
```

## Ограничения

- $1 \leq nums.length \leq 10^5$
- $-10^4 \leq nums[i] \leq 10^4$

## Потребление ресурсов
### ⏱ Time complexity: `O(n)`

- Используется **алгоритм Кадане (Kadane’s Algorithm)**.
- Проходим по каждому элементу массива один раз.  
- На каждой итерации выполняем фиксированное число операций (`max`, сложение, присваивание).

**Итог:** `O(n)`

### 🧠 Space complexity: `O(1)`

- Используем только две переменные: `cur_sub` и `max_sub`.  
- Не используется дополнительная память, стек или вспомогательные структуры.

**Итог:** `O(1)`

#medium #array #divide-and-conquer #dynamic-programming
