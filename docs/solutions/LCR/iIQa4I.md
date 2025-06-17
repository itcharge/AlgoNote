# [LCR 038. 每日温度](https://leetcode.cn/problems/iIQa4I/)

- 标签：栈、数组、单调栈
- 难度：中等

## 题目链接

- [LCR 038. 每日温度 - 力扣](https://leetcode.cn/problems/iIQa4I/)

## 题目大意

给定一个列表 `temperatures`，每一个位置对应每天的气温。要求输出一个列表，列表上每个位置代表如果要观测到更高的气温，至少需要等待的天数。如果之后的气温不再升高，则用 `0` 来代替。

## 解题思路

题目的意思实际上就是给定一个数组，每个位置上有整数值。对于每个位置，在该位置后侧找到第一个比当前值更高的值。求该点与该位置的距离，将所有距离保存为数组返回结果。

很简单的思路是对于每个温度值，向后依次进行搜索，找到比当前温度更高的值。

更好的方式使用「递减栈」。栈中保存元素的下标。

首先，将答案数组全部赋值为 0。然后遍历数组每个位置元素。

- 如果栈为空，则将当前元素的下标入栈。
- 如果栈不为空，且当前数字大于栈顶元素对应数字，则栈顶元素出栈，并计算下标差。
    - 此时当前元素就是栈顶元素的下一个更高值，将其下标差存入答案数组中保存起来，判断栈顶元素。
- 直到当前数字小于或等于栈顶元素，则停止出栈，将当前元素下标入栈。

## 代码

```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        ans = [0 for _ in range(n)]
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                ans[index] = (i - index)
            stack.append(i)
        return ans
```

