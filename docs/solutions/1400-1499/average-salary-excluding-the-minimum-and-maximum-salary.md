# [1491. 去掉最低工资和最高工资后的工资平均值](https://leetcode.cn/problems/average-salary-excluding-the-minimum-and-maximum-salary/)

- 标签：数组、排序
- 难度：简单

## 题目链接

- [1491. 去掉最低工资和最高工资后的工资平均值 - 力扣](https://leetcode.cn/problems/average-salary-excluding-the-minimum-and-maximum-salary/)

## 题目大意

**描述**：给定一个整数数组 `salary`，数组中的每一个数都是唯一的，其中 `salary[i]` 是第 `i` 个员工的工资。

**要求**：返回去掉最低工资和最高工资之后，剩下员工工资的平均值。

**说明**：

- $3 \le salary.length \le 100$。
- $10^3 \le salary[i] \le 10^6$。
- $salary[i]$ 是唯一的。
- 与真实值误差在 $10^{-5}$ 以内的结果都将视为正确答案。

**示例**：

- 示例 1：

```python
给定 salary = [1000,2000,3000]
输出 2000.00000
解释 最低工资为 1000，最高工资为 3000，去除最低工资和最高工资之后，剩下员工工资的平均值为 2000 / 1 = 2000
```

## 解题思路

### 思路 1：

因为给定 $salary.length \ge 3$，并且 $salary[i]$ 是唯一的，所以无需考虑最低工资和最高工资是同一个。接下来就是按照题意模拟过程：

- 计算出最小工资为 `min_s`，即 `min_s = min(salary)`。
- 计算出最大工资为 `max_s`，即 `max_s = max(salary)`。
- 计算出所有工资和之后再减去最小工资和最大工资，即 `total = sum(salary) - min_s - max_s`。
- 求剩下工资的平均值，并返回，即 `return total / (len(salary) - 2)`。

## 代码

### 思路 1 代码：

```python
class Solution:
    def average(self, salary: List[int]) -> float:
        min_s, max_s = min(salary), max(salary)
        total = sum(salary) - min_s - max_s
        return total / (len(salary) - 2)
```

