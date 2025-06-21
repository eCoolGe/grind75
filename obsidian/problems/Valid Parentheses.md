---
title_rus: Допустимые скобки
difficulty: Easy
leetcode_url: https://leetcode.com/problems/valid-parentheses/
topics:
  - String
  - Stack
time: O(n)
space: O(n)
grind75: true
tags:
  - problem
---

## Решение

```python
class Solution:  
    def isValid(self, s: str) -> bool:  
        storage = []  
        valid = {  
            ")": "(",  
            "]": "[",  
            "}": "{",  
        }  
  
        for char in s:  
            if char in valid.values():  
                storage.append(char)  
            elif char in valid.keys():  
                if not storage or valid[char] != storage.pop():  
                    return False  
  
        return not storage
```

## 🇺🇸 Условие

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

## 🇷🇺 Условие

<!-- Место для вставки перевода на русском языке -->

## Примеры

**Example 1:**

**Input:** s = "()"
**Output:** true

**Example 2:**

**Input:** s = "()[]{}"
**Output:** true

**Example 3:**

**Input:** s = "(]"
**Output:** false

**Example 4:**

**Input:** s = "([])"
**Output:** true

```json
{
  "examples": [
    {
      "input": {
        "s": "()"
      },
      "output": true
    },
    {
      "input": {
        "s": "()[]{}"
      },
      "output": true
    },
    {
      "input": {
        "s": "(]"
      },
      "output": false
    },
    {
      "input": {
        "s": "([])"
      },
      "output": true
    }
  ]
}
```

## Ограничения

- $1 \leq s.length \leq 10^4$
- `s` consists of parentheses only `'()[]{}'`.

## Потребление ресурсов
### ⏱ Time complexity: `O(n)`

- `n` — длина строки `s`
- Один проход по строке: `for char in s` — `O(n)`
- Все операции со стеком (`append`, `pop`, `not`) — `O(1)`

**Итог:** `O(n)`

### 🧠 Space complexity: `O(n)`

- В худшем случае (все символы — открывающие скобки), стек `storage` будет содержать `n` элементов
- Словарь `valid` — постоянного размера `O(1)`

**Итог:** `O(n)`

#easy #string #stack
