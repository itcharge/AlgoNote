# [2156. 查找给定哈希值的子串](https://leetcode.cn/problems/find-substring-with-given-hash-value/)

- 标签：字符串、滑动窗口、哈希函数、滚动哈希
- 难度：困难

## 题目链接

- [2156. 查找给定哈希值的子串 - 力扣](https://leetcode.cn/problems/find-substring-with-given-hash-value/)

## 题目大意

**描述**：如果给定整数 `p` 和 `m`，一个长度为 `k` 且下标从 `0` 开始的字符串 `s` 的哈希值按照如下函数计算：

- $hash(s, p, m) = (val(s[0]) * p^0 + val(s[1]) * p^1 + ... + val(s[k-1]) * p^{k-1}) mod m$.

其中 `val(s[i])` 表示 `s[i]` 在字母表中的下标，从 `val('a') = 1` 到 `val('z') = 26`。

现在给定一个字符串 `s` 和整数 `power`，`modulo`，`k` 和 `hashValue` 。

**要求**：返回 `s` 中 第一个 长度为 `k` 的 子串 `sub`，满足 `hash(sub, power, modulo) == hashValue`。

**说明**：

- 子串：定义为一个字符串中连续非空字符组成的序列。
- $1 \le k \le s.length \le 2 * 10^4$。
- $1 \le power, modulo \le 10^9$。
- $0 \le hashValue < modulo$。
- `s` 只包含小写英文字母。
- 测试数据保证一定存在满足条件的子串。

**示例**：

- 示例 1：

```python
输入：s = "leetcode", power = 7, modulo = 20, k = 2, hashValue = 0
输出："ee"
解释："ee" 的哈希值为 hash("ee", 7, 20) = (5 * 1 + 5 * 7) mod 20 = 40 mod 20 = 0 。
"ee" 是长度为 2 的第一个哈希值为 0 的子串，所以我们返回 "ee" 。
```

## 解题思路

### 思路 1：Rabin Karp 算法、滚动哈希算法

这道题目的思想和 Rabin Karp 字符串匹配算法中用到的滚动哈希思想是一样的。不过两者计算的公式是相反的。

- 本题目中的子串哈希计算公式：$hash(s, p, m) = (val(s[i]) * p^0 + val(s[i+1]) * p^1 + ... + val(s[i+k-1]) * p^{k-1}) \mod m$.

- RK 算法中的子串哈希计算公式：$hash(s, p, m) = (val(s[i]) * p^{k-1} + val(s[i+1]) * p^{k-2} + ... + val(s[i+k-1]) * p^0) \mod m$.

可以看出两者的哈希计算公式是反的。

在 RK 算法中，下一个子串的哈希值计算方式为：$Hash(s_{[i + 1, i + k]}) = \{[Hash(s_{[i, i + k - 1]}) - s_i \times d^{k - 1}] \times d + s_{i + k} \times d^{0} \} \mod m$。其中 $Hash(s_{[i, i + k - 1]}$ 为当前子串的哈希值，$Hash(s_{[i + 1, i + k]})$ 为下一个子串的哈希值。

这个公式也可以用文字表示为：**在计算完当前子串的哈希值后，向右滚动字符串，即移除当前子串中最左侧字符的哈希值（$val(s[i]) * p^{k-1}$）之后，再将整体乘以 $p$，再移入最右侧字符的哈希值 $val(s[i+k])$**。

我们可以参考 RK 算法中滚动哈希的计算方式，将其应用到本题中。

因为两者的哈希计算公式相反，所以本题中，我们可以从右侧想左侧逆向遍历字符串，当计算完当前子串的哈希值后，移除当前子串最右侧字符的哈希值（$ val(s[i+k-1]) * p^{k-1}$）之后，再整体乘以 $p$，再移入最左侧字符的哈希值 $val(s[i - 1])$。

在本题中，对应的下一个逆向子串的哈希值计算方式为：$Hash(s_{[i - 1, i + k - 2]}) = \{ [Hash(s_{[i, i + k - 1]}) - s_{i + k - 1} \times d^{k - 1}] \times d + s_{i - 1} \times d^{0} \} \mod m$。其中 $Hash(s_{[i, i + k - 1]})$ 为当前子串的哈希值，$Hash(s_{[i - 1, i + k - 2]})$ 是下一个逆向子串的哈希值。

利用取模运算的两个公式：

- $(a \times b) \mod m = ((a \mod m) \times (b \mod m)) \mod m$
- $(a + b) \mod m = (a \mod m + b \mod m) \mod m$

我们可以把上面的式子转变为：

$$\begin{aligned} Hash(s_{[i - 1, i + k - 2]}) &=  \{[Hash(s_{[i, i + k - 1]}) - s_{i + k - 1} \times d^{k - 1}] \times d + s_{i - 1} \times d^{0} \} \mod m  \cr &= \{[Hash(s_{[i, i + k - 1]}) - s_{i + k - 1} \times d^{k - 1}] \times d \mod m + s_{i - 1} \times d^{0} \mod m \} \mod m \cr &= \{[Hash(s_{[i, i + k - 1]}) - s_{i + k - 1} \times d^{k - 1}] \mod m \times d \mod m + s_{i - 1} \times d^{0} \mod m \} \mod m \end{aligned}$$

> 注意：这里之所以用了「反向迭代」而不是「正向迭代」是因为如果使用了正向迭代，那么每次移除的最左侧字符哈希值为 $val(s[i]) * p^0$，之后整体需要除以 $p$，再移入最右侧字符哈希值为（$val(s[i+k]) * p^{k-1})$）。
>
> 这样就用到了「除法」。而除法是不满足取模运算对应的公式的，所以这里不能用这种方法进行迭代。
>
> 而反向迭代，用到的是乘法。在整个过程中是满足取模运算相关的公式。乘法取余不影响最终结果。

### 思路 1：代码

```python
class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        hash_t = 0
        n = len(s)
        for i in range(n - 1, n - k - 1, -1):
            hash_t = (hash_t * power + (ord(s[i]) - ord('a') + 1)) % modulo # 计算最后一个子串的哈希值
    
        h = pow(power, k - 1) % modulo                                      # 计算最高位项，方便后续移除操作
        ans = ""
        if hash_t == hashValue:
            ans = s[n - k: n]
        for i in range(n - k - 1, -1, -1):                                   # 反向迭代，滚动计算子串的哈希值
            hash_t = (hash_t - h * (ord(s[i + k]) - ord('a') + 1)) % modulo  # 移除 s[i + k] 的哈希值
            hash_t = (hash_t * power % modulo + (ord(s[i]) - ord('a') + 1) % modulo) % modulo  # 添加 s[i] 的哈希值
            if hash_t == hashValue:                                          # 如果子串哈希值等于 hashValue，则为答案
                ans = s[i: i + k]
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。其中字符串 $s$ 的长度为 $n$。
- **空间复杂度**：$O(1)$。
