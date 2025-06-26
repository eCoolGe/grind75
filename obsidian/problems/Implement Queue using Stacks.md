---
title_rus: Реализовать очередь с использованием стеков
difficulty: Easy
leetcode_url: https://leetcode.com/problems/implement-queue-using-stacks/
topics:
  - Stack
  - Design
  - Queue
time: O(1)
space: O(n)
grind75: true
tags:
  - problem
---

## Решение

```python
# Your MyQueue object will be instantiated and called as such:  
# obj = MyQueue()  
# obj.push(x)  
# param_2 = obj.pop()  
# param_3 = obj.peek()  
# param_4 = obj.empty()  
  
  
class MyQueue:  
    def __init__(self):  
        self.stack_in = []  
        self.stack_out = []  
  
    def push(self, x: int) -> None:  
        self.stack_in.append(x)  
  
    def pop(self) -> int:  
        self._shift()  
        return self.stack_out.pop()  
  
    def peek(self) -> int:  
        self._shift()  
        return self.stack_out[-1]  
  
    def empty(self) -> bool:  
        return not self.stack_in and not self.stack_out  
  
    def _shift(self):  
        if not self.stack_out:  
            while self.stack_in:  
                self.stack_out.append(self.stack_in.pop())
```

## 🇺🇸 Условие

Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (`push`, `peek`, `pop`, and `empty`).

Implement the `MyQueue` class:

- `void push(int x)` Pushes element x to the back of the queue.
- `int pop()` Removes the element from the front of the queue and returns it.
- `int peek()` Returns the element at the front of the queue.
- `boolean empty()` Returns `true` if the queue is empty, `false` otherwise.

**Notes:**

- You must use **only** standard operations of a stack, which means only `push to top`, `peek/pop from top`, `size`, and `is empty` operations are valid.
- Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

## 🇷🇺 Условие

<!-- Место для вставки перевода на русском языке -->

## Примеры

**Example 1:**

**Input:**  
["MyQueue", "push", "push", "peek", "pop", "empty"]  
[ [], [1], [2], [], [], [] ]  
**Output:**  
[null, null, null, 1, 1, false]  

**Explanation:**  
MyQueue myQueue = new MyQueue();  
myQueue.push(1); // queue is: [1]  
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)  
myQueue.peek(); // return 1  
myQueue.pop(); // return 1, queue is [2]  
myQueue.empty(); // return false  

```json
{
  "examples": [
    {
      "input": {
        "args": [
          ["MyQueue","push","push","peek","pop","empty"],
          [
            [],
            [1],
            [2],
            [],
            [],
            []
          ]
        ]
      },
      "output": [null,null,null,1,1,false]
    }
  ]
}
```

## Ограничения

- $1 \leq x \leq 9$
- At most `100` calls will be made to `push`, `pop`, `peek`, and `empty`.
- All the calls to `pop` and `peek` are valid.

## Потребление ресурсов
### ⏱ Time complexity: `O(1)`

|Операция|Сложность|Пояснение|
|---|---|---|
|`push(x)`|`O(1)`|обычный `append` в список|
|`pop()`|**`O(1)` амортизированное**|каждый элемент перемещается из `in` в `out` **только один раз**, поэтому суммарно `O(n)` на `n` операций → в среднем `O(1)`|
|`peek()`|`O(1)` амортизированное|та же логика, что и у `pop()`|
|`empty()`|`O(1)`|просто проверка списков|
- Допустим, мы делаем `n` операций `push`, а потом `n` раз вызываем `pop`.
- Только при первом `pop()` мы переносим все `n` элементов в `stack_out`.
- Остальные `pop()` идут из `stack_out`, уже без копирования.
- Перемещение стоит `O(n)`, но делается **один раз на `n` операций**. Средняя стоимость `1` на операцию.

**Итог:** `O(1)`

### 🧠 Space complexity: `O(n)`

- Все элементы хранятся в двух списках, максимум — `n` элементов одновременно.

**Итог:** `O(n)`

#easy #stack #design #queue
