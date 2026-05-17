# [1116. 打印零与奇偶数](https://leetcode.cn/problems/print-zero-even-odd/)

- 标签：多线程
- 难度：中等

## 题目链接

- [1116. 打印零与奇偶数 - 力扣](https://leetcode.cn/problems/print-zero-even-odd/)

## 题目大意

**描述**：三个不同的线程共用一个 `ZeroEvenOdd` 实例：
- 线程 A：调用 `zero()`，只输出 $0$。
- 线程 B：调用 `even()`，只输出偶数。
- 线程 C：调用 `odd()`，只输出奇数。

**要求**：修改程序，输出序列 `"010203040506..."`，序列长度为 $2n$（即 $n$ 组 `"0奇数0偶数..."`）。

**说明**：

- $1 \le n \le 10^3$。

**示例**：

- 示例 1：

```python
输入：n = 2
输出："0102"
```

- 示例 2：

```python
输入：n = 5
输出："0102030405"
```

## 解题思路

### 思路 1：信号量（Semaphore）

**打印顺序规律**：$0 \to \text{奇数} \to 0 \to \text{偶数} \to 0 \to \text{奇数} \to 0 \to \text{偶数} \to \dots$

对于 $n$ 来说，奇数的顺序是 $1, 3, 5, \dots$，偶数的顺序是 $2, 4, 6, \dots$。

**拆解步骤**：

1. **创建三个信号量**：
   - `sem_zero`：控制 $0$ 的打印，初始值 $1$（有令牌）
   - `sem_odd`：控制奇数的打印，初始值 $0$（无令牌）
   - `sem_even`：控制偶数的打印，初始值 $0$（无令牌）

2. **`zero()` 线程**（负责打 $0$）：
   - 循环 $n$ 次，每次先申请 `sem_zero` 的令牌
   - 打印 $0$
   - 如果当前是第奇数个（$1$、$3$、$5$……），释放 `sem_odd` 的令牌
   - 如果当前是第偶数个（$2$、$4$、$6$……），释放 `sem_even` 的令牌

3. **`odd()` 线程**（负责打奇数）：
   - 循环打 $1, 3, 5, \dots$
   - 每次先申请 `sem_odd` 的令牌
   - 打印当前奇数
   - 释放 `sem_zero` 的令牌

4. **`even()` 线程**（负责打偶数）：
   - 循环打 $2, 4, 6, \dots$
   - 每次先申请 `sem_even` 的令牌
   - 打印当前偶数
   - 释放 `sem_zero` 的令牌

### 思路 1：代码

```python
from threading import Semaphore

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        # 一开始只有 zero 可以执行
        self.sem_zero = Semaphore(1)
        self.sem_even = Semaphore(0)
        self.sem_odd = Semaphore(0)

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.sem_zero.acquire()   # 等待 zero 的令牌
            printNumber(0)
            # 根据当前数字的奇偶性，释放对应线程的令牌
            if i % 2 == 1:
                self.sem_odd.release()   # 下一个打奇数
            else:
                self.sem_even.release()  # 下一个打偶数

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
            self.sem_even.acquire()   # 等待 even 的令牌
            printNumber(i)
            self.sem_zero.release()   # 把令牌还给 zero

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            self.sem_odd.acquire()    # 等待 odd 的令牌
            printNumber(i)
            self.sem_zero.release()   # 把令牌还给 zero
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。需要打印 $2n$ 个数字。
- **空间复杂度**：$O(1)$。只用了三个信号量，常数空间。
