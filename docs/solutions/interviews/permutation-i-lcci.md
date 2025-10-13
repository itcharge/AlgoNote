# [面试题 08.07. 无重复字符串的排列组合](https://leetcode.cn/problems/permutation-i-lcci/)

- 标签：字符串、回溯
- 难度：中等

## 题目链接

- [面试题 08.07. 无重复字符串的排列组合 - 力扣](https://leetcode.cn/problems/permutation-i-lcci/)

## 题目大意

给定一个字符串 `S`。

要求：打印出该字符串中字符的所有排列。可以以任意顺序返回这个字符串数组，但里边不能有重复元素。

## 解题思路

使用 `visited` 数组标记该元素在当前排列中是否被访问过。如果未被访问过则将其加入排列中，并在访问后将该元素变为未访问状态。然后进行回溯遍历。

## 代码

```python
class Solution:
    res = []
    path = []

    def backtrack(self, S, visited):
        if len(self.path) == len(S):
            self.res.append(''.join(self.path))
            return
        for i in range(len(S)):
            if not visited[i]:
                visited[i] = True
                self.path.append(S[i])
                self.backtrack(S, visited)
                self.path.pop()
                visited[i] = False

    def permutation(self, S: str) -> List[str]:
        self.res.clear()
        self.path.clear()
        visited = [False for _ in range(len(S))]
        self.backtrack(S, visited)
        return self.res
```

