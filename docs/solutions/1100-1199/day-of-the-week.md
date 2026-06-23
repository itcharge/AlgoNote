# [1185. 一周中的第几天](https://leetcode.cn/problems/day-of-the-week/)

- 标签：数学
- 难度：简单

## 题目链接

- [1185. 一周中的第几天 - 力扣](https://leetcode.cn/problems/day-of-the-week/)

## 题目大意

**描述**：给定年、月、日三个整数，判断这一天是星期几。

**要求**：返回 `{"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}` 中的某个值。

**说明**：

- 日期范围：$1971$ 年到 $2100$ 年之间的有效日期。
- $1971$ 年 $1$ 月 $1$ 日是星期五。

**示例**：

- 示例 1：

```python
输入：day = 31, month = 8, year = 2019
输出："Saturday"
```

- 示例 2：

```python
输入：day = 18, month = 7, year = 1999
输出："Sunday"
```

## 解题思路

### 思路 1：蔡勒公式

要知道某天是星期几，最直接的方法是用一个已知的「基准日」来推算。比如我们知道 $1971$ 年 $1$ 月 $1$ 日是星期五，那就可以算出任意一天和这个基准日相差多少天，然后对 7 取余。

不过还有一种更巧妙的方法——**蔡勒公式（Zeller's congruence）**，它可以直接用数学公式算出一个日期是星期几，不需要循环累加。

**蔡勒公式的原理**（不需要硬记，会用就行）：

$$
w = (d + 2 \times m + \lfloor \frac{3 \times (m + 1)}{5} \rfloor + y + \lfloor \frac{y}{4} \rfloor - \lfloor \frac{y}{100} \rfloor + \lfloor \frac{y}{400} \rfloor + 1) \mod 7
$$

其中：
- $w$ 是计算结果，$0$ 表示星期日，$1$ 表示星期一……$6$ 表示星期六。
- $d$ 是日期中的日。
- $m$ 是月份，但要注意一个**特殊处理**：要把 1 月、2 月看作上一年的 13 月、14 月。因为公式的设计是把 3 月当作一年的开始。
- $y$ 是年份（如果月份是 1 月或 2 月，年份要减 1）。

**步骤拆解：**

1. 检查月份。如果是 1 月或 2 月，把月份 +12（变成 13 或 14），年份 -1。
2. 代入公式计算。
3. 根据计算结果从星期数组中取出对应的星期名称。

### 思路 1：代码

```python
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        # 星期名称数组，注意顺序和公式输出对应
        week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        
        # 蔡勒公式的特殊处理：把 1 月、2 月当作上一年的 13 月、14 月
        if month < 3:
            month += 12
            year -= 1
        
        # 蔡勒公式计算星期几
        # // 表示整数除法（向下取整），% 表示取余数
        w = (day + 2 * month + 3 * (month + 1) // 5 + year + year // 4 - year // 100 + year // 400 + 1) % 7
        
        return week[w]
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(1)$。不管哪年哪月，只需要算一次公式。
- **空间复杂度**：$O(1)$。只用了几个固定变量。
