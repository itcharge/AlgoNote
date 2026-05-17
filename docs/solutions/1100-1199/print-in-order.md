# [1114. 按序打印](https://leetcode.cn/problems/print-in-order/)

- 标签：多线程
- 难度：简单

## 题目链接

- [1114. 按序打印 - 力扣](https://leetcode.cn/problems/print-in-order/)

## 题目大意

**描述**：三个不同的线程 A、B、C 会共用一个 `Foo` 实例，分别调用 `first()`、`second()` 和 `third()` 方法。三个线程是异步启动的，我们无法控制操作系统调度线程的顺序。

**要求**：确保 `second()` 在 `first()` 之后执行，`third()` 在 `second()` 之后执行。最终输出为 `"firstsecondthird"`。

**说明**：

- 尽管输入中的数字表示线程的启动顺序，但实际调度顺序是不确定的。

**示例**：

- 示例 1：

```python
输入：nums = [1,2,3]
输出："firstsecondthird"
```

- 示例 2：

```python
输入：nums = [1,3,2]
输出："firstsecondthird"
```

## 解题思路

### 思路 1：锁（Lock）

**拆解步骤**：

1. **创建两个锁**：
   - `lock_second`：控制 `second` 能否执行，初始为锁定状态（关着门）
   - `lock_third`：控制 `third` 能否执行，初始为锁定状态（关着门）

2. **`first()` 执行完后**：打开 `lock_second` 的门，允许 `second()` 执行。

3. **`second()` 执行前**：先等 `lock_second` 开门（即等 `first` 完成），执行完后打开 `lock_third` 的门，允许 `third()` 执行。

4. **`third()` 执行前**：先等 `lock_third` 开门（即等 `second` 完成），然后执行。

### 思路 1：代码

```python
from threading import Lock

class Foo:
    def __init__(self):
        # 创建两个锁，初始都是锁定状态
        self.lock_second = Lock()
        self.lock_third = Lock()
        self.lock_second.acquire()  # second 的门关着
        self.lock_third.acquire()   # third 的门关着

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.lock_second.release()  # second 可以执行了

    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.lock_second:     # 等 first 执行完
            # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
            self.lock_third.release()  # third 可以执行了

    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.lock_third:      # 等 second 执行完
            # printThird() outputs "third". Do not change or remove this line.
            printThird()
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(1)$。每个方法只执行一次，没有循环。
- **空间复杂度**：$O(1)$。只用了两个锁，常数空间。
