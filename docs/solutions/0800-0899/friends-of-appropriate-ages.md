# [0825. 适龄的朋友](https://leetcode.cn/problems/friends-of-appropriate-ages/)

- 标签：数组、双指针、二分查找、排序
- 难度：中等

## 题目链接

- [0825. 适龄的朋友 - 力扣](https://leetcode.cn/problems/friends-of-appropriate-ages/)

## 题目大意

**描述**：

在社交媒体网站上有 $n$ 个用户。给你一个整数数组 $ages$，其中 $ages[i]$ 是第 $i$ 个用户的年龄。
如果下述任意一个条件为真，那么用户 $x$ 将不会向用户 $y$（$x \ne y$）发送好友请求：

- $ages[y] \le 0.5 \times ages[x] + 7$
- $ages[y] > ages[x]$
- $ages[y] > 100 && ages[x] < 100$

否则，$x$ 将会向 $y$ 发送一条好友请求。

注意，如果 $x$ 向 $y$ 发送一条好友请求，$y$ 不必也向 $x$ 发送一条好友请求。另外，用户不会向自己发送好友请求。

**要求**：

返回在该社交媒体网站上产生的好友请求总数。

**说明**：

- $n == ages.length$。
- $1 \le n \le 2 \times 10^{4}$。
- $1 \le ages[i] \le 120$。

**示例**：

- 示例 1：

```python
输入：ages = [16,16]
输出：2
解释：2 人互发好友请求。
```

- 示例 2：

```python
输入：ages = [16,17,18]
输出：2
解释：产生的好友请求为 17 -> 16 ，18 -> 17 。
```

## 解题思路

### 思路 1：计数 + 数学

这道题要求计算好友请求的总数。根据题意，用户 $x$ 不会向用户 $y$ 发送好友请求的条件是：

1. $ages[y] \le 0.5 \times ages[x] + 7$
2. $ages[y] > ages[x]$
3. $ages[y] > 100$ 且 $ages[x] < 100$

反过来，$x$ 会向 $y$ 发送好友请求的条件是：

- $0.5 \times ages[x] + 7 < ages[y] \le ages[x]$

由于年龄范围只有 $1$ 到 $120$，我们可以使用计数数组来统计每个年龄的人数，然后枚举所有可能的年龄对。

算法步骤：

1. 使用计数数组 $count$ 统计每个年龄的人数。
2. 枚举所有可能的年龄对 $(ageX, ageY)$。
3. 如果满足发送好友请求的条件，累加请求数：
   - 如果 $ageX == ageY$，则请求数为 $count[ageX] \times (count[ageX] - 1)$（同年龄的人互相发送，但不向自己发送）。
   - 如果 $ageX \ne ageY$，则请求数为 $count[ageX] \times count[ageY]$。

### 思路 1：代码

```python
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        # 统计每个年龄的人数
        count = [0] * 121
        for age in ages:
            count[age] += 1
        
        result = 0
        # 枚举所有可能的年龄对
        for ageX in range(1, 121):
            if count[ageX] == 0:
                continue
            for ageY in range(1, 121):
                if count[ageY] == 0:
                    continue
                # 判断 x 是否会向 y 发送好友请求
                if ageY <= 0.5 * ageX + 7:
                    continue
                if ageY > ageX:
                    continue
                if ageY > 100 and ageX < 100:
                    continue
                # 累加请求数
                if ageX == ageY:
                    result += count[ageX] * (count[ageX] - 1)
                else:
                    result += count[ageX] * count[ageY]
        
        return result
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n + C^2)$，其中 $n$ 是数组 $ages$ 的长度，$C = 120$ 是年龄的范围。需要遍历数组统计年龄，然后枚举所有年龄对。
- **空间复杂度**：$O(C)$，需要使用计数数组存储每个年龄的人数。
