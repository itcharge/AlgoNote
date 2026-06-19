# [1304. 和为零的 N 个不同整数](https://leetcode.cn/problems/find-n-unique-integers-sum-up-to-zero/)

- 标签：数组、数学
- 难度：简单

## 题目链接

- [1304. 和为零的 N 个不同整数 - 力扣](https://leetcode.cn/problems/find-n-unique-integers-sum-up-to-zero/)

## 题目大意

**描述**：给定整数 $n$。

**要求**：返回一个包含 $n$ 个不同整数的数组，这些整数的和为 $0$。

**示例**：

- 示例 1：

```python
输入：n = 5
输出：[-7,-1,1,3,4]
解释：这些数组也是正确的 [-5,-1,1,2,3]，[-3,-1,2,-2,4]。
```

- 示例 2：

```python
输入：n = 3
输出：[-1,0,1]
```


## 解题思路

### 思路 1：数学构造

#### 1. 核心思想

将 $1$ 到 $n-1$ 放入数组，最后一个元素放这些数的和的相反数，即可保证总和为 $0$。

#### 2. 代码

```python
class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = list(range(1, n))
        ans.append(-sum(ans))
        return ans
```

### 思路 1：复杂度分析
- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(n)$。
