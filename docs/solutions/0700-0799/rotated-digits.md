# [0788. 旋转数字](https://leetcode.cn/problems/rotated-digits/)

- 标签：数学、动态规划
- 难度：中等

## 题目链接

- [0788. 旋转数字 - 力扣](https://leetcode.cn/problems/rotated-digits/)

## 题目大意

**描述**：给定搞一个正整数 $n$。

**要求**：计算从 $1$ 到 $n$ 中有多少个数 $x$ 是好数。

**说明**：

- **好数**：如果一个数 $x$ 的每位数字逐个被旋转 180 度之后，我们仍可以得到一个有效的，且和 $x$ 不同的数，则成该数为好数。
- 如果一个数的每位数字被旋转以后仍然还是一个数字， 则这个数是有效的。$0$、$1$ 和 $8$ 被旋转后仍然是它们自己；$2$ 和 $5$ 可以互相旋转成对方（在这种情况下，它们以不同的方向旋转，换句话说，$2$ 和 $5$ 互为镜像）；$6$ 和 $9$ 同理，除了这些以外其他的数字旋转以后都不再是有效的数字。
- $n$ 的取值范围是 $[1, 10000]$。

**示例**：

- 示例 1：

```python
输入: 10
输出: 4
解释: 
在 [1, 10] 中有四个好数： 2, 5, 6, 9。
注意 1 和 10 不是好数, 因为他们在旋转之后不变。
```

## 解题思路

### 思路 1：枚举算法

根据题目描述，一个数满足：数中没有出现 $3$、$4$、$7$，并且至少出现一次 $2$、$5$、$6$ 或 $9$，就是好数。

因此，我们可以枚举 $[1, n]$ 中的每一个正整数 $x$，并判断该正整数 $x$ 的数位中是否满足没有出现 $3$、$4$、$7$，并且至少一次出现了 $2$、$5$、$6$ 或 $9$，如果满足，则该正整数 $x$ 位好数，否则不是好数。

最后统计好数的方案个数并将其返回即可。

### 思路 1：代码

```python
class Solution:
    def rotatedDigits(self, n: int) -> int:
        check = [0, 0, 1, -1, -1, 1, 1, -1, 0, 1]
        ans = 0
        for i in range(1, n + 1):
            flag = False
            num = i
            while num:
                digit = num % 10
                num //= 10
                if check[digit] == 1:
                    flag = True
                elif check[digit] == -1:
                    flag = False
                    break
            if flag:
                ans += 1
            	
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times \log n)$。
- **空间复杂度**：$O(\log n)$。

### 思路 2：动态规划 + 数位 DP

将 $n$ 转换为字符串 $s$，定义递归函数 `def dfs(pos, hasDiff, isLimit):` 表示构造第 $pos$ 位及之后所有数位的合法方案数。其中：

1. $pos$ 表示当前枚举的数位位置。
2. $hasDiff$ 表示当前是否用到 $2$、$5$、$6$ 或 $9$ 中任何一个数字。
3. $isLimit$ 表示前一位数位是否等于上界，用于限制本次搜索的数位范围。

接下来按照如下步骤进行递归。

1. 从 `dfs(0, False, True)` 开始递归。 `dfs(0, False, True)` 表示：
   1. 从位置 $0$ 开始构造。
   2. 初始没有用到 $2$、$5$、$6$ 或 $9$ 中任何一个数字。
   3. 开始时受到数字 $n$ 对应最高位数位的约束。
2. 如果遇到  $pos == len(s)$，表示到达数位末尾，此时：
   1. 如果 $hasDiff == True$，说明当前方案符合要求，则返回方案数 $1$。
   2. 如果 $hasDiff == False$，说明当前方案不符合要求，则返回方案数 $0$。
3. 如果 $pos \ne len(s)$，则定义方案数 $ans$，令其等于 $0$，即：`ans = 0`。
4. 因为不需要考虑前导 $0$，所以当前所能选择的最小数字 $minX$ 为 $0$。
5. 根据 $isLimit$ 来决定填当前位数位所能选择的最大数字（$maxX$）。
6. 然后根据 $[minX, maxX]$ 来枚举能够填入的数字 $d$。
7. 如果当前数位与之前数位没有出现 $3$、$4$、$7$，则方案数累加上当前位选择 $d$ 之后的方案数，即：`ans += dfs(pos + 1, hasDiff or check[d], isLimit and d == maxX)`。
   1. `hasDiff or check[d]` 表示当前是否用到 $2$、$5$、$6$ 或 $9$ 中任何一个数字或者没有用到 $3$、$4$、$7$。
   2. `isLimit and d == maxX` 表示 $pos + 1$ 位受到之前位限制和 $pos$ 位限制。
8. 最后的方案数为 `dfs(0, False, True)`，将其返回即可。

### 思路 2：代码

```python
class Solution:
    def rotatedDigits(self, n: int) -> int:
        check = [0, 0, 1, -1, -1, 1, 1, -1, 0, 1]

        # 将 n 转换为字符串 s
        s = str(n)
        
        @cache
        # pos: 第 pos 个数位
        # hasDiff: 之前选过的数字是否包含 2,5,6,9 中至少一个。
        # isLimit: 表示是否受到选择限制。如果为真，则第 pos 位填入数字最多为 s[pos]；如果为假，则最大可为 9。
        def dfs(pos, hasDiff, isLimit):
            if pos == len(s):
                # isNum 为 True，则表示当前方案符合要求
                return int(hasDiff)
            
            ans = 0
            # 不需要考虑前导 0，则最小可选择数字为 0
            minX = 0
            # 如果受到选择限制，则最大可选择数字为 s[pos]，否则最大可选择数字为 9。
            maxX = int(s[pos]) if isLimit else 9
            
            # 枚举可选择的数字
            for d in range(minX, maxX + 1): 
                # d 不在选择的数字集合中，即之前没有选择过 d
                if check[d] != -1:
                    ans += dfs(pos + 1, hasDiff or check[d], isLimit and d == maxX)
            return ans
    
        return dfs(0, False, True)
```

### 思路 2：复杂度分析

- **时间复杂度**：$O(\log n)$。
- **空间复杂度**：$O(\log n)$。

