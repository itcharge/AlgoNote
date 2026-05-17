# [1115. 交替打印 FooBar](https://leetcode.cn/problems/print-foobar-alternately/)

- 标签：多线程
- 难度：中等

## 题目链接

- [1115. 交替打印 FooBar - 力扣](https://leetcode.cn/problems/print-foobar-alternately/)

## 题目大意

**描述**：给定一个类 `FooBar` 和一个整数 $n$。两个不同的线程会共用这个实例：
- 线程 A 调用 `foo()` 方法，打印 `"foo"`。
- 线程 B 调用 `bar()` 方法，打印 `"bar"`。

**要求**：修改程序，确保输出为 `"foobar"` 重复 $n$ 次（即 `"foobarfoobar..."`）。

**说明**：

- $1 \le n \le 10^3$。

**示例**：

- 示例 1：

```python
输入：n = 1
输出："foobar"
```

- 示例 2：

```python
输入：n = 2
输出："foobarfoobar"
```

## 解题思路

### 思路 1：信号量（Semaphore）

**拆解步骤**：

1. **创建两个信号量**：
   - `sem_foo`：控制 `foo` 的执行，初始值 $1$（一开始有令牌，可以执行）。
   - `sem_bar`：控制 `bar` 的执行，初始值 $0$（没有令牌，需要等待）。

2. **在 `foo()` 方法中**：
   - 先申请 `sem_foo` 的令牌（第一次来的时候有令牌，直接通过；后续需要等 `bar` 还回来）
   - 打印 `"foo"`
   - 释放 `sem_bar` 的令牌，通知 `bar` 可以执行了

3. **在 `bar()` 方法中**：
   - 先申请 `sem_bar` 的令牌（一开始没有令牌，需要等待 `foo` 释放）
   - 打印 `"bar"`
   - 释放 `sem_foo` 的令牌，通知 `foo` 可以执行下一轮

4. **重复 $n$ 次**，就完成了 $n$ 次交替打印。

### 思路 1：代码

```python
from threading import Semaphore

class FooBar:
    def __init__(self, n):
        self.n = n
        # 一开始 foo 可以执行，bar 不能执行
        self.sem_foo = Semaphore(1)
        self.sem_bar = Semaphore(0)

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.sem_foo.acquire()   # 等待 foo 的令牌
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.sem_bar.release()   # 把令牌交给 bar

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.sem_bar.acquire()   # 等待 bar 的令牌
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.sem_foo.release()   # 把令牌交还给 foo
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。需要循环 $n$ 次来交替打印。
- **空间复杂度**：$O(1)$。只用了两个信号量，常数空间。
