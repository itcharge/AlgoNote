# [0349. 两个数组的交集](https://leetcode.cn/problems/intersection-of-two-arrays/)

- 标签：数组、哈希表、双指针、二分查找、排序
- 难度：简单

## 题目链接

- [0349. 两个数组的交集 - 力扣](https://leetcode.cn/problems/intersection-of-two-arrays/)

## 题目大意

**描述**：给定两个数组 $nums1$ 和 $nums2$。

**要求**：返回两个数组的交集。重复元素只计算一次。

**说明**：

- $1 \le nums1.length, nums2.length \le 1000$。
- $0 \le nums1[i], nums2[i] \le 1000$。

**示例**：

- 示例 1：

```python
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]
示例 2：
```

- 示例 2：

```python
输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[9,4]
解释：[4,9] 也是可通过的
```

## 解题思路

### 思路 1：哈希表

1. 先遍历第一个数组，利用哈希表来存放第一个数组的元素，对应字典值设为 $1$。
2. 然后遍历第二个数组，如果哈希表中存在该元素，则将该元素加入到答案数组中，并且将该键值清空。

### 思路 1：代码

```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numDict = dict()
        nums = []
        for num in nums1:
            if num not in numDict:
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

### 思路 2：分离双指针

1. 对数组 $nums1$、$nums2$ 先排序。
2. 使用两个指针 $left\underline{\hspace{0.5em}}1$、$left\underline{\hspace{0.5em}}2$。$left\underline{\hspace{0.5em}}1$ 指向第一个数组的第一个元素，即：$left\underline{\hspace{0.5em}}1 = 0$，$left\underline{\hspace{0.5em}}2$ 指向第二个数组的第一个元素，即：$left\underline{\hspace{0.5em}}2 = 0$。
3. 如果 $nums1[left_1]$ 等于 $nums2[left_2]$，则将其加入答案数组（注意去重），并将 $left\underline{\hspace{0.5em}}1$ 和 $left\underline{\hspace{0.5em}}2$ 右移。
4. 如果 $nums1[left_1]$ 小于 $nums2[left_2]$，则将 $left\underline{\hspace{0.5em}}1$ 右移。
5. 如果 $nums1[left_1]$ 大于 $nums2[left_2]$，则将 $left\underline{\hspace{0.5em}}2$ 右移。
6. 最后返回答案数组。

### 思路 2：代码

```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        left_1 = 0
        left_2 = 0
        res = []
        while left_1 < len(nums1) and left_2 < len(nums2):
            if nums1[left_1] == nums2[left_2]:
                if nums1[left_1] not in res:
                    res.append(nums1[left_1])
                left_1 += 1
                left_2 += 1
            elif nums1[left_1] < nums2[left_2]:
                left_1 += 1
            elif nums1[left_1] > nums2[left_2]:
                left_2 += 1
        return res
```

### 思路 2：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(1)$。
