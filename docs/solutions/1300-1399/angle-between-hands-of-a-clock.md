# [1344. 时钟指针的夹角](https://leetcode.cn/problems/angle-between-hands-of-a-clock/)

- 标签：数学
- 难度：中等

## 题目链接

- [1344. 时钟指针的夹角 - 力扣](https://leetcode.cn/problems/angle-between-hands-of-a-clock/)

## 题目大意

**描述**：给定两个数 $hour$ 和 $minutes$。

**要求**：请你返回在时钟上，由给定时间的时针和分针组成的较小角的角度（$60$ 单位制）。

**说明**：

- $1 \le hour \le 12$。
- $0 \le minutes \le 59$。
- 与标准答案误差在 $10^{-5}$ 以内的结果都被视为正确结果。

**示例**：

- 示例 1：

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/02/08/sample_1_1673.png)

```python
输入：hour = 12, minutes = 30
输出：165
```

- 示例 2：

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/02/08/sample_2_1673.png)

```python
输入：hour = 3, minutes = 30
输出；75
```

## 解题思路

### 思路 1：数学

1. 我们以 $00:00$ 为基准，分别计算出分针与 $00:00$ 中垂线的夹角，以及时针与 $00:00$ 中垂线的夹角。
2. 然后计算出两者差值的绝对值 $diff$。当前差值可能为较小的角（小于 $180°$ 的角），也可能为较大的角（大于等于 $180°$ 的角）。
3. 将差值的绝对值 $diff$ 与 $360 - diff$ 进行比较，取较小值作为答案。

### 思路 1：代码

```Python
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        mins_angle = 6 * minutes
        hours_angle = (hour % 12 + minutes / 60) * 30

        diff = abs(hours_angle - mins_angle)
        return min(diff, 360 - diff)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(1)$。
- **空间复杂度**：$O(1)$。

