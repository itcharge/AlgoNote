# [1170. 比较字符串最小字母出现频次](https://leetcode.cn/problems/compare-strings-by-frequency-of-the-smallest-character/)

- 标签：数组、哈希表、字符串、二分查找、排序
- 难度：中等

## 题目链接

- [1170. 比较字符串最小字母出现频次 - 力扣](https://leetcode.cn/problems/compare-strings-by-frequency-of-the-smallest-character/)

## 题目大意

**描述**：定义函数 $f(s)$ 用来统计字符串 $s$ 中**字典序最小字母**出现的次数。

比如 `s = "dcce"`：最小的字母是 `"c"`（因为按字母表顺序，c < d < e），它出现了 2 次，所以 $f(s) = 2$。

现在给两个字符串数组：`queries`（待查表）和 `words`（词汇表）。对 `queries` 中的每个字符串，统计 `words` 中有多少个字符串 $W$ 满足 $f(queries[i]) < f(W)$。

**要求**：返回一个整数数组，$answer[i]$ 表示第 $i$ 个查询的结果。

**说明**：

- $1 \le queries.length \le 2000$。
- $1 \le words.length \le 2000$。
- $1 \le queries[i].length, words[i].length \le 10$。
- 所有字符都是小写英文字母。

**示例**：

- 示例 1：

```python
输入：queries = ["cbd"], words = ["zaaaz"]
输出：[1]
解释：f("cbd") = 1（最小字母 b 出现 1 次），f("zaaaz") = 3（最小字母 a 出现 3 次），1 < 3，所以答案=1。
```

- 示例 2：

```python
输入：queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
输出：[1,2]
解释：
f("bbb") = 3，words 中只有 f("aaaa")=4 > 3，所以是 1。
f("cc") = 2，words 中 f("aaa")=3 和 f("aaaa")=4 都 > 2，所以是 2。
```

## 解题思路

### 思路 1：排序 + 二分查找

这道题最直接的想法是：对每个查询，去遍历整个 `words` 数组，数一数有多少个词的 $f$ 值大于查询的 $f$ 值。但是如果有 2000 个查询和 2000 个词，最坏情况要算 400 万次，虽然勉强可以，但不够优雅。

更高效的方法是**排序 + 二分查找**（二分查找就像猜数字，每次猜中间，一次排除一半）：

**步骤拆解：**

1. **定义 $f(s)$ 函数。** 找到字符串中字典序最小的字母（就是按字母表排在最前面的那个），然后数它出现了几次。Python 里用 `min(s)` 找最小字母，用 `s.count(...)` 数次数。

2. **预处理 `words`。** 先把 `words` 中每个词的 $f$ 值都算出来，放到一个数组里，然后从小到大排序。

   比如 `words = ["a","aa","aaa","aaaa"]`，$f$ 值分别是 `[1, 2, 3, 4]`。

3. **对每个查询用二分查找。** 算完查询的 $f$ 值后，在排好序的 `words` $f$ 值数组里，用二分查找找到第一个**大于**查询 $f$ 值的位置。这个位置到数组末尾的元素个数，就是答案。

   比如查询的 $f$ 值是 2，在 `[1, 2, 3, 4]` 中第一个大于 2 的位置是索引 2（对应值 3），从索引 2 到末尾还剩 2 个元素，所以答案是 2。

**为什么排序后要用二分查找？**
因为排好序后，比某个数大的所有数都集中在数组的右边，用二分查找能瞬间定位到那个「分界线」，不用一个个去数。这在数据量大时能大大提速。

### 思路 1：代码

```python
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        # 定义 f(s)：返回 s 中最小字母出现的次数
        def f(s: str) -> int:
            min_char = min(s)           # 找到最小字母
            return s.count(min_char)    # 数它出现了几次
        
        # 预处理：计算 words 中每个词的 f 值，并排序
        word_freqs = sorted([f(word) for word in words])
        
        result = []
        for query in queries:
            query_freq = f(query)  # 当前查询的 f 值
            
            # 在排好序的 f 值数组中，找到第一个大于 query_freq 的位置
            # bisect_right 返回第一个 > query_freq 的位置
            idx = bisect.bisect_right(word_freqs, query_freq)
            
            # 从 idx 到数组末尾的元素，都是 f 值 > query_freq 的词
            # 它们的个数就是答案
            result.append(len(word_freqs) - idx)
        
        return result
```

### 思路 1：复杂度分析

- **时间复杂度**：$O((m + n) \times k + m \log m + n \log m)$。用人话说就是：计算所有字符串的 $f$ 值花一部分时间（$m$ 是 words 数，$n$ 是 queries 数，$k$ 是字符串平均长度），排序花一部分时间，每个查询用二分查找花非常少的时间（$\log m$）。
- **空间复杂度**：$O(m)$。需要存储 `words` 的 $f$ 值数组。
