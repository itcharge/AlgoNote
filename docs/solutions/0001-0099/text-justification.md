# [0068. 文本左右对齐](https://leetcode.cn/problems/text-justification/)

- 标签：数组、字符串、模拟
- 难度：困难

## 题目链接

- [0068. 文本左右对齐 - 力扣](https://leetcode.cn/problems/text-justification/)

## 题目大意

**描述**：

给定一个单词数组 $words$ 和一个长度 $maxWidth$，

**要求**：

重新排版单词，使其成为每行恰好有 $maxWidth$ 个字符，且左右两端对齐的文本。

你应该使用「贪心算法」来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 `' '` 填充，使得每行恰好有 $maxWidth$ 个字符。

要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。

文本的最后一行应为左对齐，且单词之间不插入额外的空格。

**说明**：

- 单词是指由非空格字符组成的字符序列。
- 每个单词的长度大于 $0$，小于等于 $maxWidth$。
- 输入单词数组 $words$ 至少包含一个单词。

**示例**：

- 示例 1：

```python
输入: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
输出:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
```

- 示例 2：

```python
输入:words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
输出:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
     因为最后一行应为左对齐，而不是左右两端对齐。       
     第二行同样为左对齐，这是因为这行只包含一个单词。
```

## 解题思路

### 思路 1：贪心算法 + 模拟

**核心思想**：

使用贪心算法尽可能多地往每行放置单词，然后根据当前行的单词数量和总长度来分配空格，确保每行恰好有 $maxWidth$ 个字符。

**算法步骤**：

1. **贪心选择单词**：从当前位置开始，尽可能多地选择单词放入当前行，直到无法再放入更多单词。
2. **计算空格分配**：根据当前行的单词数量 $word\_count$ 和总字符长度 $total\_length$，计算需要分配的空格数 $spaces\_needed = maxWidth - total\_length$。
3. **分配空格**：
   - 如果只有 $1$ 个单词，所有空格都放在单词后面。
   - 如果有多个单词，计算基础空格数 $base\_spaces = \lfloor \frac{spaces\_needed}{word\_count - 1} \rfloor$ 和额外空格数 $extra\_spaces = spaces\_needed \bmod (word\_count - 1)$。
   - 前 $extra\_spaces$ 个单词间隔分配 $base\_spaces + 1$ 个空格，其余单词间隔分配 $base\_spaces$ 个空格。
4. **处理最后一行**：最后一行左对齐，单词间只放 $1$ 个空格，剩余空格放在行末。

**关键点**：

- 使用贪心策略尽可能多地放置单词。
- 均匀分配空格，左侧空格数不少于右侧。
- 最后一行特殊处理，左对齐即可。

### 思路 1：代码

```python
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """
        文本左右对齐
        """
        result = []
        i = 0
        
        while i < len(words):
            # 贪心选择：尽可能多地选择单词放入当前行
            line_words = []
            line_length = 0
            
            # 选择当前行的单词
            while i < len(words):
                word = words[i]
                # 计算加入当前单词后的长度（包括单词间至少一个空格）
                if line_words:
                    # 已有单词，需要至少一个空格
                    new_length = line_length + 1 + len(word)
                else:
                    # 第一个单词，不需要空格
                    new_length = len(word)
                
                # 如果加入当前单词后超过最大宽度，停止选择
                if new_length > maxWidth:
                    break
                
                line_words.append(word)
                line_length = new_length
                i += 1
            
            # 处理当前行
            if i == len(words):
                # 最后一行：左对齐
                line = ' '.join(line_words)
                # 在行末添加剩余空格
                line += ' ' * (maxWidth - len(line))
            else:
                # 非最后一行：两端对齐
                word_count = len(line_words)
                if word_count == 1:
                    # 只有一个单词，所有空格放在后面
                    line = line_words[0] + ' ' * (maxWidth - len(line_words[0]))
                else:
                    # 多个单词，需要分配空格
                    total_spaces = maxWidth - line_length + word_count - 1
                    base_spaces = total_spaces // (word_count - 1)
                    extra_spaces = total_spaces % (word_count - 1)
                    
                    # 构建当前行
                    line_parts = []
                    for j in range(word_count - 1):
                        line_parts.append(line_words[j])
                        # 前 extra_spaces 个间隔多分配一个空格
                        spaces = base_spaces + (1 if j < extra_spaces else 0)
                        line_parts.append(' ' * spaces)
                    
                    # 添加最后一个单词
                    line_parts.append(line_words[-1])
                    line = ''.join(line_parts)
            
            result.append(line)
        
        return result
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times maxWidth)$，其中 $n$ 是单词的总数。需要遍历所有单词，每行最多处理 $maxWidth$ 个字符。
- **空间复杂度**：$O(n \times maxWidth)$，存储结果字符串，最坏情况下每行都是 $maxWidth$ 个字符。
