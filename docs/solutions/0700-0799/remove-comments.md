# [0722. 删除注释](https://leetcode.cn/problems/remove-comments/)

- 标签：数组、字符串
- 难度：中等

## 题目链接

- [0722. 删除注释 - 力扣](https://leetcode.cn/problems/remove-comments/)

## 题目大意

**描述**：

给一个 C++ 程序，删除程序中的注释。这个程序 $source$ 是一个数组，其中 $source[i]$ 表示第 $i$ 行源码。 这表示每行源码由 `'\n'` 分隔。

在 C++ 中有两种注释风格，行内注释和块注释。

- 字符串 `//` 表示行注释，表示//和其右侧的其余字符应该被忽略。
- 字符串 `/*` 表示一个块注释，它表示直到下一个（非重叠）出现的 `*/` 之间的所有字符都应该被忽略。（阅读顺序为从左到右）非重叠是指，字符串 `/*/` 并没有结束块注释，因为注释的结尾与开头相重叠。

第一个有效注释优先于其他注释。

- 如果字符串 `//` 出现在块注释中会被忽略。
- 同样，如果字符串 `/*` 出现在行或块注释中也会被忽略。

如果一行在删除注释之后变为空字符串，那么不要输出该行。即，答案列表中的每个字符串都是非空的。

样例中没有控制字符，单引号或双引号字符。

- 比如，`source = $string$ $s$ = "/* Not a $comment$. */";" 不会出现在测试样例里。

此外，没有其他内容（如定义或宏）会干扰注释。

我们保证每一个块注释最终都会被闭合， 所以在行或块注释之外的/*总是开始新的注释。

最后，隐式换行符可以通过块注释删除。 有关详细信息，请参阅下面的示例。

从源代码中删除注释后，需要以相同的格式返回源代码。

**要求**：

从源代码中删除注释，以相同的格式返回源代码。

**说明**：

- $1 \le source.length \le 10^{3}$。
- $0 \le source[i].length \le 80$。
- $source[i]$ 由可打印的 ASCII 字符组成。
- 每个块注释都会被闭合。
- 给定的源码中不会有单引号、双引号或其他控制字符。

**示例**：

- 示例 1：

```python
输入: source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
输出: ["int main()","{ ","  ","int a, b, c;","a = b + c;","}"]
解释: 示例代码可以编排成这样:
/*Test program */
int main()
{ 
  // variable declaration 
int a, b, c;
/* This is a test
   multiline  
   comment for 
   testing */
a = b + c;
}
第 1 行和第 6-9 行的字符串 /* 表示块注释。第 4 行的字符串 // 表示行注释。
编排后: 
int main()
{ 
  
int a, b, c;
a = b + c;
}
```

- 示例 2：

```python
输入: source = ["a/*comment", "line", "more_comment*/b"]
输出: ["ab"]
解释: 原始的 source 字符串是 "a/*comment\nline\nmore_comment*/b", 其中我们用粗体显示了换行符。删除注释后，隐含的换行符被删除，留下字符串 "ab" 用换行符分隔成数组时就是 ["ab"].
```

## 解题思路

### 思路 1：模拟

删除注释需要处理两种注释：行注释 `//` 和块注释 `/* */`。

**实现步骤**：

1. 使用一个标志 `in_block` 表示当前是否在块注释中。
2. 遍历每一行的每个字符：
   - 如果在块注释中，查找 `*/` 结束块注释。
   - 如果不在块注释中：
     - 遇到 `/*`，进入块注释。
     - 遇到 `//`，忽略该行剩余部分。
     - 否则，将字符加入当前行。
3. 如果当前行不为空且不在块注释中，将其加入结果。

### 思路 1：代码

```python
class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []
        in_block = False  # 是否在块注释中
        current_line = []  # 当前行的内容
        
        for line in source:
            i = 0
            while i < len(line):
                if in_block:
                    # 在块注释中，查找 */
                    if i + 1 < len(line) and line[i:i+2] == '*/':
                        in_block = False
                        i += 2
                    else:
                        i += 1
                else:
                    # 不在块注释中
                    if i + 1 < len(line) and line[i:i+2] == '/*':
                        # 进入块注释
                        in_block = True
                        i += 2
                    elif i + 1 < len(line) and line[i:i+2] == '//':
                        # 行注释，忽略该行剩余部分
                        break
                    else:
                        # 普通字符
                        current_line.append(line[i])
                        i += 1
            
            # 如果不在块注释中且当前行不为空，加入结果
            if not in_block and current_line:
                result.append(''.join(current_line))
                current_line = []
        
        return result
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times m)$，其中 $n$ 是源代码的行数，$m$ 是每行的平均长度。
- **空间复杂度**：$O(n \times m)$，存储结果的空间。
