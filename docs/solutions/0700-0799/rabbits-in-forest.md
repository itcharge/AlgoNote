# [0781. 森林中的兔子](https://leetcode.cn/problems/rabbits-in-forest/)

- 标签：贪心、数组、哈希表、数学
- 难度：中等

## 题目链接

- [0781. 森林中的兔子 - 力扣](https://leetcode.cn/problems/rabbits-in-forest/)

## 题目大意

**描述**：

森林中有未知数量的兔子。提问其中若干只兔子 `"还有多少只兔子与你（指被提问的兔子）颜色相同?"`，将答案收集到一个整数数组 $answers$ 中，其中 $answers[i]$ 是第 $i$ 只兔子的回答。

给定数组 $answers$。

**要求**：

返回森林中兔子的最少数量。

**说明**：

- $1 \le answers.length \le 10^{3}$。
- $0 \le answers[i] \lt 10^{3}$。

**示例**：

- 示例 1：

```python
输入：answers = [1,1,2]
输出：5
解释：
两只回答了 "1" 的兔子可能有相同的颜色，设为红色。 
之后回答了 "2" 的兔子不会是红色，否则他们的回答会相互矛盾。
设回答了 "2" 的兔子为蓝色。 
此外，森林中还应有另外 2 只蓝色兔子的回答没有包含在数组中。 
因此森林中兔子的最少数量是 5 只：3 只回答的和 2 只没有回答的。
```

- 示例 2：

```python
输入：answers = [10,10,10]
输出：11
```

## 解题思路

### 思路 1：贪心 + 哈希表

如果一只兔子回答 $x$，说明包括它自己在内，有 $x + 1$ 只相同颜色的兔子。为了使兔子总数最少，我们应该让回答相同的兔子尽可能属于同一组。

**实现步骤**：

1. 使用哈希表统计每个回答出现的次数。
2. 对于回答 $x$ 的兔子：
   - 每 $x + 1$ 只回答 $x$ 的兔子可以是同一颜色。
   - 如果有 $count$ 只兔子回答 $x$，则至少需要 $\lceil \frac{count}{x + 1} \rceil$ 组，每组有 $x + 1$ 只兔子。
   - 总数为 $\lceil \frac{count}{x + 1} \rceil \times (x + 1)$。
3. 将所有颜色的兔子数量相加。

### 思路 1：代码

```python
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        from collections import Counter
        
        # 统计每个回答出现的次数
        count = Counter(answers)
        
        total = 0
        for x, cnt in count.items():
            # 每组有 x + 1 只兔子
            group_size = x + 1
            # 需要的组数（向上取整）
            groups = (cnt + group_size - 1) // group_size
            # 总兔子数
            total += groups * group_size
        
        return total
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是 $answers$ 的长度。
- **空间复杂度**：$O(n)$，哈希表的空间。
