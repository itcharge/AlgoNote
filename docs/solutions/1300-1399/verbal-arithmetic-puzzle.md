# [1307. 口算难题](https://leetcode.cn/problems/verbal-arithmetic-puzzle/)

- 标签：数组、数学、字符串、回溯
- 难度：困难

## 题目链接

- [1307. 口算难题 - 力扣](https://leetcode.cn/problems/verbal-arithmetic-puzzle/)

## 题目大意

**描述**：给定一个方程，用字符串数组 $words$ 和字符串 $result$ 表示。其中每个字符是大写英文字母 `'A'~'Z'`，代表一个数字（$0$ ~ $9$）。

**要求**：判断是否存在一种将字母映射到数字的方案，使得 $words$ 中的字符串表示的数字之和等于 $result$ 表示的数字。每个字母代表唯一的数字，且任何数字不能有前导零（除非数字本身就是 $0$）。

**说明**：
- $2 \le words.length \le 20$。
- $result.length \le 7$。
- $words[i].length \le 7$。
- 最多有 $10$ 个不同字母。

**示例**：

- 示例 1：

```python
输入：words = ["SEND","MORE"], result = "MONEY"
输出：true
解释：映射 'S'-> 9, 'E'->5, 'N'->6, 'D'->7, 'M'->1, 'O'->0, 'R'->8, 'Y'->'2'
所以 "SEND" + "MORE" = "MONEY" ,  9567 + 1085 = 10652
```

- 示例 2：

```python
输入：words = ["SIX","SEVEN","SEVEN"], result = "TWENTY"
输出：true
解释：映射 'S'-> 6, 'I'->5, 'X'->0, 'E'->8, 'V'->7, 'N'->2, 'T'->1, 'W'->'3', 'Y'->4
所以 "SIX" + "SEVEN" + "SEVEN" = "TWENTY" ,  650 + 68782 + 68782 = 138214
```


## 解题思路

### 思路 1：回溯 + 剪枝

#### 1. 核心思想

字母数量最多 $10$ 个（$0$ ~ $9$），可以用回溯法枚举每个字母的数字映射。但由于排列组合数量大（最坏 $10!$），需要充分的剪枝优化。

关键剪枝思想：**从右到左逐列验证**。在回溯过程中，一旦发现某一列的和在已知映射下不可能成立，立即回溯。

#### 2. 具体步骤

**第 1 步：收集所有不同字母**

遍历 $words$ 和 $result$，收集出现的所有字母。如果字母数 $> 10$，直接返回 $False$。

**第 2 步：记录前导零限制**

每个单词的首字母不能为 $0$（如果单词长度 $> 1$）。记录这些字母的集合 $leading$。

**第 3 步：回溯枚举**

从最右列（个位）开始，逐列验证。递归函数参数：
- $col$：当前处理的列（从个位 $0$ 开始）
- $carry$：进位
- $idx$：当前正在分配第几个字母
- $assign$：字母到数字的映射（$26$ 长度数组，$-1$ 表示未分配）
- $used$：数字是否已使用

回溯过程：
1. 如果所有字母已分配，检查等式是否成立（所有列处理完毕且进位为 $0$）。
2. 否则，选择一个未分配数字的字母，尝试分配 $0$ ~ $9$。

**剪枝优化**：
- 在每列计算时，如果已知的字母映射已经能判断该列的和不匹配，提前回溯。
- $leading$ 字母不能分配 $0$。

**第 4 步：列验证函数**

对于当前列 $col$，计算 $words$ 中所有长度 $> col$ 的单词在该列字符的和，加上进位，检查个位是否等于 $result$ 在该列的字符（如果该字符已分配数字）。如果与已知映射矛盾，则剪枝。

#### 3. 举例说明

以 $words = ["SEND","MORE"]$，$result = "MONEY"$ 为例：

```
  S E N D
+ M O R E
---------
M O N E Y
```

从个位 $D+E=Y$ 开始：
1. 尝试 $D=7, E=5$ → $7+5=12$ → $Y=2$，进位 $1$
2. 十位 $N+R+1=E$ → $N+R+1=5$ → 不成立，回溯
3. 继续调整数字…
4. 最终解：$S=9, E=5, N=6, D=7, M=1, O=0, R=8, Y=2$
5. 验证：$9567 + 1085 = 10652$ ✓

### 思路 1：代码

```python
class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        # 第 1 步：收集所有不同字母
        letters = set()
        for w in words + [result]:
            for ch in w:
                letters.add(ch)

        if len(letters) > 10:
            return False

        # 前导零限制
        leading = set()
        for w in words + [result]:
            if len(w) > 1:
                leading.add(w[0])

        letters = list(letters)
        n = len(letters)
        letter_to_idx = {ch: i for i, ch in enumerate(letters)}

        # 第 2 步：将 words 和 result 转换为每个位置上的字母索引列表（按列从右到左）
        max_len = max(len(w) for w in words + [result])

        assign = [-1] * n  # 字母 -> 数字
        used = [False] * 10  # 数字是否已使用

        # 列校验剪枝
        def is_valid(col, carry):
            """检查当前列是否可能成立（基于已分配的字母）"""
            total = carry
            for w in words:
                if col < len(w):
                    ch = w[-(col + 1)]
                    idx = letter_to_idx[ch]
                    if assign[idx] == -1:
                        return True  # 该字母未分配，暂时无法验证
                    total += assign[idx]

            if col < len(result):
                ch = result[-(col + 1)]
                idx = letter_to_idx[ch]
                if assign[idx] != -1:
                    return total % 10 == assign[idx]
                # 该字母未分配，但该数字可能被其他字母占用
                if used[total % 10]:
                    return False
                return True
            return total % 10 == 0

        def dfs(pos, col, carry):
            """回溯分配字母"""
            if pos == n:
                # 所有字母分配完毕，检查等式是否成立
                # 从当前列到最高位逐列检查
                while col < max_len:
                    total = carry
                    for w in words:
                        if col < len(w):
                            ch = w[-(col + 1)]
                            total += assign[letter_to_idx[ch]]
                    expected = 0
                    if col < len(result):
                        expected = assign[letter_to_idx[result[-(col + 1)]]]
                    if total % 10 != expected:
                        return False
                    carry = total // 10
                    col += 1
                return carry == 0

            # 选择一个未分配的字母
            ch = letters[pos]
            idx = letter_to_idx[ch]
            is_leading = ch in leading

            for digit in range(10):
                if used[digit]:
                    continue
                if is_leading and digit == 0:
                    continue

                # 尝试分配
                assign[idx] = digit
                used[digit] = True

                # 只对当前列做剪枝
                if is_valid(col, carry):
                    # 计算新进位
                    total = carry
                    for w in words:
                        if col < len(w):
                            ch = w[-(col + 1)]
                            total += assign[letter_to_idx[ch]]
                    new_carry = total // 10
                    # 检查 result 当前列
                    valid_col = True
                    if col < len(result):
                        r_ch = result[-(col + 1)]
                        r_idx = letter_to_idx[r_ch]
                        if assign[r_idx] != -1 and assign[r_idx] != total % 10:
                            valid_col = False
                    if valid_col:
                        if dfs(pos + 1, col, carry):
                            return True

                used[digit] = False
                assign[idx] = -1

            return False

        return dfs(0, 0, 0)
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(10! \times len)$ 最坏情况，但剪枝会大幅减少搜索空间。
- **空间复杂度**：$O(n)$，递归栈深度和映射数组。

---

### 思路 2：按列逐位回溯（更高效）

仅按列回溯，不预先分配所有字母。每列确定时再分配未确定的字母。实现更复杂但搜索效率更高。

本题数据范围 $words.length \le 20$，$result.length \le 7$，最多 $10$ 个字母，用思路 1 的含剪枝回溯已经可以高效求解。
