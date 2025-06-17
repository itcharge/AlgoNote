# [0042. 接雨水](https://leetcode.cn/problems/trapping-rain-water/)

- 标签：栈、数组、双指针、动态规划、单调栈
- 难度：困难

## 题目链接

- [0042. 接雨水 - 力扣](https://leetcode.cn/problems/trapping-rain-water/)

## 题目大意

**描述**：给定 `n` 个非负整数表示每个宽度为 `1` 的柱子的高度图，用数组 `height` 表示，其中 `height[i]` 表示第 `i` 根柱子的高度。

**要求**：计算按此排列的柱子，下雨之后能接多少雨水。

**说明**：

- $n == height.length$。
- $1 \le n \le 2 * 10^4$。
- $0 \le height[i] \le 10^5$。

**示例**：

- 示例 1：

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/22/rainwatertrap.png)

```python
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
```

- 示例 2：

```python
输入：height = [4,2,0,3,2,5]
输出：9
```

## 解题思路

### 思路 1：单调栈

1. 遍历高度数组 `height`。
2. 如果当前柱体高度较小，小于等于栈顶柱体的高度，则将当前柱子高度入栈。
3. 如果当前柱体高度较大，大于栈顶柱体的高度，则一直出栈，直到当前柱体小于等于栈顶柱体的高度。
4. 假设当前柱体为 `C`，出栈柱体为 `B`，出栈之后新的栈顶柱体为 `A`。则说明：
   1. 当前柱体 `C` 是出栈柱体 `B` 向右找到的第一个大于当前柱体高度的柱体，那么以出栈柱体 `B`  为中心，可以向右将宽度扩展到当前柱体 `C`。
   2. 新的栈顶柱体 `A` 是出栈柱体 `B` 向左找到的第一个大于当前柱体高度的柱体，那么以出栈柱体 `B` 为中心，可以向左将宽度扩展到当前柱体 `A`。
5. 出栈后，以新的栈顶柱体 `A` 为左边界，以当前柱体 `C` 为右边界，以左右边界与出栈柱体 `B` 的高度差为深度，计算可以接到雨水的面积。然后记录并更新累积面积。

### 思路 1：代码

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        stack = []
        size = len(height)
        for i in range(size):
            while stack and height[i] > height[stack[-1]]:
                cur = stack.pop(-1)
                if stack:
                    left = stack[-1] + 1
                    right = i - 1
                    high = min(height[i], height[stack[-1]]) - height[cur]
                    ans += high * (right - left + 1)
                else:
                    break
            stack.append(i)
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是数组 `height` 的长度。
- **空间复杂度**：$O(n)$。