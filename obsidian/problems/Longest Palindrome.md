---
title_rus: Самый длинный палиндром
difficulty: Easy
leetcode_url: https://leetcode.com/problems/longest-palindrome/
topics:
  - Hash Table
  - String
  - Greedy
time: O(n)
space: O(1)
grind75: true
---

## Решение

```python
from collections import Counter  
  
  
class Solution:  
    def longestPalindrome(self, s: str) -> int:  
        values = Counter(s).values()  
        result = 0  
        has_odd = False  
  
        for value in values:  
            if value % 2 == 0:  
                result += value  
            else:  
                result += value - 1  
                has_odd = True  
  
        if has_odd:  
            return result + 1  
  
        return result
```

## 🇺🇸 Условие

Given a string `s` which consists of lowercase or uppercase letters, return the length of the **longest palindrome** that can be built with those letters.

Letters are **case sensitive**, for example, `"Aa"` is not considered a palindrome.

## 🇷🇺 Условие

<!-- Место для вставки перевода на русском языке -->

## Примеры

**Example 1:**

**Input:** s = "abccccdd"
**Output:** 7
**Explanation:** One longest palindrome that can be built is "dccaccd", whose length is 7.

**Example 2:**

**Input:** s = "a"
**Output:** 1
**Explanation:** The longest palindrome that can be built is "a", whose length is 1.

```json
{
  "examples": [
    {
      "input": {
        "s": "abccccdd"
      },
      "output": 7
    },
    {
      "input": {
        "s": "a"
      },
      "output": 1
    }
  ]
}
```

## Ограничения

- $1 \leq s.length \leq 2000$
- `s` consists of lowercase **and/or** uppercase English letters only.

## Потребление ресурсов
### ⏱ Time complexity: `O(n)`

- `Counter(s)` — один проход по строке `s` длины `n`.
- Проход по значениям счётчика — максимум количество уникальных символов, обычно значительно меньше `n`.
- Итог: линейное время `O(n)`.

**Итог:** `O(n)`

### 🧠 Space complexity: `O(1)`

- `Counter` хранит количество уникальных символов.
- При фиксированном наборе символов (например, латиница) — память константна.
- Иначе — `O(k)`, где `k` — число уникальных символов.

**Итог:** `O(1)` при фиксированном алфавите

#easy #hash-table #string #greedy
