# [0273. 整数转换英文表示](https://leetcode.cn/problems/integer-to-english-words/)

- 标签：递归、数学、字符串
- 难度：困难

## 题目链接

- [0273. 整数转换英文表示 - 力扣](https://leetcode.cn/problems/integer-to-english-words/)

## 题目大意

**描述**：

给定一个非负整数 $num$。

**要求**：

将非负整数 $num$ 转换为其对应的英文表示。

**说明**：

- $0 \le num \le 2^{31} - 1$。

**示例**：

- 示例 1：

```python
输入：num = 123
输出："One Hundred Twenty Three"
```

- 示例 2：

```python
输入：num = 12345
输出："Twelve Thousand Three Hundred Forty Five"
```

## 解题思路

### 思路 1：递归 + 分治

这是一个字符串处理问题，需要将非负整数转换为对应的英文表示。我们可以采用递归分治的思想来解决：

1. **数字分组**：将数字按照千位分组，每三位为一组（个位、十位、百位）。
2. **单位映射**：定义数字到英文单词的映射关系。
3. **递归处理**：对每个三位数组分别处理，然后加上相应的单位。

具体算法步骤：

1. 定义基础数字映射：$0$ 到 $19$ 的英文单词。
2. 定义十位数映射：$20$ 到 $90$ 的十位数英文单词。
3. 定义单位映射：$Thousand$、$Million$、$Billion$。
4. 递归处理每个三位数组：
   - 处理百位数：如果 $hundred > 0$，加上对应的百位数字和 `"Hundred"`。
   - 处理十位数和个位数：如果 $tens < 20$，直接使用基础映射；否则分别处理十位和个位。
5. 根据数字大小添加相应单位。

### 思路 1：代码

```python
class Solution:
    def numberToWords(self, num: int) -> str:
        # 处理特殊情况：0
        if num == 0:
            return "Zero"
        
        # 基础数字映射（0-19）
        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
                "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", 
                "Seventeen", "Eighteen", "Nineteen"]
        
        # 十位数映射（20-90）
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        
        # 单位映射
        thousands = ["", "Thousand", "Million", "Billion"]
        
        def convert_three_digits(n):
            """将三位数转换为英文表示"""
            result = []
            
            # 处理百位数
            if n >= 100:
                result.append(ones[n // 100])
                result.append("Hundred")
                n %= 100
            
            # 处理十位数和个位数
            if n >= 20:
                result.append(tens[n // 10])
                if n % 10:
                    result.append(ones[n % 10])
            elif n > 0:
                result.append(ones[n])
            
            return " ".join(result)
        
        # 将数字按千位分组处理
        result = []
        i = 0
        
        while num > 0:
            # 处理当前三位数组
            three_digits = num % 1000
            if three_digits != 0:
                # 转换当前三位数组
                current = convert_three_digits(three_digits)
                # 添加单位（如果有的话）
                if i > 0:
                    current += " " + thousands[i]
                result.append(current)
            
            # 移动到下一组
            num //= 1000
            i += 1
        
        # 从高位到低位拼接结果
        return " ".join(reversed(result))
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(\log_{10} n)$，其中 $n$ 是输入数字。我们需要处理数字的每一位，数字的位数是 $O(\log_{10} n)$。
- **空间复杂度**：$O(\log_{10} n)$，用于存储结果字符串和递归调用栈。
