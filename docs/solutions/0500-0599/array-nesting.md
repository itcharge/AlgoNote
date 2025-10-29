# [0565. 数组嵌套](https://leetcode.cn/problems/array-nesting/)

- 标签：深度优先搜索、数组
- 难度：中等

## 题目链接

- [0565. 数组嵌套 - 力扣](https://leetcode.cn/problems/array-nesting/)

## 题目大意

**描述**：

给定索引从 $0$ 开始长度为 $N$ 的数组 $A$，包含 $0 \sim N - 1$ 的所有整数。

**要求**：

找到最大的集合 $S$ 并返回其大小，其中 $S[i] = \{A[i], A[A[i]], A[A[A[i]]], ... \}$ 且遵守以下的规则。

假设选择索引为 $i$ 的元素 $A[i]$ 为 $S$ 的第一个元素，$S$ 的下一个元素应该是 $A[A[i]]$，之后是 $A[A[A[i]]]...$ 以此类推，不断添加直到 $S$ 出现重复的元素。

**说明**：

- $1 \le nums.length \le 10^{5}$。
- $0 \le nums[i] \lt nums.length$。
- $A$ 中不含有重复的元素。

**示例**：

- 示例 1：

```python
输入: A = [5,4,0,3,1,6,2]
输出: 4
解释: 
A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.

其中一种最长的 S[K]:
S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}
```

## 解题思路

### 思路 1：

将数组 $A$ 看成一个有向图：每个下标 $i$ 指向唯一的下标 $A[i]$。由于 $A$ 是 $0\sim N-1$ 的一个排列（元素不重复，且都在范围内），图中每个节点出度均为 $1$，因此整张图由若干个「不相交的简单环」组成。题目中的集合 $S[i] = \{A[i], A[A[i]], A[A[A[i]]], \ldots\}$ 实际上就是从起点 $i$ 出发顺着边前进直到首次重复时形成的环，答案即为所有环中最大的长度。

做法：从每个未访问的起点 $i$ 出发，沿着 $i \to A[i] \to A[A[i]] \to \cdots$ 走，并统计本次路径中第一次遇到已访问节点前的步数，即该环的长度。用布尔数组（或集合） $visited$ 标记已经访问过的下标，保证每个下标只被遍历一次。

**变量含义**：

- $N$：数组长度。
- $A$：输入数组。
- $visited$：访问标记数组，`visited[x] = True` 表示下标 $x$ 已被计入某个环或已遍历过。
- $ans$：当前找到的最大环长。
- $curr$：从某个起点出发的游标位置。
- $cnt$：从当前起点出发走到重复前累计的长度。

**算法步骤**：

1. 初始化 $visited$ 全为 `False`，$ans = 0$。
2. 枚举起点 $i \in [0, N-1]$。若 `visited[i]` 为 `True`，跳过；否则从 $i$ 出发：
    - 置 $cnt = 0$，$curr = i$。
    - 当 `visited[curr]` 为 `False` 时：标记 `visited[curr] = True`，令 $curr = A[curr]$，$cnt++$。
    - 本轮结束时，更新 $ans = \max(ans, cnt)$。
3. 返回 $ans$。

### 思路 1：代码

```python
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        visited = [False] * n  # 访问标记：True 表示该下标已被遍历过
        ans = 0

        for i in range(n):
            if visited[i]:
                continue  # 已处理过，跳过

            cnt = 0
            curr = i
            # 顺着 i -> nums[i] -> nums[nums[i]] ... 直到遇到已访问位置
            while not visited[curr]:
                visited[curr] = True
                curr = nums[curr]
                cnt += 1

            # 本次从起点 i 出发形成的环长度为 cnt
            if cnt > ans:
                ans = cnt

        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(N)$。每个下标至多被访问一次。
- **空间复杂度**：$O(N)$。使用了大小为 $N$ 的 $visited$ 辅助数组。
