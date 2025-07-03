---
title_rus: Содержит дубликат
difficulty: Easy
leetcode_url: https://leetcode.com/problems/contains-duplicate/
topics:
- Array
- Hash Table
- Sorting
time: O(n)
space: O(n)
grind75: true
tags:
- Array
- Easy
- Hash Table
- Sorting
- problem
---

> [!INFO]  
> **🇷🇺 Название:** Содержит дубликат  
> **LeetCode:** [contains-duplicate](https://leetcode.com/problems/contains-duplicate/)  
> **Временная сложность:** O(n)  
> **Пространственная сложность:** O(n)  

## Решение

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
```

## 🇺🇸 Условие

Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

## 🇷🇺 Условие

<!-- Место для вставки перевода на русском языке -->

## Примеры

**Example 1:**

**Input:** nums = [1,2,3,1]  
**Output:** true  
**Explanation:** The element 1 occurs at the indices 0 and 3.

**Example 2:**

**Input:** nums = [1,2,3,4]  
**Output:** false  
**Explanation:** All elements are distinct.

**Example 3:**

**Input:** nums = [1,1,1,3,3,4,3,2,4,2]  
**Output:** true  

```json
{
  "examples": [
    {
      "input": {
        "nums": [1,2,3,1]
      },
      "output": true
    },
    {
      "input": {
        "nums": [1,2,3,4]
      },
      "output": false
    },
    {
      "input": {
        "nums": [1,1,1,3,3,4,3,2,4,2]
      },
      "output": true
    }
  ]
}
```

## Ограничения

- $1 \leq nums.length \leq 10^5$
- $-10^9 \leq nums[i] \leq 10^9$

## Потребление ресурсов
### ⏱ Time complexity: `O(n)`

- Создание множества из списка — `O(n)` по времени.
- Сравнение длин — `O(1)`.

**Итог:** `O(n)`

### 🧠 Space complexity: `O(n)`

- Множество хранит уникальные элементы — в худшем случае все элементы уникальны, значит память `O(n)`.

**Итог:** `O(n)`

#easy #array #hash-table #sorting
