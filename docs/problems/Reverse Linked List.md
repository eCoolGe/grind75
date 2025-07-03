---
title_rus: Обратный связанный список
difficulty: Easy
leetcode_url: https://leetcode.com/problems/reverse-linked-list/
topics:
- Linked List
- Recursion
time: O(n)
space: O(1)
grind75: true
tags:
- Easy
- Linked List
- Recursion
- problem
---
## Решение

```python
# Definition for singly-linked list.  
# class ListNode:  
#     def __init__(self, val=0, next=None):  
#         self.val = val  
#         self.next = next  
from typing import Optional  
  
  
class Solution:  
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:  
        node = None  
        prev = head  
  
        while prev:  
            next_node = prev.next  
            prev.next = node  
            node = prev  
            prev = next_node  
  
        return node
```

> [!INFO]  
> **🇷🇺 Название:** Обратный связанный список  
> **LeetCode:** [reverse-linked-list](https://leetcode.com/problems/reverse-linked-list/)  
> **Временная сложность:** O(n)  
> **Пространственная сложность:** O(1)  



## 🇺🇸 Условие

Given the `head` of a singly linked list, reverse the list, and return _the reversed list_.

## 🇷🇺 Условие

<!-- Место для вставки перевода на русском языке -->

## Примеры

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg)

**Input:** head = [1,2,3,4,5]  
**Output:** [5,4,3,2,1]  

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg)

**Input:** head = [1,2]  
**Output:** [2,1]  

**Example 3:**

**Input:** head = []  
**Output:** []  

```json
{
  "examples": [
    {
      "input": {
        "head": [1,2,3,4,5]
      },
      "output": [5,4,3,2,1]
    },
    {
      "input": {
        "head": [1,2]
      },
      "output": [2,1]
    },
    {
      "input": {
        "head": []
      },
      "output": []
    }
  ]
}
```

## Ограничения

- The number of nodes in the list is the range `[0, 5000]`.
- $-5000 \leq Node.val \leq 5000$

## Потребление ресурсов
### ⏱ Time complexity: `O(n)`

- Проходим по каждому узлу один раз.
- На каждом шаге выполняем фиксированное число операций.

**Итог:** `O(n)`

### 🧠 Space complexity: `O(1)`

- Используем только три дополнительных указателя: `node`, `prev`, `next_node`.
- Не используется стек или вспомогательные структуры.

**Итог:** `O(1)`

#easy #linked-list #recursion
