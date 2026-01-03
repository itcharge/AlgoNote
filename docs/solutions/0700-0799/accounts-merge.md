# [0721. 账户合并](https://leetcode.cn/problems/accounts-merge/)

- 标签：深度优先搜索、广度优先搜索、并查集、数组、哈希表、字符串、排序
- 难度：中等

## 题目链接

- [0721. 账户合并 - 力扣](https://leetcode.cn/problems/accounts-merge/)

## 题目大意

**描述**：

给定一个列表 $accounts$，每个元素 $accounts[i]$ 是一个字符串列表，其中第一个元素 $accounts[i][0]$ 是名称($name$)，其余元素是 $emails$ 表示该账户的邮箱地址。

现在，我们想合并这些账户。如果两个账户都有一些共同的邮箱地址，则两个账户必定属于同一个人。请注意，即使两个账户具有相同的名称，它们也可能属于不同的人，因为人们可能具有相同的名称。一个人最初可以拥有任意数量的账户，但其所有账户都具有相同的名称。

**要求**：

合并账户后，按以下格式返回账户：每个账户的第一个元素是名称，其余元素是按字符 ASCII 顺序排列的邮箱地址。账户本身可以以任意顺序返回。

**说明**：

- $1 \le accounts.length \le 10^{3}$。
- $2 \le accounts[i].length \le 10$。
- $1 \le accounts[i][j].length \le 30$。
- $accounts[i][0]$ 由英文字母组成。
- $accounts[i][j] (for j \gt 0)$ 是有效的邮箱地址。

**示例**：

- 示例 1：

```python
输入：accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
输出：[["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
解释：
第一个和第三个 John 是同一个人，因为他们有共同的邮箱地址 "johnsmith@mail.com"。 
第二个 John 和 Mary 是不同的人，因为他们的邮箱地址没有被其他帐户使用。
可以以任何顺序返回这些列表，例如答案 [['Mary'，'mary@mail.com']，['John'，'johnnybravo@mail.com']，
['John'，'john00@mail.com'，'john_newyork@mail.com'，'johnsmith@mail.com']] 也是正确的。
```

- 示例 2：

```python
输入：accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
输出：[["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]
```

## 解题思路

### 思路 1：并查集

这道题的核心是将具有相同邮箱的账户合并在一起。可以使用并查集来解决。

**解题步骤**：

1. 将每个邮箱看作一个节点，如果两个邮箱属于同一个账户，就将它们连接起来。
2. 使用哈希表 $email\_to\_id$ 记录每个邮箱对应的账户索引。
3. 使用并查集将属于同一个人的邮箱合并到同一个集合中。
4. 遍历所有账户，对于每个账户中的邮箱：
   - 如果邮箱第一次出现，记录其账户索引。
   - 如果邮箱已经出现过，将当前账户与之前的账户合并。
5. 最后，将同一集合中的所有邮箱归类到一起，并按字典序排序。

### 思路 1：代码

```python
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # 并查集
        parent = {}
        
        def find(x):
            if x not in parent:
                parent[x] = x
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parent[root_x] = root_y
        
        # 邮箱到账户索引的映射
        email_to_id = {}
        # 邮箱到姓名的映射
        email_to_name = {}
        
        # 遍历所有账户，建立邮箱之间的连接
        for account in accounts:
            name = account[0]
            for i in range(1, len(account)):
                email = account[i]
                email_to_name[email] = name
                
                if email not in email_to_id:
                    email_to_id[email] = email
                
                # 将当前账户的所有邮箱合并到第一个邮箱的集合中
                union(account[1], email)
        
        # 将同一集合的邮箱归类
        merged = {}
        for email in email_to_id:
            root = find(email)
            if root not in merged:
                merged[root] = []
            merged[root].append(email)
        
        # 构建结果
        result = []
        for emails in merged.values():
            name = email_to_name[emails[0]]
            result.append([name] + sorted(emails))
        
        return result
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \log n)$，其中 $n$ 是所有邮箱的总数。并查集操作的时间复杂度接近 $O(1)$，主要时间消耗在排序上。
- **空间复杂度**：$O(n)$。需要存储并查集、哈希表等数据结构。
