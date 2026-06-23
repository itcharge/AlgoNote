# [1461. 检查一个字符串是否包含所有长度为 K 的二进制子串](https://leetcode.cn/problems/check-if-a-string-contains-all-binary-codes-of-size-k/)

- 标签：位运算、字符串、哈希表、滑动窗口
- 难度：中等

## 题目链接

- [1461. 检查一个字符串是否包含所有长度为 K 的二进制子串 - 力扣](https://leetcode.cn/problems/check-if-a-string-contains-all-binary-codes-of-size-k/)

## 题目大意

**描述**：给定一个二进制字符串 $s$ 和一个整数 $k$。

**要求**：检查 $s$ 中是否包含了所有长度为 $k$ 的二进制子串。如果包含所有可能，返回 $True$，否则 $False$。

**说明**：
- $1 \le s.length \le 5 \times 10^5$。
- $1 \le k \le 20$。

**示例**：

- 示例 1：

```python
输入：s = "00110110", k = 2
输出：true
解释：长度为 2 的二进制串包括 "00"，"01"，"10" 和 "11"。它们分别是 s 中下标为 0，1，3，2 开始的长度为 2 的子串。
```

- 示例 2：

```python
输入：s = "0110", k = 1
输出：true
解释：长度为 1 的二进制串包括 "0" 和 "1"，显然它们都是 s 的子串。
```

## 解题思路

### 思路 1：哈希集合统计

#### 1. 核心思想

长度为 $k$ 的二进制子串共有 $2^k$ 种可能。用长度为 $k$ 的滑动窗口遍历 $s$，将每个子串存入哈希集合。最后判断集合大小是否等于 $2^k$。

#### 2. 具体步骤

**第 1 步**：如果 $s.length < k$，返回 $False$。

**第 2 步**：用滑动窗口遍历 $s$，将每个长度为 $k$ 的子串加入集合。

**第 3 步**：如果集合大小达到 $2^k$，返回 $True$（提前终止）。

**第 4 步**：遍历完成后，判断集合大小是否等于 $2^k$。

#### 3. 举例说明

以 $s = "00110110", k = 2$ 为例：

所有长度为 $2$ 的子串：$"00", "01", "11", "10", "01", "11", "10"$。

去重后：$\{"00", "01", "10", "11"\}$，共 $4 = 2^2$ 种 → $True$。

### 思路 1：代码

```python
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        if n < k:
            return False

        seen = set()
        target = 1 << k  # 2^k

        for i in range(n - k + 1):
            seen.add(s[i:i + k])
            if len(seen) == target:
                return True

        return len(seen) == target
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times k)$，每次截取子串 $O(k)$。优化：滚动哈希可降至 $O(n)$。
- **空间复杂度**：$O(2^k)$，最坏存储所有子串。

---

### 思路 2：滚动哈希优化

将子串转为整数，避免字符串截取：

```python
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        if n < k:
            return False

        seen = set()
        target = 1 << k
        # 计算第一个子串的整数值
        val = int(s[:k], 2)
        seen.add(val)
        mask = (1 << (k - 1))  # 用于移除最高位

        for i in range(k, n):
            # 移除最高位，加入新位
            val = ((val & (mask - 1)) << 1) | (ord(s[i]) - 48)
            seen.add(val)
            if len(seen) == target:
                return True

        return len(seen) == target
```

滚动哈希将每个子串处理降为 $O(1)$，总复杂度 $O(n)$。
