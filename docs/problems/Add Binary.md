---
title_rus: Двоичное Сложение
difficulty: Easy
leetcode_url: https://leetcode.com/problems/add-binary/
topics:
- Math
- String
- Bit Manipulation
- Simulation
time: O(n)
space: O(n)
grind75: true
tags:
- Bit Manipulation
- Easy
- Math
- Simulation
- String
- problem
---
## Решение

```python
class Solution:  
    def addBinary(self, a: str, b: str) -> str:  
        return bin(int(a, 2) + int(b, 2))[2:]
```

> [!INFO]  
> **🇷🇺 Название:** Двоичное Сложение  
> **LeetCode:** [add-binary](https://leetcode.com/problems/add-binary/)  
> **Временная сложность:** O(n)  
> **Пространственная сложность:** O(n)  



## 🇺🇸 Условие

Given two binary strings `a` and `b`, return _their sum as a binary string_.

## 🇷🇺 Условие

<!-- Место для вставки перевода на русском языке -->

## Примеры

**Example 1:**

**Input:** a = "11", b = "1"  
**Output:** "100"  

**Example 2:**

**Input:** a = "1010", b = "1011"  
**Output:** "10101"  

```json
{
  "examples": [
    {
      "input": {
        "a": "11",
        "b": "1"
      },
      "output": "100"
    },
    {
      "input": {
        "a": "1010",
        "b": "1011"
      },
      "output": "10101"
    }
  ]
}
```

## Ограничения

- $1 \leq a.length, b.length \leq 10^4$
- `a` and `b` consist only of `'0'` or `'1'` characters.
- Each string does not contain leading zeros except for the zero itself.

## Потребление ресурсов
### ⏱ Time complexity: `O(n)`

- `int(a, 2)` и `int(b, 2)` — O(n), где `n` — длина строки.
- Сложение целых чисел — O(n), так как Python поддерживает произвольную длину.
- `bin(...)[2:]` — O(n) для преобразования обратно в строку.

**Итог:** `O(n)`, где `n = max(len(a), len(b))`

### 🧠 Space complexity: `O(n)`

- Память используется под числа и строки:
    - два `int`,
    - одна результирующая строка.
- Все — линейно по размеру входа.

**Итог:** `O(n)`

#easy #math #string #bit-manipulation #simulation
