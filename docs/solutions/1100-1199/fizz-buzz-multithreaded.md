# [1195. 交替打印字符串](https://leetcode.cn/problems/fizz-buzz-multithreaded/)

- 标签：多线程
- 难度：中等

## 题目链接

- [1195. 交替打印字符串 - 力扣](https://leetcode.cn/problems/fizz-buzz-multithreaded/)

## 题目大意

**描述**：编写一个多线程程序，从 $1$ 到 $n$ 输出数字，但要按以下规则替换：

- 能被 $3$ 整除 → 输出 `"fizz"`
- 能被 $5$ 整除 → 输出 `"buzz"`
- 能同时被 $3$ 和 $5$ 整除 → 输出 `"fizzbuzz"`
- 其他 → 输出数字本身

四个线程分别负责一种输出：
1. 线程 A 负责输出 `"fizz"`
2. 线程 B 负责输出 `"buzz"`
3. 线程 C 负责输出 `"fizzbuzz"`
4. 线程 D 负责输出数字

**要求**：实现多线程版的 `FizzBuzz`，让四个线程协同工作，正确交替输出。

**示例**：

```python
输入：n = 15
输出：1, 2, fizz, 4, buzz, fizz, 7, 8, fizz, buzz, 11, fizz, 13, 14, fizzbuzz
```

## 解题思路

### 思路 1：锁 + 轮询

这道题需要四个线程协同工作，每个线程只负责自己那一类数字的输出。核心机制是每个线程不停地检查当前的数字是不是自己的「职责范围」，如果是就输出并前进到下一个数字。

可以想象成四个工人站在流水线旁边，流水线上依次送来数字 1、2、3……每个工人只负责处理特定的数字，处理完后流水线才前进到下一个。

**步骤拆解：**

1. 使用一把锁（`Lock`）保护共享变量 `current`（当前要处理的数字），确保同一时间只有一个线程在操作。

2. 每个线程在自己的循环中不断检查：
   - 如果 `current > n`，退出循环（所有数字处理完了）。
   - 检查 `current` 是否符合自己的条件：
     - `fizz` 线程：`current % 3 == 0 且 current % 5 != 0`
     - `buzz` 线程：`current % 5 == 0 且 current % 3 != 0`
     - `fizzbuzz` 线程：`current % 15 == 0`
     - `number` 线程：`current % 3 != 0 且 current % 5 != 0`
   - 如果符合条件，输出并 `current += 1`。

3. 由于使用了锁，即使四个线程同时运行，同一时刻也只有一个线程能检查和输出，保证了顺序正确。

### 思路 1：代码

```python
from threading import Lock

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n                # 最大数字
        self.current = 1          # 当前要处理的数字
        self.lock = Lock()        # 互斥锁，保证线程安全

    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while True:
            with self.lock:
                if self.current > self.n:
                    break
                # 如果能被 3 整除但不能被 5 整除，输出 fizz
                if self.current % 3 == 0 and self.current % 5 != 0:
                    printFizz()
                    self.current += 1

    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while True:
            with self.lock:
                if self.current > self.n:
                    break
                # 如果能被 5 整除但不能被 3 整除，输出 buzz
                if self.current % 5 == 0 and self.current % 3 != 0:
                    printBuzz()
                    self.current += 1

    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            with self.lock:
                if self.current > self.n:
                    break
                # 如果能同时被 3 和 5 整除（即被 15 整除），输出 fizzbuzz
                if self.current % 15 == 0:
                    printFizzBuzz()
                    self.current += 1

    def number(self, printNumber: 'Callable[[int], None]') -> None:
        while True:
            with self.lock:
                if self.current > self.n:
                    break
                # 如果不能被 3 整除也不能被 5 整除，输出数字本身
                if self.current % 3 != 0 and self.current % 5 != 0:
                    printNumber(self.current)
                    self.current += 1
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。每个数字只被一个线程处理一次，总共处理 $n$ 次。
- **空间复杂度**：$O(1)$。只用了几个固定变量。
