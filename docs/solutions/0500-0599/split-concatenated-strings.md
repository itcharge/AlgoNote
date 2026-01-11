# [0555. 分割连接字符串](https://leetcode.cn/problems/split-concatenated-strings/)

- 标签：贪心、数组、字符串
- 难度：中等

## 题目链接

- [0555. 分割连接字符串 - 力扣](https://leetcode.cn/problems/split-concatenated-strings/)

## 题目大意

**描述**：

给定一个字符串数组 $strs$，你可以将这些字符串连接成一个循环字符串。你可以对每个字符串进行以下操作：

1. 选择反转或不反转该字符串
2. 将所有字符串按顺序连接成一个字符串
3. 在连接后的字符串中选择一个分割点，将字符串分成两部分，然后交换这两部分的位置

**要求**：

返回通过上述操作能得到的字典序最大的字符串。

**说明**：

- $1 \le strs.length \le 1000$。
- $1 \le strs[i].length \le 1000$。
- $1 \le sum(strs[i].length) \le 1000$。
- $strs[i]$ 只包含小写英文字母。

**示例**：

- 示例 1：

```python
输入：strs = ["abc","xyz"]
输出："zyxcba"
解释：
反转两个字符串得到 "cba" 和 "zyx"
连接得到 "cbazyx"
在位置 3 分割得到 "cba" 和 "zyx"
交换得到 "zyxcba"
```

- 示例 2：

```python
输入：strs = ["abc"]
输出："cba"
```

## 解题思路

### 思路 1：贪心 + 枚举

**核心策略**：

1. 对于每个字符串，预先选择它本身和它的反转中字典序较大的版本。
2. 枚举每个字符串作为分割点的起始位置。
3. 对于每个分割点，枚举该字符串的每个位置作为分割位置。
4. 尝试该字符串使用原串或反转串。
5. 计算分割后的结果，保留字典序最大的。

**算法步骤**：

1. 预处理：对于数组中的每个字符串 $s$，选择 $\max(s, reverse(s))$。
2. 枚举每个字符串 $strs[i]$ 作为分割的起始位置。
3. 对于当前字符串，尝试使用原串和反转串。
4. 枚举该字符串的每个位置 $j$ 作为分割点。
5. 构造候选字符串：$s[j:] + strs[i+1:] + strs[:i] + s[:j]$。
6. 更新字典序最大的结果。

### 思路 1：代码

```python
class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:
        # 预处理：对每个字符串，选择它和反转后较大的版本
        strs = [max(s, s[::-1]) for s in strs]
        
        result = ""
        
        # 枚举每个字符串作为分割的起始位置
        for i in range(len(strs)):
            # 尝试原串和反转串
            for s in [strs[i], strs[i][::-1]]:
                # 枚举该字符串的每个位置作为分割点
                for j in range(len(s)):
                    # 构造分割后的字符串
                    # 从位置 j 开始的部分 + 后面的字符串 + 前面的字符串 + 位置 j 之前的部分
                    candidate = s[j:] + "".join(strs[i+1:]) + "".join(strs[:i]) + s[:j]
                    result = max(result, candidate)
        
        return result
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times L^2)$，其中 $n$ 是字符串数量，$L$ 是字符串的平均长度。需要枚举每个字符串和每个分割位置，字符串拼接需要 $O(L)$ 时间。
- **空间复杂度**：$O(n \times L)$，需要存储处理后的字符串数组。
