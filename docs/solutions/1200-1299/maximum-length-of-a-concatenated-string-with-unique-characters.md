# [1239. 串联字符串的最大长度](https://leetcode.cn/problems/maximum-length-of-a-concatenated-string-with-unique-characters/)

- 标签：位运算、数组、字符串、回溯
- 难度：中等

## 题目链接

- [1239. 串联字符串的最大长度 - 力扣](https://leetcode.cn/problems/maximum-length-of-a-concatenated-string-with-unique-characters/)

## 题目大意

**描述**：给定一个字符串数组 $arr$。字符串 $s$ 是由 $arr$ 中某些子串（字符串）串联连接得到的，且 $s$ 中的每个字符都只出现一次。

**要求**：返回满足条件的 $s$ 的最大长度。

**说明**：

- $1 \le arr.length \le 16$。
- $1 \le arr[i].length \le 26$。
- $arr[i]$ 中只包含小写英文字母。

**示例**：

- 示例 1：

```python
输入：arr = ["un","iq","ue"]
输出：4
解释：所有可能的串联组合为："", "un", "iq", "ue", "uniq", "ique"，其中长度最大为 4 的 "uniq"。
```

- 示例 2：

```python
输入：arr = ["cha","r","act","ers"]
输出：6
解释：最长的有效串联为 "chaers" 或 "acters"，长度为 6。
```

- 示例 3：

```python
输入：arr = ["abcdefghijklmnopqrstuvwxyz"]
输出：26
```

## 解题思路

### 思路 1：回溯 + 位运算

#### 1. 核心思想

这道题的本质是：从 $arr$ 中选择一个**不冲突**的子集，使得串联后的字符串长度最大，且串联结果中每个字符恰好出现一次。

"不冲突"有两层含义：
1. 单个字符串内部不能有重复字符（例如 `"aa"` 自己就含重复字符，不能选）。
2. 选中的多个字符串之间不能有相同的字符（例如选了 `"ab"` 就不能选 `"ac"`，因为 `'a'` 冲突了）。

$arr.length \le 16$，指数级别的枚举（$2^{16} = 65536$ 种组合）是可行的，因此可以用回溯法枚举所有子集。

为了高效判断冲突，可以用**位运算**：将每个字符串压缩成一个 26 位的整数（bitmask），每一位表示对应字母是否出现。这样判断两个字符串是否有重复字符，只需检查两个 bitmask 的按位与是否为 0。

#### 2. 选择、限制与终止

回溯三要素：

- **选择**：对于当前的字符串 $arr[i]$，有两种选择——选它加入串联，或者跳过它不选。
- **限制**：
  - 如果 $arr[i]$ 自身含有重复字符，只能跳过。
  - 如果 $arr[i]$ 与已选字符串集合有重复字符（`mask & arr[i]_mask != 0`），只能跳过。
- **终止**：遍历完所有字符串后，用已选集合的长度（即 bitmask 中 1 的个数）更新最大长度。

#### 3. 具体步骤

**第 1 步**：预处理
- 遍历 $arr$，将每个字符串转换为 bitmask。
- 如果某个字符串内部有重复字符，标记为无效（mask 设为 -1）。

**第 2 步**：回溯函数 $backtrack(i, mask)$
- $i$：当前处理到的字符串下标。
- $mask$：当前已选字符串的字符集合（26 位 bitmask）。

对于 $arr[i]$：
- 如果 $mask[i] \ne -1$（自身有效）且 $mask \ \&\ mask[i] == 0$（不冲突），选择 $arr[i]$：
  - 更新 $mask = mask \ |\ mask[i]$。
  - 递归处理 $i + 1$。
  - 回溯：恢复 $mask$（用参数传递，自动恢复）。
- 不选 $arr[i]$，直接递归处理 $i + 1$。

**第 3 步**：记录答案
- 在每次递归进入时（不仅仅在终止时），用当前 $mask$ 中 1 的个数更新最大长度。

#### 4. 结合示例走一遍

$arr = ["un", "iq", "ue"]$

预处理 bitmask：
- `"un"` → 二进制 `... 0b100000000000001000000`（'u'、'n' 位为 1）
- `"iq"` → 二进制 `... 0b1000000000010000000000`（'i'、'q' 位为 1）
- `"ue"` → 二进制 `... 0b10000000000000100000`（'u'、'e' 位为 1）

回溯过程（简化表示，用字母集合代替 bitmask）：

```
i=0, mask={}, 不选 → i=1
    i=1, mask={}, 不选 → i=2
        i=2, mask={}, 不选 → 长度=0
        i=2, mask={}, 选 'ue' → mask={u,e}, 长度=2
    i=1, mask={}, 选 'iq' → mask={i,q}, 递归 i=2
        i=2, mask={i,q}, 不选 → 长度=2
        i=2, mask={i,q}, 选 'ue' → 冲突(u), 跳过
i=0, mask={}, 选 'un' → mask={u,n}, 递归 i=1
    i=1, mask={u,n}, 不选 → i=2
        i=2, mask={u,n}, 不选 → 长度=2
        i=2, mask={u,n}, 选 'ue' → 冲突(u), 跳过
    i=1, mask={u,n}, 选 'iq' → mask={u,n,i,q}, 递归 i=2
        i=2, mask={u,n,i,q}, 不选 → 长度=4 ← 最大
        i=2, mask={u,n,i,q}, 选 'ue' → 冲突(u), 跳过
```

最大长度为 4，对应 `"uniq"`。

### 思路 1：代码

```python
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # 预处理每个字符串的 bitmask
        masks = []
        for s in arr:
            mask = 0
            valid = True
            for ch in s:
                bit = 1 << (ord(ch) - ord('a'))
                # 如果已有该字符，说明自身重复，无效
                if mask & bit:
                    valid = False
                    break
                mask |= bit
            masks.append(mask if valid else -1)

        n = len(arr)
        self.ans = 0

        def backtrack(i: int, mask: int):
            if i == n:
                # 统计 mask 中 1 的个数，即当前串联字符串的长度
                self.ans = max(self.ans, mask.bit_count())
                return

            # 情况 1：选择当前字符串（如果可以选）
            if masks[i] != -1 and (mask & masks[i]) == 0:
                backtrack(i + 1, mask | masks[i])

            # 情况 2：不选当前字符串
            backtrack(i + 1, mask)

        backtrack(0, 0)
        return self.ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(2^n + L)$，其中 $n$ 是 $arr$ 的长度，$L$ 是所有字符串的总长度。预处理需要 $O(L)$ 时间，回溯需要 $O(2^n)$ 时间。
- **空间复杂度**：$O(n)$，需要存储所有字符串的 bitmask，递归栈深度为 $O(n)$。

### 思路 2：状态压缩（迭代枚举）

#### 1. 核心思想

回溯本质上是 DFS 枚举所有子集，但 $n \le 16$ 时也可以用**状态压缩**的方式，从 $0$ 遍历到 $2^n - 1$，用整数的二进制位表示每个字符串的选取状态，依次检查每个状态是否合法。

#### 2. 代码

```python
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # 预处理每个字符串的 bitmask 和长度
        masks = []
        lengths = []
        for s in arr:
            mask = 0
            valid = True
            for ch in s:
                bit = 1 << (ord(ch) - ord('a'))
                if mask & bit:
                    valid = False
                    break
                mask |= bit
            if valid:
                masks.append(mask)
                lengths.append(len(s))

        n = len(masks)
        ans = 0
        # 枚举所有子集 [1, 2^n - 1]
        for state in range(1, 1 << n):
            mask = 0
            length = 0
            ok = True
            # 检查 state 中每个被选中的字符串
            for i in range(n):
                if state >> i & 1:
                    if mask & masks[i]:   # 冲突
                        ok = False
                        break
                    mask |= masks[i]
                    length += lengths[i]
            if ok:
                ans = max(ans, length)
        return ans
```

#### 3. 复杂度分析

- **时间复杂度**：$O(2^n \times n)$，枚举所有子集，每个子集需要检查 $n$ 位。
- **空间复杂度**：$O(n)$，存储 masks 和 lengths 数组。

两种思路的时间复杂度不同，但在 $n \le 16$ 时都完全可行。回溯法有剪枝优化，实际运行效率更高。
