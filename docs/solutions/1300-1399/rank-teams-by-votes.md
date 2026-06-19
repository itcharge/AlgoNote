# [1366. 通过投票对团队排名](https://leetcode.cn/problems/rank-teams-by-votes/)

- 标签：数组、哈希表、字符串、排序、计数
- 难度：中等

## 题目链接

- [1366. 通过投票对团队排名 - 力扣](https://leetcode.cn/problems/rank-teams-by-votes/)

## 题目大意

**描述**：给定一个字符串数组 $votes$，代表投票情况。每个投票人按从高到低的顺序对参赛团队进行排名。其中 $votes[i]$ 表示第 $i$ 个投票人给出的排名顺序（第一个字符为第一名，第二个为第二名，依此类推）。

**要求**：按照以下规则对所有参赛团队进行排名：
1. 比较各团队在「第 1 名」位置上的得票数，得票高的排名靠前。
2. 如果平局，比较「第 2 名」位置上的得票数，依此类推。
3. 如果所有名次的得票数都相同，按团队名称字母顺序升序排列。

**说明**：
- $1 \le votes.length \le 1000$。
- $1 \le votes[i].length \le 26$。
- $votes[i]$ 中的字符均为大写英文字母，且每个字符串都是包含不同字符的排列。

**示例**：

- 示例 1：

```python
输入：votes = ["ABC","ACB","ABC","ACB","ACB"]
输出："ACB"
解释：
A 队获得五票「排位第一」，没有其他队获得「排位第一」，所以 A 队排名第一。
B 队获得两票「排位第二」，三票「排位第三」。
C 队获得三票「排位第二」，两票「排位第三」。
由于 C 队「排位第二」的票数较多，所以 C 队排第二，B 队排第三。
```

- 示例 2：

```python
输入：votes = ["WXYZ","XYZW"]
输出："XWYZ"
解释：
X 队在并列僵局打破后成为排名第一的团队。X 队和 W 队的「排位第一」票数一样，但是 X 队有一票「排位第二」，而 W 没有获得「排位第二」。
```


## 解题思路

### 思路 1：自定义排序

#### 1. 核心思想

统计每个团队在每个名次上获得的票数，然后定义排序规则。

#### 2. 具体步骤

**第 1 步：统计票数**

用字典或二维数组统计。每个团队 $t$ 有一个长度为 $m$ 的票数数组 $count[t]$，其中 $count[t][i]$ 表示团队 $t$ 在第 $i$ 名（$0$ 索引）上的得票数。此外还需要空数组表示名次不够时的处理。

**第 2 步：自定义排序**

Python 的 `sorted` 支持自定义 `key` 函数。排序键可以这样构造：
- 主要：按第 $1$ 名到第 $m$ 名的得票数降序排列
- 次要：如果所有名次都相同，按团队名称升序排列

具体实现：$key = (-count[t][0], -count[t][1], ..., team\_name)$

**第 3 步：拼接结果**

将排好序的团队名称拼接成字符串。

#### 3. 举例说明

以 $votes = ["ABC","ACB","ABC","ACB","ACB"]$ 为例：

各团队名次得票：

| 团队 | 第 1 名票数 | 第 2 名票数 | 第 3 名票数 |
| --- | ---------- | ---------- | ---------- |
| A   | 5          | 0          | 0          |
| B   | 0          | 2          | 3          |
| C   | 0          | 3          | 2          |

排序：
- A 第 1 名 5 票，最高，排第 1
- B 和 C 第 1 名都是 0 票，比较第 2 名：C（3 票）> B（2 票），C 在前

最终排名：`"ACB"`。

### 思路 1：代码

```python
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        if not votes:
            return ""

        teams = list(votes[0])  # 所有参赛团队
        m = len(teams)          # 团队数量（也等于排名位置数）

        # 统计每个团队在每个名次上的得票数
        # count[team] 是长度为 m 的数组
        count = {t: [0] * m for t in teams}

        for vote in votes:
            for rank, team in enumerate(vote):
                count[team][rank] += 1

        # 自定义排序
        # 按名次得票降序（从第 1 名开始），最后按团队名称升序
        def sort_key(team):
            # 返回一个元组：所有名次的得票数取负（降序），团队名称（升序）
            return [-count[team][i] for i in range(m)] + [team]

        teams.sort(key=sort_key)
        return ''.join(teams)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(m \times (n + \log m))$，其中 $n$ 是 $votes$ 长度，$m$ 是团队数。统计票数 $O(m \times n)$，排序 $O(m \log m \times m)$。
- **空间复杂度**：$O(m^2)$，存储每个团队在每个名次的票数。$m \le 26$，空间可忽略。

---

### 思路 2：简写版 key 函数

Python 中可以用 `functools.cmp_to_key` 实现更直观的比较逻辑，但用负数组构造 tuple 的写法更简洁高效。另一种写法是直接用 lambda：

```python
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        if not votes:
            return ""

        teams = list(votes[0])  # 所有参赛团队
        m = len(teams)          # 团队数量（也等于排名位置数）

        # 统计每个团队在每个名次上的得票数
        # count[team] 是长度为 m 的数组
        count = {t: [0] * m for t in teams}

        for vote in votes:
            for rank, team in enumerate(vote):
                count[team][rank] += 1

        # 自定义排序
        # 按名次得票降序（从第 1 名开始），最后按团队名称升序
        teams.sort(key=lambda t: ([-count[t][i] for i in range(m)], t))
        return ''.join(teams)
```
