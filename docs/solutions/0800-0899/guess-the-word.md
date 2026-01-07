# [0843. 猜猜这个单词](https://leetcode.cn/problems/guess-the-word/)

- 标签：数组、数学、字符串、博弈、交互
- 难度：困难

## 题目链接

- [0843. 猜猜这个单词 - 力扣](https://leetcode.cn/problems/guess-the-word/)

## 题目大意

**描述**：

给定一个由「不同」字符串组成的单词列表 $words$，其中 $words[i]$ 长度均为 6。$words$ 中的一个单词将被选作秘密单词 $secret$。

另给你一个辅助对象 Master，你可以调用 `Master.guess(word)` 来猜单词，其中参数 $word$ 长度为 6 且必须是 $words$ 中的字符串。

`Master.guess(word)` 将会返回如下结果：

- 如果 $word$ 不是 $words$ 中的字符串，返回 -1，或者
- 一个整数，表示你所猜测的单词 $word$ 与「秘密单词 $secret$」的准确匹配（值和位置同时匹配）的数目。

每组测试用例都会包含一个参数 $allowedGuesses$，其中 $allowedGuesses$ 是你可以调用 `Master.guess(word)` 的最大次数。

**要求**：

对于每组测试用例，如果在不超过允许猜测的次数的前提下：

- 如果能够通过调用 `Master.guess` 来猜出秘密单词，则返回 `"You guessed the secret word correctly."`。
- 如果猜不出或者超过允许猜测的次数，则返回 `"Either you took too many guesses, or you did not find the secret word."`。

**说明**：

- 生成的测试用例保证你可以利用某种合理的策略（而不是暴力）猜到秘密单词。
- $1 \le words.length \le 10^{3}$。
- $words[i].length == 6$。
- $words[i]$ 仅由小写英文字母组成。
- $words$ 中所有字符串「互不相同」。
- $secret$ 存在于 $words$ 中。
- $10 \le allowedGuesses \le 30$。

**示例**：

- 示例 1：

```python
输入：secret = "acckzz", words = ["acckzz","ccbazz","eiowzz","abcczz"], allowedGuesses = 10
输出：You guessed the secret word correctly.
解释：
master.guess("aaaaaa") 返回 -1 ，因为 "aaaaaa" 不在 words 中。
master.guess("acckzz") 返回 6 ，因为 "acckzz" 是秘密单词 secret ，共有 6 个字母匹配。
master.guess("ccbazz") 返回 3 ，因为 "ccbazz" 共有 3 个字母匹配。
master.guess("eiowzz") 返回 2 ，因为 "eiowzz" 共有 2 个字母匹配。
master.guess("abcczz") 返回 4 ，因为 "abcczz" 共有 4 个字母匹配。
一共调用 5 次 master.guess ，其中一个为秘密单词，所以通过测试用例。
```

- 示例 2：

```python
输入：secret = "hamada", words = ["hamada","khaled"], allowedGuesses = 10
输出：You guessed the secret word correctly.
解释：共有 2 个单词，且其中一个为秘密单词，可以通过测试用例。
```

## 解题思路

### 思路 1：MinMax 策略 + 预计算匹配矩阵

这道题要求通过调用 API 猜测秘密单词。关键是设计一个好的策略来选择每次猜测的单词。

**核心思想**：

- 每次猜测后，根据返回的匹配数，可以过滤掉大量不可能的候选单词。
- 我们希望选择一个单词，使得无论返回什么匹配数，剩余的候选单词数量都尽可能少。
- 这是一个 MinMax 策略：最小化最坏情况下的候选单词数量。

**关键优化**：

1. **预计算匹配矩阵**：提前计算所有单词对之间的匹配数，避免重复计算。
2. **排除已猜单词**：在选择猜测单词时，排除已经猜过的单词。
3. **MinMax 选择**：对于每个候选单词，统计不同匹配数对应的候选单词分组，选择最大分组最小的单词。

**算法步骤**：

1. 预计算所有单词对之间的匹配数矩阵 $H[i][j]$，表示单词 $i$ 和单词 $j$ 的匹配数。
2. 初始化候选单词索引列表和已猜单词集合。
3. 每次使用 MinMax 策略选择最优的猜测单词：
   - 对于每个未猜过的候选单词，统计不同匹配数对应的候选单词分组。
   - 选择最大分组最小的单词（即最坏情况下剩余候选单词最少的单词）。
4. 调用 `master.guess()` 获取匹配数。
5. 如果匹配数为 $6$，说明猜中，直接返回。
6. 否则，过滤候选单词：只保留与猜测单词有相同匹配数的单词。
7. 重复步骤 3-6，直到猜中。

### 思路 1：代码

```python
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        n = len(words)
        
        # 预计算所有单词对之间的匹配数矩阵
        H = [[sum(a == b for a, b in zip(words[i], words[j])) 
              for j in range(n)] for i in range(n)]
        
        # 候选单词索引列表
        possible = list(range(n))
        # 已猜单词集合
        guessed = set()
        
        while possible:
            # 使用 MinMax 策略选择最优单词
            guess_idx = self.solve(H, possible, guessed)
            
            # 猜测单词
            matches = master.guess(words[guess_idx])
            
            # 如果猜中，直接返回
            if matches == len(words[0]):
                return
            
            # 将当前猜测加入已猜集合
            guessed.add(guess_idx)
            
            # 过滤候选单词：只保留与猜测单词有相同匹配数的单词
            possible = [j for j in possible if H[guess_idx][j] == matches]
    
    def solve(self, H, possible, guessed):
        # 如果候选单词数量很少，直接返回第一个
        if len(possible) <= 2:
            return possible[0]
        
        min_max_group_size = float('inf')
        best_guess = possible[0]
        
        # 遍历所有未猜过的单词
        for guess_idx in range(len(H)):
            if guess_idx in guessed:
                continue
            
            # 统计不同匹配数对应的候选单词分组
            groups = [[] for _ in range(7)]  # 匹配数从 0 到 6
            
            for j in possible:
                if j != guess_idx:
                    groups[H[guess_idx][j]].append(j)
            
            # 找到最大的分组（最坏情况）
            max_group = max(groups, key=len)
            
            # 选择最坏情况最好的单词
            if len(max_group) < min_max_group_size:
                min_max_group_size = len(max_group)
                best_guess = guess_idx
        
        return best_guess
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^2 \times m + n^2 \times k)$，其中 $n$ 是单词数量，$m$ 是单词长度，$k$ 是猜测次数（最多 $10$ 次）。预计算匹配矩阵需要 $O(n^2 \times m)$ 时间，每次选择最优单词需要 $O(n^2)$ 时间。
- **空间复杂度**：$O(n^2)$，需要存储匹配矩阵。
