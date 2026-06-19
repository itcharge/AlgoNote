# [1354. 多次求和构造目标数组](https://leetcode.cn/problems/construct-target-array-with-multiple-sums/)

- 标签：数组、堆（优先队列）
- 难度：困难

## 题目链接

- [1354. 多次求和构造目标数组 - 力扣](https://leetcode.cn/problems/construct-target-array-with-multiple-sums/)

## 题目大意

**描述**：给定一个目标数组 $target$，初始数组 $arr$ 全是 $1$。每一步可以将 $arr$ 中的某个元素替换为 $arr$ 中所有元素的和。

**要求**：判断是否可以通过若干次操作得到 $target$。

**说明**：
- $1 \le target.length \le 5 \times 10^4$。
- $1 \le target[i] \le 10^9$。

**示例**：

- 示例 1：

```python
输入：target = [9,3,5]
输出：true
解释：从 [1, 1, 1] 开始
[1, 1, 1], 和为 3 ，选择下标 1
[1, 3, 1], 和为 5， 选择下标 2
[1, 3, 5], 和为 9， 选择下标 0
[9, 3, 5] 完成
```

- 示例 2：

```python
输入：target = [1,1,1,2]
输出：false
解释：不可能从 [1,1,1,1] 出发构造目标数组。
```


## 解题思路

### 思路 1：逆推（最大堆）

#### 1. 核心思想

正向推导很难，因为有无数种可能。考虑**逆推**：从 $target$ 出发，每次将当前最大值替换回它在上一轮中的值。

假设当前数组的和为 $total$，最大值为 $max\_val$。这个最大值是某个上一轮的元素替换了所有元素的和后得到的。所以在上一轮中，这个元素的值是 $max\_val - (total - max\_val)$，即 $2 \times max\_val - total$。

重复这个过程，直到：
- 所有数都是 $1$ → 返回 $True$。
- 最大值 $\le 0$ → 返回 $False$。

#### 2. 具体步骤

**第 1 步**：计算 $total = sum(target)$，构建最大堆。

**第 2 步**：循环直到最大值变为 $1$：
- 弹出最大值 $max\_val$。
- 剩余和 $rest = total - max\_val$。
- 如果 $rest == 1$（即只剩一个大于 $1$ 的数），返回 $True$（因为下一轮将和替换回去即可得到 $1$）。
- 计算上一轮中的值 $prev = max\_val - rest$。
- 如果 $prev \le 0$ 或 $prev >= max\_val$，返回 $False$。
- 将 $prev$ 重新入堆，更新 $total$。

**第 3 步**：返回 $True$。

### 思路 1：代码

```python
import heapq

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1:
            return target[0] == 1

        total = sum(target)
        # Python 的 heapq 是最小堆，取负数实现最大堆
        heap = [-x for x in target]
        heapq.heapify(heap)

        while -heap[0] > 1:
            max_val = -heapq.heappop(heap)
            rest = total - max_val
            if rest == 1:
                return True
            # 批量跳过重复减法：当 rest 远小于 max_val 时，用模运算直接得到最终值
            prev = max_val % rest
            if prev == 0:
                prev = rest
            if prev >= max_val:
                return False
            heapq.heappush(heap, -prev)
            total = total - max_val + prev

        return True
```

### 思路 1：复杂度分析
- **时间复杂度**：$O(n \log n)$，每次堆操作 $O(\log n)$，约 $O(\log \max(target))$ 次。
- **空间复杂度**：$O(n)$。
