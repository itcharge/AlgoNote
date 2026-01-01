# [0500. 键盘行](https://leetcode.cn/problems/keyboard-row/)

- 标签：数组、哈希表、字符串
- 难度：简单

## 题目链接

- [0500. 键盘行 - 力扣](https://leetcode.cn/problems/keyboard-row/)

## 题目大意

**描述**：

给定一个字符串数组 $words$。

**要求**：

只返回可以使用在「美式键盘」同一行的字母打印出来的单词。键盘如下图所示。

![](https://assets.leetcode.cn/aliyun-lc-upload/uploads/2018/10/12/keyboard.png)

**说明**：

- 字符串「不区分大小写」，相同字母的大小写形式都被视为在同一行。
- 美式键盘中：
   - 第一行由字符 `"qwertyuiop"` 组成。
   - 第二行由字符 `"asdfghjkl"` 组成。
   - 第三行由字符 `"zxcvbnm"` 组成。
- $1 \le words.length \le 20$。
- $1 \le words[i].length \le 10^{3}$。
- $words[i]$ 由英文字母（小写和大写字母）组成。

**示例**：

- 示例 1：

```python
输入：words = ["Hello","Alaska","Dad","Peace"]

输出：["Alaska","Dad"]

解释：

由于不区分大小写，"a" 和 "A" 都在美式键盘的第二行。
```

- 示例 2：

```python
输入：words = ["omk"]

输出：[]
```

## 解题思路

### 思路 1：哈希表映射

将键盘的三行字符分别存储，使用哈希表记录每个字符属于哪一行。对于每个单词，检查其所有字符（转换为小写）是否都在同一行。

具体步骤：

1. 定义三行字符：`row1 = "qwertyuiop", row2 = "asdfghjkl", row3 = "zxcvbnm"`。
2. 创建哈希表，将每个字符映射到其所在行号。
3. 遍历每个单词，检查所有字符是否在同一行。
4. 如果都在同一行，加入结果列表。

### 思路 1：代码

```python
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # 定义键盘三行
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        
        result = []
        
        for word in words:
            # 转换为小写
            word_lower = word.lower()
            # 判断单词的所有字符是否在同一行
            if all(c in row1 for c in word_lower) or \
               all(c in row2 for c in word_lower) or \
               all(c in row3 for c in word_lower):
                result.append(word)
        
        return result
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times m)$，其中 $n$ 是单词数量，$m$ 是平均单词长度，需要检查每个单词的每个字符。
- **空间复杂度**：$O(1)$，只使用了常数额外空间存储三行字符集合。
