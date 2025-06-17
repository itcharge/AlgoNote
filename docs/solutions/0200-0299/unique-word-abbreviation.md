# [0288. 单词的唯一缩写](https://leetcode.cn/problems/unique-word-abbreviation/)

- 标签：设计、数组、哈希表、字符串
- 难度：中等

## 题目链接

- [0288. 单词的唯一缩写 - 力扣](https://leetcode.cn/problems/unique-word-abbreviation/)

## 题目大意

单词缩写规则：<起始字母><中间字母><结尾字母>。如果单词长度不超过 2，则单词本身就是缩写。

举例：

- `dog --> d1g`：第一个字母`d`，最后一个字母 `g`，中间隔着 1 个字母。
- `internationalization --> i18n`：第一个字母 `i` ，最后一个字母 `n`，中间隔着 18 个字母。
- `it --> it`：单词只有两个字符，它就是它自身的缩写。

要求实现 ValidWordAbbr 类：

- `ValidWordAbbr(dictionary: List[str]):`使用单词字典初始化对象
- `def isUnique(self, word: str) -> bool:`
  - 如果字典 dictionary 中没有其他单词的缩写与该单词 word 的缩写相同，返回 True。
  - 如果字典 dictionary 中所有与该单词 word 的缩写相同的单词缩写都与 word 相同。

## 解题思路

将相同缩写的单词进行分类，利用哈希表进行存储。键值对格式为 缩写：该缩写对应的 word 列表。

然后初始化的时候，将 dictionary 里的单词按照缩写进行哈希表存储。

在判断的时候，先判断单词 word 的缩写是否能在哈希表中找到对应的映射关系。

- 如果 word 的缩写 abbr 没有在哈希表中，则返回 True。
- 如果 word 的缩写 abbr 在哈希表中：
  - 如果缩写 abbr 对应的字符串列表只有一个字符串，并且就是 word，则返回 True。Ï
  - 否则返回 False。
- 不满足上述要求也返回 False。

## 代码

```python
    def isUnique(self, word: str) -> bool:
        if len(word) <= 2:
            abbr = word
        else:
            abbr = word[0] + chr(len(word)-2) + word[-1]
        if abbr not in self.abbr_dict:
            return True
        if len(set(self.abbr_dict[abbr])) == 1 and word in set(self.abbr_dict[abbr]):
            return True
        return False
```

