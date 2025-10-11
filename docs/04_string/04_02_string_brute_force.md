## 1. Brute Force 算法介绍

> **Brute Force 算法**：简称为 BF 算法，也可以叫做「朴素匹配算法」。
> 
> - **Brute Force 算法核心思想**：将模式串 $p$ 依次与文本串 $T$ 的每个起点对齐，从左到右逐字符比对；相等则继续，不等则把对齐起点右移一位，直到匹配成功或遍历完文本。

![朴素匹配算法](https://qcdn.itcharge.cn/images/20240511154456.png)

## 2. Brute Force 算法步骤

1. 设文本串 $T$ 长度为 $n$，模式串 $p$ 长度为 $m$。
2. 从 $T$ 的每个起点 $0..n - m$ 依次与 $p$ 对齐，逐字符比较：如果相等则继续，不相等则起点右移一位、$p$ 归零。
3. 如果某次对齐能把 $p$ 的全部字符匹配完，则返回该起点；否则无解。

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

BF 简单直观，但因不匹配时会完全回退、重新对齐，存在大量重复比较，效率较低。

| 指标         | 复杂度         | 说明                                 |
| ------------ | -------------- | ------------------------------------ |
| 最好时间复杂度   | $O(m)$         | 首个起点即匹配成功                   |
| 最坏时间复杂度   | $O(n \times m)$ | 每次都需回退，全部比较               |
| 平均时间复杂度   | $O(n \times m)$ | 一般情况下的复杂度                   |
| 空间复杂度     | $O(1)$         | 原地匹配，无需额外空间               |

- 大量回溯导致重复比较，是 BF 变慢的根源。
- 当文本或模式较长时，更应考虑 KMP、BM、Sunday 等改进算法。

## 5. 总结

Brute Force（BF）算法通过将模式串与文本串每个可能的起点逐字符对齐比较，遇到不匹配时起点右移、模式串重头开始。该算法实现简单，空间复杂度为 $O(1)$，但时间复杂度较高：最好情况下为 $O(m)$（首位即匹配），平均和最坏情况下为 $O(n\times m)$，适合小规模或一次性匹配场景。

- **优点**：实现简单、无需预处理、适合小规模或一次性匹配。
- **缺点**：回溯多、效率低，不适合长文本/长模式或多次匹配场景。


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
