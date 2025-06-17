# [1408. 数组中的字符串匹配](https://leetcode.cn/problems/string-matching-in-an-array/)

- 标签：数组、字符串、字符串匹配
- 难度：简单

## 题目链接

- [1408. 数组中的字符串匹配 - 力扣](https://leetcode.cn/problems/string-matching-in-an-array/)

## 题目大意

**描述**：给定一个字符串数组 `words`，数组中的每个字符串都可以看作是一个单词。如果可以删除 `words[j]` 最左侧和最右侧的若干字符得到 `word[i]`，那么字符串 `words[i]` 就是 `words[j]` 的一个子字符串。

**要求**：按任意顺序返回 `words` 中是其他单词的子字符串的所有单词。

**说明**：

- $1 \le words.length \le 100$。
- $1 \le words[i].length \le 30$
- `words[i]` 仅包含小写英文字母。
- 题目数据保证每个 `words[i]` 都是独一无二的。

**示例**：

- 示例 1：

```python
输入：words = ["mass","as","hero","superhero"]
输出：["as","hero"]
解释："as" 是 "mass" 的子字符串，"hero" 是 "superhero" 的子字符串。此外，["hero","as"] 也是有效的答案。
```

## 解题思路

### 思路 1：KMP 算法

1. 先按照字符串长度从小到大排序，使用数组 `res` 保存答案。
2. 使用两重循环遍历，对于 `words[i]` 和 `words[j]`，使用 `KMP` 匹配算法，如果 `wrods[j]` 包含 `words[i]`，则将其加入到答案数组中，并跳出最里层循环。
3. 返回答案数组 `res`。

### 思路 1：代码

```python
class Solution:
    # 生成 next 数组
    # next[j] 表示下标 j 之前的模式串 p 中，最长相等前后缀的长度
    def generateNext(self, p: str):
        m = len(p)
        next = [0 for _ in range(m)]                # 初始化数组元素全部为 0
        
        left = 0                                    # left 表示前缀串开始所在的下标位置
        for right in range(1, m):                   # right 表示后缀串开始所在的下标位置
            while left > 0 and p[left] != p[right]: # 匹配不成功, left 进行回退, left == 0 时停止回退
                left = next[left - 1]               # left 进行回退操作
            if p[left] == p[right]:                 # 匹配成功，找到相同的前后缀，先让 left += 1，此时 left 为前缀长度
                left += 1
            next[right] = left                      # 记录前缀长度，更新 next[right], 结束本次循环, right += 1

        return next

    # KMP 匹配算法，T 为文本串，p 为模式串
    def kmp(self, T: str, p: str) -> int:
        n, m = len(T), len(p)
        
        next = self.generateNext(p)                      # 生成 next 数组
        
        j = 0                                       # j 为模式串中当前匹配的位置
        for i in range(n):                          # i 为文本串中当前匹配的位置
            while j > 0 and T[i] != p[j]:           # 如果模式串前缀匹配不成功, 将模式串进行回退, j == 0 时停止回退
                j = next[j - 1]
            if T[i] == p[j]:                        # 当前模式串前缀匹配成功，令 j += 1，继续匹配
                j += 1
            if j == m:                              # 当前模式串完全匹配成功，返回匹配开始位置
                return i - j + 1
        return -1                                   # 匹配失败，返回 -1
        
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=lambda x:len(x))

        res = []
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if self.kmp(words[j], words[i]) != -1:
                    res.append(words[i])           
                    break
        return res
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^2 \times m)$，其中字符串数组长度为 $n$，字符串数组中最长字符串长度为 $m$。
- **空间复杂度**：$O(m)$。
