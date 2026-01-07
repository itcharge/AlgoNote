# [0893. 特殊等价字符串组](https://leetcode.cn/problems/groups-of-special-equivalent-strings/)

- 标签：数组、哈希表、字符串、排序
- 难度：中等

## 题目链接

- [0893. 特殊等价字符串组 - 力扣](https://leetcode.cn/problems/groups-of-special-equivalent-strings/)

## 题目大意

**描述**：

给定一个字符串数组 $words$。

一步操作中，你可以交换字符串 $words[i]$ 的任意两个偶数下标对应的字符或任意两个奇数下标对应的字符。
对两个字符串 $words[i]$ 和 $words[j]$ 而言，如果经过任意次数的操作，$words[i] == words[j]$，那么这两个字符串是 特殊等价 的。

- 例如，$words[i] = "zzxy"$ 和 $words[j] = "xyzz"$ 是一对「特殊等价」字符串，因为可以按 `"zzxy"` -> `"xzzy"` -> `"xyzz"` 的操作路径使 $words[i] == words[j]$。

现在规定，$words$ 的「一组特殊等价字符串」就是 $words$ 的一个同时满足下述条件的非空子集：

- 该组中的每一对字符串都是 特殊等价 的
- 该组字符串已经涵盖了该类别中的所有特殊等价字符串，容量达到理论上的最大值（也就是说，如果一个字符串不在该组中，那么这个字符串就 不会 与该组内任何字符串特殊等价）

**要求**：

返回 $words$ 中「特殊等价字符串组」的数量。

**说明**：

- $1 \le words.length \le 10^{3}$。
- $1 \le words[i].length \le 20$。
- 所有 $words[i]$ 都只由小写字母组成。
- 所有 $words[i]$ 都具有相同的长度。

**示例**：

- 示例 1：

```python
输入：words = ["abcd","cdab","cbad","xyzz","zzxy","zzyx"]
输出：3
解释：
其中一组为 ["abcd", "cdab", "cbad"]，因为它们是成对的特殊等价字符串，且没有其他字符串与这些字符串特殊等价。
另外两组分别是 ["xyzz", "zzxy"] 和 ["zzyx"]。特别需要注意的是，"zzxy" 不与 "zzyx" 特殊等价。
```

- 示例 2：

```python
输入：words = ["abc","acb","bac","bca","cab","cba"]
输出：3
解释：3 组 ["abc","cba"]，["acb","bca"]，["bac","cab"]
```

## 解题思路

### 思路 1：哈希表

这道题要求统计特殊等价字符串组的数量。两个字符串特殊等价的条件是：可以任意交换偶数位置的字符，也可以任意交换奇数位置的字符。

关键观察：

- 如果两个字符串特殊等价，那么它们的偶数位置字符集合相同，奇数位置字符集合也相同。
- 可以将字符串的偶数位置字符排序后和奇数位置字符排序后拼接，作为该字符串的"签名"。
- 特殊等价的字符串具有相同的签名。

算法步骤：

1. 对于每个字符串，提取偶数位置和奇数位置的字符。
2. 分别对偶数位置和奇数位置的字符排序。
3. 将排序后的字符拼接作为签名。
4. 使用哈希集合统计不同签名的数量。

### 思路 1：代码

```python
class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        def get_signature(word):
            # 提取偶数位置和奇数位置的字符
            even_chars = []
            odd_chars = []
            for i, char in enumerate(word):
                if i % 2 == 0:
                    even_chars.append(char)
                else:
                    odd_chars.append(char)
            
            # 排序后拼接作为签名
            even_chars.sort()
            odd_chars.sort()
            return ''.join(even_chars) + '|' + ''.join(odd_chars)
        
        # 使用哈希集合统计不同签名的数量
        signatures = set()
        for word in words:
            signatures.add(get_signature(word))
        
        return len(signatures)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times m \log m)$，其中 $n$ 是字符串数组的长度，$m$ 是字符串的平均长度。需要遍历每个字符串并对其字符排序。
- **空间复杂度**：$O(n \times m)$，需要使用哈希集合存储签名。
