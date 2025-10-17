# [0739. 每日温度](https://leetcode.cn/problems/daily-temperatures/)

- 标签：栈、数组、单调栈
- 难度：中等

## 题目链接

- [0739. 每日温度 - 力扣](https://leetcode.cn/problems/daily-temperatures/)

## 题目大意

**描述**：给定一个列表 `temperatures`，`temperatures[i]` 表示第 `i` 天的气温。

**要求**：输出一个列表，列表上每个位置代表「如果要观测到更高的气温，至少需要等待的天数」。如果之后的气温不再升高，则用 `0` 来代替。

**说明**：

- $1 \le temperatures.length \le 10^5$。
- $30 \le temperatures[i] \le 100$。

**示例**：

- 示例 1：

```python
输入: temperatures = [73,74,75,71,69,72,76,73]
输出: [1,1,4,2,1,1,0,0]
```

- 示例 2：

```python
输入: temperatures = [30,40,50,60]
输出: [1,1,1,0]
```

## 解题思路

题目的意思实际上就是给定一个数组，每个位置上有整数值。对于每个位置，在该位置右侧找到第一个比当前元素更大的元素。求「该元素」与「右侧第一个比当前元素更大的元素」之间的距离，将所有距离保存为数组返回结果。

最简单的思路是对于每个温度值，向后依次进行搜索，找到比当前温度更高的值。

更好的方式使用「单调递增栈」，栈中保存元素的下标。

### 思路 1：单调栈

1. 首先，将答案数组 `ans` 全部赋值为 0。然后遍历数组每个位置元素。
2. 如果栈为空，则将当前元素的下标入栈。
3. 如果栈不为空，且当前数字大于栈顶元素对应数字，则栈顶元素出栈，并计算下标差。
4. 此时当前元素就是栈顶元素的下一个更高值，将其下标差存入答案数组 `ans` 中保存起来，判断栈顶元素。
5. 直到当前数字小于或等于栈顶元素，则停止出栈，将当前元素下标入栈。
6. 最后输出答案数组 `ans`。

### 思路 1：代码

```python
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n = len(T)
        stack = []
        ans = [0 for _ in range(n)]
        for i in range(n):
            while stack and T[i] > T[stack[-1]]:
                index = stack.pop()
                ans[index] = (i-index)
            stack.append(i)
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(n)$。

