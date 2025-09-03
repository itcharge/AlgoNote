# [0900. RLE 迭代器](https://leetcode.cn/problems/rle-iterator/)

- 标签：设计、数组、计数、迭代器
- 难度：中等

## 题目链接

- [0900. RLE 迭代器 - 力扣](https://leetcode.cn/problems/rle-iterator/)

## 题目大意

**描述**：我们可以使用游程编码（即 RLE）来编码一个整数序列。在偶数长度 $encoding$ ( 从 $0$ 开始 )的游程编码数组中，对于所有偶数 $i$，$encoding[i]$ 告诉我们非负整数 $encoding[i + 1]$ 在序列中重复的次数。

- 例如，序列 $arr = [8,8,8,5,5]$ 可以被编码为 $encoding =[3,8,2,5]$。$encoding =[3,8,0,9,2,5]$ 和 $encoding =[2,8,1,8,2,5]$ 也是 $arr$ 有效的 RLE。

给定一个游程长度的编码数组 $encoding$。

**要求**：设计一个迭代器来遍历它。

实现 `RLEIterator` 类:

- `RLEIterator(int[] encoded)` 用编码后的数组初始化对象。
- `int next(int n)` 以这种方式耗尽后 $n$ 个元素并返回最后一个耗尽的元素。如果没有剩余的元素要耗尽，则返回 $-1$。

**说明**：

- $2 \le encoding.length \le 1000$。
- $encoding.length$ 为偶。
- $0 \le encoding[i] \le 10^9$。
- $1 \le n \le 10^9$。
- 每个测试用例调用 `next` 不高于 $1000$ 次。

**示例**：

- 示例 1：

```python
输入：
["RLEIterator","next","next","next","next"]
[[[3,8,0,9,2,5]],[2],[1],[1],[2]]
输出：
[null,8,8,5,-1]
解释：
RLEIterator rLEIterator = new RLEIterator([3, 8, 0, 9, 2, 5]); // 这映射到序列 [8,8,8,5,5]。
rLEIterator.next(2); // 耗去序列的 2 个项，返回 8。现在剩下的序列是 [8, 5, 5]。
rLEIterator.next(1); // 耗去序列的 1 个项，返回 8。现在剩下的序列是 [5, 5]。
rLEIterator.next(1); // 耗去序列的 1 个项，返回 5。现在剩下的序列是 [5]。
rLEIterator.next(2); // 耗去序列的 2 个项，返回 -1。 这是由于第一个被耗去的项是 5，
但第二个项并不存在。由于最后一个要耗去的项不存在，我们返回 -1。
```

## 解题思路

### 思路 1：模拟

1. 初始化时：
   1. 保存数组 $encoding$ 作为成员变量。
   2. 保存当前位置 $index$，表示当前迭代器指向元素 $encoding[index + 1]$。初始化赋值为 $0$。
   3. 保存当前指向元素 $encoding[index + 1]$ 已经被删除的元素个数 $d\_cnt$。初始化赋值为 $0$。
2. 调用 `next(n)` 时：
   1. 对于当前元素，先判断当前位置是否超出 $encoding$ 范围，超过则直接返回 $-1$。
   2. 如果未超过，再判断当前元素剩余个数 $encoding[index] - d\_cnt$ 是否小于 $n$ 个。
      1. 如果小于 $n$ 个，则删除当前元素剩余所有个数，并指向下一位置继续删除剩余元素。
      2. 如果等于大于等于 $n$ 个，则令当前指向元素 $encoding[index + 1]$ 已经被删除的元素个数 $d\_cnt$ 加上 $n$。

### 思路 1：代码

```Python
class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        self.index = 0
        self.d_cnt = 0

    def next(self, n: int) -> int:
        while self.index < len(self.encoding):
            if self.d_cnt + n > self.encoding[self.index]:
                n -= self.encoding[self.index] - self.d_cnt
                self.d_cnt = 0
                self.index += 2
            else:
                self.d_cnt += n
                return self.encoding[self.index + 1]
        return -1
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n + m)$，其中 $n$ 为数组 $encoding$ 的长度，$m$ 是调用 `next(n)` 的次数。
- **空间复杂度**：$O(n)$。

