# [0997. 找到小镇的法官](https://leetcode.cn/problems/find-the-town-judge/)

- 标签：图、数组、哈希表
- 难度：简单

## 题目链接

- [0997. 找到小镇的法官 - 力扣](https://leetcode.cn/problems/find-the-town-judge/)

## 题目大意

**描述**：

小镇里有 $n$ 个人，按从 1 到 $n$ 的顺序编号。传言称，这些人中有一个暗地里是小镇法官。

如果小镇法官真的存在，那么：

1. 小镇法官不会信任任何人。
2. 每个人（除了小镇法官）都信任这位小镇法官。
3. 只有一个人同时满足属性 1 和属性 2。

给你一个数组 $trust$，其中 $trust[i] = [ai, bi]$ 表示编号为 $ai$ 的人信任编号为 $bi$ 的人。

**要求**：

如果小镇法官存在并且可以确定他的身份，请返回该法官的编号；否则，返回 -1。

**说明**：

- $1 \le n \le 10^{3}$。
- $0 \le trust.length \le 10^{4}$。
- $trust[i].length == 2$。
- $trust$ 中的所有 $trust[i] = [ai, bi]$ 互不相同。
- $ai \ne bi$。
- $1 \le ai, bi \le n$。

**示例**：

- 示例 1：

```python
输入：n = 2, trust = [[1,2]]
输出：2
```

- 示例 2：

```python
输入：n = 3, trust = [[1,3],[2,3]]
输出：3
```

## 解题思路

### 思路 1：入度和出度统计

#### 思路

这道题可以看作一个有向图问题。法官的特点是：

1. 法官不信任任何人（出度为 $0$）。
2. 所有其他人都信任法官（入度为 $n - 1$）。

我们可以用一个数组 $degree$ 来统计每个人的「信任度」：

- 如果 $a$ 信任 $b$，则 $degree[a]$ 减 $1$（出度），$degree[b]$ 加 $1$（入度）。
- 最后遍历数组，找到 $degree$ 值为 $n - 1$ 的人，即为法官。

#### 代码

```python
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # degree[i] 表示 i 的信任度（入度 - 出度）
        degree = [0] * (n + 1)
        
        # 统计每个人的信任度
        for a, b in trust:
            degree[a] -= 1  # a 信任别人，出度 +1
            degree[b] += 1  # b 被信任，入度 +1
        
        # 查找法官：信任度为 n - 1 的人
        for i in range(1, n + 1):
            if degree[i] == n - 1:
                return i
        
        return -1
```

#### 复杂度分析

- **时间复杂度**：$O(n + m)$，其中 $n$ 是人数，$m$ 是信任关系的数量。需要遍历所有信任关系和所有人。
- **空间复杂度**：$O(n)$，需要一个长度为 $n + 1$ 的数组来存储信任度。
