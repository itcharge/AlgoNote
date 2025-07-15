# [面试题 08.08. 有重复字符串的排列组合](https://leetcode.cn/problems/permutation-ii-lcci/)

- 标签：字符串、回溯
- 难度：中等

## 题目链接

- [面试题 08.08. 有重复字符串的排列组合 - 力扣](https://leetcode.cn/problems/permutation-ii-lcci/)

## 题目大意

给定一个字符串 `s`，字符串中包含有重复字符。

要求：打印出该字符串中字符的所有排列。可以以任意顺序返回这个字符串数组。

## 解题思路

因为原字符串可能含有重复元素，所以在回溯的时候需要进行去重。先将字符串 `s` 转为 `list` 列表，再对列表进行排序，然后使用 `visited` 数组标记该元素在当前排列中是否被访问过。若未被访问过则将其加入排列中，并在访问后将该元素变为未访问状态。

然后再递归遍历下一层元素之前，增加一句语句进行判重：`if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]: continue`。

然后进行回溯遍历。

## 代码

```python
class Solution:
    res = []
    path = []

    def backtrack(self, ls, visited):
        if len(self.path) == len(ls):
            self.res.append(''.join(self.path))
            return
        for i in range(len(ls)):
            if i > 0 and ls[i] == ls[i - 1] and not visited[i - 1]:
                continue

            if not visited[i]:
                visited[i] = True
                self.path.append(ls[i])
                self.backtrack(ls, visited)
                self.path.pop()
                visited[i] = False

    def permutation(self, S: str) -> List[str]:
        self.res.clear()
        self.path.clear()
        ls = list(S)
        ls.sort()
        visited = [False for _ in range(len(S))]
        self.backtrack(ls, visited)
        return self.res
```

