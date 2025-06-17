# [0982. 按位与为零的三元组](https://leetcode.cn/problems/triples-with-bitwise-and-equal-to-zero/)

- 标签：位运算、数组、哈希表
- 难度：困难

## 题目链接

- [0982. 按位与为零的三元组 - 力扣](https://leetcode.cn/problems/triples-with-bitwise-and-equal-to-zero/)

## 题目大意

**描述**：给定一个整数数组 $nums$。

**要求**：返回其中「按位与三元组」的数目。

**说明**：

- **按位与三元组**：由下标 $(i, j, k)$ 组成的三元组，并满足下述全部条件：
  - $0 \le i < nums.length$。
  - $0 \le j < nums.length$。
  - $0 \le k < nums.length$。
  - $nums[i] \text{ \& } nums[j] \text{ \& } nums[k] == 0$ ，其中 $\text{ \& }$ 表示按位与运算符。

- $1 \le nums.length \le 1000$。
- $0 \le nums[i] < 2^{16}$。

**示例**：

- 示例 1：

```python
输入：nums = [2,1,3]
输出：12
解释：可以选出如下 i, j, k 三元组：
(i=0, j=0, k=1) : 2 & 2 & 1
(i=0, j=1, k=0) : 2 & 1 & 2
(i=0, j=1, k=1) : 2 & 1 & 1
(i=0, j=1, k=2) : 2 & 1 & 3
(i=0, j=2, k=1) : 2 & 3 & 1
(i=1, j=0, k=0) : 1 & 2 & 2
(i=1, j=0, k=1) : 1 & 2 & 1
(i=1, j=0, k=2) : 1 & 2 & 3
(i=1, j=1, k=0) : 1 & 1 & 2
(i=1, j=2, k=0) : 1 & 3 & 2
(i=2, j=0, k=1) : 3 & 2 & 1
(i=2, j=1, k=0) : 3 & 1 & 2
```

- 示例 2：

```python
输入：nums = [0,0,0]
输出：27
```

## 解题思路

### 思路 1：枚举

最直接的方法是使用三重循环直接枚举 $(i, j, k)$，然后再判断 $nums[i] \text{ \& } nums[j] \text{ \& } nums[k]$ 是否为 $0$。但是这样做的时间复杂度为 $O(n^3)$。

从题目中可以看出 $nums[i]$ 的值域范围为 $[0, 2^{16}]$，而 $2^{16} = 65536$。所以我们可以按照下面步骤优化时间复杂度：

1. 先使用两重循环枚举 $(i, j)$，计算出 $nums[i] \text{ \& } nums[j]$ 的值，将其存入一个大小为 $2^{16}$ 的数组或者哈希表 $cnts$ 中，并记录每个 $nums[i] \text{ \& } nums[j]$ 值出现的次数。
2. 然后遍历该数组或哈希表，再使用一重循环遍历 $k$，找出所有满足 $nums[k] \text{ \& } x == 0$ 的 $x$，并将其对应数量 $cnts[x]$ 累积到答案 $ans$ 中。
3. 最后返回答案 $ans$ 即可。

### 思路 1：代码

```python
class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        states = 1 << 16
        cnts = [0 for _ in range(states)]

        for num_x in nums:
            for num_y in nums:
                cnts[num_x & num_y] += 1
        
        ans = 0
        for num in nums:
            for x in range(states):
                if num & x == 0:
                    ans += cnts[x]
        
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^2 + 2^{16} \times n)$，其中 $n$ 为数组 $nums$ 的长度。
- **空间复杂度**：$O(2^{16})$。

### 思路 2：枚举 + 优化

第一步跟思路 1 一样，我们先使用两重循环枚举 $(i, j)$，计算出 $nums[i] \text{ \& } nums[j]$ 的值，将其存入一个大小为 $2^{16}$ 的数组或者哈希表 $cnts$ 中，并记录每个 $nums[i] \text{ \& } nums[j]$ 值出现的次数。

接下来我们对思路 1 中的第二步进行优化，在思路 1 中，我们是通过枚举数组或哈希表的方式得到 $x$ 的，这里我们换一种方法。

使用一重循环遍历 $k$，对于 $nums[k]$，我们先计算出 $nums[k]$ 的补集，即将 $nums[k]$ 与 $2^{16} - 1$（二进制中 $16$ 个 $1$）进行按位异或操作，得到 $nums[k]$ 的补集 $com$。如果 $nums[k] \text{ \& } x == 0$，则 $x$ 一定是 $com$ 的子集。

换句话说，$x$ 中 $1$ 的位置一定与 $nums[k]$ 中 $1$ 的位置不同，如果 $nums[k]$ 中第 $m$ 位为 $1$，则 $x$ 中第 $m$ 位一定为 $0$。

接下来我们通过下面的方式来枚举子集：

1. 定义子集为 $sub$，初始时赋值为 $com$，即：$sub = com$。
2. 令 $sub$ 减 $1$，然后与 $com$ 做按位与操作，得到下一个子集，即：$sub = (sub - 1) \text{ \& } com$。
3. 不断重复第 $2$ 步，直到 $sub$ 为空集时为止。

这种方法能枚举子集的原理是：$sub$ 减 $1$ 会将最低位的 $1$ 改为 $0$，而比这个 $1$ 更低位的 $0$ 都改为了 $1$。此时再与 $com$ 做按位与操作，就会过保留原本高位上的 $1$，滤掉当前最低位的 $1$，并且保留比这个 $1$ 更低位上的原有的 $1$，也就得到嘞下一个子集。

举个例子，比如补集 $com$ 为 $(00010110)_2$：

1. 初始 $sub = (00010110)_2$。
2. 令其减 $1$ 后为 $(00010101)_2$，然后与 $com$ 做按位与操作，得到下一个子集 $sub = (00010100)_2$，即：$(00010101)_2 \text{ \& } (00010110)_2$）。
3. 令其减 $1$ 后为 $(00010011)_2$，然后与 $com$ 做按位与操作，得到下一个子集 $sub = (00010010)_2$，即： $(00010011)_2 \text{ \& } (00010110)_2$。
4. 令其减 $1$ 后为 $(00010001)_2$，然后与 $com$ 做按位与操作，得到下一个子集 $sub = (00010000)_2$，即：$(00010001)_2 \text{ \& } (00010110)_2$。
5. 令其减 $1$ 后为 $(00001111)_2$，然后与 $com$ 做按位与操作，得到下一个子集 $sub = (00000110)_2$，即：$(00001111)_2 \text{ \& } (00010110)_2$。
6. 令其减 $1$ 后为 $(00000101)_2$，然后与 $com$ 做按位与操作，得到下一个子集 $sub = (00000100)_2$，即：$(00000101)_2 \text{ \& } (00010110)_2$。
7. 令其减 $1$ 后为 $(00000011)_2$，然后与 $com$ 做按位与操作，得到下一个子集 $sub = (00000010)_2$，即：$(00000011)_2 \text{ \& } (00010110)_2$。
8. 令其减 $1$ 后为 $(00000001)_2$，然后与 $com$ 做按位与操作，得到下一个子集 $sub = (00000000)_2$，即：$(00000001)_2 \text{ \& } (00010110)_2$。
9. $sub$ 变为了空集。

### 思路 2：代码

```python
class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        states = 1 << 16
        cnts = [0 for _ in range(states)]

        for num_x in nums:
            for num_y in nums:
                cnts[num_x & num_y] += 1
        
        ans = 0
        for num in nums:
            com = num ^ 0xffff			# com: num 的补集
            sub = com					# sub: 子集
            while True:
                ans += cnts[sub]
                if sub == 0:
                    break
                sub = (sub - 1) & com
        
        return ans
```

### 思路 2：复杂度分析

- **时间复杂度**：$O(n^2 + 2^{16} \times n)$，其中 $n$ 为数组 $nums$ 的长度。
- **空间复杂度**：$O(2^{16})$。

## 参考资料

- 【题解】[按位与为零的三元组 - 按位与为零的三元组](https://leetcode.cn/problems/triples-with-bitwise-and-equal-to-zero/solution/an-wei-yu-wei-ling-de-san-yuan-zu-by-lee-gjud/)
- 【题解】[有技巧的枚举 + 常数优化（Python/Java/C++/Go） - 按位与为零的三元组](https://leetcode.cn/problems/triples-with-bitwise-and-equal-to-zero/solution/you-ji-qiao-de-mei-ju-chang-shu-you-hua-daxit/)
