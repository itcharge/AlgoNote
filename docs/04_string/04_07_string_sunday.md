## 1. Sunday 算法介绍

> **Sunday 算法**：Sunday 算法是一种高效的字符串查找算法，由 Daniel M. Sunday 于 1990 年提出，专门用于在主串中查找子串的位置。
>
> - **核心思想**：对于给定的文本串 $T$ 和模式串 $p$，Sunday 算法首先对模式串 $p$ 进行预处理，生成一个「后移位数表」。在匹配过程中，每当发现不匹配时，算法会根据文本串中参与本轮匹配的末尾字符的「下一个字符」，决定模式串应向右滑动的距离，从而尽可能跳过无效的比较，加快匹配速度。

Sunday 算法的思想与 Boyer-Moore 算法类似，但 Sunday 算法始终从左到右进行匹配。当匹配失败时，Sunday 算法关注的是文本串 $T$ 当前匹配窗口末尾的下一个字符 $T[i + m]$，并据此决定模式串的滑动距离，实现快速跳跃。

具体来说，遇到不匹配时有两种情况：

- **情况 1：$T[i + m]$ 出现在模式串 $p$ 中**
  - 此时，将模式串 $p$ 向右移动，使其最后一次出现 $T[i + m]$ 的位置与 $T[i + m]$ 对齐。
  - **向右移动的位数 = 模式串中 $T[i + m]$ 最右侧出现的位置到末尾的距离**
  - 说明：$T[i + m]$ 即为当前匹配窗口末尾的下一个字符。

![Sunday 算法情况 1](https://qcdn.itcharge.cn/images/20240511165526.png)

- **情况 2：$T[i + m]$ 未出现在模式串 $p$ 中**
  - 此时，直接将模式串整体向右移动 $m + 1$ 位。
  - **向右移动的位数 = 模式串长度 $m + 1$**

![Sunday 算法情况 2](https://qcdn.itcharge.cn/images/20240511165540.png)

## 2. Sunday 算法步骤

Sunday 算法的具体流程如下：

- 设文本串 $T$ 长度为 $n$，模式串 $p$ 长度为 $m$。
- 首先对模式串 $p$ 进行预处理，生成后移位数表 $bc\_table$。
- 令 $i = 0$，表示当前模式串 $p$ 的起始位置与文本串 $T$ 的第 $i$ 位对齐。
- 在每一轮匹配中，从头开始比较 $T[i + j]$ 与 $p[j]$（$j$ 从 $0$ 到 $m-1$）：
  - 如果所有字符均匹配，则返回当前匹配的起始位置 $i$。
  - 如果出现不匹配，或未全部匹配完毕，则：
    - 检查 $T[i + m]$（即当前匹配窗口末尾的下一个字符）：
      - 如果 $T[i + m]$ 存在于后移位数表中，则将 $i$ 增加 $bc\_table[T[i + m]]$，即将模式串向右滑动相应距离。
      - 如果 $T[i + m]$ 不存在于后移位数表中，则将 $i$ 增加 $m + 1$，即整体右移 $m + 1$ 位。
- 若遍历完整个文本串仍未找到匹配，则返回 $-1$。

## 3. Sunday 算法代码实现

### 3.1 后移位数表代码实现

后移位数表的实现非常简洁，与 Horspool 算法类似。具体思路如下：

- 使用一个哈希表 $bc\_table$，其中 $bc\_table[bad\_char]$ 表示遇到该字符时，模式串可以向右移动的距离。
- 遍历模式串 $p$，将每个字符 $p[i]$ 作为键，其对应的移动距离 $m - i$ 作为值存入字典。如果字符重复出现，则以最右侧（下标最大的）位置为准，覆盖之前的值。这样，哈希表中存储的就是每个字符在模式串中最右侧出现时可向右移动的距离。

在 Sunday 算法匹配过程中，如果 $T[i + m]$ 不在 $bc\_table$ 中，则默认移动 $m + 1$ 位，即将模式串整体右移到当前匹配窗口末尾的下一个字符之后。如果 $T[i + m]$ 存在于表中，则移动距离为 $bc\_table[T[i + m]]$。这样即可高效计算每次滑动的步长。

后移位数表的代码如下：

```python
# 生成 Sunday 算法的后移位数表
# bc_table[bad_char] 表示遇到坏字符 bad_char 时，模式串可以向右移动的距离
def generateBadCharTable(p: str):
    """
    构建 Sunday 算法的后移位数表。
    输入:
        p: 模式串
    输出:
        bc_table: 字典，key 为字符，value 为遇到该字符时可向右移动的距离
    """
    m = len(p)
    bc_table = dict()
    # 遍历模式串的每一个字符（包括最后一个字符）
    for i in range(m):
        # 对于每个字符 p[i]，记录其对应的移动距离
        # 移动距离 = 模式串长度 - 当前字符下标
        bc_table[p[i]] = m - i
        # 如果字符重复出现，保留最右侧（下标最大）的距离
    return bc_table
```

### 3.2 Sunday 算法整体代码实现

```python
# Sunday 算法实现，T 为文本串，p 为模式串
def sunday(T: str, p: str) -> int:
    """
    Sunday 算法主函数，返回模式串 p 在文本串 T 中首次出现的位置，若未匹配则返回 -1。
    参数:
        T: 文本串
        p: 模式串
    返回:
        int: 第一个匹配位置的下标，未匹配返回 -1
    """
    n, m = len(T), len(p)
    if m == 0:
        return 0  # 空模式串视为匹配在开头

    bc_table = generateBadCharTable(p)  # 生成后移位数表

    i = 0  # i 表示当前窗口在文本串中的起始下标
    while i <= n - m:
        # 逐字符比较当前窗口是否与模式串完全匹配
        j = 0
        while j < m and T[i + j] == p[j]:
            j += 1
        if j == m:
            return i  # 匹配成功，返回起始下标
        # 检查窗口末尾的下一个字符，决定滑动距离
        if i + m >= n:
            return -1  # 已到文本串末尾，未匹配
        next_char = T[i + m]  # 当前窗口末尾的下一个字符
        # 若 next_char 在后移位数表中，滑动对应距离，否则滑动 m+1
        shift = bc_table.get(next_char, m + 1)
        i += shift
    return -1  # 未找到匹配

# 生成 Sunday 算法的后移位数表
# bc_table[bad_char] 表示遇到坏字符 bad_char 时，模式串可以向右移动的距离
def generateBadCharTable(p: str):
    """
    构建 Sunday 算法的后移位数表。
    参数:
        p: 模式串
    返回:
        dict: 字典，key 为字符，value 为遇到该字符时可向右移动的距离
    """
    m = len(p)
    bc_table = dict()
    # 遍历模式串每个字符（包括最后一个字符）
    for i in range(m):
        # 记录每个字符在模式串中最右侧出现时可向右移动的距离
        bc_table[p[i]] = m - i
    return bc_table

# 测试用例
print(sunday("abbcfdddbddcaddebc", "aaaaa"))  # 输出: -1，未匹配
print(sunday("abbcfdddbddcaddebc", "bcf"))    # 输出: 2，匹配成功
```

## 4. Sunday 算法分析

| 指标         | 复杂度           | 说明                                                         |
| ------------ | ---------------- | ------------------------------------------------------------ |
| 最好时间复杂度   | $O(n)$           | 模式串字符分布均匀，后移位数表能实现最大跳跃，比较次数最少。         |
| 最坏时间复杂度   | $O(n \times m)$  | 模式串字符高度重复且与文本不匹配时，每次只能滑动一位。             |
| 平均时间复杂度   | $O(n)$           | 实际应用中通常接近最好情况，比较次数较少。                       |
| 空间复杂度     | $O(m + \sigma)$   | 主要用于存储后移位数表，$m$ 为模式串长度，$\sigma$ 为字符集大小。    |

- $n$ 为文本串长度，$m$ 为模式串长度，$\sigma$ 为字符集大小。
- Sunday 算法在大多数实际场景下效率较高，但极端情况下可能退化为 $O(n \times m)$。
- 空间消耗主要体现在后移位数表的构建上。

## 5. 总结

Sunday 算法是一种高效的字符串匹配算法，通过利用窗口末尾字符的后移位数表，实现大步跳跃式匹配，提升了实际查找效率，适用于大多数文本搜索场景。

**优点**：
- 实现简单，易于理解和编码。
- 平均性能优良，实际应用中匹配效率高。
- 只需构建一次后移位数表，预处理开销小。
- 跳跃能力强，适合大多数实际文本搜索场景。

**缺点**：
- 最坏情况下时间复杂度较高，可能退化为 $O(n \times m)$。
- 只利用窗口末尾字符的信息，未充分利用更多启发式规则（如 BM 算法的好后缀规则）。
- 对极端重复或特殊构造的模式串不够友好，跳跃能力有限。


## 参考资料

- 【书籍】柔性字符串匹配 - 中科院计算所网络信息安全研究组 译
- 【博文】[字符串模式匹配算法：BM、Horspool、Sunday、KMP、KR、AC算法 - schips - 博客园](https://www.cnblogs.com/schips/p/11098041.html)
- 【博文】[字符串匹配——Sunday 算法 - Switch 的博客 - CSDN 博客](https://blog.csdn.net/q547550831/article/details/51860017)

## 练习题目

- [0028. 找出字符串中第一个匹配项的下标](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0001-0099/find-the-index-of-the-first-occurrence-in-a-string.md)
- [0459. 重复的子字符串](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0400-0499/repeated-substring-pattern.md)
- [0686. 重复叠加字符串匹配](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0600-0699/repeated-string-match.md)
- [0796. 旋转字符串](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/0700-0799/rotate-string.md)
- [1408. 数组中的字符串匹配](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/1400-1499/string-matching-in-an-array.md)
- [2156. 查找给定哈希值的子串](https://github.com/ITCharge/AlgoNote/tree/main/docs/solutions/2100-2199/find-substring-with-given-hash-value.md)

- [单模式串匹配题目列表](https://github.com/ITCharge/AlgoNote/tree/main/docs/00_preface/00_06_categories_list.md#%E5%8D%95%E6%A8%A1%E5%BC%8F%E4%B8%B2%E5%8C%B9%E9%85%8D%E9%A2%98%E7%9B%AE)