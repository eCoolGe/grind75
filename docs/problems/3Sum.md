---
title_rus: Сумма 3
difficulty: Medium
leetcode_url: https://leetcode.com/problems/3sum/
topics:
- Array
- Two Pointers
- Sorting
time: O(n²)
space: O(1)
grind75: true
tags:
- Array
- Medium
- Sorting
- Two Pointers
- problem
---
## Решение

```python
from typing import List  
  
  
class Solution:  
    def threeSum(self, nums: List[int]) -> List[List[int]]:  
        result = []  
        nums.sort()  
  
        for i in range(len(nums)):  
            if i > 0 and nums[i] == nums[i - 1]:  
                continue  
  
            left = i + 1  
            right = len(nums) - 1  
  
            while left < right:  
                target = nums[i] + nums[left] + nums[right]  
  
                if target > 0:  
                    right -= 1  
                elif target < 0:  
                    left += 1  
                else:  
                    result.append([nums[i], nums[left], nums[right]])  
                    left += 1  
  
                    while nums[left] == nums[left - 1] and left < right:  
                        left += 1  
  
        return result
```

> [!INFO]  
> **🇷🇺 Название:** Сумма 3  
> **LeetCode:** [3sum](https://leetcode.com/problems/3sum/)  
> **Временная сложность:** O(n²)  
> **Пространственная сложность:** O(1)  



## 🇺🇸 Условие

Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

## 🇷🇺 Условие

<!-- Место для вставки перевода на русском языке -->

## Примеры

**Example 1:**

**Input:** nums = [-1,0,1,2,-1,-4]  
**Output:** [ [-1,-1,2],[-1,0,1] ]  
**Explanation:**   
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.  
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.  
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.  
The distinct triplets are [-1,0,1] and [-1,-1,2].  
Notice that the order of the output and the order of the triplets does not matter.  

**Example 2:**

**Input:** nums = [0,1,1]  
**Output:** []  
**Explanation:** The only possible triplet does not sum up to 0.  

**Example 3:**

**Input:** nums = [0,0,0]  
**Output:** [ [0,0,0] ]  
**Explanation:** The only possible triplet sums up to 0.  

```json
{
  "examples": [
    {
      "input": {
        "nums": [-1,0,1,2,-1,-4]
      },
      "output": [
        [-1,-1,2],
        [-1,0,1]
      ]
    },
    {
      "input": {
        "nums": [0,1,1]
      },
      "output": []
    },
    {
      "input": {
        "nums": [0,0,0]
      },
      "output": [
        [0,0,0]
      ]
    }
  ]
}
```

## Ограничения

- $3 \leq nums.length \leq 3000$
- $-10^5 \leq nums[i] \leq 10^5$

## Потребление ресурсов
### ⏱ Time complexity: `O(n²)`

- Сортировка: `O(n log n)`
- Основной цикл по `i`: `O(n)`
- Внутренний цикл с двумя указателями (`j`, `k`) — в сумме по всем `i`: **`O(n)`**

**Итог:** `O(n²)`

### 🧠 Space complexity: `O(1)`

- Не используем дополнительные структуры
- Храним только результат
- По стандарту анализа алгоритмов, **`res` не учитывается** (**анализ сложности** оценивает **дополнительную** память, которую использует алгоритм **поверх входных и выходных данных**)
- Если считать результат — память будет **`O(k)`**, где `k` — число найденных троек (в худшем `O(n²)`)

**Итог:** `O(1)`

#medium #array #two-pointers #sorting
