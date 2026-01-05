# [0777. 在 LR 字符串中交换相邻字符](https://leetcode.cn/problems/swap-adjacent-in-lr-string/)

- 标签：双指针、字符串
- 难度：中等

## 题目链接

- [0777. 在 LR 字符串中交换相邻字符 - 力扣](https://leetcode.cn/problems/swap-adjacent-in-lr-string/)

## 题目大意

**描述**：

在一个由 `'L'`, `'R'` 和 `'X'` 三个字符组成的字符串（例如 `"RXXLRXRXL"`）中进行移动操作。一次移动操作指用一个 `"LX"` 替换一个 `"XL"`，或者用一个 `"XR"` 替换一个 `"RX"`。

现给定起始字符串 $start$ 和结束字符串 $result$。

**要求**：

请编写代码，当且仅当存在一系列移动操作使得 $start$ 可以转换成 $result$ 时，返回 True。

**说明**：

- $1 \le start.length \le 10^{4}$。
- $start.length == result.length$。
- $start$ 和 $result$ 都只包含 `'L'`, `'R'` 或 `'X'`。

**示例**：

- 示例 1：

```python
输入：start = "RXXLRXRXL", result = "XRLXXRRLX"
输出：true
解释：通过以下步骤我们可以将 start 转化为 result：
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX
```

- 示例 2：

```python
输入：start = "X", result = "L"
输出：false
```

## 解题思路

### 思路 1：双指针

观察移动规则：

- `XL` → `LX`：`L` 可以向左移动。
- `RX` → `XR`：`R` 可以向右移动。
- `L` 只能向左移动，`R` 只能向右移动，`X` 不影响相对顺序。

**判断条件**：

1. 去掉所有 `X` 后，$start$ 和 $result$ 的字符序列必须相同。
2. 对于每个 `L`，在 $start$ 中的位置必须 $\ge$ 在 $result$ 中的位置（只能向左移）。
3. 对于每个 `R$，在 $start$ 中的位置必须 $\le$ 在 $result$ 中的位置（只能向右移）。

### 思路 1：代码

```python
class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        # 去掉 X 后的字符序列必须相同
        if start.replace('X', '') != result.replace('X', ''):
            return False
        
        n = len(start)
        i = j = 0
        
        # 使用双指针检查位置关系
        while i < n and j < n:
            # 跳过 X
            while i < n and start[i] == 'X':
                i += 1
            while j < n and result[j] == 'X':
                j += 1
            
            # 如果一个到达末尾，另一个也必须到达末尾
            if (i < n) != (j < n):
                return False
            
            if i < n and j < n:
                # 字符必须相同
                if start[i] != result[j]:
                    return False
                
                # L 只能向左移动，start 中的位置必须 >= result 中的位置
                if start[i] == 'L' and i < j:
                    return False
                
                # R 只能向右移动，start 中的位置必须 <= result 中的位置
                if start[i] == 'R' and i > j:
                    return False
                
                i += 1
                j += 1
        
        return True
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是字符串的长度。
- **空间复杂度**：$O(n)$，字符串替换操作的空间。
