# [1157. 子数组中占绝大多数的元素](https://leetcode.cn/problems/online-majority-element-in-subarray/)

- 标签：设计、树状数组、线段树、数组、二分查找
- 难度：困难

## 题目链接

- [1157. 子数组中占绝大多数的元素 - 力扣](https://leetcode.cn/problems/online-majority-element-in-subarray/)

## 题目大意

**描述**：设计一个数据结构，能高效地查询任意子数组中的"多数元素"。

多数元素是指在子数组中出现次数 $\ge threshold$ 的元素。注意这里的 $threshold$ 不是传统意义上的"超过一半"，而是由查询指定的任意阈值。但题目保证了一个重要性质：$2 \times threshold >$ 子数组长度，也就是说多数元素如果存在，它在子数组中的占比超过 $50\%$。

实现 $MajorityChecker$ 类：
- $MajorityChecker(int[] arr)$：用数组 $arr$ 初始化。
- $int\ query(int\ left, int\ right, int\ threshold)$：返回子数组 $arr[left...right]$ 中出现次数 $\ge threshold$ 的元素，不存在则返回 $-1$。

**要求**：实现上述类。

**说明**：

- $1 \le arr.length \le 2 \times 10^4$。
- $1 \le arr[i] \le 2 \times 10^4$。
- $0 \le left \le right < arr.length$。
- $threshold \le right - left + 1$。
- $2 \times threshold > right - left + 1$（重要性质）。
- 调用 $query$ 的次数最多为 $10^4$。

**示例**：

```python
输入：
["MajorityChecker", "query", "query", "query"]
[[[1, 1, 2, 2, 1, 1]], [0, 5, 4], [0, 3, 3], [2, 3, 2]]
输出：
[null, 1, -1, 2]
```

## 解题思路

### 思路 1：随机化 + 二分查找

**为什么随机化可行？** 想象一个子数组有 $100$ 个数，其中某个数出现了 $51$ 次。随机挑 $1$ 个数，选中这个数的概率是 $51\%$，超过一半。连续 $20$ 次都选不中的概率只有 $(0.49)^{20} \approx 0.0001\%$，几乎不可能。

**怎么快速验证出现次数？** 预处理时，对每个不同的数值，按顺序记录它出现的所有位置（下标）。验证时，在对应数值的位置列表中，用二分查找找到第一个 $\ge left$ 的位置和最后一个 $\le right$ 的位置，两个位置之差 $+1$ 就是出现次数。

**拆解步骤**：

1. **初始化**：遍历数组，用哈希表记录每个数值出现的所有位置列表（按顺序）。

2. **查询**：
   - 重复 $20$ 次（几乎能保证正确）：
     - 在 $[left, right]$ 范围内随机选一个下标
     - 取出该下标对应的数值作为候选者
     - 在该数值的位置列表中用二分查找，计算它在 $[left, right]$ 中出现了几次
     - 如果出现次数 $\ge threshold$，返回该数值
   - $20$ 次都没找到，返回 $-1$

### 思路 1：代码

```python
import random
from bisect import bisect_left, bisect_right
from collections import defaultdict

class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.arr = arr
        # 记录每个数值出现的所有位置（按下标从小到大）
        self.pos = defaultdict(list)
        for i, num in enumerate(arr):
            self.pos[num].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        # 随机尝试 20 次
        for _ in range(20):
            # 在子数组中随机选一个下标
            idx = random.randint(left, right)
            candidate = self.arr[idx]

            # 用二分查找计算候选值在 [left, right] 中出现了几次
            positions = self.pos[candidate]
            # 第一个 >= left 的位置
            left_idx = bisect_left(positions, left)
            # 第一个 > right 的位置
            right_idx = bisect_right(positions, right)

            count = right_idx - left_idx

            # 如果出现次数达标，返回该候选值
            if count >= threshold:
                return candidate

        # 20 次都没找到，说明不存在
        return -1
```

### 思路 1：复杂度分析

- **时间复杂度**：初始化 $O(n)$，用人话说就是把数组遍历一遍记录每个数的位置。每次查询 $O(\log n)$，因为二分查找一次只需要 $\log n$ 时间，重复 $20$ 次常数次。
- **空间复杂度**：$O(n)$，需要存储每个数值出现的位置列表。
