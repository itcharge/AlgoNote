# [0350. 两个数组的交集 II](https://leetcode.cn/problems/intersection-of-two-arrays-ii/)

- 标签：数组、哈希表
- 难度：简单

## 题目链接

- [0350. 两个数组的交集 II - 力扣](https://leetcode.cn/problems/intersection-of-two-arrays-ii/)

## 题目大意

**描述**：给定两个数组 $nums1$ 和 $nums2$。

**要求**：返回两个数组的交集。可以不考虑输出结果的顺序。

**说明**：

- 输出结果中，每个元素出现的次数，应该与元素在两个数组中都出现的次数一致（如果出现次数不一致，则考虑取较小值）。
- $1 \le nums1.length, nums2.length \le 1000$。
- $0 \le nums1[i], nums2[i] \le 1000$。

**示例**：

```python
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]


输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]
```

## 解题思路

### 思路 1：哈希表

1. 先遍历第一个数组，利用字典来存放第一个数组的元素出现次数。
2. 然后遍历第二个数组，如果字典中存在该元素，则将该元素加入到答案数组中，并减少字典中该元素出现的次数。
3. 遍历完之后，返回答案数组。

### 思路 1：代码

```python
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numDict = dict()
        nums = []
        for num in nums1:
            if num in numDict:
                numDict[num] += 1
            else:
                numDict[num] = 1
        for num in nums2:
            if num in numDict and numDict[num] != 0:
                numDict[num] -= 1
                nums.append(num)
        return nums
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(n)$。