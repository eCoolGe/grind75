---
title_rus: Цикл создания связанного списка
difficulty: Easy
leetcode_url: https://leetcode.com/problems/linked-list-cycle/
topics:
  - Hash Table
  - Linked List
  - Two Pointers
time: O(n)
space: O(1)
grind75: true
tags:
  - problem
---

## Решение

```python
# Definition for singly-linked list.  
# class ListNode:  
#     def __init__(self, x):  
#         self.val = x  
#         self.next = None  
from typing import Optional  
  
  
class Solution:  
    def hasCycle(self, head: Optional[ListNode]) -> bool:  
        fast = head  
        slow = head  
  
        while fast and fast.next:  
            fast = fast.next.next  
            slow = slow.next  
  
            if fast == slow:  
                return True  
  
        return False
```

## 🇺🇸 Условие

Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that `pos` is not passed as a parameter**.

Return `true` _if there is a cycle in the linked list_. Otherwise, return `false`.

## 🇷🇺 Условие

<!-- Место для вставки перевода на русском языке -->

## Примеры

**Example 1:**

![](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)

**Input:** head = [3,2,0,-4], pos = 1  
**Output:** true  
**Explanation:** There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

**Example 2:**

![](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png)

**Input:** head = [1,2], pos = 0  
**Output:** true  
**Explanation:** There is a cycle in the linked list, where the tail connects to the 0th node.

**Example 3:**

![](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png)

**Input:** head = [1], pos = -1  
**Output:** false  
**Explanation:** There is no cycle in the linked list.

```json
{
  "examples": [
    {
      "input": {
        "head": [3,2,0,-4],
        "pos": 1
      },
      "output": true
    },
    {
      "input": {
        "head": [1,2],
        "pos": 0
      },
      "output": true
    },
    {
      "input": {
        "head": [1],
        "pos": -1
      },
      "output": false
    }
  ]
}
```

## Ограничения

- The number of the nodes in the list is in the range $[0, 10^4]$.
- $-10^5 \leq Node.val \leq 10^5$
- `pos` is `-1` or a **valid index** in the linked-list.

## Потребление ресурсов
### ⏱ Time complexity: `O(n)`

- В худшем случае оба указателя (`slow`, `fast`) проходят по всем `n` узлам.
- Нет повторных обходов и вложенных циклов.

**Итог:** `O(n)`

### 🧠 Space complexity: `O(1)`

- Используются только два указателя, независимо от размера списка.

**Итог:** `O(1)`

#easy #hash-table #linked-list #two-pointers
