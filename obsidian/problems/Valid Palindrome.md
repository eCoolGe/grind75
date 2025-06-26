---
title_rus: Допустимый палиндром
difficulty: Easy
leetcode_url: https://leetcode.com/problems/valid-palindrome/
topics:
  - Two Pointers
  - String
time: O(n)
space: O(1)
grind75: true
tags:
  - problem
---

## Решение

```python
class Solution:  
    def isPalindrome(self, s: str) -> bool:  
        left = 0  
        right = len(s) - 1  
  
        while left < right:  
            while left < right and not s[left].isalnum():  
                left += 1  
            while left < right and not s[right].isalnum():  
                right -= 1  
            if s[left].lower() != s[right].lower():  
                return False  
            left += 1  
            right -= 1  
  
        return True
```

## 🇺🇸 Условие

A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` _if it is a **palindrome**, or_ `false` _otherwise_.

## 🇷🇺 Условие

<!-- Место для вставки перевода на русском языке -->

## Примеры

**Example 1:**

**Input:** s = "A man, a plan, a canal: Panama"  
**Output:** true  
**Explanation:** "amanaplanacanalpanama" is a palindrome.  

**Example 2:**

**Input:** s = "race a car"  
**Output:** false  
**Explanation:** "raceacar" is not a palindrome.  

**Example 3:**

**Input:** s = " "  
**Output:** true  
**Explanation:** s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

```json
{
  "examples": [
    {
      "input": {
        "s": "A man, a plan, a canal: Panama"
      },
      "output": true
    },
    {
      "input": {
        "s": "race a car"
      },
      "output": false
    },
    {
      "input": {
        "s": " "
      },
      "output": true
    }
  ]
}
```

## Ограничения

- $1 \leq s.length \leq 2 * 10^5$
- `s` consists only of printable ASCII characters.

## Потребление ресурсов
### ⏱ Time complexity: `O(n)`

- Указатели `left` и `right` проходят по строке максимум один раз каждый.
- Внутренние циклы пропускают символы, не двигая указатели назад.
- Суммарно каждый символ проверяется не более одного раза.

**Итог:** `O(n)`

### 🧠 Space complexity: `O(1)`

- Используются только несколько переменных-счётчиков (`left`, `right`).
- Нет дополнительной памяти, зависящей от размера входа.

**Итог:** `O(1)`

#easy #two-pointers #string
