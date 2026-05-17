# [1255. 得分最高的单词集合](https://leetcode.cn/problems/maximum-score-words-formed-by-letters/)

- 标签：位运算、数组、字符串、动态规划、回溯、状态压缩
- 难度：困难

## 题目链接

- [1255. 得分最高的单词集合 - 力扣](https://leetcode.cn/problems/maximum-score-words-formed-by-letters/)

## 题目大意

**描述**：给定一个单词列表 $words$、一个字母列表 $letters$（每个字母出现次数有限）以及每个字母的得分 $score$（$score[0]$ 对应 `'a'`，$score[1]$ 对应 `'b'`，依此类推）。

**要求**：从 $words$ 中选择一个子集，使得这些单词可以用 $letters$ 中的字母拼出（不超出字母的数量限制），并且总得分最高。返回这个最高得分。

**说明**：

- $1 \le words.length \le 14$。
- $1 \le words[i].length \le 15$。
- $1 \le letters.length \le 100$。
- $letters$ 中可能包含重复字母。
- $score.length == 26$。

**示例**：

- 示例 1：

```python
输入：words = ["dog","cat","dad","good"], 
     letters = ["a","a","c","d","d","d","g","o","o"], 
     score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
输出：23
解释：选择 "dad"(5+1+5=11) 和 "good"(3+2+2+5=12)，总得分 23。
```

- 示例 2：

```python
输入：words = ["xxxz","ax","bx","cx"], 
     letters = ["z","a","b","c","x","x","x"], 
     score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
输出：27
```

## 解题思路

### 思路 1：回溯

#### 1. 核心思想

$words.length \le 14$，指数级别的枚举是可行的。可以使用回溯法（子集枚举）来判断每种组合是否能拼出，并计算最高得分。

这题的思路和 1239（串联字符串的最大长度）非常相似，只不过约束条件从"字符不能重复"变成了"字符不能超出可用数量"。

#### 2. 选择、限制与终止

回溯三要素：

- **选择**：对于当前单词 $words[i]$，有两种选择——选它加入集合，或者跳过它。
- **限制**：选择前，检查当前单词的每个字母是否都能从剩余可用字母中取到（即剩余字母数量足够）。
- **终止**：遍历完所有单词后，用当前总得分更新答案。

#### 3. 具体步骤

**第 1 步**：统计 $letters$ 中每个字母的可用数量 $remain[26]$。

**第 2 步**：定义回溯函数 $backtrack(i, remain, total\_score)$：
- $i$：当前处理到的单词下标。
- $remain$：剩余可用字母的数量数组。
- $total\_score$：当前已选单词的总得分。

对于 $words[i]$：
- 先尝试不选，递归 $i+1$。
- 检查是否能选（$remain$ 是否足够提供 $words[i]$ 所需的所有字母）：
  - 如果能选，从 $remain$ 中扣除这些字母，加上单词得分，递归 $i+1$。
  - 回溯时恢复 $remain$。

**第 3 步**：在递归过程中用 $total\_score$ 更新最大得分。

#### 4. 优化

每次检查单词是否能选时，可以提前计算好每个单词的字母频率和总得分，避免重复计算。

#### 5. 结合示例走一遍

$words = ["dog","cat","dad","good"]$  
$letters = ["a","a","c","d","d","d","g","o","o"]$  
可用字母：a:2, c:1, d:3, g:1, o:2

提前计算每个单词的字母需求：

| 单词 | 字母需求 | 总分 |
|-----|---------|------|
| dog | d:1, o:1, g:1 | 5+2+3=10 |
| cat | c:1, a:1, t:1 | 1+1+0=2 |
| dad | d:2, a:1 | 5+1+5=11 |
| good | g:1, o:2, d:1 | 3+2+2+5=12 |

回溯过程（简化）：

```
i=0(dog): 不选 → ...
i=0(dog): 选 → 扣 d,o,g, 得10分 → i=1
  i=1(cat): 不选 → ...
  i=1(cat): 选 → 还需 c,a,t, a只剩1 ✓ → 扣 c,a,t, 得12分 → i=2
    i=2(dad): 不选 → ...
    i=2(dad): 选 → 还需 d:2,a:1, 剩余 d:2,a:0 → 扣 → 得23分 → i=3
      i=3(good): 不选 → 得分23 ★
      i=3(good): 选 → 还需 g:1,o:2,d:1, 剩余 g:0,o:0,d:1 → 不够 → 跳过
    i=2(dad): 回溯 → 恢复 d:2,a:1
  i=1(cat): 回溯 → 恢复 c,a,t
...
```

最终最大得分为 $23$。

### 思路 1：代码

```python
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        # 统计每个字母的可用数量
        remain = [0] * 26
        for ch in letters:
            remain[ord(ch) - ord('a')] += 1

        # 预处理每个单词的字母需求和得分
        n = len(words)
        word_count = []
        word_score = []
        for word in words:
            cnt = [0] * 26
            s = 0
            for ch in word:
                idx = ord(ch) - ord('a')
                cnt[idx] += 1
                s += score[idx]
            word_count.append(cnt)
            word_score.append(s)

        self.ans = 0

        def backtrack(i: int, remain: list, total: int):
            if i == n:
                self.ans = max(self.ans, total)
                return

            # 不选当前单词
            backtrack(i + 1, remain, total)

            # 尝试选当前单词
            cnt = word_count[i]
            can_pick = True
            for j in range(26):
                if cnt[j] > remain[j]:
                    can_pick = False
                    break

            if can_pick:
                # 扣除字母
                for j in range(26):
                    remain[j] -= cnt[j]
                backtrack(i + 1, remain, total + word_score[i])
                # 回溯恢复
                for j in range(26):
                    remain[j] += cnt[j]

        backtrack(0, remain, 0)
        return self.ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(2^n \times L)$，其中 $n$ 是 $words$ 的长度，$L$ 是单词的平均长度。最坏情况下枚举所有子集，每个子集需要检查单词是否能拼出。
- **空间复杂度**：$O(n)$，递归栈深度为 $O(n)$，以及存储每个单词的字母需求数组。

### 思路 2：状态压缩（迭代枚举）

#### 1. 核心思想

和 1239 题类似，也可以用状态压缩枚举所有子集。对于每个子集，计算总字母需求是否超出限制，以及总得分。

#### 2. 代码

```python
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        # 可用字母总数
        max_count = [0] * 26
        for ch in letters:
            max_count[ord(ch) - ord('a')] += 1

        # 预处理每个单词的字母需求和得分
        n = len(words)
        word_count = []
        word_score = []
        for word in words:
            cnt = [0] * 26
            s = 0
            for ch in word:
                idx = ord(ch) - ord('a')
                cnt[idx] += 1
                s += score[idx]
            word_count.append(cnt)
            word_score.append(s)

        ans = 0
        # 枚举所有子集
        for state in range(1, 1 << n):
            total_need = [0] * 26
            total_score = 0
            ok = True
            for i in range(n):
                if state >> i & 1:
                    for j in range(26):
                        total_need[j] += word_count[i][j]
                        if total_need[j] > max_count[j]:
                            ok = False
                            break
                    if not ok:
                        break
                    total_score += word_score[i]
            if ok:
                ans = max(ans, total_score)
        return ans
```

#### 3. 复杂度分析

- **时间复杂度**：$O(2^n \times n \times 26)$，枚举所有子集，每个子集需要检查字母需求。
- **空间复杂度**：$O(n)$，存储每个单词的字母需求。

回溯法在实际运行中由于剪枝会更快，而状态压缩法的优势在于实现简单、无需递归。
