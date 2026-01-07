# [0895. 最大频率栈](https://leetcode.cn/problems/maximum-frequency-stack/)

- 标签：栈、设计、哈希表、有序集合
- 难度：困难

## 题目链接

- [0895. 最大频率栈 - 力扣](https://leetcode.cn/problems/maximum-frequency-stack/)

## 题目大意

**要求**：

设计一个类似堆栈的数据结构，将元素推入堆栈，并从堆栈中弹出出现频率最高的元素。

实现 FreqStack 类:

- `FreqStack$()` 构造一个空的堆栈。
- `void push(int val)` 将一个整数 $val$ 压入栈顶。
- `int pop()` 删除并返回堆栈中出现频率最高的元素。
- 如果出现频率最高的元素不只一个，则移除并返回最接近栈顶的元素。

**说明**：

- $0 \le val \le 10^{9}$。
- `push` 和 `pop` 的操作数不大于 $2 \times 10^{4}$。
- 输入保证在调用 `pop` 之前堆栈中至少有一个元素。

**示例**：

- 示例 1：

```python
输入：
["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
输出：[null,null,null,null,null,null,null,5,7,5,4]
解释：
FreqStack = new FreqStack();
freqStack.push (5);//堆栈为 [5]
freqStack.push (7);//堆栈是 [5,7]
freqStack.push (5);//堆栈是 [5,7,5]
freqStack.push (7);//堆栈是 [5,7,5,7]
freqStack.push (4);//堆栈是 [5,7,5,7,4]
freqStack.push (5);//堆栈是 [5,7,5,7,4,5]
freqStack.pop ();//返回 5 ，因为 5 出现频率最高。堆栈变成 [5,7,5,7,4]。
freqStack.pop ();//返回 7 ，因为 5 和 7 出现频率最高，但7最接近顶部。堆栈变成 [5,7,5,4]。
freqStack.pop ();//返回 5 ，因为 5 出现频率最高。堆栈变成 [5,7,4]。
freqStack.pop ();//返回 4 ，因为 4, 5 和 7 出现频率最高，但 4 是最接近顶部的。堆栈变成 [5,7]。
```

## 解题思路

### 思路 1：哈希表 + 频率栈

这道题要求设计一个数据结构，支持 `push` 和 `pop` 操作，其中 `pop` 操作返回频率最高的元素（如果有多个，返回最接近栈顶的）。

关键数据结构：

1. $freq$ 哈希表：记录每个元素的出现频率。
2. $group$ 哈希表：记录每个频率对应的元素栈。$group[f]$ 存储所有频率为 $f$ 的元素。
3. $max\_freq$：记录当前最大频率。

算法步骤：

- **push 操作**：
  1. 更新元素的频率 $freq[val]$。
  2. 将元素加入对应频率的栈 $group[freq[val]]$。
  3. 更新最大频率 $max\_freq$。

- **pop 操作**：
  1. 从最大频率的栈 $group[max\_freq]$ 中弹出元素。
  2. 更新该元素的频率 $freq[val]$。
  3. 如果最大频率的栈为空，减小 $max\_freq$。

### 思路 1：代码

```python
class FreqStack:

    def __init__(self):
        self.freq = {}  # 记录每个元素的频率
        self.group = {}  # 记录每个频率对应的元素栈
        self.max_freq = 0  # 当前最大频率

    def push(self, val: int) -> None:
        # 更新元素的频率
        self.freq[val] = self.freq.get(val, 0) + 1
        f = self.freq[val]
        
        # 将元素加入对应频率的栈
        if f not in self.group:
            self.group[f] = []
        self.group[f].append(val)
        
        # 更新最大频率
        self.max_freq = max(self.max_freq, f)

    def pop(self) -> int:
        # 从最大频率的栈中弹出元素
        val = self.group[self.max_freq].pop()
        
        # 更新元素的频率
        self.freq[val] -= 1
        
        # 如果最大频率的栈为空，减小最大频率
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
```

### 思路 1：复杂度分析

- **时间复杂度**：`push` 和 `pop` 操作的时间复杂度都是 $O(1)$。
- **空间复杂度**：$O(n)$，其中 $n$ 是元素的总数。需要存储频率和分组信息。
