# [0710. 黑名单中的随机数](https://leetcode.cn/problems/random-pick-with-blacklist/)

- 标签：数组、哈希表、数学、二分查找、排序、随机化
- 难度：困难

## 题目链接

- [0710. 黑名单中的随机数 - 力扣](https://leetcode.cn/problems/random-pick-with-blacklist/)

## 题目大意

**描述**：

给定一个整数 $n$ 和一个「无重复」黑名单整数数组 $blacklist$。设计一种算法，从 $[0, n - 1]$ 范围内的任意整数中选取一个「未加入」黑名单 $blacklist$ 的整数。任何在上述范围内且不在黑名单 $blacklist$ 中的整数都应该有「同等的可能性」被返回。

优化你的算法，使它最小化调用语言「内置」随机函数的次数。

**要求**：

实现 Solution 类:

- `Solution(int n, int[] blacklist)` 初始化整数 $n$ 和被加入黑名单 $blacklist$ 的整数。
- `int pick()` 返回一个范围为 $[0, n - 1]$ 且不在黑名单 $blacklist$ 中的随机整数。

**说明**：

- $1 \le n \le 10^{9}$。
- $0 \le blacklist.length \le min(10^{5}, n - 1)$。
- $0 \le blacklist[i] \lt n$。
- $blacklist$ 中所有值都不同。
- $pick$ 最多被调用 $2 \times 10^{4}$ 次。

**示例**：

- 示例 1：

```python
输入
["Solution", "pick", "pick", "pick", "pick", "pick", "pick", "pick"]
[[7, [2, 3, 5]], [], [], [], [], [], [], []]
输出
[null, 0, 4, 1, 6, 1, 0, 4]

解释
Solution solution = new Solution(7, [2, 3, 5]);
solution.pick(); // 返回0，任何[0,1,4,6]的整数都可以。注意，对于每一个pick的调用，
                 // 0、1、4和6的返回概率必须相等(即概率为1/4)。
solution.pick(); // 返回 4
solution.pick(); // 返回 1
solution.pick(); // 返回 6
solution.pick(); // 返回 1
solution.pick(); // 返回 0
solution.pick(); // 返回 4
```

## 解题思路

### 思路 1：哈希表 + 随机映射

将黑名单中的数字映射到 $[n - len(blacklist), n)$ 范围内的白名单数字。

**实现步骤**：

1. 计算白名单的大小：$white\_count = n - len(blacklist)$。
2. 将黑名单中 $\ge white\_count$ 的数字放入集合 $black\_set$。
3. 对于黑名单中 $< white\_count$ 的数字，将其映射到 $[white\_count, n)$ 范围内不在黑名单中的数字。
4. 随机生成 $[0, white\_count)$ 范围内的数字：
   - 如果在映射表中，返回映射后的值。
   - 否则，直接返回该数字。

### 思路 1：代码

```python
class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        import random
        self.random = random
        
        # 白名单的大小
        self.white_count = n - len(blacklist)
        
        # 黑名单中 >= white_count 的数字
        black_set = set()
        for b in blacklist:
            if b >= self.white_count:
                black_set.add(b)
        
        # 映射表：将黑名单中 < white_count 的数字映射到 [white_count, n) 范围内的白名单数字
        self.mapping = {}
        white = self.white_count
        for b in blacklist:
            if b < self.white_count:
                # 找到下一个不在黑名单中的数字
                while white in black_set or white in blacklist:
                    white += 1
                self.mapping[b] = white
                white += 1

    def pick(self) -> int:
        # 随机生成 [0, white_count) 范围内的数字
        rand = self.random.randint(0, self.white_count - 1)
        # 如果在映射表中，返回映射后的值
        return self.mapping.get(rand, rand)


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()
```

### 思路 1：复杂度分析

- **时间复杂度**：
  - 初始化：$O(B)$，其中 $B$ 是黑名单的长度。
  - 查询：$O(1)$。
- **空间复杂度**：$O(B)$，映射表的空间。
