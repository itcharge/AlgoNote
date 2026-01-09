# [0911. 在线选举](https://leetcode.cn/problems/online-election/)

- 标签：设计、数组、哈希表、二分查找
- 难度：中等

## 题目链接

- [0911. 在线选举 - 力扣](https://leetcode.cn/problems/online-election/)

## 题目大意

**描述**：

给定两个整数数组 $persons$ 和 $times$。在选举中，第 $i$ 张票是在时刻为 $times[i]$ 时投给候选人 $persons[i]$ 的。

对于发生在时刻 $t$ 的每个查询，需要找出在 $t$ 时刻在选举中领先的候选人的编号。
在 $t$ 时刻投出的选票也将被计入我们的查询之中。在平局的情况下，最近获得投票的候选人将会获胜。

**要求**：

实现 TopVotedCandidate 类：

- `TopVotedCandidate(int[] persons, int[] times)` 使用 $persons$ 和 $times$ 数组初始化对象。
- `int q(int t)` 根据前面描述的规则，返回在时刻 $t$ 在选举中领先的候选人的编号。

**说明**：

- $1 \le persons.length \le 5000$。
- $times.length == persons.length$。
- $0 \le persons[i] \lt persons.length$。
- $0 \le times[i] \le 10^{9}$。
- $times$ 是一个严格递增的有序数组。
- $times[0] \le t \le 10^{9}$。
- 每个测试用例最多调用 $10^{4}$ 次 `q`。

**示例**：

- 示例 1：

```python
输入：
["TopVotedCandidate", "q", "q", "q", "q", "q", "q"]
[[[0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]], [3], [12], [25], [15], [24], [8]]
输出：
[null, 0, 1, 1, 0, 0, 1]

解释：
TopVotedCandidate topVotedCandidate = new TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]);
topVotedCandidate.q(3); // 返回 0 ，在时刻 3 ，票数分布为 [0] ，编号为 0 的候选人领先。
topVotedCandidate.q(12); // 返回 1 ，在时刻 12 ，票数分布为 [0,1,1] ，编号为 1 的候选人领先。
topVotedCandidate.q(25); // 返回 1 ，在时刻 25 ，票数分布为 [0,1,1,0,0,1] ，编号为 1 的候选人领先。（在平局的情况下，1 是最近获得投票的候选人）。
topVotedCandidate.q(15); // 返回 0
topVotedCandidate.q(24); // 返回 0
topVotedCandidate.q(8); // 返回 1
```

## 解题思路

### 思路 1：预处理 + 二分查找

这道题需要快速查询某个时刻的领先候选人，可以通过预处理和二分查找来优化。

1. **预处理**：在初始化时，遍历所有投票记录，计算每个时刻的领先候选人。
   - 使用哈希表记录每个候选人的票数
   - 维护当前领先的候选人和最高票数
   - 在平局时，选择最近获得投票的候选人
2. **二分查找**：查询时，使用二分查找找到不超过 $t$ 的最大时刻，返回该时刻的领先候选人。

### 思路 1：代码

```python
class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.leaders = []  # 记录每个时刻的领先者
        
        vote_count = collections.defaultdict(int)
        leader = -1
        max_votes = 0
        
        for person in persons:
            vote_count[person] += 1
            # 票数更多，或票数相同但是最近获得投票
            if vote_count[person] >= max_votes:
                leader = person
                max_votes = vote_count[person]
            self.leaders.append(leader)

    def q(self, t: int) -> int:
        # 二分查找：找到不超过 t 的最大时刻
        left, right = 0, len(self.times) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if self.times[mid] <= t:
                left = mid
            else:
                right = mid - 1
        return self.leaders[left]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
```

### 思路 1：复杂度分析

- **时间复杂度**：初始化 $O(n)$，查询 $O(\log n)$，其中 $n$ 是投票记录的数量。
- **空间复杂度**：$O(n)$，需要存储每个时刻的领先者。
