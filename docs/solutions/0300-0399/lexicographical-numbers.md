# [0386. 字典序排数](https://leetcode.cn/problems/lexicographical-numbers/)

- 标签：深度优先搜索、字典树
- 难度：中等

## 题目链接

- [0386. 字典序排数 - 力扣](https://leetcode.cn/problems/lexicographical-numbers/)

## 题目大意

给定一个整数 `n`。

要求：按字典序返回范围 `[1, n]` 的所有整数。并且要求时间复杂度为 `O(n)`，空间复杂度为 `o(1)`。

## 解题思路

按照字典序进行深度优先搜索。实质上算是构造一棵字典树，然后将 `[1, n]` 中的数插入到字典树中，并将遍历结果存储到列表中。

## 代码

```python
class Solution:
    def dfs(self, cur, n, res):
        if cur > n:
            return
        res.append(cur)
        for i in range(10):
            num = 10 * cur + i
            if num > n:
                return
            self.dfs(num, n, res)

    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        for i in range(1, 10):
            self.dfs(i, n, res)
        return res
```

