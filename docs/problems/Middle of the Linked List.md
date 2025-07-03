---
title_rus: Середина связанного списка
difficulty: Easy
leetcode_url: https://leetcode.com/problems/middle-of-the-linked-list/
topics:
- Linked List
- Two Pointers
time: O(n)
space: O(1)
grind75: true
tags:
- Easy
- Linked List
- Two Pointers
- problem
---

> [!INFO]  
> **🇷🇺 Название:** Середина связанного списка  
> **LeetCode:** [middle-of-the-linked-list](https://leetcode.com/problems/middle-of-the-linked-list/)  
> **Временная сложность:** O(n)  
> **Пространственная сложность:** O(1)  

## Решение

```python
# Definition for singly-linked list.  
# class ListNode:  
#     def __init__(self, val=0, next=None):  
#         self.val = val  
#         self.next = next  
from typing import Optional  
  
  
class Solution:  
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:  
        slow_pointer = head  
        fast_pointer = head  
  
        while fast_pointer is not None and fast_pointer.next is not None:  
            slow_pointer = slow_pointer.next  
            fast_pointer = fast_pointer.next.next  
  
        return slow_pointer
```

## 🇺🇸 Условие

Given the `head` of a singly linked list, return _the middle node of the linked list_.

If there are two middle nodes, return **the second middle** node.

## 🇷🇺 Условие

<!-- Место для вставки перевода на русском языке -->

## Примеры

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/07/23/lc-midlist1.jpg)

**Input:** head = [1,2,3,4,5]  
**Output:** [3,4,5]  
**Explanation:** The middle node of the list is node 3.  

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/07/23/lc-midlist2.jpg)

**Input:** head = [1,2,3,4,5,6]  
**Output:** [4,5,6]  
**Explanation:** Since the list has two middle nodes with values 3 and 4, we return the second one.

```json
{
  "examples": [
    {
      "input": {
        "head": [1,2,3,4,5]
      },
      "output": [3,4,5]
    },
    {
      "input": {
        "head": [1,2,3,4,5,6]
      },
      "output": [4,5,6]
    }
  ]
}
```

## Ограничения

- The number of nodes in the list is in the range `[1, 100]`.
- $1 \leq Node.val \leq 100$

## Потребление ресурсов
### ⏱ Time complexity: `O(n)`

- Один проход по списку двумя указателями.
- `fast_pointer` проходит по `n` элементам с шагом 2, `slow_pointer` — с шагом 1.

**Итог:** `O(n)`

### 🧠 Space complexity: `O(1)`

- Используются только два указателя (`slow_pointer`, `fast_pointer`), независимо от размера списка.

**Итог:** `O(1)`

#easy #linked-list #two-pointers
