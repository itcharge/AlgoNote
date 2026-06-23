# [1442. 形成两个异或相等数组的三元组数目](https://leetcode.cn/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/)

- 标签：位运算、数组、哈希表、数学
- 难度：中等

## 题目链接

- [1442. 形成两个异或相等数组的三元组数目 - 力扣](https://leetcode.cn/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/)

## 题目大意

**描述**：给定一个整数数组 $arr$。选择三个下标 $i, j, k$，满足 $0 \le i < j \le k < n$。

定义：
- $a = arr[i] \oplus arr[i+1] \oplus \dots \oplus arr[j-1]$
- $b = arr[j] \oplus arr[j+1] \oplus \dots \oplus arr[k]$

**要求**：返回满足 $a == b$ 的三元组 $(i, j, k)$ 的数量。

**说明**：
- $1 \le arr.length \le 300$。
- $0 \le arr[i] \le 10^8$。

**示例**：

- 示例 1：

```python
输入：arr = [2,3,1,6,7]
输出：4
解释：满足题意的三元组分别是 (0,1,2), (0,2,2), (2,3,4) 以及 (2,4,4)
```

- 示例 2：

```python
输入：arr = [1,1,1,1,1]
输出：10
```

## 解题思路

### 思路 1：异或性质 + 哈希优化

#### 1. 核心思想

根据异或运算的性质，$a == b$ 等价于 $a \oplus b = 0$，即：

$$arr[i] \oplus arr[i+1] \oplus \dots \oplus arr[k] = 0$$

此时对于任意满足条件的 $j$（$i < j \le k$），都有 $a = b$。

因此问题转化为：找下标对 $(i, k)$（$i < k$），使得 $arr[i] \oplus arr[i+1] \oplus \dots \oplus arr[k] = 0$。对于每个满足条件的 $(i, k)$，有 $(k - i)$ 个可行的 $j$。

#### 2. 具体步骤

**第 1 步**：计算前缀异或。定义 $prefix[i] = arr[0] \oplus arr[1] \oplus \dots \oplus arr[i-1]$，则 $arr[i] \oplus \dots \oplus arr[k] = prefix[k+1] \oplus prefix[i]$。

**第 2 步**：条件 $prefix[k+1] \oplus prefix[i] = 0$ 等价于 $prefix[k+1] == prefix[i]$。

**第 3 步**：遍历 $i$ 和 $k$（$0 \le i < k < n$），如果 $prefix[i] == prefix[k+1]$，则 $ans += (k - i)$。

**第 4 步**：可以进一步优化为 $O(n)$ 哈希法。

#### 3. 举例说明

以 $arr = [2, 3, 1, 6, 7]$ 为例：

$prefix = [0, 2, 1, 0, 6, 1]$

满足 $prefix[i] == prefix[k+1]$ 的对：
- $i=0, k=3$：$prefix[0]=0, prefix[4]=0$ → $(k-i)=3$ 个三元组
- $i=2, k=5$（但 $k < n$，实际 $k=4$）：$prefix[2]=1, prefix[5]=1$ → 实际 $k=4, (k-i)=2$

### 思路 1：代码

```python
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] ^ arr[i]

        ans = 0
        for i in range(n):
            for k in range(i + 1, n):
                if prefix[i] == prefix[k + 1]:
                    ans += (k - i)
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^2)$。
- **空间复杂度**：$O(n)$。

### 思路 2：哈希表优化到 $O(n)$

```python
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        # count[x] 表示前缀异或值为 x 出现的次数
        # total[x] 表示前缀异或值为 x 的索引和
        count = {0: 1}
        total = {0: 0}
        prefix = 0
        ans = 0

        for k in range(n):
            prefix ^= arr[k]
            # 如果 prefix 之前出现过，设上次出现位置为 i-1
            # 则 arr[i...k] 的异或和为 0
            # 对于每个出现位置 i-1，j 可以取 i...k 中的任意值，贡献 k-i+1
            # 用 count 和 total 累计
            if prefix in count:
                # j 可选的个数 = k * count[prefix] - total[prefix]
                ans += k * count[prefix] - total[prefix]
                count[prefix] += 1
                total[prefix] += k + 1
            else:
                count[prefix] = 1
                total[prefix] = k + 1

        return ans
```

哈希法巧妙地将 $O(n^2)$ 优化为 $O(n)$。
