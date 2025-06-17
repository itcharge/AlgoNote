# [0691. 贴纸拼词](https://leetcode.cn/problems/stickers-to-spell-word/)

- 标签：位运算、数组、字符串、动态规划、回溯、状态压缩
- 难度：困难

## 题目链接

- [0691. 贴纸拼词 - 力扣](https://leetcode.cn/problems/stickers-to-spell-word/)

## 题目大意

**描述**：给定一个字符串数组 $stickers$ 表示不同的贴纸，其中 $stickers[i]$ 表示第 $i$ 张贴纸上的小写英文单词。再给定一个字符串 $target$。为了拼出给定字符串 $target$，我们需要从贴纸中切割单个字母并重新排列它们。贴纸的数量是无限的，可以重复多次使用。

**要求**：返回需要拼出 $target$ 的最小贴纸数量。如果任务不可能，则返回 $-1$。

**说明**：

- 在所有的测试用例中，所有的单词都是从 $1000$ 个最常见的美国英语单词中随机选择的，并且 $target$ 被选择为两个随机单词的连接。
- $n == stickers.length$。
- $1 \le n \le 50$。
- $1 \le stickers[i].length \le 10$。
- $1 \le target.length \le 15$。
- $stickers[i]$ 和 $target$ 由小写英文单词组成。

**示例**：

- 示例 1：

```python
输入：stickers = ["with","example","science"], target = "thehat"
输出：3
解释：
我们可以使用 2 个 "with" 贴纸，和 1 个 "example" 贴纸。
把贴纸上的字母剪下来并重新排列后，就可以形成目标 “thehat“ 了。
此外，这是形成目标字符串所需的最小贴纸数量。
```

- 示例 2：

```python
输入：stickers = ["notice","possible"], target = "basicbasic"
输出：-1
解释：我们不能通过剪切给定贴纸的字母来形成目标“basicbasic”。
```

## 解题思路

### 思路 1：状态压缩 DP + 广度优先搜索

根据题意，$target$ 的长度最大为 $15$，所以我们可以使用一个长度最多为 $15$ 位的二进制数 $state$ 来表示 $target$ 的某个子序列，如果 $state$ 第 $i$ 位二进制值为 $1$，则说明 $target$ 的第 $i$ 个字母被选中。

然后我们从初始状态 $state = 0$（没有选中 $target$ 中的任何字母）开始进行广度优先搜索遍历。

在广度优先搜索过程中，对于当前状态 $cur\underline{\hspace{0.5em}}state$，我们遍历所有贴纸的所有字母，如果当前字母可以拼到 $target$ 中的某个位置上，则更新状态 $next\underline{\hspace{0.5em}}state$ 为「选中 $target$ 中对应位置上的字母」。

为了得到最小最小贴纸数量，我们可以使用动态规划的方法，定义 $dp[state]$ 表示为到达 $state$ 状态需要的最小贴纸数量。

那么在广度优先搜索中，在更新状态时，同时进行状态转移，即 $dp[next\underline{\hspace{0.5em}}state] = dp[cur\underline{\hspace{0.5em}}state] + 1$。

> 注意：在进行状态转移时，要跳过 $dp[next\underline{\hspace{0.5em}}state]$ 已经有值的情况。

这样在到达状态 $1 \text{ <}\text{< } len(target) - 1$ 时，所得到的 $dp[1 \text{ <}\text{< } len(target) - 1]$ 即为答案。

如果最终到达不了 $dp[1 \text{ <}\text{< } len(target) - 1]$，则说明无法完成任务，返回 $-1$。

### 思路 1：代码

```python
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        size = len(target)
        states = 1 << size
        dp = [0 for _ in range(states)]

        queue = collections.deque([0])

        while queue:
            cur_state = queue.popleft()
            for sticker in stickers:
                next_state = cur_state
                cnts = [0 for _ in range(26)]
                for ch in sticker:
                    cnts[ord(ch) - ord('a')] += 1
                for i in range(size):
                    if cnts[ord(target[i]) - ord('a')] and next_state & (1 << i) == 0:
                        next_state |= (1 << i)
                        cnts[ord(target[i]) - ord('a')] -= 1
                
                if dp[next_state] or next_state == 0:
                    continue
                
                queue.append(next_state)
                dp[next_state] = dp[cur_state] + 1
                if next_state == states - 1:
                    return dp[next_state]
        return -1
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(2^n \times \sum_{i = 0}^{m - 1} len(stickers[i]) \times n$，其中 $n$ 为 $target$ 的长度，$m$ 为 $stickers$ 的元素个数。
- **空间复杂度**：$O(2^n)$。

