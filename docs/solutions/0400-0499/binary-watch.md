# [0401. 二进制手表](https://leetcode.cn/problems/binary-watch/)

- 标签：位运算、回溯
- 难度：简单

## 题目链接

- [0401. 二进制手表 - 力扣](https://leetcode.cn/problems/binary-watch/)

## 题目大意

**描述**：

二进制手表顶部有 $4$ 个 LED 代表「小时（$0 \sim 11$）」，底部的 $6$ 个 LED 代表「分钟（$0 \sim 59$）」。每个 LED 代表一个 $0$ 或 $1$，最低位在右侧。

- 例如，下面的二进制手表读取 `"4:51"`。

![](https://assets.leetcode.com/uploads/2021/04/08/binarywatch.jpg)

**要求**：

返回二进制手表可以表示的所有可能时间。你可以按任意顺序返回答案。

**说明**：

- 小时不会以零开头：
   - 例如，`"01:00"` 是无效的时间，正确的写法应该是 `"1:00"`。
- 分钟必须由两位数组成，可能会以零开头：
   - 例如，`"10:2"` 是无效的时间，正确的写法应该是 `"10:02"`。
- $0 \le turnedOn \le 10$。

**示例**：

- 示例 1：

```python
输入：turnedOn = 1
输出：["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
```

- 示例 2：

```python
输入：turnedOn = 9
输出：[]
```

## 解题思路

### 思路 1：枚举所有可能的时间

1. 二进制手表有 $4$ 个 LED 表示小时（$0 \sim 11$），$6$ 个 LED 表示分钟（$0 \sim 59$）。
2. 我们需要找到所有可能的 LED 组合，使得总共亮起的 LED 数量等于 $turnedOn$。
3. 对于每个可能的小时 $h$（$0 \leq h \leq 11$），计算其二进制表示中 $1$ 的个数 $count\_hour$。
4. 对于每个可能的分钟 $m$（$0 \leq m \leq 59$），计算其二进制表示中 $1$ 的个数 $count\_minute$。
5. 如果 $count\_hour + count\_minute = turnedOn$，则时间 $h:m$ 是一个有效解。
6. 将所有有效解格式化为字符串形式（小时不补零，分钟补零到两位数）。

### 思路 1：代码

```python
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []
        
        # 枚举所有可能的小时 (0-11)
        for hour in range(12):
            # 计算小时对应的二进制中 1 的个数
            hour_ones = bin(hour).count('1')
            
            # 枚举所有可能的分钟 (0-59)
            for minute in range(60):
                # 计算分钟对应的二进制中 1 的个数
                minute_ones = bin(minute).count('1')
                
                # 如果总 LED 数量等于 turnedOn，则是一个有效时间
                if hour_ones + minute_ones == turnedOn:
                    # 格式化时间：小时不补零，分钟补零到两位数
                    time_str = f"{hour}:{minute:02d}"
                    result.append(time_str)
        
        return result
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(12 \times 60) = O(720)$，需要枚举所有可能的小时和分钟组合。
- **空间复杂度**：$O(k)$，其中 $k$ 是结果的数量，最多为 $720$ 个时间字符串。
