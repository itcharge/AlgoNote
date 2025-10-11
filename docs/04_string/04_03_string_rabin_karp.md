## 1. Rabin Karp 算法介绍

> **Rabin Karp（RK）算法**：由 Michael Oser Rabin 与 Richard Manning Karp 于 1987 年提出，是一种利用哈希快速筛查匹配起点的单模式串匹配算法。
>
> - **Rabin Karp 算法核心思想**：给定文本串 $T$ 与模式串 $p$，先计算 $p$ 的哈希值，再对 $T$ 的所有长度为 $m=|p|$ 的子串高效计算哈希。借助「滚动哈希」在 $O(1)$ 时间更新相邻子串的哈希，用哈希相等作为快速筛选，仅在相等时再逐字符比对以排除哈希冲突。

## 2. Rabin Karp 算法步骤

### 2.1 Rabin Karp 算法整体流程

1. 设 $n=|T|$、$m=|p|$。
2. 计算模式串哈希 $H(p)$。
3. 计算文本首个长度为 $m$ 的子串 $T_{[0,m-1]}$ 的哈希 $H(T_{[0,m-1]})$，并用滚动哈希依次得到其余 $n - m$ 个相邻子串的哈希。
4. 逐一比较 $H(T_{[i,i+m-1]})$ 与 $H(p)$：
   - 如果不相等，跳过；
   - 如果相等，逐字符核验：完全相同则返回起点 $i$，否则继续。
5. 全部位置检查后仍未匹配，返回 $-1$。

### 2.2 滚动哈希算法

实现 RK 的关键是 **滚动哈希**：使相邻子串哈希的更新从 $O(m)$ 降为 $O(1)$，显著提升效率。

滚动哈希采用 **Rabin fingerprint** 思想：把子串视作 $d$ 进制多项式，基于上一个子串的哈希在 $O(1)$ 时间得到下一个子串的哈希。

下面我们用一个例子来解释一下这种算法思想。

设字符集大小为 $d$，用 $d$ 进制多项式哈希表示子串。

举个例子，假如字符串只包含 $a \sim z$ 这 $26$ 个小写字母，那么我们就可以用 $26$ 进制数来表示一个字符串，$a$ 表示为 $0$，$b$ 表示为 $1$，以此类推，$z$ 就用 $25$ 表示。

例如 `"cat"` 的哈希可表示为：

$$\begin{aligned} Hash(cat) &= c \times 26^2 + a \times 26^1 + t \times 26^0 \cr &= 2 \times 26^2 + 0 \times 26^1 + 19 \times 26^0 \cr &= 1371 \end{aligned}$$

这种多项式哈希的特点是：相邻子串的哈希可由上一个快速推得。

如果 $cat$ 的相邻子串为 `"ate"`，直接计算其哈希：

$$\begin{aligned} Hash(ate) &= a \times 26^2 + t \times 26^1 + e \times 26^0 \cr &= 0 \times 26^2 + 19 \times 26^1 + 4 \times 26^0 \cr &= 498 \end{aligned}$$

如果利用上一个子串 `"cat"` 的哈希滚动更新：

$$\begin{aligned} Hash(ate) &= (Hash(cat) - c \times 26^2) \times 26 + e \times 26^0 \cr &= (1371 - 2 \times 26^2) \times 26 + 4 \times 26^0 \cr &= 498 \end{aligned}$$

可以看出，这两种方式计算出的哈希值是相同的。但是第二种计算方式不需要再遍历子串，只需要进行一位字符的计算即可得出整个子串的哈希值。这样每次计算子串哈希值的时间复杂度就降到了 $O(1)$。然后我们就可以通过滚动哈希算法快速计算出子串的哈希值了。

将上述规律形式化如下。

给定文本串 $T$ 与模式串 $p$，设 $n=|T|$、$m=|p|$、字符集大小为 $d$，则：

- 模式串：$H(p)=\sum\limits_{k=0}^{m-1} p_k\, d^{m-1-k}$；
- 文本首子串：$H(T_{[0,m-1]})=\sum\limits_{k=0}^{m-1} T_k\, d^{m-1-k}$；
- 滚动关系：$H(T_{[i+1,i+m]})=\big(H(T_{[i,i+m-1]})-T_i\, d^{m-1}\big)\, d+T_{i+m}$。

为避免溢出与降低冲突，计算时通常对大质数 $q$ 取模（模数宜大且为质数）。

## 3. Rabin–Karp 代码实现

```python
# T: 文本串，p: 模式串，d: 字符集大小（基数），q: 模数（质数）
def rabinKarp(T: str, p: str, d: int, q: int) -> int:
    n, m = len(T), len(p)
    if m == 0:
        return 0
    if n < m:
        return -1

    hash_p, hash_t = 0, 0

    # 计算 H(p) 与首个子串的哈希
    for i in range(m):
        hash_p = (hash_p * d + ord(p[i])) % q
        hash_t = (hash_t * d + ord(T[i])) % q

    # 使用 pow 的三参形式避免中间溢出
    power = pow(d, m - 1, q)  # d^(m-1) % q，用于移除最高位字符

    for i in range(n - m + 1):
        if hash_p == hash_t:
            # 避免冲突：逐字符核验
            match = True
            for j in range(m):
                if T[i + j] != p[j]:
                    match = False
                    break
            if match:
                return i
        if i < n - m:
            # 滚动更新到下一个子串
            hash_t = (hash_t - power * ord(T[i])) % q  # 去掉最高位字符
            hash_t = (hash_t * d + ord(T[i + m])) % q  # 加入新字符

    return -1
```

## 4. 复杂度与性质

| 指标         | 复杂度         | 说明                                 |
| ------------ | -------------- | ------------------------------------ |
| 最好时间复杂度   | $O(n-m+1)$     | 无哈希冲突时，仅需 $n-m+1$ 次哈希对比，均为 $O(1)$，无需逐字符校验 |
| 最坏时间复杂度   | $O(m(n-m+1))\approx O(nm)$ | 每次哈希均冲突，需 $n-m+1$ 次逐字符全量比对，每次 $O(m)$ |
| 平均时间复杂度   | $O(n-m+1)$     | 期望哈希冲突极少，绝大多数位置仅哈希对比，均摊 $O(1)$ |
| 空间复杂度     | $O(1)$         | 仅需常数变量存储哈希值与辅助参数      |

说明：与 BF 相比，RK 通过哈希筛选把大多数不匹配位置在 $O(1)$ 内排除；但哈希冲突会触发逐字符校验，致使最坏复杂度退化。

## 5. 总结

Rabin-Karp（RK）算法通过将模式串和文本子串转化为哈希值，利用「滚动哈希」快速筛查匹配位置，大幅减少无效字符比较。其平均时间复杂度远优于朴素算法，适合大文本和多模式串场景，但哈希冲突时需回退逐字符比对，最坏情况下复杂度与朴素法相同。合理选择哈希参数可有效降低冲突概率，是一种高效且易于扩展的字符串匹配算法。

- **优点**：
   - 滚动哈希使子串哈希更新为 $O(1)$，平均性能优于 BF；
   - 易于扩展到多模式串场景（统一维护多哈希）。
- **缺点**：
   - 存在哈希冲突，最坏复杂度可退化至 $O(nm)$；
   - 需合理选择基数 $d$ 与大质数模 $q$，以降低冲突概率。

## 练习题目

- [0028. 找出字符串中第一个匹配项的下标](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0001-0099/find-the-index-of-the-first-occurrence-in-a-string.md)
- [0459. 重复的子字符串](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0400-0499/repeated-substring-pattern.md)
- [0686. 重复叠加字符串匹配](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0600-0699/repeated-string-match.md)
- [0796. 旋转字符串](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0700-0799/rotate-string.md)
- [1408. 数组中的字符串匹配](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/1400-1499/string-matching-in-an-array.md)
- [2156. 查找给定哈希值的子串](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/2100-2199/find-substring-with-given-hash-value.md)

- [单模式串匹配题目列表](https://github.com/ITCharge/AlgoNote/tree/main/docs/00_preface/00_06_categories_list.md#%E5%8D%95%E6%A8%A1%E5%BC%8F%E4%B8%B2%E5%8C%B9%E9%85%8D%E9%A2%98%E7%9B%AE)

## 参考资料

- 【书籍】数据结构与算法 Python 语言描述 - 裘宗燕 著
- 【文章】[字符串匹配基础（上）- 数据结构与算法之美 - 极客时间](https://time.geekbang.org/column/article/71187)
- 【文章】[字符串匹配算法 - Rabin Karp 算法 - coolcao 的小站](https://coolcao.com/2020/08/20/rabin-karp/)
- 【问答】[string - Python: Rabin-Karp algorithm hashing - Stack Overflow](https://stackoverflow.com/questions/22216948/python-rabin-karp-algorithm-hashing)