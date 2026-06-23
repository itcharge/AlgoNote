# [1415. 长度为 n 的开心字符串中字典序第 k 小的字符串](https://leetcode.cn/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/)

- 标签：字符串、回溯
- 难度：中等

## 题目链接

- [1415. 长度为 n 的开心字符串中字典序第 k 小的字符串 - 力扣](https://leetcode.cn/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/)

## 题目大意

**描述**：长度为 $n$ 的「开心字符串」只包含 $a,b,c$，且相邻字符不同。

**要求**：按字典序返回第 $k$ 个开心字符串。如果不存在（即总数 $< k$），返回空字符串。

**说明**：
- $1 \le n \le 10$。
- $1 \le k \le 100$。

**示例**：

- 示例 1：

```python
输入：n = 1, k = 3
输出："c"
解释：列表 ["a", "b", "c"] 包含了所有长度为 1 的开心字符串。按照字典序排序后第三个字符串为 "c" 。
```

- 示例 2：

```python
输入：n = 1, k = 4
输出：""
解释：长度为 1 的开心字符串只有 3 个。
```

## 解题思路

### 思路 1：回溯枚举 + 计数

#### 1. 核心思想

开心字符串总数最多 $3 \times 2^{n-1}$ 种，$n \le 10$，最多 $1536$ 种，可以枚举所有并排序取第 $k$ 个。或用回溯直接生成第 $k$ 个。

#### 2. 具体步骤

**第 1 步**：定义回溯函数 $backtrack(cur)$：
- 如果 $len(cur) == n$：计数 $+1$，如果 $count == k$，记录结果。
- 否则，按 $a,b,c$ 顺序尝试下一个字符（保证字典序），要求与当前末尾字符不同。

**第 2 步**：如果找到了第 $k$ 个，返回结果。否则返回空字符串。

#### 3. 举例说明

以 $n=3, k=9$ 为例：

所有开心字符串排列：
```
aba, abc, aca, acb, bab, bac, bca, bcb, cab, cac, cba, cbc
```

第 $9$ 个是 `cab`。

### 思路 1：代码

```python
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.count = 0
        self.ans = ""

        def backtrack(cur):
            if self.ans:
                return
            if len(cur) == n:
                self.count += 1
                if self.count == k:
                    self.ans = cur
                return

            for ch in 'abc':
                if not cur or cur[-1] != ch:
                    backtrack(cur + ch)

        backtrack("")
        return self.ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(3 \times 2^{n-1})$，即生成到第 $k$ 个开心字符串为止。
- **空间复杂度**：$O(n)$，递归栈深度。
