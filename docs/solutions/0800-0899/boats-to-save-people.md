# [0881. 救生艇](https://leetcode.cn/problems/boats-to-save-people/)

- 标签：贪心、数组、双指针、排序
- 难度：中等

## 题目链接

- [0881. 救生艇 - 力扣](https://leetcode.cn/problems/boats-to-save-people/)

## 题目大意

**描述**：给定一个整数数组 `people` 代表每个人的体重，其中第 `i` 个人的体重为 `people[i]`。再给定一个整数 `limit`，代表每艘船可以承载的最大重量。每艘船最多可同时载两人，但条件是这些人的重量之和最多为 `limit`。

**要求**：返回载到每一个人所需的最小船数（保证每个人都能被船载）。

**说明**：

- $1 \le people.length \le 5 \times 10^4$。
- $1 \le people[i] \le limit \le 3 \times 10^4$。

**示例**：

- 示例 1：

```python
输入：people = [1,2], limit = 3
输出：1
解释：1 艘船载 (1, 2)
```

- 示例 2：

```python
输入：people = [3,2,2,1], limit = 3
输出：3
解释：3 艘船分别载 (1, 2), (2) 和 (3)
```

## 解题思路

### 思路 1：贪心算法 + 双指针

暴力枚举的时间复杂度为 $O(n^2)$。使用双指针可以减少循环内的时间复杂度。

我们可以利用贪心算法的思想，让最重的和最轻的人一起走。这样一只船就可以尽可能的带上两个人。

具体做法如下：

1. 先对数组进行升序排序，使用 `ans` 记录所需最小船数。
2. 使用两个指针 `left`、`right`。`left` 指向数组开始位置，`right` 指向数组结束位置。
3. 判断 `people[left]` 和 `people[right]` 加一起是否超重。
   1. 如果 `people[left] + people[right] > limit`，则让重的人上船，船数量 + 1，令 `right` 左移，继续判断。
   2. 如果 `people[left] + people[right] <= limit`，则两个人都上船，船数量 + 1，并令 `left` 右移，`right` 左移，继续判断。
4. 如果 `lefft == right`，则让最后一个人上船，船数量 + 1。并返回答案。

### 思路 1：代码

```python
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        size = len(people)
        left, right = 0, size - 1
        ans = 0
        while left < right:
            if people[left] + people[right] > limit:
                right -= 1
            else:
                left += 1
                right -= 1
            ans += 1
        if left == right:
            ans += 1
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times \log n)$，其中 $n$ 是数组 `people` 的长度。
- **空间复杂度**：$O(\log n)$。

