# [1029. 两地调度](https://leetcode.cn/problems/two-city-scheduling/)

- 标签：贪心、数组、排序
- 难度：中等

## 题目链接

- [1029. 两地调度 - 力扣](https://leetcode.cn/problems/two-city-scheduling/)

## 题目大意

**描述**：公司计划面试 `2 * n` 人。给你一个数组 `costs`，其中 `costs[i] = [aCosti, bCosti]`，表示第 `i` 人飞往 `a` 市的费用为 `aCosti` ，飞往 `b` 市的费用为 `bCosti`。

**要求**：返回将每个人都飞到 `a`、`b` 中某座城市的最低费用，要求每个城市都有 `n` 人抵达。

**说明**：

- $2 * n == costs.length$。
- $2 \le costs.length \le 100$。
- $costs.length$ 为偶数。
- $1 \le aCosti, bCosti \le 1000$。

**示例**：

- 示例 1：

```python
输入：costs = [[10,20],[30,200],[400,50],[30,20]]
输出：110
解释：
第一个人去 a 市，费用为 10。
第二个人去 a 市，费用为 30。
第三个人去 b 市，费用为 50。
第四个人去 b 市，费用为 20。

最低总费用为 10 + 30 + 50 + 20 = 110，每个城市都有一半的人在面试。
```

## 解题思路

### 思路 1：贪心算法

我们先假设所有人都去了城市 `a`。然后令一半的人再去城市 `b`。现在的问题就变成了，让一半的人改变城市去向，从原本的 `a` 城市改成 `b` 城市的最低费用为多少。

已知第 `i` 个人更换去向的费用为「去城市 `b` 的费用 - 去城市 `a` 的费用」。所以我们可以根据「去城市 `b` 的费用 - 去城市 `a` 的费用」对数组 `costs` 进行排序，让前 `n` 个改变方向去城市 `b`，后 `n` 个人去城市 `a`。

最后统计所有人员的费用，将其返回即可。

### 思路 1：贪心算法代码

```python
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x:x[1] - x[0])
        cost = 0
        size = len(costs) // 2
        for i in range(size):
            cost += costs[i][ 1]
            cost += costs[i + size][0]

        return cost
```
