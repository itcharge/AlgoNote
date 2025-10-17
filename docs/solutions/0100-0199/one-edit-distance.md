# [0161. 相隔为 1 的编辑距离](https://leetcode.cn/problems/one-edit-distance/)

- 标签：双指针、字符串
- 难度：中等

## 题目链接

- [0161. 相隔为 1 的编辑距离 - 力扣](https://leetcode.cn/problems/one-edit-distance/)

## 题目大意

**描述**：

给定两个字符串 $s$ 和 $t$。

**要求**：

如果它们的编辑距离为 $1$，则返回 $true$，否则返回 $false$。

字符串 $s$ 和字符串 $t$ 之间满足编辑距离等于 $1$ 有三种可能的情形：

- 往 $s$ 中插入「恰好一个」字符得到 $t$。
- 从 $s$ 中删除「恰好一个」字符得到 $t$。
- 在 $s$ 中用「一个不同的字符」替换「恰好一个」字符得到 $t$。

**说明**：

- $0 \le s.length, t.length \le 10^{4}$。
- $s$ 和 $t$ 由小写字母，大写字母和数字组成。

**示例**：

- 示例 1：

```python
输入: s = "ab", t = "acb"
输出: true
解释: 可以将 'c' 插入字符串 s 来得到 t。
```

- 示例 2：

```python
输入: s = "cab", t = "ad"
输出: false
解释: 无法通过 1 步操作使 s 变为 t。
```

## 解题思路

### 思路 1：双指针

我们可以使用双指针的方法来判断两个字符串的编辑距离是否为 $1$。具体思路如下：

1. **长度检查**：如果两个字符串的长度差大于 $1$，则编辑距离不可能为 $1$，直接返回 $false$。
2. **双指针遍历**：使用双指针 $i$ 和 $j$ 分别遍历字符串 $s$ 和 $t$。
3. **字符匹配**：当字符匹配时，两个指针同时前进。
4. **处理不匹配**：当字符不匹配时，根据长度关系判断操作类型：
   - 如果 $len(s) = len(t)$，则进行替换操作，两个指针都前进。
   - 如果 $len(s) < len(t)$，则进行插入操作，只有 $j$ 指针前进。
   - 如果 $len(s) > len(t)$，则进行删除操作，只有 $i$ 指针前进。
5. **计数操作**：记录不匹配的次数，如果超过 $1$ 次，则返回 $false$。

**关键点**：

- 使用双指针 $i$ 和 $j$ 同时遍历两个字符串。
- 根据字符串长度关系判断操作类型。
- 最多允许 $1$ 次不匹配操作。

### 思路 1：代码

```python
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        # 获取字符串长度
        len_s, len_t = len(s), len(t)
        
        # 如果长度差大于1，编辑距离不可能为1
        if abs(len_s - len_t) > 1:
            return False
        
        # 如果两个字符串完全相同，编辑距离为0
        if s == t:
            return False
        
        # 双指针遍历
        i, j = 0, 0
        edit_count = 0  # 记录编辑操作次数
        
        while i < len_s and j < len_t:
            if s[i] == t[j]:
                # 字符匹配，两个指针都前进
                i += 1
                j += 1
            else:
                # 字符不匹配，需要编辑操作
                edit_count += 1
                
                if edit_count > 1:
                    return False
                
                if len_s == len_t:
                    # 长度相等，进行替换操作
                    i += 1
                    j += 1
                elif len_s < len_t:
                    # s较短，进行插入操作
                    j += 1
                else:
                    # s较长，进行删除操作
                    i += 1
        
        # 处理剩余字符
        remaining_edits = (len_s - i) + (len_t - j)
        edit_count += remaining_edits
        
        return edit_count == 1
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(min(m, n))$，其中 $m$ 和 $n$ 分别是字符串 $s$ 和 $t$ 的长度。我们需要遍历较短的字符串。
- **空间复杂度**：$O(1)$。只使用了常数额外空间。
