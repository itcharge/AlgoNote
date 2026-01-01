# [0591. 标签验证器](https://leetcode.cn/problems/tag-validator/)

- 标签：栈、字符串
- 难度：困难

## 题目链接

- [0591. 标签验证器 - 力扣](https://leetcode.cn/problems/tag-validator/)

## 题目大意

**描述**：

给定一个表示代码片段的字符串。

**要求**：

实现一个验证器来解析这段代码，并返回它是否合法。

**说明**：

- 合法的代码片段需要遵守以下的所有规则：
   1. 代码必须被合法的闭合标签包围。否则，代码是无效的。
   2. 闭合标签（不一定合法）要严格符合格式：`<TAG_NAME>TAG_CONTENT</TAG_NAME>`。其中，`<TAG_NAME>` 是起始标签，`</TAG_NAME>` 是结束标签。起始和结束标签中的 `TAG_NAME` 应当相同。当且仅当 `TAG_NAME` 和 `TAG_CONTENT` 都是合法的，闭合标签才是合法的。
   3. 合法的 `TAG_NAME` 仅含有大写字母，长度在范围 $[1,9]$ 之间。否则，该 `TAG_NAME` 是不合法的。
   4. 合法的 `TAG_CONTENT` 可以包含其他合法的闭合标签，$cdata$ （请参考规则7）和任意字符（注意参考规则 1）除了不匹配的 `<`、不匹配的起始和结束标签、不匹配的或带有不合法 `TAG_NAME` 的闭合标签。否则，`TAG_CONTENT` 是不合法的。
   5. 一个起始标签，如果没有具有相同 `TAG_NAME` 的结束标签与之匹配，是不合法的。反之亦然。不过，你也需要考虑标签嵌套的问题。
   6. 一个 `<`，如果你找不到一个后续的 `>` 与之匹配，是不合法的。并且当你找到一个 `<` 或 `</` 时，所有直到下一个 `>` 的前的字符，都应当被解析为 `TAG_NAME`（不一定合法）。
   7. $cdata$ 有如下格式：`<![CDATA[CDATA_CONTENT]]>`。`CDATA_CONTENT` 的范围被定义成 `<![CDATA[` 和后续的第一个 `]]>` 之间的字符。
   8. `CDATA_CONTENT` 可以包含任意字符。$cdata$ 的功能是阻止验证器解析 `CDATA_CONTENT`，所以即使其中有一些字符可以被解析为标签（无论合法还是不合法），也应该将它们视为常规字符。
- 假设输入的代码（包括提到的任意字符）只包含数字, 字母, `<`, `>`, `/`, `!`, `[`, `]` 和 ` `。


**示例**：

- 示例 1：

```python
合法代码的例子:

输入: "<DIV>This is the first line <![CDATA[<div>]]></DIV>"

输出: True

解释: 

代码被包含在了闭合的标签内： <DIV> 和 </DIV> 。

TAG_NAME 是合法的，TAG_CONTENT 包含了一些字符和 cdata 。 

即使 CDATA_CONTENT 含有不匹配的起始标签和不合法的 TAG_NAME，它应该被视为普通的文本，而不是标签。

所以 TAG_CONTENT 是合法的，因此代码是合法的。最终返回True。


输入: "<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>"

输出: True

解释:

我们首先将代码分割为： start_tag|tag_content|end_tag 。

start_tag -> "<DIV>"

end_tag -> "</DIV>"

tag_content 也可被分割为： text1|cdata|text2 。

text1 -> ">>  ![cdata[]] "

cdata -> "<![CDATA[<div>]>]]>" ，其中 CDATA_CONTENT 为 "<div>]>"

text2 -> "]]>>]"


start_tag 不是 "<DIV>>>" 的原因参照规则 6 。
cdata 不是 "<![CDATA[<div>]>]]>]]>" 的原因参照规则 7 。
```

- 示例 2：

```python
不合法代码的例子:

输入: "<A>  <B> </A>   </B>"
输出: False
解释: 不合法。如果 "<A>" 是闭合的，那么 "<B>" 一定是不匹配的，反之亦然。

输入: "<DIV>  div tag is not closed  <DIV>"
输出: False

输入: "<DIV>  unmatched <  </DIV>"
输出: False

输入: "<DIV> closed tags with invalid tag name  <b>123</b> </DIV>"
输出: False

输入: "<DIV> unmatched tags with invalid tag name  </1234567890> and <CDATA[[]]>  </DIV>"
输出: False

输入: "<DIV>  unmatched start tag <B>  and unmatched end tag </C>  </DIV>"
输出: False
```

## 解题思路

### 思路 1：栈 + 状态机

这是一个复杂的字符串解析问题，需要使用栈来匹配标签，并处理多种特殊情况。

关键点：

1. 使用栈存储标签名，匹配开始和结束标签
2. 处理 CDATA 部分，CDATA 内的内容不需要验证
3. 验证标签名的合法性（1-9 个大写字母）
4. 确保代码被合法的闭合标签包围
5. 处理各种边界情况

步骤：

1. 从左到右扫描字符串
2. 遇到 `<` 时，判断是开始标签、结束标签还是 CDATA
3. 使用栈维护标签的嵌套关系
4. 验证每个标签的合法性

### 思路 1：代码

```python
class Solution:
    def isValid(self, code: str) -> bool:
        stack = []
        i = 0
        n = len(code)
        
        while i < n:
            if i > 0 and not stack:
                # 如果不在标签内且不是开头，无效
                return False
            
            if code[i:i+9] == '<![CDATA[':
                # CDATA 部分
                if not stack:
                    return False
                j = code.find(']]>', i)
                if j == -1:
                    return False
                i = j + 3
            elif code[i:i+2] == '</':
                # 结束标签
                j = code.find('>', i)
                if j == -1:
                    return False
                tag_name = code[i+2:j]
                if not self.is_valid_tag_name(tag_name):
                    return False
                if not stack or stack[-1] != tag_name:
                    return False
                stack.pop()
                i = j + 1
            elif code[i] == '<':
                # 开始标签
                j = code.find('>', i)
                if j == -1:
                    return False
                tag_name = code[i+1:j]
                if not self.is_valid_tag_name(tag_name):
                    return False
                stack.append(tag_name)
                i = j + 1
            else:
                # 普通字符
                if not stack:
                    return False
                i += 1
        
        return len(stack) == 0
    
    def is_valid_tag_name(self, tag_name: str) -> bool:
        # 标签名必须是 1-9 个大写字母
        if not tag_name or len(tag_name) > 9:
            return False
        return all(c.isupper() for c in tag_name)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是字符串长度，需要遍历整个字符串。
- **空间复杂度**：$O(n)$，栈的深度最多为 $O(n)$。
