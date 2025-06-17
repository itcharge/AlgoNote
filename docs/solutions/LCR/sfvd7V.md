# [LCR 033. 字母异位词分组](https://leetcode.cn/problems/sfvd7V/)

- 标签：数组、哈希表、字符串、排序
- 难度：中等

## 题目链接

- [LCR 033. 字母异位词分组 - 力扣](https://leetcode.cn/problems/sfvd7V/)

## 题目大意

给定一个字符串数组 `strs`。

要求：将包含字母相同的字符串组合在一起，不需要考虑输出顺序。

## 解题思路

使用哈希表记录字母相同的字符串。对每一个字符串进行排序，按照 排序字符串：字母相同的字符串数组 的键值顺序进行存储。最终将哈希表的值转换为对应数组返回结果。

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

