# [1324. 竖直打印单词](https://leetcode.cn/problems/print-words-vertically/)

- 标签：数组、字符串、模拟
- 难度：中等

## 题目链接

- [1324. 竖直打印单词 - 力扣](https://leetcode.cn/problems/print-words-vertically/)

## 题目大意

**描述**：给定一个字符串 $s$。

**要求**：按照单词在 $s$ 中出现顺序将它们全部竖直返回。

**说明**：

- 单词应该以字符串列表的形式返回，必要时用空格补位，但输出尾部的空格需要删除（不允许尾随空格）。
- 每个单词只能放在一列上，每一列中也只能有一个单词。
- $1 \le s.length \le 200$。
- $s$ 仅含大写英文字母。
- 题目数据保证两个单词之间只有一个空格。

**示例**：

- 示例 1：

```python
输入：s = "HOW ARE YOU"
输出：["HAY","ORO","WEU"]
解释：每个单词都应该竖直打印。 
 "HAY"
 "ORO"
 "WEU"
```

- 示例 2：

```python
输入：s = "TO BE OR NOT TO BE"
输出：["TBONTB","OEROOE","   T"]
解释：题目允许使用空格补位，但不允许输出末尾出现空格。
"TBONTB"
"OEROOE"
"   T"
```

## 解题思路

### 思路 1：模拟

1. 将字符串 $s$ 按空格分割为单词数组 $words$。
2. 计算出单词数组 $words$ 中单词的最大长度 $max\underline{\hspace{0.5em}}len$。
3. 第一重循环遍历竖直单词的每个单词位置 $i$，第二重循环遍历当前第 $j$ 个单词。
   1. 如果当前单词没有第 $i$ 个字符（当前单词的长度超过了单词位置 $i$），则将空格插入到竖直单词中。
   2. 如果当前单词有第 $i$ 个字符，泽讲当前单词的第 $i$ 个字符插入到竖直单词中。
4. 第二重循环遍历完，将竖直单词去除尾随空格，并加入到答案数组中。
5. 第一重循环遍历完，则返回答案数组。

### 思路 1：代码

```Python
class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split(' ')
        max_len = 0
        for word in words:
            max_len = max(len(word), max_len)

        res = []
        for i in range(max_len):
            ans = ""
            for j in range(len(words)):
                if i + 1 > len(words[j]):
                    ans += ' '
                else:
                    ans += words[j][i]
            res.append(ans.rstrip())
        
        return res
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times max(|word|))$，其中 $n$ 为字符串 $s$ 中的单词个数，$max(|word|)$ 是最长的单词长度。。
- **空间复杂度**：$O(n \times max(|word|))$。

