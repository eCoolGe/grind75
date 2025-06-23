---
title_rus: Объединить два отсортированных списка
difficulty: Easy
leetcode_url: https://leetcode.com/problems/merge-two-sorted-lists/
topics:
  - Linked List
  - Recursion
time: O(n + m)
space: O(1)
grind75: true
tags:
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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:  
        dummy = ListNode()  
        current = dummy  
  
        while list1 and list2:  
            if list1.val <= list2.val:  
                current.next = list1  
                list1 = list1.next  
            else:  
                current.next = list2  
                list2 = list2.next  
            current = current.next  
  
        current.next = list1 if list1 else list2  
  
        return dummy.next
```

## 🇺🇸 Условие

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one **sorted** list. The list should be made by splicing together the nodes of the first two lists.

Return _the head of the merged linked list_.

## 🇷🇺 Условие

<!-- Место для вставки перевода на русском языке -->

## Примеры

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg)

**Input:** list1 = [1,2,4], list2 = [1,3,4]
**Output:** [1,1,2,3,4,4]

**Example 2:**

**Input:** list1 = [], list2 = []
**Output:** []

**Example 3:**

**Input:** list1 = [], list2 = [0]
**Output:** [0]

```json
{
  "examples": [
    {
      "input": {
        "list1": [1,2,4],
        "list2": [1,3,4]
      },
      "output": [1,1,2,3,4,4]
    },
    {
      "input": {
        "list1": [],
        "list2": []
      },
      "output": []
    },
    {
      "input": {
        "list1": [],
        "list2": [0]
      },
      "output": [0]
    }
  ]
}
```

## Ограничения

- The number of nodes in both lists is in the range `[0, 50]`.
- $-100 \leq Node.val \leq 100$
- Both `list1` and `list2` are sorted in **non-decreasing** order.

## Потребление ресурсов
### ⏱ Time complexity: `O(n + m)`

- Алгоритм проходит по всем элементам обоих списков один раз.
- Сравнение и связывание узлов происходит за константное время на каждом шаге.
- Итоговое время пропорционально сумме длин списков.

**Итог:** `O(n + m)`

### 🧠 Space complexity: `O(1)`

- Рекурсивный вызов функции формирует стек глубиной до `m + n`, поэтому дополнительная память — `O(n + m)`.
- Итеративный вариант обходится константной памятью (указатели), то есть `O(1)`.

**Итог:** `O(1)`

#easy #linked-list #recursion
