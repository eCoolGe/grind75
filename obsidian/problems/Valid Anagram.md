---
title_rus: Допустимая анаграмма
difficulty: Easy
leetcode_url: https://leetcode.com/problems/valid-anagram/
topics:
  - Hash Table
  - String
  - Sorting
time: O(n)
space: O(1)
grind75: true
---

## Решение

```python
class Solution:  
    def isAnagram(self, s: str, t: str) -> bool:  
        if len(s) != len(t):  
            return False  
  
        counts = [0] * 26  
        for c1, c2 in zip(s, t):  
            counts[ord(c1) - ord('a')] += 1  
            counts[ord(c2) - ord('a')] -= 1  
  
        return all(c == 0 for c in counts)
```

## 🇺🇸 Условие

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

## 🇷🇺 Условие

<!-- Место для вставки перевода на русском языке -->

## Примеры

**Example 1:**

**Input:** s = "anagram", t = "nagaram"

**Output:** true

**Example 2:**

**Input:** s = "rat", t = "car"

**Output:** false

```json
{
  "examples": [
    {
      "input": {
        "s": "anagram",
        "t": "nagaram"
      },
      "output": true
    },
    {
      "input": {
        "s": "rat",
        "t": "car"
      },
      "output": false
    }
  ]
}
```

## Ограничения

- $1 <= s.length, t.length <= 5 * 10^4$
- `s` and `t` consist of lowercase English letters.

## Потребление ресурсов
### ⏱ Time complexity: `O(n)`

- Один проход по каждой строке длины `n`, где считаются частоты символов.
- Сравнение двух счётчиков также занимает `O(n)` в худшем случае.

**Итог:** `O(n)`

### 🧠 Space complexity: `O(1)`

- Используется `Counter` или массив фиксированной длины (например, `counts[26]` для латиницы).
- Память не растёт с длиной строки, только зависит от количества уникальных символов.

**Итог:** `O(1)` (при фиксированном алфавите), иначе `O(k)`, где `k` — число уникальных символов.

#easy #hash-table #string #sorting
