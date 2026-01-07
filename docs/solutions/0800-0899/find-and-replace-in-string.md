# [0833. 字符串中的查找与替换](https://leetcode.cn/problems/find-and-replace-in-string/)

- 标签：数组、哈希表、字符串、排序
- 难度：中等

## 题目链接

- [0833. 字符串中的查找与替换 - 力扣](https://leetcode.cn/problems/find-and-replace-in-string/)

## 题目大意

**描述**：

给定一个字符串 $s$ (索引从 0 开始)，你必须对它执行 $k$ 个替换操作。替换操作以三个长度均为 $k$ 的并行数组给出：$indices$, $sources$, $targets$。

要完成第 $i$ 个替换操作:

1. 检查「子字符串 $sources[i]$」是否出现在「原字符串 $s$」的索引 $indices[i]$ 处。
2. 如果没有出现，什么也不做。
3. 如果出现，则用 $targets[i]$「替换」该子字符串。

例如，如果 `s = "abcd"`， `indices[i] = 0`, `sources[i] = "ab"`，`targets[i] = "eee"`，那么替换的结果将是 `"eeecd"`。

所有替换操作必须「同时」发生，这意味着替换操作不应该影响彼此的索引。测试用例保证元素间不会重叠 。

- 例如，一个 `s = "abc"`，`indices = [0,1]`，`sources = ["ab"，"bc"]` 的测试用例将不会生成，因为 `"ab"` 和 `"bc"` 替换重叠。

**要求**：

在对 $s$ 执行所有替换操作后返回「结果字符串」。

**说明**：

- 「子字符串」是字符串中连续的字符序列。
- $1 \le s.length \le 10^{3}$。
- $k == indices.length == sources.length == targets.length$。
- $1 \le k \le 10^{3}$。
- $0 \le indices[i] \lt s.length$。
- $1 \le sources[i].length, targets[i].length \le 50$。
- $s$ 仅由小写英文字母组成。
- $sources[i]$ 和 $targets[i]$ 仅由小写英文字母组成。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2021/06/12/833-ex1.png)

```python
输入：s = "abcd", indices = [0,2], sources = ["a","cd"], targets = ["eee","ffff"]
输出："eeebffff"
解释：
"a" 从 s 中的索引 0 开始，所以它被替换为 "eee"。
"cd" 从 s 中的索引 2 开始，所以它被替换为 "ffff"。
```

- 示例 2：

![](https://assets.leetcode.com/uploads/2021/06/12/833-ex2-1.png)

```python
输入：s = "abcd", indices = [0,2], sources = ["ab","ec"], targets = ["eee","ffff"]
输出："eeecd"
解释：
"ab" 从 s 中的索引 0 开始，所以它被替换为 "eee"。
"ec" 没有从原始的 S 中的索引 2 开始，所以它没有被替换。
```

## 解题思路

### 思路 1：排序 + 模拟

这道题要求对字符串进行多次替换操作，关键是所有替换操作必须同时发生，不能相互影响。

1. 将所有替换操作按照索引从大到小排序，这样从后往前替换时，前面的索引不会受到影响。
2. 对于每个替换操作，检查在指定位置 $indices[i]$ 处是否匹配 $sources[i]$。
3. 如果匹配，则用 $targets[i]$ 替换该子串；否则跳过。
4. 由于从后往前处理，可以直接在原字符串上进行替换操作。

### 思路 1：代码

```python
class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        # 将替换操作按索引从大到小排序，从后往前替换不会影响前面的索引
        operations = sorted(zip(indices, sources, targets), reverse=True)
        
        # 将字符串转为列表，方便操作
        s_list = list(s)
        
        for idx, source, target in operations:
            # 检查在位置 idx 处是否匹配 source
            if s[idx:idx + len(source)] == source:
                # 替换：删除原来的子串，插入新的子串
                s_list[idx:idx + len(source)] = list(target)
        
        return ''.join(s_list)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(k \log k + n)$，其中 $k$ 是替换操作的数量，$n$ 是字符串 $s$ 的长度。排序需要 $O(k \log k)$，每次替换操作最多需要 $O(n)$。
- **空间复杂度**：$O(n)$，需要将字符串转换为列表进行操作。
