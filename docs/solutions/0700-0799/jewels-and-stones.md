# [0771. 宝石与石头](https://leetcode.cn/problems/jewels-and-stones/)

- 标签：哈希表、字符串
- 难度：简单

## 题目链接

- [0771. 宝石与石头 - 力扣](https://leetcode.cn/problems/jewels-and-stones/)

## 题目大意

**描述**：给定一个字符串 $jewels$ 代表石头中宝石的类型，再给定一个字符串 $stones$ 代表你拥有的石头。$stones$ 中每个字符代表了一种你拥有的石头的类型。

**要求**：计算出拥有的石头中有多少是宝石。

**说明**：

- 字母区分大小写，因此 $a$ 和 $A$ 是不同类型的石头。
- $1 \le jewels.length, stones.length \le 50$。
- $jewels$ 和 $stones$ 仅由英文字母组成。
- $jewels$ 中的所有字符都是唯一的。

**示例**：

- 示例 1：

```python
输入：jewels = "aA", stones = "aAAbbbb"
输出：3
```

- 示例 2：

```python
输入：jewels = "z", stones = "ZZ"
输出：0
```

## 解题思路

### 思路 1：哈希表

1. 用 $count$ 来维护石头中的宝石个数。
2. 先使用哈希表或者集合存储宝石。
3. 再遍历数组 $stones$，并统计每块石头是否在哈希表中或集合中。
   1. 如果当前石头在哈希表或集合中，则令 $count$ 加 $1$。
   2. 如果当前石头不在哈希表或集合中，则不统计。
4. 最后返回 $count$。

### 思路 1：代码

```python
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_dict = dict()
        for jewel in jewels:
            jewel_dict[jewel] = 1
        count = 0
        for stone in stones:
            if stone in jewel_dict:
                count += 1
        return count
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(m + n)$，其中 $m$ 是字符串 $jewels$ 的长度，$n$ 是 $stones$ 的长度。
- **空间复杂度**：$O(m)$，其中 $m$ 是字符串 $jewels$ 的长度。

