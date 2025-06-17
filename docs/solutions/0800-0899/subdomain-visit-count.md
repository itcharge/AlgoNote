# [0811. 子域名访问计数](https://leetcode.cn/problems/subdomain-visit-count/)

- 标签：数组、哈希表、字符串、计数
- 难度：中等

## 题目链接

- [0811. 子域名访问计数 - 力扣](https://leetcode.cn/problems/subdomain-visit-count/)

## 题目大意

**描述**：网站域名是由多个子域名构成的。

- 例如 `"discuss.leetcode.com"` 的顶级域名为 `"com"`，二级域名为 `"leetcode.com"`，三级域名为 `"discuss.leetcode.com"`。

当访问 `"discuss.leetcode.com"` 时，也会隐式访问其父域名 `"leetcode.com"` 以及 `"com"`。

计算机配对域名的格式为 `"rep d1.d2.d3"` 或 `"rep d1.d2"`。其中 `rep` 表示访问域名的次数，`d1.d2.d3` 或 `d1.d2` 为域名本身。

- 例如：`"9001 discuss.leetcode.com"` 就是一个 计数配对域名 ，表示 `discuss.leetcode.com` 被访问了 `9001` 次。

现在给定一个由计算机配对域名组成的数组 `cpdomains`。

**要求**：解析每一个计算机配对域名，计算出所有域名的访问次数，并以数组形式返回。可以按任意顺序返回答案。

## 解题思路

这道题求解的是不同层级的域名的次数汇总，很容易想到使用哈希表。我们可以使用哈希表来统计不同层级的域名访问次数。具体做如下：

1. 如果数组 `cpdomains` 为空，直接返回空数组。
2. 使用哈希表 `times_dict` 存储不同层级的域名访问次数。
3. 遍历数组 `cpdomains`。对于每一个计算机配对域名 `cpdomain`：
    1. 先将计算机配对域名的访问次数 `times` 和域名 `domain` 进行分割。
    2. 然后将域名转为子域名数组 `domain_list`，逆序拼接不同等级的子域名 `sub_domain`。
    3. 如果子域名 `sub_domain` 没有出现在哈希表 `times_dict` 中，则在哈希表中存入 `sub_domain` 和访问次数 `times` 的键值对。
    4. 如果子域名 `sub_domain` 曾经出现在哈希表 `times_dict` 中，则在哈希表对应位置加上 `times`。
4. 遍历完之后，遍历哈希表 `times_dict`，将所有域名和访问次数拼接为字符串，存入答案数组中。
5. 最后返回答案数组。

## 代码

```python
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        if not cpdomains:
            return []

        times_dict = dict()
        for cpdomain in cpdomains:
            tiems, domain = cpdomain.split()
            tiems = int(tiems)
            
            domain_list = domain.split('.')
            for i in range(len(domain_list) - 1, -1, -1):
                sub_domain = '.'.join(domain_list[i:])
                if sub_domain not in times_dict:
                    times_dict[sub_domain] = tiems
                else:
                    times_dict[sub_domain] += tiems
        
        res = []
        for key in times_dict.keys():
            res.append(str(times_dict[key]) + ' ' + key)
        return res
```

