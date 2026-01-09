# [0955. 删列造序 II](https://leetcode.cn/problems/delete-columns-to-make-sorted-ii/)

- 标签：贪心、数组、字符串
- 难度：中等

## 题目链接

- [0955. 删列造序 II - 力扣](https://leetcode.cn/problems/delete-columns-to-make-sorted-ii/)

## 题目大意

**描述**：

给定由 $n$ 个字符串组成的数组 $strs$，其中每个字符串长度相等。

选取一个删除索引序列，对于 $strs$ 中的每个字符串，删除对应每个索引处的字符。

比如，有 $strs = ["abcdef", "uvwxyz"]$，删除索引序列 ${0, 2, 3}$，删除后 $strs$ 为 $["bef", "vyz"]$。

假设，我们选择了一组删除索引 $answer$，那么在执行删除操作之后，最终得到的数组的元素是按 字典序（$strs[0] \le strs[1] \le strs[2] ... \le strs[n - 1]$）排列的。

**要求**：

返回 $answer.length$ 的最小可能值。

**说明**：

- $n == strs.length$。
- $1 \le n \le 10^{3}$。
- $1 \le strs[i].length \le 10^{3}$。
- $strs[i]$ 由小写英文字母组成。

**示例**：

- 示例 1：

```python
输入：strs = ["ca","bb","ac"]
输出：1
解释： 
删除第一列后，strs = ["a", "b", "c"]。
现在 strs 中元素是按字典排列的 (即，strs[0] <= strs[1] <= strs[2])。
我们至少需要进行 1 次删除，因为最初 strs 不是按字典序排列的，所以答案是 1。
```

- 示例 2：

```python
输入：strs = ["xc","yb","za"]
输出：0
解释：
strs 的列已经是按字典序排列了，所以我们不需要删除任何东西。
注意 strs 的行不需要按字典序排列。
也就是说，strs[0][0] <= strs[0][1] <= ... 不一定成立。
```

## 解题思路

### 思路 1：贪心算法

#### 思路

这道题要求删除最少的列，使得删除后的字符串数组按字典序排列。与删列造序 I 不同，这里要求的是整个字符串的字典序，而不是每一列的字典序。

我们可以使用贪心策略：

1. 维护一个数组 $sorted$，记录每一行是否已经确定了字典序关系（即前面的列已经使得该行严格小于下一行）。
2. 遍历每一列：
   - 检查该列是否会破坏字典序：对于未确定字典序的相邻行，如果当前列使得前一行大于后一行，则需要删除该列。
   - 如果该列不需要删除，更新 $sorted$ 数组：对于未确定字典序的相邻行，如果当前列使得前一行小于后一行，则标记为已确定。
3. 返回删除的列数。

#### 代码

```python
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)  # 行数
        m = len(strs[0])  # 列数
        count = 0  # 需要删除的列数
        
        # sorted[i] 表示第 i 行和第 i+1 行是否已经确定了字典序关系
        sorted_rows = [False] * (n - 1)
        
        # 遍历每一列
        for j in range(m):
            # 检查当前列是否需要删除
            need_delete = False
            for i in range(n - 1):
                # 如果该行还未确定字典序，且当前列破坏了字典序
                if not sorted_rows[i] and strs[i][j] > strs[i + 1][j]:
                    need_delete = True
                    break
            
            if need_delete:
                # 删除当前列
                count += 1
            else:
                # 更新已确定字典序的行
                for i in range(n - 1):
                    if strs[i][j] < strs[i + 1][j]:
                        sorted_rows[i] = True
        
        return count
```

#### 复杂度分析

- **时间复杂度**：$O(n \times m)$，其中 $n$ 是字符串数组的长度，$m$ 是每个字符串的长度。需要遍历所有字符。
- **空间复杂度**：$O(n)$，需要一个长度为 $n - 1$ 的数组记录字典序关系。
