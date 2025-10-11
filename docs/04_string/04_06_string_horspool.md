## 1. Horspool 算法介绍

> **Horspool 算法**：由 Nigel Horspool 教授于 1980 年提出，是对 Boyer Moore 算法的简化版，用于在字符串中查找子串。
>
> - **Horspool 算法核心思想**：先对模式串 $p$ 预处理，生成移动表。匹配时，从模式串末尾开始比较，遇到不匹配时，根据移动表跳过尽可能多的位置，加快查找速度。

Horspool 算法本质上继承了 Boyer-Moore 的思想，但只保留了「坏字符规则」并加以简化。当文本串 $T$ 某字符与模式串 $p$ 不匹配时，模式串可以根据以下两种情况快速右移：

- **情况 1：$T[i + m - 1]$（文本串当前窗口的最后一个字符）在模式串 $p$ 中出现过**
   - 将该字符在模式串中最后一次出现的位置与模式串末尾对齐。
   - **右移位数 = 模式串长度 - 1 - 该字符在模式串中最后一次出现的位置**

![Horspool 算法情况 1](https://qcdn.itcharge.cn/images/20240511165106.png)

- **情况 2：$T[i + m - 1]$ 没有在模式串 $p$ 中出现**
   - 直接将模式串整体右移一整个长度。
   - **右移位数 = 模式串长度**

![Horspool 算法情况 2](https://qcdn.itcharge.cn/images/20240511165122.png)

## 2. Horspool 算法步骤

Horspool 算法流程如下：

1. 设文本串 $T$ 长度为 $n$，模式串 $p$ 长度为 $m$。
2. 预处理模式串 $p$，生成后移位数表 $bc\_table$。
3. 从文本串起始位置 $i = 0$ 开始，将模式串与文本串对齐，比较方式如下：
   - 从模式串末尾 $j = m - 1$ 开始，依次向前比较 $T[i + j]$ 与 $p[j]$。
   - 如果全部字符匹配，返回 $i$，即匹配起始位置。
   - 如果遇到不匹配，查找 $T[i + m - 1]$ 在 $bc\_table$ 中的值，右移相应距离（如果未出现则右移 $m$）。
4. 如果遍历完文本串仍未找到匹配，返回 $-1$。

## 3. Horspool 算法代码实现

### 3.1 后移位数表代码实现

后移位数表的生成非常简单，类似于 Boyer-Moore 算法的坏字符表：

- 用一个哈希表 $bc\_table$，记录每个字符在模式串中可向右移动的距离。
- 遍历模式串 $p$，对每个字符 $p[i]$，将 $m - 1 - i$ 作为其移动距离存入表中。如果字符重复，保留最右侧的距离。

匹配时，如果 $T[i + m - 1]$ 不在表中，则右移 $m$；如果在表中，则右移 $bc\_table[T[i + m - 1]]$。

后移位数表代码如下：

```python
# 生成后移位数表
# bc_table[bad_char] 表示遇到坏字符时可以向右移动的距离
def generateBadCharTable(p: str):
    """
    构建 Horspool 算法的后移位数表。
    输入:
        p: 模式串
    输出:
        bc_table: 字典，key 为字符，value 为遇到该字符时可向右移动的距离
    """
    m = len(p)
    bc_table = dict()
    # 只处理模式串的前 m - 1 个字符（最后一个字符不需要处理）
    for i in range(m - 1):  # i 从 0 到 m - 2
        # 对于每个字符 p[i]，记录其对应的移动距离
        # 移动距离 = 模式串长度 - 1 - 当前字符下标
        bc_table[p[i]] = m - 1 - i
        # 如果字符重复出现，保留最右侧（下标最大）的距离
    return bc_table
```

### 3.2 Horspool 算法整体代码实现

```python
# Horspool 算法实现，T 为文本串，p 为模式串
def horspool(T: str, p: str) -> int:
    """
    Horspool 字符串匹配算法。
    返回模式串 p 在文本串 T 中首次出现的位置，若无则返回 -1。
    """
    n, m = len(T), len(p)
    if m == 0:
        return 0 if n == 0 else -1  # 约定：空模式串匹配空文本串返回 0，否则返回 -1
    if n < m:
        return -1                   # 模式串比文本串长，必不匹配

    bc_table = generateBadCharTable(p)  # 生成后移位数表

    i = 0
    while i <= n - m:
        j = m - 1
        # 从模式串末尾向前逐位比较
        while j >= 0 and T[i + j] == p[j]:
            j -= 1
        if j < 0:
            return i  # 匹配成功，返回起始下标
        # 取文本串当前窗口最右字符，查表决定滑动距离
        shift_char = T[i + m - 1]
        shift = bc_table.get(shift_char, m)  # 如果未出现则右移 m 位
        i += shift
    return -1  # 匹配失败，未找到

# 生成 Horspool 算法的后移位数表
# bc_table[bad_char] 表示遇到坏字符 bad_char 时可以向右移动的距离
def generateBadCharTable(p: str):
    """
    构建 Horspool 算法的后移位数表。
    输入:
        p: 模式串
    输出:
        bc_table: 字典，key 为字符，value 为遇到该字符时可向右移动的距离
    """
    m = len(p)
    bc_table = dict()
    # 只处理模式串的前 m - 1 个字符（最后一个字符不处理）
    for i in range(m - 1):  # i 从 0 到 m - 2
        # 对于每个字符 p[i]，记录其对应的移动距离
        # 移动距离 = 模式串长度 - 1 - 当前字符下标
        bc_table[p[i]] = m - 1 - i
        # 如果字符重复出现，保留最右侧（下标最大）的距离
    return bc_table

# 测试用例
print(horspool("abbcfdddbddcaddebc", "aaaaa"))  # -1，未匹配
print(horspool("abbcfdddbddcaddebc", "bcf"))    # 2，匹配成功
```

## 4. Horspool 算法分析

| 指标         | 复杂度           | 说明                                                         |
| ------------ | ---------------- | ------------------------------------------------------------ |
| 最好时间复杂度   | $O(n)$           | 模式串字符分布均匀，坏字符表能实现最大跳跃，比较次数最少。         |
| 最坏时间复杂度   | $O(n \times m)$  | 模式串字符高度重复且与文本不匹配时，每次只能滑动一位。             |
| 平均时间复杂度   | $O(n)$           | 实际应用中通常接近最好情况，比较次数较少。                       |
| 空间复杂度     | $O(m + \sigma)$   | 主要用于存储坏字符表，$m$ 为模式串长度，$\sigma$ 为字符集大小。    |

- $n$ 为文本串长度，$m$ 为模式串长度，$\sigma$ 为字符集大小。
- Horspool 算法在大多数实际场景下效率较高，但极端情况下可能退化为 $O(n \times m)$。
- 空间消耗主要体现在坏字符表的构建上。

## 4. 总结

Horspool 算法是一种基于坏字符规则的高效字符串匹配算法，通过预处理模式串构建坏字符表，实现快速跳跃以提升匹配效率，适用于大多数实际场景。

- **优点**：
   - 实现简单，代码量少，易于理解。
   - 平均性能优良，适合大多数实际应用场景。
   - 只需构建坏字符表，预处理开销小。
- **缺点**：
   - 最坏情况下时间复杂度较高，可能退化为 $O(n \times m)$。
   - 只利用坏字符规则，跳跃能力不如 BM 算法。
   - 不适合极端重复或特殊构造的模式串。

## 练习题目

- [0028. 找出字符串中第一个匹配项的下标](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0001-0099/find-the-index-of-the-first-occurrence-in-a-string.md)
- [0459. 重复的子字符串](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0400-0499/repeated-substring-pattern.md)
- [0686. 重复叠加字符串匹配](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0600-0699/repeated-string-match.md)
- [0796. 旋转字符串](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0700-0799/rotate-string.md)
- [1408. 数组中的字符串匹配](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/1400-1499/string-matching-in-an-array.md)
- [2156. 查找给定哈希值的子串](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/2100-2199/find-substring-with-given-hash-value.md)

- [单模式串匹配题目列表](https://github.com/ITCharge/AlgoNote/tree/main/docs/00_preface/00_06_categories_list.md#%E5%8D%95%E6%A8%A1%E5%BC%8F%E4%B8%B2%E5%8C%B9%E9%85%8D%E9%A2%98%E7%9B%AE)

## 参考资料

- 【书籍】柔性字符串匹配 - 中科院计算所网络信息安全研究组 译
- 【博文】[字符串模式匹配算法：BM、Horspool、Sunday、KMP、KR、AC算法 - schips - 博客园](https://www.cnblogs.com/schips/p/11098041.html)

