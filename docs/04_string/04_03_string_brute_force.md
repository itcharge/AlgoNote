## 1. Brute Force 算法介绍

> **Brute Force 算法**：简称为 BF 算法。中文意思是暴力匹配算法，也可以叫做朴素匹配算法。
>
> - **BF 算法思想**：对于给定文本串 $T$ 与模式串 $p$，从文本串的第一个字符开始与模式串 $p$ 的第一个字符进行比较，如果相等，则继续逐个比较后续字符，否则从文本串 $T$ 的第二个字符起重新和模式串 $p$ 进行比较。依次类推，直到模式串 $p$ 中每个字符依次与文本串 $T$ 的一个连续子串相等，则模式匹配成功。否则模式匹配失败。

![朴素匹配算法](https://qcdn.itcharge.cn/images/20240511154456.png)

## 2. Brute Force 算法步骤

1. 对于给定的文本串 $T$ 与模式串 $p$，求出文本串 $T$ 的长度为 $n$，模式串 $p$ 的长度为 $m$。
2. 同时遍历文本串 $T$ 和模式串 $p$，先将 $T[0]$ 与 $p[0]$ 进行比较。
   1. 如果相等，则继续比较 $T[1]$ 和 $p[1]$。以此类推，一直到模式串 $p$ 的末尾 $p[m - 1]$ 为止。
   2. 如果不相等，则将文本串 $T$ 移动到上次匹配开始位置的下一个字符位置，模式串 $p$ 则回退到开始位置，再依次进行比较。
3. 当遍历完文本串 $T$ 或者模式串 $p$ 的时候停止搜索。

## 3. Brute Force 算法代码实现

```python
def bruteForce(T: str, p: str) -> int:
    n, m = len(T), len(p)
    
    i, j = 0, 0                     # i 表示文本串 T 的当前位置，j 表示模式串 p 的当前位置
    while i < n and j < m:          # i 或 j 其中一个到达尾部时停止搜索
        if T[i] == p[j]:            # 如果相等，则继续进行下一个字符匹配
            i += 1
            j += 1
        else:
            i = i - (j - 1)         # 如果匹配失败则将 i 移动到上次匹配开始位置的下一个位置
            j = 0                   # 匹配失败 j 回退到模式串开始位置

    if j == m:
        return i - j                # 匹配成功，返回匹配的开始位置
    else:
        return -1                   # 匹配失败，返回 -1
```

## 4. Brute Force 算法分析

BF 算法非常简单，容易理解，但其效率很低。主要是因为在匹配过程中可能会出现回溯：当遇到一对字符不同时，模式串 $p$ 直接回到开始位置，文本串也回到匹配开始位置的下一个位置，再重新开始比较。

在回溯之后，文本串和模式串中一些部分的比较是没有必要的。由于这种操作策略，导致 BF 算法的效率很低。最坏情况是每一趟比较都在模式串的最后遇到了字符不匹配的情况，每轮比较需要进行 $m$ 次字符对比，总共需要进行 $n - m + 1$ 轮比较，总的比较次数为 $m \times (n - m + 1) $。所以 BF 算法的最坏时间复杂度为 $O(m \times n)$。

在最理想的情况下（第一次匹配直接匹配成功），BF 算法的最佳时间复杂度是 $O(m)$。

在一般情况下，根据等概率原则，平均搜索次数为 $\frac{(n + m)}{2}$，所以 Brute Force 算法的平均时间复杂度为 $O(n \times m)$。

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
- 【文章】[动画：什么是 BF 算法 ？- 吴师兄学编程](https://www.cxyxiaowu.com/560.html)
- 【文章】[BF 算法（普通模式匹配算法）及 C 语言实现 - 数据结构与算法教程](http://data.biancheng.net/view/12.html)
- 【文章】[字符串匹配基础（上）- 数据结构与算法之美 - 极客时间](https://time.geekbang.org/column/article/71187)
