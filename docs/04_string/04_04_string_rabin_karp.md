## 1. Rabin Karp 算法介绍

> **Rabin Karp 算法**：简称为 RK 算法。是由它的两位发明者 Michael Oser Rabin 和 Richard Manning Karp 的名字来命名的。RK 算法是他们在 1987 年提出的、使用哈希函数以在文本中搜寻单个模式串的字符串搜索算法。
>
> - **Rabin Karp 算法思想**：对于给定文本串 $T$ 与模式串 $p$，通过滚动哈希算快速筛选出与模式串 $p$ 不匹配的文本位置，然后在其余位置继续检查匹配项。

## 2. Rabin Karp 算法步骤

### 2.1 Rabin Karp 算法整体步骤

1. 对于给定的文本串 $T$ 与模式串 $p$，求出文本串 $T$ 的长度为 $n$，模式串 $p$ 的长度为 $m$。
2. 通过滚动哈希算法求出模式串 $p$ 的哈希值 $hash\underline{\hspace{0.5em}}p$。
3. 再通过滚动哈希算法对文本串 $T$ 中 $n - m + 1$ 个子串分别求哈希值 $hash\underline{\hspace{0.5em}}t$。
4. 然后逐个与模式串的哈希值比较大小。
   1. 如果当前子串的哈希值 $hash\underline{\hspace{0.5em}}t$ 与模式串的哈希值 $hash\underline{\hspace{0.5em}}p$ 不同，则说明两者不匹配，则继续向后匹配。
   2. 如果当前子串的哈希值 $hash\underline{\hspace{0.5em}}t$ 与模式串的哈希值 $hash\underline{\hspace{0.5em}}p$ 相等，则验证当前子串和模式串的每个字符是否真的相等（避免哈希冲突）。
      1. 如果当前子串和模式串的每个字符相等，则说明当前子串和模式串匹配。
      2. 如果当前子串和模式串的每个字符不相等，则说明两者不匹配，继续向后匹配。
5. 比较到末尾，如果仍未成功匹配，则说明文本串 $T$ 中不包含模式串 $p$，方法返回 $-1$。

### 2.2 滚动哈希算法

实现 RK 算法中一个重要步骤是 **「滚动哈希算法」**，通过滚动哈希算法，将每次计算子串哈希值的复杂度从 $O(m)$ 降到了 $O(1)$，从而提升了整个算法效率。

RK 算法中的滚动哈希算法主要是利用了 **「Rabin fingerprint 思想」**。这种算法思想利用了子串中每一位字符的哈希值，并且还可以根据上一个子串的哈希值，快速计算相邻子串的哈希值，从而使得每次计算子串哈希值的时间复杂度降为了 $O(1)$。

下面我们用一个例子来解释一下这种算法思想。

假设给定的字符串的字符集中只包含 $d$ 种字符，那么我们就可以用一个 $d$ 进制数表示子串的哈希值。

举个例子，假如字符串只包含 $a \sim z$ 这 $26$ 个小写字母，那么我们就可以用 $26$ 进制数来表示一个字符串，$a$ 表示为 $0$，$b$ 表示为 $1$，以此类推，$z$ 就用 $25$ 表示。

比如 `"cat"` 的哈希值就可以表示为：

$$\begin{aligned} Hash(cat) &= c \times 26^2 + a \times 26^1 + t \times 26^0 \cr &= 2 \times 26^2 + 0 \times 26^1 + 19 \times 26^0 \cr &= 1371 \end{aligned}$$

这种按位计算哈希值的哈希函数有一个特点：在计算相邻子串时，可以利用上一个子串的哈希值。

比如说 $cat$ 的相邻子串为 `"ate"`。按照刚才哈希函数计算，可以得出 `"ate"` 的哈希值为：

$$\begin{aligned} Hash(ate) &= a \times 26^2 + t \times 26^1 + e \times 26^0 \cr &= 0 \times 26^2 + 19 \times 26^1 + 4 \times 26^0 \cr &= 498 \end{aligned}$$

如果利用上一个子串 `"cat"` 的哈希值计算 `"ate"`，则 `"ate"` 的哈希值为：

$$\begin{aligned} Hash(ate) &= (Hash(cat) - c \times 26^2) \times 26 + e \times 26^0 \cr &= (1371 - 2 \times 26^2) \times 26 + 4 \times 26^0 \cr &= 498 \end{aligned}$$

可以看出，这两种方式计算出的哈希值是相同的。但是第二种计算方式不需要再遍历子串，只需要进行一位字符的计算即可得出整个子串的哈希值。这样每次计算子串哈希值的时间复杂度就降到了 $O(1)$。然后我们就可以通过滚动哈希算法快速计算出子串的哈希值了。

我们将上面的规律扩展总结一下。

给定的文本串 $T$ 与模式串 $p$，求出文本串 $T$ 的长度为 $n$，模式串 $p$ 的长度为 $m$。字符串字符种类数为 $d$，则：

- 模式串 $p$ 的哈希值计算方式为：$Hash(p) = p_0 \times d^{m - 1} + p_1 \times d^{m - 2} + … + p_{m-1} \times d^{0}$。
- 文本串中起始于位置 $0$，长度为 $m$ 的子串 $T_{[0,m-1]}$ 对应哈希值计算方法为：$Hash(T_{[0, m - 1]}) = T_0 \times d^{m - 1} + T_1 \times d^{m - 2} + ... + T_{m - 1} \times d^0$。
- 已知子串的哈希值 $Hash(T_{[i,i + m - 1]})$，将子串向右移动一位的子串对应哈希值计算方法为：$Hash(T_{[i + 1, i + m]}) = [Hash(T_{[i, i + m - 1]}) - T_i \times d^{m - 1}] \times d + T_{i + m} \times d^{0}$。

因为哈希值过大会造成溢出，所以我们在计算过程中还要对结果取模。取模的值应该尽可能大，并且应该是质数，这样才能减少哈希碰撞的概率。

## 3. Rabin Karp 算法代码实现

```python
# T 为文本串，p 为模式串，d 为字符集的字符种类数，q 为质数
def rabinKarp(T: str, p: str, d, q) -> int:
    n, m = len(T), len(p)
    if n < m:
        return -1
    
    hash_p, hash_t = 0, 0
    
    for i in range(m):
        hash_p = (hash_p * d + ord(p[i])) % q           # 计算模式串 p 的哈希值
        hash_t = (hash_t * d + ord(T[i])) % q           # 计算文本串 T 中第一个子串的哈希值
    
    power = pow(d, m - 1) % q                           # power 用于移除字符哈希时
    
    for i in range(n - m + 1):
        if hash_p == hash_t:                            # 检查模式串 p 的哈希值和子串的哈希值
            match = True                                # 如果哈希值相等，验证模式串和子串每个字符是否完全相同（避免哈希冲突）
            for j in range(m):
                if T[i + j] != p[j]:
                    match = False                       # 模式串和子串某个字符不相等，验证失败，跳出循环
                    break
            if match:                                   # 如果模式串和子串每个字符是否完全相同，返回匹配开始位置
                return i
        if i < n - m:                                   # 计算下一个相邻子串的哈希值
            hash_t = (hash_t - power * ord(T[i])) % q   # 移除字符 T[i]
            hash_t = (hash_t * d + ord(T[i + m])) % q   # 增加字符 T[i + m]
            hash_t = (hash_t + q) % q                   # 确保 hash_t >= 0
        
    return -1
```

## 4. RK 算法分析

RK 算法可以看做是 BF 算法的一种改进。在 BF 算法中，每一个字符都需要进行比较。而在 RK 算法中，判断模式串的哈希值与每个子串的哈希值之间是否相等的时间复杂度为 $O(1)$。总共需要比较 $n - m + 1$ 个子串的哈希值，所以 RK 算法的整体时间复杂度为 $O(n)$。跟 BF 算法相比，RK 算法的效率提高了很多。

但是如果存在冲突的情况下，算法的效率会降低。最坏情况是每一次比较模式串的哈希值和子串的哈希值时都相等，但是每一次都会出现冲突，那么每一次都需要验证模式串和子串每个字符是否完全相同，那么总的比较次数就是 $m \times (n - m + 1)$，时间复杂度就会退化为 $O(m \times n)$。

## 练习题目

- [单模式串匹配题目列表](https://github.com/itcharge/AlgoNote/blob/main/docs/00_preface/00_06_categories_list.md#%E5%8D%95%E6%A8%A1%E5%BC%8F%E4%B8%B2%E5%8C%B9%E9%85%8D%E9%A2%98%E7%9B%AE)

## 参考资料

- 【书籍】数据结构与算法 Python 语言描述 - 裘宗燕 著
- 【文章】[字符串匹配基础（上）- 数据结构与算法之美 - 极客时间](https://time.geekbang.org/column/article/71187)
- 【文章】[字符串匹配算法 - Rabin Karp 算法 - coolcao 的小站](https://coolcao.com/2020/08/20/rabin-karp/)
- 【问答】[string - Python: Rabin-Karp algorithm hashing - Stack Overflow](https://stackoverflow.com/questions/22216948/python-rabin-karp-algorithm-hashing)