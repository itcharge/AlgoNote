# [0967. 连续差相同的数字](https://leetcode.cn/problems/numbers-with-same-consecutive-differences/)

- 标签：广度优先搜索、回溯
- 难度：中等

## 题目链接

- [0967. 连续差相同的数字 - 力扣](https://leetcode.cn/problems/numbers-with-same-consecutive-differences/)

## 题目大意

**描述**：

给定两个整数 $n$ 和 $k$。

**要求**：

返回所有长度为 $n$ 且满足其每两个连续位上的数字之间的差的绝对值为 $k$ 的 非负整数。

你可以按「任何顺序」返回答案。

**说明**：

- 注意：除了「数字 0」本身之外，答案中的每个数字都「不能」有前导零。例如，01 有一个前导零，所以是无效的；但 0 是有效的。
- $2 \le n \le 9$。
- $0 \le k \le 9$。

**示例**：

- 示例 1：

```python
输入：n = 3, k = 7
输出：[181,292,707,818,929]
解释：注意，070 不是一个有效的数字，因为它有前导零。
```

- 示例 2：

```python
输入：n = 2, k = 1
输出：[10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
```

## 解题思路

### 思路 1：广度优先搜索

使用 BFS 逐层构建满足条件的数字。

1. **初始化**：从 $1 \sim 9$ 开始（不能有前导零），将它们加入队列。
2. **BFS 扩展**：对于队列中的每个数字，尝试在末尾添加新的数字：
   - 新数字与当前数字的最后一位的差的绝对值必须等于 $k$
   - 即可以添加 $\text{lastDigit} + k$ 或 $\text{lastDigit} - k$（如果在 $[0, 9]$ 范围内）
3. **长度控制**：当数字长度达到 $n$ 时，加入结果集。
4. **去重**：注意当 $k = 0$ 时，$\text{lastDigit} + k$ 和 $\text{lastDigit} - k$ 相同，需要避免重复添加。

### 思路 1：代码

```python
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        # 初始化：从 1-9 开始
        queue = list(range(1, 10))
        
        # BFS 构建 n 位数
        for _ in range(n - 1):
            next_queue = []
            for num in queue:
                last_digit = num % 10
                
                # 尝试添加 last_digit + k
                if last_digit + k <= 9:
                    next_queue.append(num * 10 + last_digit + k)
                
                # 尝试添加 last_digit - k（避免重复）
                if k != 0 and last_digit - k >= 0:
                    next_queue.append(num * 10 + last_digit - k)
            
            queue = next_queue
        
        return queue
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(2^n)$，每个数字最多可以扩展出 $2$ 个新数字，最多有 $n$ 层。
- **空间复杂度**：$O(2^n)$，队列中最多存储 $O(2^n)$ 个数字。
