# [0972. 相等的有理数](https://leetcode.cn/problems/equal-rational-numbers/)

- 标签：数学、字符串
- 难度：困难

## 题目链接

- [0972. 相等的有理数 - 力扣](https://leetcode.cn/problems/equal-rational-numbers/)

## 题目大意

**描述**：

给定两个字符串 $s$ 和 $t$，每个字符串代表一个非负有理数。

有理数 最多可以用三个部分来表示：整数部分 `<IntegerPart>`、小数非重复部分 `<NonRepeatingPart>` 和小数重复部分 `<(><RepeatingPart><)>`。数字可以用以下三种方法之一来表示：

- `<IntegerPart> `
   - 例： 0, 12 和 123 
- `<IntegerPart><.><NonRepeatingPart>`
   - 例： 0.5, 1., 2.12 和 123.0001
- `<IntegerPart><.><NonRepeatingPart><(><RepeatingPart><)>`
   - 例： 0.1(6), 1.(9), 123.00(1212)

十进制展开的重复部分通常在一对圆括号内表示。例如：

`1 / 6 = 0.16666666... = 0.1(6) = 0.1666(6) = 0.166(66)`

**要求**：

只有当它们表示相同的数字时才返回 true，否则返回 false。字符串中可以使用括号来表示有理数的重复部分。

**说明**：

- 每个部分仅由数字组成。
- 整数部分 `<IntegerPart>` 不会以零开头。（零本身除外）
- $1 \le$ `<IntegerPart>.length` $\le 4$。
- $0 \le$ `<NonRepeatingPart>.length` $\le 4$。
- $1 \le$ `<RepeatingPart>.length` $\le 4$。

**示例**：

- 示例 1：

```python
输入：s = "0.(52)", t = "0.5(25)"
输出：true
解释：因为 "0.(52)" 代表 0.52525252...，而 "0.5(25)" 代表 0.52525252525.....，则这两个字符串表示相同的数字。
```

- 示例 2：

```python
输入：s = "0.1666(6)", t = "0.166(66)"
输出：true
```

## 解题思路

### 思路 1：数学 + 字符串处理

#### 思路

这道题要求判断两个有理数字符串是否相等。有理数可以表示为：整数部分 + 非重复小数部分 + 重复小数部分。

关键思路：

1. **解析字符串**：将字符串解析为整数部分、非重复部分和重复部分。
2. **转换为分数**：将有理数转换为分数形式进行比较。
   - 对于重复小数，可以使用数学公式：$0.\overline{abc} = \frac{abc}{999}$，$0.d\overline{abc} = \frac{d}{10} + \frac{abc}{9990}$
3. **比较**：将两个分数化简后比较是否相等。

由于实现较复杂，我们可以使用一个简化的方法：将有理数展开为足够长的小数（例如 $20$ 位），然后比较。

#### 代码

```python
class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        def parse(s):
            """将有理数字符串转换为浮点数"""
            # 查找小数点和括号
            if '.' not in s:
                return float(s)
            
            integer_part, decimal_part = s.split('.')
            
            if '(' not in decimal_part:
                # 没有重复部分
                return float(s)
            
            # 有重复部分
            non_repeat, repeat = decimal_part.split('(')
            repeat = repeat.rstrip(')')
            
            # 构造足够长的小数（20 位）
            # 重复部分重复多次
            repeat_count = (20 - len(non_repeat)) // len(repeat) + 1
            full_decimal = non_repeat + repeat * repeat_count
            full_decimal = full_decimal[:20]  # 截取 20 位
            
            return float(integer_part + '.' + full_decimal)
        
        # 比较两个有理数（使用足够小的误差）
        return abs(parse(s) - parse(t)) < 1e-9
```

#### 复杂度分析

- **时间复杂度**：$O(1)$，字符串长度有限，处理时间为常数。
- **空间复杂度**：$O(1)$，只使用了常数个额外变量。
