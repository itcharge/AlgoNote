# [2023. 连接后等于目标字符串的字符串对](https://leetcode.cn/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/)

- 标签：数组、字符串
- 难度：中等

## 题目链接

- [2023. 连接后等于目标字符串的字符串对 - 力扣](https://leetcode.cn/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/)

## 题目大意

**描述**：给定一个数字字符串数组 `nums` 和一个数字字符串 `target`。

**要求**：返回 `nums[i] + nums[j]` （两个字符串连接，其中 `i != j`）结果等于 `target` 的下标 `(i, j)` 的数目。

**说明**：

- $2 \le nums.length \le 100$。
- $1 \le nums[i].length \le 100$。
- $2 \le target.length \le 100$。
- `nums[i]` 和 `target` 只包含数字。
- `nums[i]` 和 `target` 不含有任何前导 $0$。

**示例**：

- 示例 1：

```python
输入：nums = ["777","7","77","77"], target = "7777"
输出：4
解释：符合要求的下标对包括：
- (0, 1)："777" + "7"
- (1, 0)："7" + "777"
- (2, 3)："77" + "77"
- (3, 2)："77" + "77"
```

- 示例 2：

```python
输入：nums = ["123","4","12","34"], target = "1234"
输出：2
解释：符合要求的下标对包括
- (0, 1)："123" + "4"
- (2, 3)："12" + "34"
```

## 解题思路

### 思路 1：暴力枚举

1. 双重循环遍历所有的 `i` 和 `j`，满足 `i != j` 并且 `nums[i] + nums[j] == target` 时，记入到答案数目中。
2. 遍历完，返回答案数目。

### 思路 1：代码

```python
class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    res += 1
        
        return res
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^2)$。
- **空间复杂度**：$O(1)$。

### 思路 2：哈希表

1. 使用哈希表记录字符串数组 `nums` 中所有数字字符串的数量。
2. 遍历哈希表中的键 `num`。
3. 将 `target` 根据 `num` 的长度分为前缀 `prefix` 和 `suffix`。
4. 如果 `num` 等于 `prefix`，则判断后缀 `suffix` 是否在哈希表中，如果在哈希表中，则说明 `prefix` 和 `suffix` 能够拼接为 `target`。
   1. 如果 `num` 等于 `suffix`，此时 `perfix == suffix`，则答案数目累积为 `table[prefix] * (table[suffix] - 1)`。
   2. 如果 `num` 不等于 `suffix`，则答案数目累积为 `table[prefix] * table[suffix]`。
5. 最后输出答案数目。

### 思路 2：代码

```python
class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        res = 0
        table = collections.defaultdict(int)
        for num in nums:
            table[num] += 1

        for num in table:
            size = len(num)
            prefix, suffix = target[ :size], target[size: ]
            if num == prefix and suffix in table:
                if num == suffix:
                    res += table[prefix] * (table[suffix] - 1)
                else:
                    res += table[prefix] * table[suffix]
        
        return res
```

### 思路 2：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(n)$。