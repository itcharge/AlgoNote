# [0352. 将数据流变为多个不相交区间](https://leetcode.cn/problems/data-stream-as-disjoint-intervals/)

- 标签：设计、二分查找、有序集合
- 难度：困难

## 题目链接

- [0352. 将数据流变为多个不相交区间 - 力扣](https://leetcode.cn/problems/data-stream-as-disjoint-intervals/)

## 题目大意

**描述**：

给定一个由非负整数 $a1, a2, ..., an$ 组成的数据流输入。

**要求**：

请你将到目前为止看到的数字总结为不相交的区间列表。

实现 `SummaryRanges` 类：

- `SummaryRanges()` 使用一个空数据流初始化对象。
- `void addNum(int val)` 向数据流中加入整数 $val$ 。
- `int[][] getIntervals()` 以不相交区间 $[start_i, end_i]$ 的列表形式返回对数据流中整数的总结。

**说明**：

- $0 \le val \le 10^{4}$。
- 最多调用 `addNum` 和 `getIntervals` 方法 $3 \times 10^{4}$ 次。

- 进阶：如果存在大量合并，并且与数据流的大小相比，不相交区间的数量很小，该怎么办?

**示例**：

- 示例 1：

```python
输入：
["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
[[], [1], [], [3], [], [7], [], [2], [], [6], []]
输出：
[null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]

解释：
SummaryRanges summaryRanges = new SummaryRanges();
summaryRanges.addNum(1);      // arr = [1]
summaryRanges.getIntervals(); // 返回 [[1, 1]]
summaryRanges.addNum(3);      // arr = [1, 3]
summaryRanges.getIntervals(); // 返回 [[1, 1], [3, 3]]
summaryRanges.addNum(7);      // arr = [1, 3, 7]
summaryRanges.getIntervals(); // 返回 [[1, 1], [3, 3], [7, 7]]
summaryRanges.addNum(2);      // arr = [1, 2, 3, 7]
summaryRanges.getIntervals(); // 返回 [[1, 3], [7, 7]]
summaryRanges.addNum(6);      // arr = [1, 2, 3, 6, 7]
summaryRanges.getIntervals(); // 返回 [[1, 3], [6, 7]]
```

## 解题思路

### 思路 1：集合 + 动态生成区间

这道题的核心是维护一个数字集合，然后在需要时动态生成不相交的区间列表。

**算法思路**：

1. **数据结构选择**：使用集合（set）存储所有出现过的数字，利用集合的去重特性自动处理重复数字。
2. **添加数字**：当添加数字 $val$ 时，直接将其加入集合中，时间复杂度为 $O(1)$。
3. **获取区间**：当需要获取区间列表时：
   - 将集合中的所有数字排序。
   - 遍历排序后的数字，连续的数字合并为一个区间。
   - 遇到不连续的数字时，开始新的区间。

**具体步骤**：

1. 使用集合存储所有添加的数字。
2. `addNum(val)`：将 $val$ 添加到集合中。
3. `getIntervals()`：
   - 对集合中的数字排序得到 $sorted\_nums$。
   - 初始化 $start = end = sorted\_nums[0]$。
   - 遍历剩余数字，如果 $sorted\_nums[i] = end + 1$，则扩展当前区间 $end = sorted\_nums[i]$。
   - 否则，保存当前区间 $[start, end]$，开始新区间 $start = end = sorted\_nums[i]$。
   - 最后添加最后一个区间。

### 思路 1：代码

```python
class SummaryRanges:
    def __init__(self):
        # 使用集合存储所有出现过的数字
        self.nums = set()

    def addNum(self, value: int) -> None:
        # 将数字添加到集合中，集合自动去重
        self.nums.add(value)

    def getIntervals(self) -> List[List[int]]:
        # 如果集合为空，返回空列表
        if not self.nums:
            return []
        
        # 将集合中的数字排序
        sorted_nums = sorted(self.nums)
        intervals = []
        
        # 初始化第一个区间
        start = end = sorted_nums[0]
        
        # 遍历剩余数字，构建区间
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == end + 1:
                # 当前数字与前一个数字连续，扩展当前区间
                end = sorted_nums[i]
            else:
                # 当前数字与前一个数字不连续，保存当前区间并开始新区间
                intervals.append([start, end])
                start = end = sorted_nums[i]
        
        # 添加最后一个区间
        intervals.append([start, end])
        
        return intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
```

### 思路 1：复杂度分析

- **时间复杂度**：
  - `addNum(val)`：$O(1)$，集合的插入操作时间复杂度为常数。
  - `getIntervals()`：$O(n \log n)$，其中 $n$ 为集合中数字的个数，主要时间消耗在排序上。
- **空间复杂度**：$O(n)$，其中 $n$ 为添加的不同数字的个数。
