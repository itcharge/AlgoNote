# [1405. 最长快乐字符串](https://leetcode.cn/problems/longest-happy-string/)

- 标签：贪心、字符串、堆（优先队列）
- 难度：中等

## 题目链接

- [1405. 最长快乐字符串 - 力扣](https://leetcode.cn/problems/longest-happy-string/)

## 题目大意

**描述**：给定三个整数 $a$、$b$、$c$，分别表示字符 `'a'`、`'b'`、`'c'` 的可用数量。

定义「快乐字符串」为不含 `"aaa"`、`"bbb"`、`"ccc"` 作为子串的字符串，且只包含这三种字符。

**要求**：返回任意一个尽可能长的快乐字符串。如果无法构造，返回空字符串。

**说明**：
- $0 \le a, b, c \le 100$。

**示例**：

- 示例 1：

```python
输入：a = 1, b = 1, c = 7
输出："ccaccbcc"
解释："ccbccacc" 也是一种正确答案。
```

- 示例 2：

```python
输入：a = 2, b = 2, c = 1
输出："aabbc"
```

## 解题思路

### 思路 1：贪心 + 优先队列

#### 1. 核心思想

每次选择当前剩余字符数最多的字符追加到结果末尾，但不能连续出现三个相同字符。如果当前可选字符和结果末尾相同（连续两次），则选次多的字符。

#### 2. 具体步骤

**第 1 步**：构建最大堆，存储 $(\text{剩余数量}, \text{字符})$。

**第 2 步**：每次从堆顶取当前剩余最多的字符：

- 如果堆顶字符与结果末尾相同（已连续两位），弹出堆顶暂存，取次多的。如果堆空，结束。
- 将选中的字符追加到结果，剩余数 $-1$。
- 暂存的字符放回堆。

**第 3 步**：当堆为空或无法再选时停止，返回结果。

#### 3. 举例说明

以 $a=1, b=1, c=7$ 为例：

堆：$(7,c), (1,b), (1,a)$

- 选 `c`，剩 $(6,c)$，结果：`"c"`
- 选 `c`，剩 $(5,c)$，结果：`"cc"`
- 选 `c` 会连续 3 个 `c`，选次多的 `b`，结果：`"ccb"`，$(4,c), (0,b), (1,a)$
- 选 `c`，结果：`"ccbc"`
- 选 `c`，结果：`"ccbcc"`
- 选 `c` 会三连，选 `a`，结果：`"ccbccca"`
- ...

最终结果：`"ccbccaccbcc"` 或类似。

### 思路 1：代码

```python
import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # 最大堆（Python 用负数）
        heap = []
        for count, ch in [(a, 'a'), (b, 'b'), (c, 'c')]:
            if count > 0:
                heapq.heappush(heap, (-count, ch))

        ans = []
        while heap:
            cnt1, ch1 = heapq.heappop(heap)
            # 检查是否会造成三个连续
            if len(ans) >= 2 and ans[-1] == ans[-2] == ch1:
                if not heap:
                    break
                cnt2, ch2 = heapq.heappop(heap)
                ans.append(ch2)
                if -cnt2 > 1:
                    heapq.heappush(heap, (cnt2 + 1, ch2))
                heapq.heappush(heap, (cnt1, ch1))
            else:
                ans.append(ch1)
                if -cnt1 > 1:
                    heapq.heappush(heap, (cnt1 + 1, ch1))

        return ''.join(ans)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O((a+b+c) \times \log 3) = O(n)$，堆操作 $O(\log 3) = O(1)$。
- **空间复杂度**：$O(n)$，结果字符串。
