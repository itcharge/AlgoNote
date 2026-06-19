# [1360. 日期之间隔几天](https://leetcode.cn/problems/number-of-days-between-two-dates/)

- 标签：数学、字符串
- 难度：简单

## 题目链接

- [1360. 日期之间隔几天 - 力扣](https://leetcode.cn/problems/number-of-days-between-two-dates/)

## 题目大意

**描述**：给定两个字符串形式的日期 $date1$ 和 $date2$，格式为 `YYYY-MM-DD`。

**要求**：计算两个日期之间相差的天数（绝对值）。

**说明**：
- 输入的日期在 $1971$ 年到 $2100$ 年之间。
- 闰年判定规则：能被 $4$ 整除但不能被 $100$ 整除，或能被 $400$ 整除。

**示例**：

- 示例 1：

```python
输入：date1 = "2019-06-29", date2 = "2019-06-30"
输出：1
```

- 示例 2：

```python
输入：date1 = "2020-01-15", date2 = "2019-12-31"
输出：15
```


## 解题思路

### 思路 1：公式计算

#### 1. 核心思想

将两个日期分别转换为从公元元年（第 $0$ 年）开始经过的总天数，然后计算差值取绝对值。这种方式将日期比较问题转化为整数比较，避免了复杂的借位计算。

计算某一天到公元元年的总天数，可以分解为：
1. 整年的天数之和
2. 整月的天数之和
3. 当月已过的天数

#### 2. 具体步骤

**第 1 步：判断闰年**

定义函数 $is\_leap(year)$：
- 如果 $year \% 400 == 0$，是闰年
- 如果 $year \% 100 == 0$，不是闰年
- 如果 $year \% 4 == 0$，是闰年
- 否则不是闰年

**第 2 步：计算到公元元年的总天数**

定义函数 $days\_from\_epoch(year, month, day)$：

累加 $1971$ 年到 $year - 1$ 年的天数（每年 $365$ 天，闰年 $+1$ 天）。

累加 $1$ 月到 $month - 1$ 月的天数（用月份天数数组，二月根据闰年判断）。

加上 $day$。

**第 3 步：返回绝对值差**

$res = |days\_from\_epoch(date1) - days\_from\_epoch(date2)|$。

#### 3. 月份天数数组

平年月份天数：$[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]$

闰年时，二月为 $29$ 天。

#### 4. 举例说明

以 $date1 = "2020-01-15"$，$date2 = "2019-12-31"$ 为例：

计算 $date2$ 到公元元年的天数：
- $1971 \sim 2018$ 年总天数
- $2019$ 年 $1 \sim 11$ 月总天数：$31+28+31+30+31+30+31+31+30+31+30 = 334$
- $2019$ 年 $12$ 月 $31$ 天，加上 $31$ 天 → $334 + 31 = 365$（即 $2019$ 年全年）

计算 $date1$ 到公元元年的天数，减去 $date2$ 的，得到差值 $15$。

### 思路 1：代码

```python
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def is_leap(year):
            """判断闰年"""
            return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

        def days_from_epoch(year, month, day):
            """计算从公元元年到给定日期的总天数"""
            # 整年天数
            days = 0
            for y in range(1971, year):
                days += 366 if is_leap(y) else 365

            # 月份天数
            month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if is_leap(year):
                month_days[1] = 29
            for m in range(month - 1):
                days += month_days[m]

            # 当月天数
            days += day
            return days

        # 解析日期字符串
        y1, m1, d1 = map(int, date1.split('-'))
        y2, m2, d2 = map(int, date2.split('-'))

        return abs(days_from_epoch(y1, m1, d1) - days_from_epoch(y2, m2, d2))
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(year)$，需要遍历年份计算整年天数，年份跨度最大约 $130$ 年。
- **空间复杂度**：$O(1)$，只使用了常数个变量。

---

### 思路 2：使用 Python 内置库

#### 1. 核心思想

Python 的 `datetime` 库内置了日期计算功能，可以直接使用。

#### 2. 思路 2：代码

```python
from datetime import datetime

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        d1 = datetime.strptime(date1, "%Y-%m-%d")
        d2 = datetime.strptime(date2, "%Y-%m-%d")
        return abs((d1 - d2).days)
```

#### 3. 思路 2：复杂度分析

- **时间复杂度**：$O(1)$，库函数高效实现。
- **空间复杂度**：$O(1)$。

---

### 思路 3：对比与总结

| 思路 | 优点 | 缺点 |
| --- | --- | --- |
| 手算日期 | 不依赖外部库，面试中可直接实现 | 代码稍长 |
| 内置库 | 代码简洁，不易出错 | 面试中需确认是否允许使用 |

竞赛中推荐使用内置库，手算方法则适合面试场景。
