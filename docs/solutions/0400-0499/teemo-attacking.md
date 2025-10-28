# [0495. 提莫攻击](https://leetcode.cn/problems/teemo-attacking/)

- 标签：数组、模拟
- 难度：简单

## 题目链接

- [0495. 提莫攻击 - 力扣](https://leetcode.cn/problems/teemo-attacking/)

## 题目大意

**描述**：

在《英雄联盟》的世界中，有一个叫「提莫」的英雄。他的攻击可以让敌方英雄艾希（编者注：寒冰射手）进入中毒状态。

当提莫攻击艾希，艾希的中毒状态正好持续 $duration$ 秒。

正式地讲，提莫在 $t$ 发起攻击意味着艾希在时间区间 $[t, t + duration - 1]$（含 $t$ 和 $t + duration - 1$）处于中毒状态。如果提莫在中毒影响结束「前」再次攻击，中毒状态计时器将会「重置」，在新的攻击之后，中毒影响将会在 $duration$ 秒后结束。

给定一个「非递减」的整数数组 $timeSeries$ ，其中 $timeSeries[i]$ 表示提莫在 $timeSeries[i]$ 秒时对艾希发起攻击，以及一个表示中毒持续时间的整数 $duration$。

**要求**：

返回艾希处于中毒状态的总秒数。

**说明**：

- $1 \le timeSeries.length \le 10^{4}$。
- $0 \le timeSeries[i], duration \le 10^{7}$。
- $timeSeries$ 按非递减顺序排列。

**示例**：

- 示例 1：

```python
输入：timeSeries = [1,4], duration = 2
输出：4
解释：提莫攻击对艾希的影响如下：
- 第 1 秒，提莫攻击艾希并使其立即中毒。中毒状态会维持 2 秒，即第 1 秒和第 2 秒。
- 第 4 秒，提莫再次攻击艾希，艾希中毒状态又持续 2 秒，即第 4 秒和第 5 秒。
艾希在第 1、2、4、5 秒处于中毒状态，所以总中毒秒数是 4。
```

- 示例 2：

```python
输入：timeSeries = [1,2], duration = 2
输出：3
解释：提莫攻击对艾希的影响如下：
- 第 1 秒，提莫攻击艾希并使其立即中毒。中毒状态会维持 2 秒，即第 1 秒和第 2 秒。
- 第 2 秒，提莫再次攻击艾希，并重置中毒计时器，艾希中毒状态需要持续 2 秒，即第 2 秒和第 3 秒。
艾希在第 1、2、3 秒处于中毒状态，所以总中毒秒数是 3。
```

## 解题思路

### 思路 1：贪心算法

**核心思想**：使用贪心算法，按顺序处理每次攻击，计算相邻两次攻击之间前一次攻击贡献的中毒秒数。

**算法步骤**：

1. 初始化总中毒秒数 $res = 0$。
2. 遍历攻击时刻数组，设相邻两次攻击的时间差为 $gap = timeSeries[i+1] - timeSeries[i]$。
3. 判断时间差 $gap$ 与持续时间 $duration$ 的关系：
   - 如果 $gap \ge duration$：说明前一次中毒已经完全结束，前一次攻击贡献 $duration$ 秒，将 $duration$ 累加到 $res$。
   - 如果 $gap < duration$：说明前一次中毒还没结束就被重置了，只贡献了 $gap$ 秒，将 $gap$ 累加到 $res$。
4. 最后一次攻击总是完整贡献 $duration$ 秒，将其累加到 $res$。
5. 返回总中毒秒数 $res$。

**关键点**：通过比较相邻攻击的时间间隔和中毒持续时间，确定每次攻击实际贡献的中毒秒数。

### 思路 1：代码

```python
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        # 初始化总中毒秒数
        res = 0
        
        # 遍历攻击时刻数组
        for i in range(len(timeSeries) - 1):
            # 计算相邻两次攻击的时间差
            gap = timeSeries[i + 1] - timeSeries[i]
            
            if gap >= duration:
                # 前一次中毒完全结束，贡献 duration 秒
                res += duration
            else:
                # 前一次中毒被重置，只贡献 gap 秒
                res += gap
        
        # 最后一次攻击总是完整贡献 duration 秒
        res += duration
        
        return res
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。其中 $n$ 是数组 $timeSeries$ 的长度。需要遍历数组一次。
- **空间复杂度**：$O(1)$。只使用常数额外空间。
