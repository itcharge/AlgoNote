# [1716. 计算力扣银行的钱](https://leetcode.cn/problems/calculate-money-in-leetcode-bank/)

- 标签：数学
- 难度：简单

## 题目链接

- [1716. 计算力扣银行的钱 - 力扣](https://leetcode.cn/problems/calculate-money-in-leetcode-bank/)

## 题目大意

**描述**：Hercy 每天都往力扣银行里存钱。

最开始，他在周一的时候存入 $1$ 块钱。从周二到周日，他每天都比前一天多存入 $1$ 块钱。在接下来的每个周一，他都会比前一个周一多存入 $1$ 块钱。

给定一个整数 $n$。

**要求**：计算在第 $n$ 天结束的时候，Hercy 在力扣银行中总共存了多少块钱。

**说明**：

- $1 \le n \le 1000$。

**示例**：

- 示例 1：

```python
输入：n = 4
输出：10
解释：第 4 天后，总额为 1 + 2 + 3 + 4 = 10。
```

- 示例 2：

```python
输入：n = 10
输出：37
解释：第 10 天后，总额为 (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37 。注意到第二个星期一，Hercy 存入 2 块钱。
```

## 解题思路

### 思路 1：暴力模拟

1. 记录当前周 $week$ 和当前周的当前天数 $day$。
2. 按照题目要求，每天增加 $1$ 块钱，每周一比上周一增加 $1$ 块钱。这样，每天存钱数为 $week + day - 1$。
3. 将每天存的钱数累加起来即为答案。

### 思路 1：代码

```python
class Solution:
    def totalMoney(self, n: int) -> int:
        weak, day = 1, 1
        ans = 0
        for i in range(n):
            ans += weak + day - 1
            day += 1
            if day == 8:
                day = 1
                weak += 1
        
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(1)$。

### 思路 2：等差数列计算优化

每周一比上周一增加 $1$ 块钱，则每周七天存钱总数比上一周多 $7$ 块钱。所以每周存的钱数是一个等差数列。我们可以通过高斯求和公式求出所有整周存的钱数，再计算出剩下天数存的钱数，两者相加即为答案。

### 思路 2：代码

```python
class Solution:
    def totalMoney(self, n: int) -> int:
        week_cnt = n // 7
        weak_first_money = (1 + 7) * 7 // 2
        weak_last_money = weak_first_money + 7 * (week_cnt - 1)
        week_ans =  (weak_first_money + weak_last_money) * week_cnt // 2

        day_cnt = n % 7
        day_first_money = 1 + week_cnt
        day_last_money = day_first_money + day_cnt - 1
        day_ans = (day_first_money + day_last_money) * day_cnt // 2
        
        return week_ans + day_ans
```

### 思路 2：复杂度分析

- **时间复杂度**：$O(1)$。
- **空间复杂度**：$O(1)$。
