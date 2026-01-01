# [0551. 学生出勤记录 I](https://leetcode.cn/problems/student-attendance-record-i/)

- 标签：字符串
- 难度：简单

## 题目链接

- [0551. 学生出勤记录 I - 力扣](https://leetcode.cn/problems/student-attendance-record-i/)

## 题目大意

**描述**：

给定一个字符串 $s$ 表示一个学生的出勤记录，其中的每个字符用来标记当天的出勤情况（缺勤、迟到、到场）。记录中只含下面三种字符：

- `A`：Absent，缺勤
- `L`：Late，迟到
- `P`：Present，到场

如果学生能够 同时 满足下面两个条件，则可以获得出勤奖励：

- 按「总出勤」计，学生缺勤（`A`）严格 少于两天。
- 学生 不会 存在 连续 3 天或 连续 3 天以上的迟到（`L`）记录。

**要求**：

如果学生可以获得出勤奖励，返回 true ；否则，返回 false 。

**说明**：

- $1 \le s.length \le 10^{3}$。
- $s[i]$ 为 `A`、`L` 或 `P`。

**示例**：

- 示例 1：

```python
输入：s = "PPALLP"
输出：true
解释：学生缺勤次数少于 2 次，且不存在 3 天或以上的连续迟到记录。
```

- 示例 2：

```python
输入：s = "PPALLL"
输出：false
解释：学生最后三天连续迟到，所以不满足出勤奖励的条件。
```

## 解题思路

### 思路 1：遍历检查

根据题目要求，需要同时满足两个条件：

1. 缺勤（`A`）次数严格少于 2 天，即 $count_A < 2$
2. 不存在连续 3 天或以上的迟到（`L`）记录

遍历字符串，统计：

- `A` 的出现次数
- 连续 `L` 的最大长度

如果 `A` 次数 $\ge 2$ 或存在连续 3 个或以上的 `L`，返回 `False`；否则返回 `True`。

### 思路 1：代码

```python
class Solution:
    def checkRecord(self, s: str) -> bool:
        absent_count = 0
        late_streak = 0
        max_late_streak = 0
        
        for char in s:
            if char == 'A':
                absent_count += 1
                late_streak = 0
            elif char == 'L':
                late_streak += 1
                max_late_streak = max(max_late_streak, late_streak)
            else:  # 'P'
                late_streak = 0
        
        # 检查条件：缺勤少于 2 次，且没有连续 3 天或以上的迟到
        return absent_count < 2 and max_late_streak < 3
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是字符串长度，需要遍历字符串一次。
- **空间复杂度**：$O(1)$，只使用了常数额外空间。
