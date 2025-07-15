# [面试题 10.02. 变位词组](https://leetcode.cn/problems/group-anagrams-lcci/)

- 标签：数组、哈希表、字符串、排序
- 难度：中等

## 题目链接

- [面试题 10.02. 变位词组 - 力扣](https://leetcode.cn/problems/group-anagrams-lcci/)

## 题目大意

给定一个字符串数组 `strs`。

要求：将所有变位词组合在一起。不需要考虑输出顺序。

- 变位词：字母相同，但排列不同的字符串。

## 解题思路

使用哈希表记录变位词。对每一个字符串进行排序，按照 `排序字符串：变位词数组` 的键值顺序进行存储。

最终将哈希表的值转换为对应数组返回结果。

## 代码

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = dict()
        res = []
        for s in strs:
            sort_s = str(sorted(s))
            if sort_s in str_dict:
                str_dict[sort_s] += [s]
            else:
                str_dict[sort_s] = [s]

        for sort_s in str_dict:
            res += [str_dict[sort_s]]
        return res
```

