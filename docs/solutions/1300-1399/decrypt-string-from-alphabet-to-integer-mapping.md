# [1309. 解码字母到整数映射](https://leetcode.cn/problems/decrypt-string-from-alphabet-to-integer-mapping/)

- 标签：字符串
- 难度：简单

## 题目链接

- [1309. 解码字母到整数映射 - 力扣](https://leetcode.cn/problems/decrypt-string-from-alphabet-to-integer-mapping/)

## 题目大意

**描述**：给定一个由数字、`#` 组成的字符串，规则为：
- `'1'` 到 `'9'` 分别对应 `'a'` 到 `'i'`。
- `"10#"` 到 `"26#"` 分别对应 `'j'` 到 `'z'`。

**要求**：返回解码后的字符串。

**示例**：

- 示例 1：

```python
输入：s = "10#11#12"
输出："jkab"
解释："j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
```

- 示例 2：

```python
输入：s = "1326#"
输出："acz"
```


## 解题思路

### 思路 1：反向遍历

#### 1. 核心思想

从右向左遍历，遇到 `#` 说明是两位数映射（$10$-$26$），否则是单个数字映射。

#### 2. 具体步骤

**第 1 步**：初始化指针 $i = n-1$，结果列表 $ans$。

**第 2 步**：从右向左遍历：
- 如果 $s[i] == \text{\#}$，取 $s[i-2:i]$ 作为两位数，$i -= 3$。
- 否则取 $s[i]$ 作为个位数，$i -= 1$。
- 将数字转换为对应字母（`'a'` 起始 ASCII 为 $97$）。

### 思路 1：代码

```python
class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = len(s) - 1
        ans = []
        while i >= 0:
            if s[i] == '#':
                num = int(s[i-2:i])
                i -= 3
            else:
                num = int(s[i])
                i -= 1
            ans.append(chr(ord('a') + num - 1))
        return ''.join(reversed(ans))
```

### 思路 1：复杂度分析
- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(n)$。
