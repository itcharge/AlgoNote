# [1152. 用户网站访问行为分析](https://leetcode.cn/problems/analyze-user-website-visit-pattern/)

- 标签：数组、哈希表、字符串、排序
- 难度：中等

## 题目链接

- [1152. 用户网站访问行为分析 - 力扣](https://leetcode.cn/problems/analyze-user-website-visit-pattern/)

## 题目大意

**描述**：题目给了三个等长的数组 —— 用户名列表 $username$、访问时间列表 $timestamp$、网站列表 $website$。把它们组合起来看，每个位置 $i$ 代表：「用户 $username[i]$ 在时间 $timestamp[i]$ 访问了网站 $website[i]$。」

**访问模式（Pattern）**：就是按顺序访问的三个网站，比如 `["home", "about", "career"]`。三个网站可以重复，比如 `["leetcode", "love", "leetcode"]` 也算。

**得分**：一个模式每被一个用户按顺序访问过（不要求连续，按顺序就行），就得 1 分。同一个用户重复走同一个模式只算 1 次。

**要求**：返回得分最高的那个模式（以列表形式）。如果最高分有多个模式并列，返回字典序（可以理解为按字母排的先后顺序）最小的那个。

**说明**：

- $3 \le username.length \le 50$（最多 50 条访问记录）。
- $1 \le username[i].length \le 10$。
- $timestamp.length == username.length$。
- $1 \le timestamp[i] \le 10^{9}$。
- $website.length == username.length$。
- $1 \le website[i].length \le 10$。
- $username[i]$ 和 $website[i]$ 都只含小写字符。
- 保证至少有一个用户访问了至少三个网站。
- 所有记录 $[username[i], timestamp[i], website[i]]$ 均不重复。

**示例**：

- 示例 1：

```python
输入：username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"], 
      timestamp = [1,2,3,4,5,6,7,8,9,10], 
      website = ["home","about","career","home","cart","maps","home","home","about","career"]
输出：["home","about","career"]
解释：
joe 访问了：home → about → career（刚好三次，组成一个模式）
james 访问了：home → cart → maps → home（四次，从中可以抽出多种三元组）
mary 访问了：home → about → career（刚好三次，和 joe 模式相同）
所以模式 ("home", "about", "career") 有 joe 和 mary 两个用户，得分最高。
```

- 示例 2：

```python
输入: username = ["ua","ua","ua","ub","ub","ub"], 
      timestamp = [1,2,3,4,5,6], 
      website = ["a","b","a","a","b","c"]
输出: ["a","b","a"]
解释：
ua 访问了 a → b → a，模式 ("a","b","a") 得 1 分。
ub 访问了 a → b → c，模式 ("a","b","c") 等也得 1 分。
("a","b","a") 字典序最小，所以选它。
```

## 解题思路

### 思路 1：哈希表 + 组合枚举

这道题本质上就是一个「统计哪种访问模式最受欢迎」的问题。可以把数据看作一堆「谁在什么时间访问了什么网站」的记录，需要从中找出最受欢迎的「三个网站的访问序列」。

用人话来说，整个过程可以分成以下几步：

**第 1 步：把三条数据合并成一条记录，并按时间排序。**

三个数组是分开给的，但描述的是同一件事。先把它们捏在一起，形成 `(时间, 用户, 网站)` 这样的三元组（可以想象成一条表格里的三列）。然后按时间排好序，这样每个用户的访问顺序就清楚了。

**第 2 步：按用户分组，整理出每个人依次访问了哪些网站。**

用哈希表（可以想象成一本通讯录，每个用户名字对应一个列表）来整理。遍历排序后的记录，把每个用户访问的网站按时间先后顺序放进他的列表里。

比如：
```
joe  → ["home", "about", "career"]
james → ["home", "cart", "maps", "home"]
mary → ["home", "about", "career"]
```

**第 3 步：对每个用户，找出他访问过的所有「三个网站的组合」。**

这里的「组合」是指按顺序选三个网站，但不要求连续。比如 james 访问了 4 个网站，从中按顺序选 3 个，有这些可能：
- `("home", "cart", "maps")`
- `("home", "cart", "home")`
- `("home", "maps", "home")`
- `("cart", "maps", "home")`

注意，同一用户重复的相同模式只算一次（比如 joe 和 mary 虽然模式相同，但他们是不同用户，各算一次）。

**第 4 步：统计每个模式被多少个不同的用户访问过。**

再用一个哈希表来统计：键是模式（三个网站组成的元组），值是一个集合（用来去重，记录有哪些用户访问过这个模式）。遍历每个用户的模式列表，把用户加入对应模式的集合中。

**第 5 步：找出得分最高的模式。**

遍历统计结果，找到集合大小（也就是用户数）最大的模式。如果有多个并列，选字典序（可以理解为字符串比较的顺序）最小的那个。

**小结：** 这个方法的思路很简单——先把数据理清楚，再把所有可能的模式都列出来，最后统计哪个模式最受欢迎。

### 思路 1：代码

```python
from collections import defaultdict
from itertools import combinations

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # 第 1 步：把用户名、时间、网站三个数组合并，按时间排序
        # zip 把三个数组中对应位置的元素捏成三元组，sorted 按时间先后排列
        data = sorted(zip(timestamp, username, website))
        
        # 第 2 步：按用户分组，记录每个人依次访问了哪些网站
        # defaultdict(list) 的意思是：用字典来存，值默认是空列表
        user_visits = defaultdict(list)
        for time, user, site in data:
            user_visits[user].append(site)
        
        # 第 3~4 步：统计每个模式被多少个不同的用户访问过
        # pattern_count 的键是 (网站1, 网站2, 网站3)，值是一个集合（存放用户名）
        pattern_count = defaultdict(set)
        
        for user, sites in user_visits.items():
            # 如果该用户访问的网站不够 3 个，不可能组成模式，直接跳过
            if len(sites) < 3:
                continue
            
            # 用 combinations 函数生成所有可能的"按顺序选 3 个"组合
            # combinations(sites, 3) 会按顺序选出所有三元素子序列
            # 用 set 去重，同一用户重复的相同模式只算一次
            patterns = set(combinations(sites, 3))
            
            # 把这个用户加入每个模式的集合中
            for pattern in patterns:
                pattern_count[pattern].add(user)
        
        # 第 5 步：从所有模式中找出得分最高的
        max_count = 0
        result = None
        
        for pattern, users in pattern_count.items():
            count = len(users)  # 这个模式有多少个不同的用户访问过
            # 如果得分更高，或者得分相同但字典序更小，就更新结果
            if count > max_count or (count == max_count and (result is None or pattern < result)):
                max_count = count
                result = pattern
        
        # 把结果从元组转成列表返回
        return list(result)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \log n + m \times k^3)$。用人话说就是：排序花了一些时间（$n$ 越大越明显）；每个用户 $m$ 需要从他访问的 $k$ 个网站中枚举所有三元组组合，组合数量最多是 $\binom{k}{3}$（即 $k$ 个里选 3 个的方案数）。
- **空间复杂度**：$O(n + m \times k^3)$。需要存储所有用户的访问记录，以及所有可能的三元组模式。
