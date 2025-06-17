# [1184. 公交站间的距离](https://leetcode.cn/problems/distance-between-bus-stops/)

- 标签：数组
- 难度：简单

## 题目链接

- [1184. 公交站间的距离 - 力扣](https://leetcode.cn/problems/distance-between-bus-stops/)

## 题目大意

**描述**：环形公交路线上有 $n$ 个站，序号为 $0 \sim n - 1$。给定一个数组 $distance$ 表示每一对相邻公交站之间的距离，其中 $distance[i]$ 表示编号为 $i$ 的车站与编号为 $(i + 1) \mod n$ 的车站之间的距离。再给定乘客的出发点编号 $start$ 和目的地编号 $destination$。

**要求**：返回乘客从出发点 $start$ 到目的地 $destination$ 之间的最短距离。

**说明**：

- $1 \le n \le 10^4$。
- $distance.length == n$。
- $0 \le start, destination < n$。
- $0 \le distance[i] \le 10^4$。

**示例**：

- 示例 1：

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/09/08/untitled-diagram-1.jpg)

```python
输入：distance = [1,2,3,4], start = 0, destination = 1
输出：1
解释：公交站 0 和 1 之间的距离是 1 或 9，最小值是 1。
```

- 示例 2：

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/09/08/untitled-diagram-1-1.jpg)

```python
输入：distance = [1,2,3,4], start = 0, destination = 2
输出：3
解释：公交站 0 和 2 之间的距离是 3 或 7，最小值是 3。
```

## 解题思路

### 思路 1：简单模拟

1. 因为 $start$ 和 $destination$ 的先后顺序不影响结果，为了方便计算，我们先令 $start \le destination$。
2. 遍历数组 $distance$，计算出 $[start, destination]$ 之间的距离和 $dist$。
3. 计算出环形路线中 $[destination, start]$ 之间的距离和为 $sum(distance) - dist$。
4. 比较 $2 \sim 3$ 中两个距离的大小，将距离最小值作为答案返回。

### 思路 1：代码

```python
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        start, destination = min(start, destination), max(start, destination)
        dist = 0
        for i in range(len(distance)):
            if start <= i < destination:
                dist += distance[i]
        
        return min(dist, sum(distance) - dist)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(1)$。
