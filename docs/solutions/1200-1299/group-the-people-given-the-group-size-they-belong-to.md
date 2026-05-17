# [1282. 用户分组](https://leetcode.cn/problems/group-the-people-given-the-group-size-they-belong-to/)

- 标签：贪心、数组、哈希表
- 难度：中等

## 题目链接

- [1282. 用户分组 - 力扣](https://leetcode.cn/problems/group-the-people-given-the-group-size-they-belong-to/)

## 题目大意

**描述**：有 $n$ 个人被分成数量未知的组。每个人被标记为一个从 $0$ 到 $n-1$ 的唯一 ID。给定一个整数数组 $groupSizes$，其中 $groupSizes[i]$ 是第 $i$ 个人所在的组的大小。

**要求**：返回一个组列表，使每个人 $i$ 都在一个大小为 $groupSizes[i]$ 的组中。每个人恰好只出现在一个组中。如果有多个答案，返回任意一个。保证至少有一个有效的解。

**说明**：

- $groupSizes.length == n$。
- $1 \le n \le 500$。
- $1 \le groupSizes[i] \le n$。

**示例**：

- 示例 1：

```python
输入：groupSizes = [3,3,3,3,3,1,3]
输出：[[5],[0,1,2],[3,4,6]]
解释：
第一组是 [5]，大小为 1，groupSizes[5] = 1。
第二组是 [0,1,2]，大小为 3，groupSizes[0] = groupSizes[1] = groupSizes[2] = 3。
第三组是 [3,4,6]，大小为 3，groupSizes[3] = groupSizes[4] = groupSizes[6] = 3。 
```

- 示例 2：

```python
输入：groupSizes = [2,1,3,3,3,2]
输出：[[1],[0,5],[2,3,4]]
```

## 解题思路

### 思路 1：哈希表分组

###### 1. 核心思想

需要相同组大小的人可以放在一起。比如所有组大小为 $3$ 的人，可以先收集到一个列表中，每凑满 $3$ 个人就切分成一组。

这个过程可以形象地理解为「分班」：先让所有想进入 $3$ 人班的同学排好队，每 $3$ 个人组成一个班离开队列，直到排完。

###### 2. 具体步骤

**第 1 步：收集分组**

用哈希表 $groups$ 记录每个组大小对应的人员列表。遍历 $groupSizes$，将每个人 $i$ 追加到 $groups[groupSizes[i]]$ 列表中。

**第 2 步：切分**

遍历哈希表，对于每个组大小 $size$ 和对应的人员列表 $people$：
- 从位置 $0$ 开始，每隔 $size$ 个人切分成一个子列表。
- 将这些子列表依次加入结果中。

因为题目保证有解，所以每个人的数量一定是 $size$ 的整数倍。

**第 3 步：返回结果**

**结合示例 1 走一遍：**

$groupSizes = [3,3,3,3,3,1,3]$

收集：
- $groups[3] = [0, 1, 2, 3, 4, 6]$
- $groups[1] = [5]$

切分：
- $size=3$：$[0,1,2]$、$[3,4,6]$ → 两组
- $size=1$：$[5]$ → 一组

结果：$[[0,1,2],[3,4,6],[5]]$（或任意顺序，示例答案是 $[[5],[0,1,2],[3,4,6]]$）。

### 思路 1：代码

```python
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # 第 1 步：按组大小分组
        groups = {}
        for i, size in enumerate(groupSizes):
            if size not in groups:
                groups[size] = []
            groups[size].append(i)

        # 第 2 步：每 size 个人切分一次
        ans = []
        for size, people in groups.items():
            for i in range(0, len(people), size):
                ans.append(people[i:i + size])

        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是数组 $groupSizes$ 的长度。只需要一次遍历收集和一次遍历切分。
- **空间复杂度**：$O(n)$，需要存储所有人员的临时分组信息。
