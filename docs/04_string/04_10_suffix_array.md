## 1. 后缀数组简介

> **后缀数组（Suffix Array）**：是一种高效处理字符串后缀相关问题的数据结构。它将字符串的所有后缀按字典序排序，并记录每个后缀在原串中的起始位置，便于实现高效的子串查找、最长重复子串、最长公共子串等操作。

后缀数组常与 **LCP（Longest Common Prefix）数组** 配合使用，进一步提升字符串处理的效率。

---

## 2. 基本原理与定义

给定一个长度为 $n$ 的字符串 $S$，其后缀数组 $SA$ 是一个长度为 $n$ 的整数数组，$SA[i]$ 表示 $S$ 的第 $i$ 小后缀在原串中的起始下标。

例如：

> $S = "banana"$
>
> $S$ 的所有后缀及其下标：
> - 0: banana
> - 1: anana
> - 2: nana
> - 3: ana
> - 4: na
> - 5: a
>
> 按字典序排序后：
> 1. a      (5)
> 2. ana    (3)
> 3. anana  (1)
> 4. banana (0)
> 5. na     (4)
> 6. nana   (2)
>
> 所以 $SA = [5, 3, 1, 0, 4, 2]$

---

## 3. 后缀数组的构建方法

后缀数组的构建有多种方法，常见的有：

- **朴素排序法**：直接生成所有后缀并排序，时间复杂度 $O(n^2 \log n)$，适合短串。
- **倍增算法**：利用基数排序思想，时间复杂度 $O(n \log n)$。
- **DC3/Skew 算法**：线性时间 $O(n)$ 构建，适合大数据量。

### 3.1 朴素法（适合理解原理）

```python
# 朴素法构建后缀数组
S = "banana"
suffixes = [(S[i:], i) for i in range(len(S))]
suffixes.sort()
SA = [idx for (suf, idx) in suffixes]
print(SA)  # 输出: [5, 3, 1, 0, 4, 2]
```

### 3.2 倍增算法（常用高效实现）

```python
def build_suffix_array(s):
    n = len(s)
    k = 1
    rank = [ord(c) for c in s]
    tmp = [0] * n
    sa = list(range(n))
    while True:
        sa.sort(key=lambda x: (rank[x], rank[x + k] if x + k < n else -1))
        tmp[sa[0]] = 0
        for i in range(1, n):
            tmp[sa[i]] = tmp[sa[i-1]] + \
                ((rank[sa[i]] != rank[sa[i-1]]) or
                 (rank[sa[i]+k] if sa[i]+k < n else -1) != (rank[sa[i-1]+k] if sa[i-1]+k < n else -1))
        rank = tmp[:]
        if rank[sa[-1]] == n-1:
            break
        k <<= 1
    return sa

# 示例
S = "banana"
print(build_suffix_array(S))  # 输出: [5, 3, 1, 0, 4, 2]
```

---

## 4. LCP（最长公共前缀）数组

> **LCP 数组**：LCP[i] 表示 $SA[i]$ 和 $SA[i-1]$ 所指向的两个后缀的最长公共前缀长度。

LCP 数组常用于：

- 快速查找最长重复子串
- 计算不同子串个数
- 字符串压缩等

### LCP 数组的构建

```python
def build_lcp(s, sa):
    n = len(s)
    rank = [0] * n
    for i in range(n):
        rank[sa[i]] = i
    h = 0
    lcp = [0] * n
    for i in range(n):
        if rank[i] == 0:
            lcp[0] = 0
        else:
            j = sa[rank[i] - 1]
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            lcp[rank[i]] = h
            if h > 0:
                h -= 1
    return lcp

# 示例
S = "banana"
SA = build_suffix_array(S)
LCP = build_lcp(S, SA)
print(LCP)  # 输出: [0, 1, 3, 0, 0, 2]
```

## 5. 算法复杂度分析

- **朴素法**：$O(n^2 \log n)$
- **倍增法**：$O(n \log n)$
- **DC3/Skew**：$O(n)$
- **LCP 构建**：$O(n)$

## 参考资料

- 《算法竞赛进阶指南》—— 胡策
- 《算法竞赛入门经典》—— 刘汝佳
- [OI Wiki - 后缀数组](https://oi-wiki.org/string/sa/)


