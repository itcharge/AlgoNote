# [1370. 上升下降字符串](https://leetcode.cn/problems/increasing-decreasing-string/)

- 标签：哈希表、字符串、计数
- 难度：简单

## 题目链接

- [1370. 上升下降字符串 - 力扣](https://leetcode.cn/problems/increasing-decreasing-string/)

## 题目大意

**描述**：给定一个字符串 $s$。

**要求**：按照以下步骤重新排列字符：
1. 从 $s$ 中选出最小的字符追加到结果。
2. 从剩余字符中选出比上一个字符大的最小字符追加。
3. 重复直到没有更大的字符。
4. 从剩余字符中选出最大的字符追加。
5. 从剩余字符中选出比上一个字符小的最大字符追加。
6. 重复直到没有更小的字符。
7. 重复 1-6 直到所有字符用完。

**示例**：

- 示例 1：

```python
输入：s = "aaaabbbbcccc"
输出："abccbaabccba"
解释：第一轮的步骤 1，2，3 后，结果字符串为 result = "abc"
第一轮的步骤 4，5，6 后，结果字符串为 result = "abccba"
第一轮结束，现在 s = "aabbcc" ，我们再次回到步骤 1
第二轮的步骤 1，2，3 后，结果字符串为 result = "abccbaabc"
第二轮的步骤 4，5，6 后，结果字符串为 result = "abccbaabccba"
```

- 示例 2：

```python
输入：s = "rat"
输出："art"
解释：单词 "rat" 在上述算法重排序以后变成 "art"
```


## 解题思路

### 思路 1：计数排序

#### 1. 核心思想

用长度为 $26$ 的计数数组统计每个字母的出现次数。按规则交替从 `'a'` 到 `'z'` 和从 `'z'` 到 `'a'` 遍历，每取一个字符计数减 $1$，直到所有计数为 $0$。

#### 2. 代码

```python
class Solution:
    def sortString(self, s: str) -> str:
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1
        ans = []
        while len(ans) < len(s):
            for i in range(26):
                if cnt[i]:
                    ans.append(chr(ord('a') + i))
                    cnt[i] -= 1
            for i in range(25, -1, -1):
                if cnt[i]:
                    ans.append(chr(ord('a') + i))
                    cnt[i] -= 1
        return ''.join(ans)
```

### 思路 1：复杂度分析
- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(1)$。
