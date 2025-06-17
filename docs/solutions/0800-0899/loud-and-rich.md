# [0851. 喧闹和富有](https://leetcode.cn/problems/loud-and-rich/)

- 标签：深度优先搜索、图、拓扑排序、数组
- 难度：中等

## 题目链接

- [0851. 喧闹和富有 - 力扣](https://leetcode.cn/problems/loud-and-rich/)

## 题目大意

**描述**：有一组 `n` 个人作为实验对象，从 `0` 到 `n - 1` 编号，其中每个人都有不同数目的钱，以及不同程度的安静值 `quietness`。

现在给定一个数组 `richer`，其中 `richer[i] = [ai, bi]` 表示第 `ai` 个人比第 `bi` 个人更有钱。另给你一个整数数组 `quiet`，其中 `quiet[i]` 是第 `i` 个人的安静值。数组 `richer` 中所给出的数据逻辑自洽（也就是说，在第 `ai` 个人比第 `bi` 个人更有钱的同时，不会出现第 `bi` 个人比第 `ai` 个人更有钱的情况 ）。

**要求**：返回一个长度为 `n` 的整数数组 `answer` 作为答案，其中 `answer[i]` 表示在所有比第 `i` 个人更有钱或者和他一样有钱的人中，安静值最小的那个人的编号。 

**说明**：

- $n == quiet.length$
- $1 \le n \le 500$。
- $0 \le quiet[i] \le n$。
- $quiet$ 的所有值互不相同。
- $0 \le richer.length \le n * (n - 1) / 2$。
- $0 \le ai, bi < n$。
- $ai != bi$。
- $richer$ 中的所有数对 互不相同。
- 对 $richer$ 的观察在逻辑上是一致的。

**示例**：

- 示例 1：

```python
输入：richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet = [3,2,5,4,6,1,7,0]
输出：[5,5,2,5,4,5,6,7]

解释：
answer[0] = 5，
person 5 比 person 3 有更多的钱，person 3 比 person 1 有更多的钱，person 1 比 person 0 有更多的钱。
唯一较为安静（有较低的安静值 quiet[x]）的人是 person 7，
但是目前还不清楚他是否比 person 0 更有钱。
answer[7] = 7，
在所有拥有的钱肯定不少于 person 7 的人中（这可能包括 person 3，4，5，6 以及 7），
最安静（有较低安静值 quiet[x]）的人是 person 7。
其他的答案也可以用类似的推理来解释。
```

## 解题思路

### 思路 1：拓扑排序

对于第 `i` 个人，我们要求解的是比第 `i` 个人更有钱或者和他一样有钱的人中，安静值最小的那个人的编号。 

我们可以建立一张有向无环图，由富人指向穷人。这样，对于任意一点来说（比如 `x`），通过有向边链接的点（比如 `y`），拥有的钱都没有 `x` 多。则我们可以根据 `answer[x]` 去更新所有 `x` 能连接到的点的 `answer` 值。

我们可以先将数组 `answer`  元素初始化为当前元素编号。然后对建立的有向无环图进行拓扑排序，按照拓扑排序的顺序去更新 `x` 能连接到的点的 `answer` 值。

### 思路 1：拓扑排序代码

```python
import collections

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        size = len(quiet)
        indegrees = [0 for _ in range(size)]
        edges = collections.defaultdict(list)

        for x, y in richer:
            edges[x].append(y)
            indegrees[y] += 1

        res = [i for i in range(size)]
        queue = collections.deque([])
        for i in range(size):
            if not indegrees[i]:
                queue.append(i)

        while queue:
            x = queue.popleft()
            size -= 1
            for y in edges[x]:
                if quiet[res[x]] < quiet[res[y]]:
                    res[y] = res[x]
                indegrees[y] -= 1
                if not indegrees[y]:
                    queue.append(y)
        return res
```
