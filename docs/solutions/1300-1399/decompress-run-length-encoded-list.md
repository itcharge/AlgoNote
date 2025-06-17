# [1313. 解压缩编码列表](https://leetcode.cn/problems/decompress-run-length-encoded-list/)

- 标签：数组
- 难度：简单

## 题目链接

- [1313. 解压缩编码列表 - 力扣](https://leetcode.cn/problems/decompress-run-length-encoded-list/)

## 题目大意

**描述**：给定一个以行程长度编码压缩的整数列表 $nums$。

考虑每对相邻的两个元素 $[freq, val] = [nums[2 \times i], nums[2 \times i + 1]]$ （其中 $i \ge 0$ ），每一对都表示解压后子列表中有 $freq$ 个值为 $val$ 的元素，你需要从左到右连接所有子列表以生成解压后的列表。

**要求**：返回解压后的列表。

**说明**：

- $2 \le nums.length \le 100$。
- $nums.length \mod 2 == 0$。
- $1 \le nums[i] \le 100$。

**示例**：

- 示例 1：

```python
输入：nums = [1,2,3,4]
输出：[2,4,4,4]
解释：第一对 [1,2] 代表着 2 的出现频次为 1，所以生成数组 [2]。
第二对 [3,4] 代表着 4 的出现频次为 3，所以生成数组 [4,4,4]。
最后将它们串联到一起 [2] + [4,4,4] = [2,4,4,4]。
```

- 示例 2：

```python
输入：nums = [1,1,2,3]
输出：[1,3,3]
```

## 解题思路

### 思路 1：模拟

1. 以步长为 $2$，遍历数组 $nums$。
2. 对于遍历到的元素 $nums[i]$、$nnums[i + 1]$，将 $nums[i]$ 个 $nums[i + 1]$ 存入答案数组中。
3. 返回答案数组。

### 思路 1：代码

```Python
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(0, len(nums), 2):
            cnts = nums[i]
            for cnt in range(cnts):
                res.append(nums[i + 1])
        
        return res
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n + s)$，其中 $n$ 为数组 $nums$ 的长度，$s$ 是数组 $nums$  中所有偶数下标对应元素之和。
- **空间复杂度**：$O(s)$。

