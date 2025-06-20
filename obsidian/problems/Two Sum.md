---
title_rus: Две суммы
difficulty: Easy
leetcode_url: https://leetcode.com/problems/two-sum/
topics:
  - Array
  - Hash Table
time: O(n)
space: O(n)
grind75: true
---

## Решение

```python
from typing import List


class Solution:  
    def twoSum(self, nums: List[int], target: int) -> List[int]:  
        pair = {}  
  
        for i, num in enumerate(nums):  
            if target - num in pair:  
                return[i, pair[target - num]]  
            pair[num] = i  
        return []
```

## 🇺🇸 Условие

Given an array of integers `nums` and an integer `target`, return _indices of the two numbers such that they add up to `target`_.

You may assume that each input would have **_exactly_ one solution**, and you may not use the _same_ element twice.

You can return the answer in any order.

## 🇷🇺 Условие

<!-- Место для вставки перевода на русском языке -->

## Примеры

**Example 1:**

**Input:** nums = [2,7,11,15], target = 9
**Output:** [0,1]
**Explanation:** Because nums[0] + nums[1] == 9, we return [0, 1].

**Example 2:**

**Input:** nums = [3,2,4], target = 6
**Output:** [1,2]

**Example 3:**

**Input:** nums = [3,3], target = 6
**Output:** [0,1]

```json
{
  "examples": [
    {
      "input": {
        "nums": [2,7,11,15],
        "target": 9
      },
      "output": [0,1]
    },
    {
      "input": {
        "nums": [3,2,4],
        "target": 6
      },
      "output": [1,2]
    },
    {
      "input": {
        "nums": [3,3],
        "target": 6
      },
      "output": [0,1]
    }
  ]
}
```

## Ограничения

- `2 <= nums.length <= 104`
- `-109 <= nums[i] <= 109`
- `-109 <= target <= 109`
- **Only one valid answer exists.**

## Потребление ресурсов
### ⏱ Time complexity: `O(n)`

- Один проход по списку `nums` (длина `n`)
- Каждая операция со словарём (поиск `in`, вставка) — `O(1)`

**Итог:** `O(n)`

### 🧠 Space complexity: `O(n)`

- В худшем случае в `pair` сохраняются все `n` чисел (если решение в конце или отсутствует)
- Дополнительная память зависит от размера `nums`

**Итог:** `O(n)`

#easy #array #hash-table
