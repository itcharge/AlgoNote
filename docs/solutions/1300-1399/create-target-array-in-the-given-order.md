# [1389. 按既定顺序创建目标数组](https://leetcode.cn/problems/create-target-array-in-the-given-order/)

- 标签：数组、模拟
- 难度：简单

## 题目链接

- [1389. 按既定顺序创建目标数组 - 力扣](https://leetcode.cn/problems/create-target-array-in-the-given-order/)

## 题目大意

**描述**：给定两个数组 $nums$ 和 $index$。需要按顺序将 $nums[i]$ 插入到目标数组的 $index[i]$ 位置。如果 $index[i]$ 已有元素，将该位置及之后的所有元素右移。

**要求**：返回目标数组。

**说明**：
- $1 \le nums.length, index.length \le 100$。
- $0 \le index[i] \le i$。

**示例**：

- 示例 1：

```python
输入：nums = [0,1,2,3,4], index = [0,1,2,2,1]
输出：[0,4,1,3,2]
解释：
nums       index     target
0            0        [0]
1            1        [0,1]
2            2        [0,1,2]
3            2        [0,1,3,2]
4            1        [0,4,1,3,2]
```

- 示例 2：

```python
输入：nums = [1,2,3,4,0], index = [0,1,2,3,0]
输出：[0,1,2,3,4]
解释：
nums       index     target
1            0        [1]
2            1        [1,2]
3            2        [1,2,3]
4            3        [1,2,3,4]
0            0        [0,1,2,3,4]
```


## 解题思路

### 思路 1：模拟

#### 1. 核心思想

用列表模拟插入操作。Python 的列表 $insert$ 方法可以在指定位置插入元素，已有元素自动右移。

#### 2. 代码

```python
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans = []
        for num, idx in zip(nums, index):
            ans.insert(idx, num)
        return ans
```

### 思路 1：复杂度分析
- **时间复杂度**：$O(n^2)$，每次插入是 $O(n)$，共 $n$ 次。
- **空间复杂度**：$O(n)$。
