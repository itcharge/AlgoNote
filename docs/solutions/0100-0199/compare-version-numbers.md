# [0165. 比较版本号](https://leetcode.cn/problems/compare-version-numbers/)

- 标签：双指针、字符串
- 难度：中等

## 题目链接

- [0165. 比较版本号 - 力扣](https://leetcode.cn/problems/compare-version-numbers/)

## 题目大意

**描述**：

给定两个版本号字符串 $version1$ 和 $version2$。

**要求**：

请你比较它们。版本号由被点 `'.'` 分开的修订号组成。修订号的值是它转换为整数并忽略前导零。
比较版本号时，请按从左到右的顺序 依次比较它们的修订号。如果其中一个版本字符串的修订号较少，则将缺失的修订号视为 $0$。

返回规则如下：

- 如果 $version1 < version2$ 返回 $-1$。
- 如果 $version1 > version2$ 返回 $1$。
- 除此之外返回 $0$。

**说明**：

- $1 \le version1.length, version2.length \le 500$。
- $version1$ 和 $version2$ 仅包含数字和 `'.'`。
- $version1$ 和 $version2$ 都是有效版本号。
- $version1$ 和 $version2$ 的所有修订号都可以存储在 $32$ 位整数中。

**示例**：

- 示例 1：

```python
输入：version1 = "1.2", version2 = "1.10"
输出：-1
解释：version1 的第二个修订号为 "2"，version2 的第二个修订号为 "10"：2 < 10，所以 version1 < version2。
```

- 示例 2：

```python
输入：version1 = "1.01", version2 = "1.001"
输出：0
解释：忽略前导零，"01" 和 "001" 都代表相同的整数 "1"。
```

## 解题思路

### 思路 1：双指针

我们可以使用双指针的方法来比较版本号。具体思路如下：

1. **分割版本号**：使用双指针 $i$ 和 $j$ 分别遍历 $version1$ 和 $version2$。
2. **提取修订号**：当遇到点号 `'.'` 时，提取当前修订号并转换为整数。
3. **比较修订号**：比较两个修订号的大小：
   - 如果 $num1 < num2$，返回 $-1$。
   - 如果 $num1 > num2$，返回 $1$。
   - 如果相等，继续比较下一个修订号。
4. **处理长度差异**：当某个版本号的修订号遍历完毕时，将缺失的修订号视为 $0$。

**关键点**：

- 使用 `int()` 函数自动忽略前导零。
- 当指针超出字符串长度时，对应的修订号视为 $0$。
- 需要同时处理两个版本号都遍历完毕的情况。

### 思路 1：代码

```python
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # 初始化双指针
        i, j = 0, 0
        len1, len2 = len(version1), len(version2)
        
        # 使用双指针遍历两个版本号
        while i < len1 or j < len2:
            # 提取 version1 的当前修订号
            num1 = 0
            while i < len1 and version1[i] != '.':
                num1 = num1 * 10 + int(version1[i])
                i += 1
            i += 1  # 跳过点号
            
            # 提取 version2 的当前修订号
            num2 = 0
            while j < len2 and version2[j] != '.':
                num2 = num2 * 10 + int(version2[j])
                j += 1
            j += 1  # 跳过点号
            
            # 比较修订号
            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1
        
        # 所有修订号都相等
        return 0
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(m + n)$，其中 $m$ 和 $n$ 分别是 $version1$ 和 $version2$ 的长度。我们需要遍历两个字符串的每个字符。
- **空间复杂度**：$O(1)$。只使用了常数额外空间。
