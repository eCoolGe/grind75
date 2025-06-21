---
title_rus: Записка с требованием выкупа
difficulty: Easy
leetcode_url: https://leetcode.com/problems/ransom-note/
topics:
  - Hash Table
  - String
  - Counting
time: O(n + m)
space: O(1)
grind75: true
---

## Решение

```python
from collections import Counter  


class Solution:  
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:  
        r_count = Counter(ransomNote)  
        m_count = Counter(magazine)  
  
        for char in r_count:  
            if r_count[char] > m_count.get(char, 0):  
                return False  
        return True
```

## 🇺🇸 Условие

Given two strings `ransomNote` and `magazine`, return `true` _if_ `ransomNote` _can be constructed by using the letters from_ `magazine` _and_ `false` _otherwise_.

Each letter in `magazine` can only be used once in `ransomNote`.

## 🇷🇺 Условие

<!-- Место для вставки перевода на русском языке -->

## Примеры

**Example 1:**

**Input:** ransomNote = "a", magazine = "b"
**Output:** false

**Example 2:**

**Input:** ransomNote = "aa", magazine = "ab"
**Output:** false

**Example 3:**

**Input:** ransomNote = "aa", magazine = "aab"
**Output:** true

```json
{
  "examples": [
    {
      "input": {
        "ransomNote": "a",
        "magazine": "b"
      },
      "output": false
    },
    {
      "input": {
        "ransomNote": "aa",
        "magazine": "ab"
      },
      "output": false
    },
    {
      "input": {
        "ransomNote": "aa",
        "magazine": "aab"
      },
      "output": true
    }
  ]
}
```

## Ограничения

- $1 <= ransomNote.length, magazine.length <= 10^5$
- `ransomNote` and `magazine` consist of lowercase English letters.

## Потребление ресурсов
### ⏱ Time complexity: `O(n + m)`

- `Counter(ransomNote)` — `O(n)`, где `n = len(ransomNote)`
- `Counter(magazine)` — `O(m)`, где `m = len(magazine)`
- Проход по `r_count` — максимум `O(k)`, где `k` — число уникальных символов в `ransomNote` (в худшем случае `k = 26` для латиницы)

**Итог:** `O(n + m)`

### 🧠 Space complexity: `O(1)`

- `Counter` использует память пропорционально количеству уникальных символов.
- Для латиницы максимум 26 символов → считается `O(1)`
- Если допускать Unicode/большой алфавит → `O(k)`

**Итог:** `O(1)` при фиксированном алфавите, иначе `O(k)`

#easy #hash-table #string #counting
