# [1371. 每个元音包含偶数次的最长子字符串](https://leetcode.cn/problems/find-the-longest-substring-containing-vowels-in-even-counts/)

- 标签：位运算、哈希表、字符串、前缀和
- 难度：中等

## 题目链接

- [1371. 每个元音包含偶数次的最长子字符串 - 力扣](https://leetcode.cn/problems/find-the-longest-substring-containing-vowels-in-even-counts/)

## 题目大意

**描述**：给定一个字符串 $s$。

**要求**：返回包含每个元音字母（a、e、i、o、u）出现次数均为偶数的最长子串的长度。

**说明**：
- $1 \le s.length \le 5 \times 10^5$。

**示例**：

- 示例 1：

```python
输入：s = "eleetminicoworoep"
输出：13
解释：最长子字符串是 "leetminicowor" ，它包含 e，i，o 各 2 个，以及 0 个 a，u 。
```

- 示例 2：

```python
输入：s = "leetcodeisgreat"
输出：5
解释：最长子字符串是 "leetc" ，其中包含 2 个 e 。
```


## 解题思路

### 思路 1：位运算 + 前缀和

#### 1. 核心思想

用 5 位二进制数表示 a、e、i、o、u 出现次数的奇偶性（$0$ 表示偶数，$1$ 表示奇数）。遍历时维护当前状态 $mask$。

如果两个位置的 $mask$ 相同，说明这两个位置之间的子串中每个元音出现次数均为偶数。用哈希表记录每个 $mask$ 首次出现的位置，取最大距离。

#### 2. 具体步骤

**第 1 步**：初始化 $mask = 0$，哈希表 ${0: -1}$。

**第 2 步**：遍历字符串，更新 $mask$（用异或切换元音位），如果 $mask$ 已存在则更新答案，否则记录位置。

### 思路 1：代码

```python
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowel = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        mask = 0
        first = {0: -1}
        ans = 0
        for i, ch in enumerate(s):
            if ch in vowel:
                mask ^= 1 << vowel[ch]
            if mask in first:
                ans = max(ans, i - first[mask])
            else:
                first[mask] = i
        return ans
```

### 思路 1：复杂度分析
- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(n)$。
