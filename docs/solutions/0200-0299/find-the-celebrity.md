# [0277. 搜寻名人](https://leetcode.cn/problems/find-the-celebrity/)

- 标签：图、双指针、交互
- 难度：中等

## 题目链接

- [0277. 搜寻名人 - 力扣](https://leetcode.cn/problems/find-the-celebrity/)

## 题目大意

**描述**：

假设你是一个专业的狗仔，参加了一个 $n$ 人派对，其中每个人被从 $0$ 到 $n - 1$ 标号。在这个派对人群当中可能存在一位「名人」。所谓「名人」的定义是：其他所有 $n - 1$ 个人都认识他 / 她，而他 / 她并不认识其他任何人。
现在你想要确认这个「名人」是谁，或者确定这里没有「名人」。而你唯一能做的就是问诸如「A 你好呀，请问你认不认识 B 呀？」的问题，以确定 A 是否认识 B。你需要在（渐近意义上）尽可能少的问题内来确定这位「名人」是谁（或者确定这里没有 “名人”）。

给定整数 $n$ 和一个辅助函数 `bool knows(a, b)` 用来获取 a 是否认识 b。

**要求**：

实现一个函数 `int findCelebrity(n)`。派对最多只会有一个「名人」参加。

若「名人」存在，请返回他 / 她的编号；若「名人」不存在，请返回 $-1$。

**说明**：

- 注意：$n \times n$ 的二维数组 $graph$ 给定的输入并不是直接提供给你的，而是只能通过辅助函数 `knows` 获取。$graph[i][j] == 1$ 表示 $i$ 认识 $j$，而 $graph[i][j] == 0$ 表示 $j$ 不认识 $i$。
- $n == graph.length == graph[i].length$。
- $2 \le n \le 10^{3}$。
- $graph[i][j]$ 是 $0$ 或 $1$。
- $graph[i][i] == 1$。
 
- 进阶：如果允许调用 API `knows` 的最大次数为 $3 \times n$ ，你可以设计一个不超过最大调用次数的解决方案吗？

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2022/01/19/g1.jpg)

```python
输入: graph = [[1,1,0],[0,1,0],[1,1,1]]
输出: 1
解释: 有编号分别为 0、1 和 2 的三个人。graph[i][j] = 1 代表编号为 i 的人认识编号为 j 的人，而 graph[i][j] = 0 则代表编号为 i 的人不认识编号为 j 的人。“名人” 是编号 1 的人，因为 0 和 2 均认识他/她，但 1 不认识任何人。
```

- 示例 2：

![](https://assets.leetcode.com/uploads/2022/01/19/g2.jpg)

```python
输入: graph = [[1,0,1],[1,1,0],[0,1,1]]
输出: -1
解释: 没有 “名人”
```

## 解题思路

### 思路 1：

利用「候选人淘汰法」在线性次数调用 `knows` 找到唯一可能的名人候选人，再做一次线性校验。

核心观察：若第一个人选为候选人 $cand$，当我们考察另一个人 $i$ 时：

- 如果 `knows(cand, i)` 为真，则 $cand$ 不可能是名人（名人不认识任何人），把候选人更新为 $i$。
- 若 `knows(cand, i)` 为假，则 $i$ 不可能是名人（名人需要被所有人认识，但 $cand$ 就不认识 $i$），候选人保持不变。

一次线性扫描后，剩下的 $cand$ 是唯一可能的名人。再用一轮检查验证：对所有 $j \neq cand$，必须满足 `knows(cand, j) == False` 且 `knows(j, cand) == True`，否则不存在名人。

这保证了调用次数为 $O(n)$ 量级，不会超时。

### 思路 1：代码

```python
# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        # 第一阶段：线性淘汰，确定唯一候选人 cand
        cand = 0
        for i in range(1, n):
            if knows(cand, i):
                # cand 认识 i，cand 不可能是名人
                cand = i
            else:
                # cand 不认识 i，i 不可能是名人，cand 保持
                pass

        # 第二阶段：校验 cand 是否为真正名人
        for j in range(n):
            if j == cand:
                continue
            # 名人不认识任何人，且所有人都认识名人
            if knows(cand, j) or not knows(j, cand):
                return -1

        return cand
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。第一阶段线性淘汰 $n-1$ 次，第二阶段线性校验 $n-1$ 次，总体为线性。
- **空间复杂度**：$O(1)$。仅使用常数个辅助变量。
