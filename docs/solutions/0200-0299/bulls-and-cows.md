# [0299. 猜数字游戏](https://leetcode.cn/problems/bulls-and-cows/)

- 标签：哈希表、字符串、计数
- 难度：中等

## 题目链接

- [0299. 猜数字游戏 - 力扣](https://leetcode.cn/problems/bulls-and-cows/)

## 题目大意

**描述**：

你在和朋友一起玩 猜数字（Bulls and Cows）游戏，该游戏规则如下：

写出一个秘密数字，并请朋友猜这个数字是多少。朋友每猜测一次，你就会给他一个包含下述信息的提示：

- 猜测数字中有多少位属于数字和确切位置都猜对了（称为 `"Bulls"`，公牛），
- 有多少位属于数字猜对了但是位置不对（称为 `"Cows"`，奶牛）。也就是说，这次猜测中有多少位非公牛数字可以通过重新排列转换成公牛数字。

给定一个秘密数字 $secret$ 和朋友猜测的数字 $guess$。

**要求**：

请你返回对朋友这次猜测的提示。

提示的格式为 `"xAyB"`，$x$ 是公牛个数， $y$ 是奶牛个数，$A$ 表示公牛，$B$ 表示奶牛。

请注意秘密数字和朋友猜测的数字都可能含有重复数字。

**说明**：

- $1 \le secret.length, guess.length \le 10^{3}$。
- $secret.length == guess.length$。
- $secret$ 和 $guess$ 仅由数字组成。

**示例**：

- 示例 1：

```python
输入：secret = "1807", guess = "7810"
输出："1A3B"
解释：数字和位置都对（公牛）用 '|' 连接，数字猜对位置不对（奶牛）的采用斜体加粗标识。
"1807"
  |
"7810"
```

- 示例 2：

```python
输入：secret = "1123", guess = "0111"
输出："1A1B"
解释：数字和位置都对（公牛）用 '|' 连接，数字猜对位置不对（奶牛）的采用斜体加粗标识。
"1123"        "1123"
  |      or     |
"0111"        "0111"
注意，两个不匹配的 1 中，只有一个会算作奶牛（数字猜对位置不对）。通过重新排列非公牛数字，其中仅有一个 1 可以成为公牛数字。
```

## 解题思路

### 思路 1：哈希表计数

这是一个典型的计数问题。我们需要分别统计 Bulls 和 Cows 的数量。

**算法步骤**：

1. **统计 Bulls**：遍历 $secret$ 和 $guess$，如果 $secret[i] = guess[i]$，则 $bulls$ 计数加 $1$。

2. **统计 Cows**：
   - 使用哈希表 $secret\_count$ 统计 $secret$ 中每个数字的出现次数（排除 Bulls 位置）。
   - 使用哈希表 $guess\_count$ 统计 $guess$ 中每个数字的出现次数（排除 Bulls 位置）。
   - 对于每个数字 $digit$，$cows$ 加上 $min(secret\_count[digit], guess\_count[digit])$。

3. **返回结果**：返回格式为 $f"{bulls}A{cows}B"$。

**关键点**：

- Bulls 位置的数字不能重复计算为 Cows。
- 对于重复数字，Cows 的数量是两者中较小值。

### 思路 1：代码

```python
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0  # Bulls 计数：位置和数字都正确
        cows = 0   # Cows 计数：数字正确但位置错误
        
        # 统计 Bulls
        secret_chars = list(secret)
        guess_chars = list(guess)
        
        for i in range(len(secret)):
            if secret_chars[i] == guess_chars[i]:
                bulls += 1
                # 将 Bulls 位置的字符标记为已使用，避免重复计算
                secret_chars[i] = 'X'
                guess_chars[i] = 'X'
        
        # 统计 Cows
        secret_count = {}  # secret 中每个数字的出现次数（排除 Bulls）
        guess_count = {}   # guess 中每个数字的出现次数（排除 Bulls）
        
        # 统计 secret 中非 Bulls 位置的数字
        for char in secret_chars:
            if char != 'X':
                secret_count[char] = secret_count.get(char, 0) + 1
        
        # 统计 guess 中非 Bulls 位置的数字
        for char in guess_chars:
            if char != 'X':
                guess_count[char] = guess_count.get(char, 0) + 1
        
        # 计算 Cows：对于每个数字，取两者中的较小值
        for digit in secret_count:
            if digit in guess_count:
                cows += min(secret_count[digit], guess_count[digit])
        
        return f"{bulls}A{cows}B"
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是字符串长度。需要遍历字符串两次，哈希表操作的时间复杂度为 $O(1)$。
- **空间复杂度**：$O(1)$，因为数字只有 $0-9$ 共 $10$ 种，哈希表最多存储 $10$ 个键值对，空间复杂度为常数。
