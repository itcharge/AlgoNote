# [0949. 给定数字能组成的最大时间](https://leetcode.cn/problems/largest-time-for-given-digits/)

- 标签：数组、字符串、回溯、枚举
- 难度：中等

## 题目链接

- [0949. 给定数字能组成的最大时间 - 力扣](https://leetcode.cn/problems/largest-time-for-given-digits/)

## 题目大意

**描述**：

24 小时格式为 `"HH:MM"`，其中 $HH$ 在 00 到 23 之间，$MM$ 在 00 到 59 之间。最小的 24 小时制时间是 `00:00`，而最大的是 `23:59`。从 `00:00` （午夜）开始算起，过得越久，时间越大。

给定一个由 4 位数字组成的数组。

**要求**：

返回可以设置的符合 24 小时制的最大时间。

长度为 5 的字符串，按 `"HH:MM"` 格式返回答案。如果不能确定有效时间，则返回空字符串。

**说明**：

- $arr.length == 4$。
- $0 \le arr[i] \le 9$。

**示例**：

- 示例 1：

```python
输入：arr = [1,2,3,4]
输出："23:41"
解释：有效的 24 小时制时间是 "12:34"，"12:43"，"13:24"，"13:42"，"14:23"，"14:32"，"21:34"，"21:43"，"23:14" 和 "23:41" 。这些时间中，"23:41" 是最大时间。
```

- 示例 2：

```python
输入：arr = [5,5,5,5]
输出：""
解释：不存在有效的 24 小时制时间，因为 "55:55" 无效。
```

## 解题思路

### 思路 1：枚举

#### 思路

这道题要求用 $4$ 个数字组成符合 $24$ 小时制的最大时间。由于只有 $4$ 个数字，我们可以枚举所有可能的排列（共 $4! = 24$ 种），然后检查每个排列是否能组成有效的时间，并记录最大的时间。

有效时间的条件：

- 小时部分：$00 \sim 23$，即第一位 $\le 2$，如果第一位是 $2$，第二位 $\le 3$。
- 分钟部分：$00 \sim 59$，即第三位 $\le 5$。

#### 代码

```python
class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        from itertools import permutations
        
        max_time = -1  # 记录最大时间（用分钟数表示）
        
        # 枚举所有排列
        for perm in permutations(arr):
            hour = perm[0] * 10 + perm[1]
            minute = perm[2] * 10 + perm[3]
            
            # 检查是否是有效时间
            if hour < 24 and minute < 60:
                # 转换为分钟数进行比较
                time_in_minutes = hour * 60 + minute
                max_time = max(max_time, time_in_minutes)
        
        # 如果没有有效时间，返回空字符串
        if max_time == -1:
            return ""
        
        # 将分钟数转换为时间格式
        hour = max_time // 60
        minute = max_time % 60
        return f"{hour:02d}:{minute:02d}"
```

#### 复杂度分析

- **时间复杂度**：$O(1)$，因为数组长度固定为 $4$，排列数固定为 $24$。
- **空间复杂度**：$O(1)$，只使用了常数个额外变量。
