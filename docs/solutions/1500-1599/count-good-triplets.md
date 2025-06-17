# [1534. 统计好三元组](https://leetcode.cn/problems/count-good-triplets/)

- 标签：数组、枚举
- 难度：简单

## 题目链接

- [1534. 统计好三元组 - 力扣](https://leetcode.cn/problems/count-good-triplets/)

## 题目大意

**描述**：给定一个整数数组 $arr$，以及 $a$、$b$、$c$ 三个整数。

**要求**：统计其中好三元组的数量。

**说明**：

- **好三元组**：如果三元组（$arr[i]$、$arr[j]$、$arr[k]$）满足下列全部条件，则认为它是一个好三元组。
  - $0 \le i < j < k < arr.length$。
  - $| arr[i] - arr[j] | \le a$。
  - $| arr[j] - arr[k] | \le b$。
  - $| arr[i] - arr[k] | \le c$。

- $3 \le arr.length \le 100$。
- $0 \le arr[i] \le 1000$。
- $0 \le a, b, c \le 1000$。

**示例**：

- 示例 1：

```python
输入：arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
输出：4
解释：一共有 4 个好三元组：[(3,0,1), (3,0,1), (3,1,1), (0,1,1)]。
```

- 示例 2：

```python
输入：arr = [1,1,2,2,3], a = 0, b = 0, c = 1
输出：0
解释：不存在满足所有条件的三元组。
```

## 解题思路

### 思路 1：枚举

- 使用三重循环依次枚举所有的 $(i, j, k)$，判断对应 $arr[i]$、$arr[j]$、$arr[k]$ 是否满足条件。
- 然后统计出所有满足条件的三元组的数量。

### 思路 1：代码

```python
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        size = len(arr)
        ans = 0
        
        for i in range(size):
            for j in range(i + 1, size):
                for k in range(j + 1, size):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        ans += 1
        
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n^3)$，其中 $n$ 是数组 $arr$ 的长度。
- **空间复杂度**：$O(1)$。

### 思路 2：枚举优化 + 前缀和

我们可以先通过二重循环遍历二元组 $(j, k)$，找出所有满足 $| arr[j] - arr[k] | \le b$ 的二元组。

然后在 $| arr[j] - arr[k] | \le b$ 的条件下，我们需要找到满足以下要求的 $arr[i]$ 数量：

1. $i < j$。
2. $| arr[i] - arr[j] | \le a$。
3. $| arr[i] - arr[k] | \le c$。
4. $0 \le arr[i] \le 1000$。

其中 $2$、$3$ 去除绝对值之后可变为：

1. $arr[j] - a \le arr[i] \le arr[j] + a$。
2. $arr[k] - c \le arr[i] \le arr[k] + c$。

将这两个条件再结合第 $4$ 个条件综合一下就变为：$max(0, arr[j] - a, arr[k] - c) \le arr[i] \le min(arr[j] + a, arr[k] + c, 1000)$。

假如定义 $left = max(0, arr[j] - a, arr[k] - c)$，$right = min(arr[j] + a, arr[k] + c, 1000)$。

现在问题就转变了如何快速获取在值域区间 $[left, right]$ 中，有多少个 $arr[i]$。

我们可以利用前缀和数组，先计算出 $[0, 1000]$ 范围中，满足 $arr[i] < num$ 的元素个数，即为 $prefix\underline{\hspace{0.5em}}cnts[num]$。

然后对于区间 $[left, right]$，通过 $prefix\underline{\hspace{0.5em}}cnts[right] - prefix\underline{\hspace{0.5em}}cnts[left - 1]$ 即可快速求解出区间 $[left, right]$ 内 $arr[i]$ 的个数。

因为 $i < j < k$，所以我们可以在每次 $j$ 向右移动一位的时候，更新 $arr[j]$ 对应的前缀和数组，保证枚举到 $j$ 时，$prefix\underline{\hspace{0.5em}}cnts$ 存储对应元素值的个数足够正确。

### 思路 2：代码

```python
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        size = len(arr)
        ans = 0
        prefix_cnts = [0 for _ in range(1010)]

        for j in range(size):
            for k in range(j + 1, size):
                if abs(arr[j] - arr[k]) <= b:
                    left_j, right_j = arr[j] - a, arr[j] + a
                    left_k, right_k = arr[k] - c, arr[k] + c
                    left, right = max(0, left_j, left_k), min(1000, right_j, right_k)
                    if left <= right:
                        if left == 0:
                            ans += prefix_cnts[right]
                        else:
                            ans += prefix_cnts[right] - prefix_cnts[left - 1]

            for k in range(arr[j], 1001):
                prefix_cnts[k] += 1
        
        return ans
```

### 思路 2：复杂度分析

- **时间复杂度**：$O(n^2 + n \times S)$，其中 $n$ 是数组 $arr$ 的长度，$S$ 为数组的值域上限。
- **空间复杂度**：$O(S)$。

