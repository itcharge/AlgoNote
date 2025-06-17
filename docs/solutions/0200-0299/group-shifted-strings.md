# [0249. 移位字符串分组](https://leetcode.cn/problems/group-shifted-strings/)

- 标签：数组、哈希表、字符串
- 难度：中等

## 题目链接

- [0249. 移位字符串分组 - 力扣](https://leetcode.cn/problems/group-shifted-strings/)

## 题目大意

给定一个仅包含小写字母的字符串列表。其中每个字符串都可以进行「移位」操作，也就是将字符串中的每个字母变为其在字母表中后续的字母。比如：`abc` -> `bcd`。

要求：将该列表中满足「移位」操作规律的组合进行分组并返回。

## 解题思路

我们可以先将满足相同「移位」操作规律的组合翻译为相同的模式，然后利用哈希表进行存储。哈希表对应关系为 翻译后模式：该模式对应的原字符串列表。

## 代码

```python
import collections
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        str_dict = collections.defaultdict(list)
        for string in strings:
            if string[0] == 'a':
                str_dict[string].append(string)
            else:
                list_string = list(string)
                for i in range(len(list_string)):
                    num = (ord(list_string[i]) - ord(string[0]) + 26) % 26
                    list_string[i] = chr(num + ord('a'))
                temp_string = ''.join(list_string)
                str_dict[temp_string].append(string)
        res = list()
        for string, sublist in str_dict.items():
            res.append(sublist)
        return res
```

