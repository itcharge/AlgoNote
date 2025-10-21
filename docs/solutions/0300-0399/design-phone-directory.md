# [0379. 电话目录管理系统](https://leetcode.cn/problems/design-phone-directory/)

- 标签：设计、队列、数组、哈希表、链表
- 难度：中等

## 题目链接

- [0379. 电话目录管理系统 - 力扣](https://leetcode.cn/problems/design-phone-directory/)

## 题目大意

**要求**：

设计一个电话目录管理系统，一开始有 $maxNumbers$ 个位置能够储存号码。系统应该存储号码，检查某个位置是否为空，并清空给定的位置。

实现 `PhoneDirectory` 类：

- `PhoneDirectory(int maxNumbers)` 电话目录初始有 $maxNumbers$ 个可用位置。
- `int get()` 提供一个未分配给任何人的号码。如果没有可用号码则返回 $-1$。
- `bool check(int number)` 如果位置 $number$ 可用返回 $true$ 否则返回 $false$。
- `void release(int number)` 回收或释放位置 $number$。

**说明**：

- $1 \le maxNumbers \le 10^{4}$。
- $0 \le number \lt maxNumbers$。
- `get`，`check` 和 `release` 最多被调用 $2 \times 10^{4}$ 次。

**示例**：

- 示例 1：

```python
输入：
["PhoneDirectory", "get", "get", "check", "get", "check", "release", "check"]
[[3], [], [], [2], [], [2], [2], [2]]
输出：
[null, 0, 1, true, 2, false, null, true]

解释：
PhoneDirectory phoneDirectory = new PhoneDirectory(3);
phoneDirectory.get();      // 它可以返回任意可用的数字。这里我们假设它返回 0。
phoneDirectory.get();      // 假设它返回 1。
phoneDirectory.check(2);   // 数字 2 可用，所以返回 true。
phoneDirectory.get();      // 返回剩下的唯一一个数字 2。
phoneDirectory.check(2);   // 数字 2 不再可用，所以返回 false。
phoneDirectory.release(2); // 将数字 2 释放回号码池。
phoneDirectory.check(2);   // 数字 2 重新可用，返回 true。
```

## 解题思路

### 思路 1：集合 + 队列

使用集合来快速检查号码是否可用，使用队列来高效分配号码。这种方法结合了集合的 $O(1)$ 查找性能和队列的先进先出特性。

具体步骤：

1. **初始化**：创建集合 $available$ 存储所有可用号码，创建队列 $queue$ 用于快速分配号码。
2. **get 操作**：从队列头部取出一个号码，并从集合中移除该号码。
3. **check 操作**：检查号码是否在可用集合中。
4. **release 操作**：将号码重新加入集合和队列。

这种方法的关键是维护两个数据结构的一致性，确保号码的状态在两个数据结构中保持同步。

### 思路 1：代码

```python
from collections import deque

class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        # 使用集合存储所有可用的号码，支持 O(1) 查找
        self.available = set()
        # 使用队列存储可用号码，支持 O(1) 分配
        self.queue = deque()
        
        # 初始化所有号码为可用状态
        for i in range(maxNumbers):
            self.available.add(i)
            self.queue.append(i)

    def get(self) -> int:
        # 如果没有可用号码，返回 -1
        if not self.available:
            return -1
        
        # 从队列头部取出一个号码
        number = self.queue.popleft()
        # 从可用集合中移除该号码
        self.available.remove(number)
        
        return number

    def check(self, number: int) -> bool:
        # 检查号码是否在可用集合中
        return number in self.available

    def release(self, number: int) -> None:
        # 如果号码已经可用，不需要重复释放
        if number in self.available:
            return
        
        # 将号码重新加入可用集合和队列
        self.available.add(number)
        self.queue.append(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
```

### 思路 1：复杂度分析

- **时间复杂度**：
  - `get` 操作：$O(1)$，从队列头部取出元素，从集合中移除元素。
  - `check` 操作：$O(1)$，集合查找操作。
  - `release` 操作：$O(1)$，向集合和队列添加元素。
- **空间复杂度**：$O(n)$，其中 $n$ 是 $maxNumbers$，需要存储所有号码的状态。
