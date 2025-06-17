# [0953. 验证外星语词典](https://leetcode.cn/problems/verifying-an-alien-dictionary/)

- 标签：数组、哈希表、字符串
- 难度：简单

## 题目链接

- [0953. 验证外星语词典 - 力扣](https://leetcode.cn/problems/verifying-an-alien-dictionary/)

## 题目大意

给定一组用外星语书写的单词字符串数组 `words`，以及表示外星字母表的顺序的字符串 `order` 。

要求：判断 `words` 中的单词是否都是按照 `order` 来排序的。如果是，则返回 `True`，否则返回 `False`。

## 解题思路

如果所有单词是按照 `order` 的规则升序排列，则所有单词都符合规则。而判断所有单词是升序排列，只需要两两比较相邻的单词即可。所以我们可以先用哈希表存储所有字母的顺序，然后对所有相邻单词进行两两比较，如果最终是升序排列，则符合要求。具体步骤如下：

- 使用哈希表 `order_map` 存储字母的顺序。
- 遍历单词数组 `words`，比较相邻单词 `word1` 和 `word2` 中所有字母在 `order_map` 中的下标，看是否满足 `word1 <= word2`。
- 如果全部满足，则返回 `True`。如果有不满足的情况，则直接返回 `False`。 

## 代码

```python
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = dict()
        for i in range(len(order)):
            order_map[order[i]] = i
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            flag = True

            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    if order_map[word1[j]] > order_map[word2[j]]:
                        return False
                    else:
                        flag = False
                        break

            if flag and len(word1) > len(word2):
                return False
        return True
```

