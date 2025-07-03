---
title_rus: Самая длинная подстрока Без повторяющихся Символов
difficulty: Medium
leetcode_url: https://leetcode.com/problems/longest-substring-without-repeating-characters/
topics:
- Hash Table
- String
- Sliding Window
time: O(n)
space: O(k)
grind75: true
tags:
- Hash Table
- Medium
- Sliding Window
- String
- problem
---

> [!INFO]  
> **🇷🇺 Название:** Самая длинная подстрока Без повторяющихся Символов  
> **LeetCode:** [longest-substring-without-repeating-characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)  
> **Временная сложность:** O(n)  
> **Пространственная сложность:** O(k)  

## Решение

```python
class Solution:  
    def lengthOfLongestSubstring(self, s: str) -> int:  
        last_index = {}  
        left = max_length = 0  
  
        for right, char in enumerate(s):  
            if char in last_index and last_index[char] >= left:  
                left = last_index[char] + 1  
  
            last_index[char] = right  
            max_length = max(max_length, right - left + 1)  
  
        return max_length
```

## 🇺🇸 Условие

Given a string `s`, find the length of the **longest** **substring** without duplicate characters.

## 🇷🇺 Условие

<!-- Место для вставки перевода на русском языке -->

## Примеры

**Example 1:**

**Input:** s = "abcabcbb"  
**Output:** 3  
**Explanation:** The answer is "abc", with the length of 3.

**Example 2:**

**Input:** s = "bbbbb"  
**Output:** 1  
**Explanation:** The answer is "b", with the length of 1.

**Example 3:**

**Input:** s = "pwwkew"  
**Output:** 3  
**Explanation:** The answer is "wke", with the length of 3.  
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

```json
{
  "examples": [
    {
      "input": {
        "s": "abcabcbb"
      },
      "output": 3
    },
    {
      "input": {
        "s": "bbbbb"
      },
      "output": 1
    },
    {
      "input": {
        "s": "pwwkew"
      },
      "output": 3
    }
  ]
}
```

## Ограничения

- $0 \leq s.length \leq 5 * 10^4$
- `s` consists of English letters, digits, symbols and spaces.

## Потребление ресурсов
### ⏱ Time complexity: `O(n)`

- Переменная `right` движется от начала строки до конца — всего `n` итераций.
- `left` сдвигается только вперёд и никогда не двигается назад.  
    Даже если символ повторяется, переход выполняется за один шаг (через индекс в `last_index`).
- Все операции над хэш-таблицей `last_index` выполняются за **амортизированное `O(1)`** (вставка, проверка, обновление по ключу).

**Итог:** `O(n)`

### 🧠 Space complexity: `O(k)`

- Используется хэш-таблица `last_index` для хранения **последней позиции каждого уникального символа**.
- В худшем случае, когда все символы строки уникальны, таблица хранит `k = n` записей.

**Итог:** `O(min(n, a))`, где:
- `n` — длина строки,
- `a` — размер алфавита (обычно `128` для ASCII, `256` для extended ASCII или до $2^{21}$ для Unicode).

#medium #hash-table #string #sliding-window
