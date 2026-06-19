# [1316. 不同的循环子字符串](https://leetcode.cn/problems/distinct-echo-substrings/)

- 标签：字典树、字符串、哈希函数、滚动哈希
- 难度：困难

## 题目链接

- [1316. 不同的循环子字符串 - 力扣](https://leetcode.cn/problems/distinct-echo-substrings/)

## 题目大意

**描述**：给定一个字符串 $text$。如果一个子串可以由某个长度为 $k$ 的字符串重复两次得到（即 $t + t$），则称为循环子串。

**要求**：返回不同的非空循环子串的数量。

**说明**：
- $1 \le text.length \le 2000$。

**示例**：

- 示例 1：

```python
输入：text = "abcabcabc"
输出：3
解释：3 个子字符串分别为 "abcabc"，"bcabca" 和 "cabcab" 。
```

- 示例 2：

```python
输入：text = "leetcodeleetcode"
输出：2
解释：2 个子字符串为 "ee" 和 "leetcodeleetcode" 。
```


## 解题思路

### 思路 1：滚动哈希

#### 1. 核心思想

枚举可能的起始位置和长度，检查前半段和后半段是否相同。用滚动哈希将字符串比较优化到 $O(1)$。

为了去重，使用集合存储不同的循环子串。

#### 2. 具体步骤

**第 1 步**：预处理字符串的滚动哈希值和幂次。

**第 2 步**：枚举长度 $len$ 从 $2$ 到 $n$（步长为 $2$），对每个可能的起始位置 $i$：
- 前半段 $text[i:i+len//2]$，后半段 $text[i+len//2:i+len]$。
- 用哈希 $O(1)$ 比较是否相等。
- 如果相等，将子串加入结果集合。

**第 3 步**：返回结果集合的大小。

### 思路 1：代码

```python
class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        base, mod = 131, 10**9 + 7
        # 前缀哈希
        prefix = [0] * (n + 1)
        power = [1] * (n + 1)
        for i in range(n):
            prefix[i + 1] = (prefix[i] * base + ord(text[i])) % mod
            power[i + 1] = (power[i] * base) % mod

        def get_hash(l, r):
            """返回 text[l:r] 的哈希值"""
            return (prefix[r] - prefix[l] * power[r - l]) % mod

        ans = set()
        for length in range(2, n + 1, 2):  # 偶数长度
            half = length // 2
            for i in range(n - length + 1):
                h1 = get_hash(i, i + half)
                h2 = get_hash(i + half, i + length)
                if h1 == h2:
                    ans.add(text[i:i + length])
        return len(ans)
```

### 思路 1：复杂度分析
- **时间复杂度**：$O(n^2)$。$n \le 2000$，$2000^2 = 4 \times 10^6$，可接受。
- **空间复杂度**：$O(n)$。
