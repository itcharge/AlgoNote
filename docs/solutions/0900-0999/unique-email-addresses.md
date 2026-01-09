# [0929. 独特的电子邮件地址](https://leetcode.cn/problems/unique-email-addresses/)

- 标签：数组、哈希表、字符串
- 难度：简单

## 题目链接

- [0929. 独特的电子邮件地址 - 力扣](https://leetcode.cn/problems/unique-email-addresses/)

## 题目大意

**描述**：

每个「有效电子邮件地址」都由一个「本地名」和一个「域名」组成，以 `'@'` 符号分隔。除小写字母之外，电子邮件地址还可以含有一个或多个 `'.'` 或 `'+'`。

- 例如，在 `alice@leetcode.com` 中， $alice$ 是 本地名 ，而 `leetcode.com` 是「域名」。

如果在电子邮件地址的「本地名」部分中的某些字符之间添加句点（`'.'`），则发往那里的邮件将会转发到本地名中没有点的同一地址。请注意，此规则「不适用于域名」。

- 例如，`"alice.z@leetcode.com"` 和 `"alicez@leetcode.com"` 会转发到同一电子邮件地址。

如果在「本地名」中添加加号（`'+'`），则会忽略第一个加号后面的所有内容。这允许过滤某些电子邮件。同样，此规则「不适用于域名」。

- 例如 `m.y+name@email.com` 将转发到 `my@email.com`。

可以同时使用这两个规则。

给定一个字符串数组 $emails$，我们会向每个 $emails[i]$ 发送一封电子邮件。

**要求**：

返回实际收到邮件的不同地址数目。

**说明**：

- $1 \le emails.length \le 10^{3}$。
- $1 \le emails[i].length \le 10^{3}$。
- $emails[i]$ 由小写英文字母、`'+'`、`'.'` 和 `'@'` 组成。
- 每个 $emails[i]$ 都包含有且仅有一个 `'@'` 字符。
- 所有本地名和域名都不为空。
- 本地名不会以 `'+'` 字符作为开头。
- 域名以 `".com"` 后缀结尾。
- 域名在 `".com"` 后缀前至少包含一个字符。

**示例**：

- 示例 1：

```python
输入：emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
输出：2
解释：实际收到邮件的是 "testemail@leetcode.com" 和 "testemail@lee.tcode.com"。
```

- 示例 2：

```python
输入：emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
输出：3
```

## 解题思路

### 思路 1：哈希表 + 字符串处理

对每个邮箱地址进行规范化处理，然后使用哈希表统计不同的邮箱地址数量。

1. 将邮箱地址按 `@` 分割成本地名和域名。
2. 对本地名进行处理：
   - 遇到 `+` 时，忽略 `+` 及其后面的所有字符。
   - 忽略所有 `.` 字符。
3. 将处理后的本地名和域名组合成规范化的邮箱地址。
4. 使用哈希表统计不同的邮箱地址数量。

### 思路 1：代码

```python
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        
        for email in emails:
            # 分割本地名和域名
            local, domain = email.split('@')
            
            # 处理本地名
            # 1. 遇到 '+' 时截断
            if '+' in local:
                local = local[:local.index('+')]
            # 2. 移除所有 '.'
            local = local.replace('.', '')
            
            # 组合规范化的邮箱地址
            normalized = local + '@' + domain
            unique_emails.add(normalized)
        
        return len(unique_emails)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times m)$，其中 $n$ 是邮箱地址的数量，$m$ 是每个邮箱地址的平均长度。
- **空间复杂度**：$O(n \times m)$，需要存储所有规范化后的邮箱地址。
