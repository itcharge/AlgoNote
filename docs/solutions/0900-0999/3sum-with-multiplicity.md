# [0923. 三数之和的多种可能](https://leetcode.cn/problems/3sum-with-multiplicity/)

- 标签：数组、哈希表、双指针、计数、排序
- 难度：中等

## 题目链接

- [0923. 三数之和的多种可能 - 力扣](https://leetcode.cn/problems/3sum-with-multiplicity/)

## 题目大意

**描述**：

给定一个整数数组 $arr$，以及一个整数 $target$ 作为目标值。

**要求**：

返回满足 $i < j < k$ 且 $arr[i] + arr[j] + arr[k] == target$ 的元组 $i, j, k$ 的数量。

由于结果会非常大，请返回 $10^9 + 7$ 的模。

**说明**：

- $3 \le arr.length \le 3000$。
- $0 \le arr[i] \le 10^{3}$。
- $0 \le target \le 300$。

**示例**：

- 示例 1：

```python
输入：arr = [1,1,2,2,3,3,4,4,5,5], target = 8
输出：20
解释：
按值枚举(arr[i], arr[j], arr[k])：
(1, 2, 5) 出现 8 次；
(1, 3, 4) 出现 8 次；
(2, 2, 4) 出现 2 次；
(2, 3, 3) 出现 2 次。
```

- 示例 2：

```python
输入：arr = [1,1,2,2,2,2], target = 5
输出：12
解释：
arr[i] = 1, arr[j] = arr[k] = 2 出现 12 次：
我们从 [1,1] 中选择一个 1，有 2 种情况，
从 [2,2,2,2] 中选出两个 2，有 6 种情况。
```

## 解题思路

### 思路 1：哈希表 + 双指针

#### 思路

这道题要求统计满足 $i < j < k$ 且 $arr[i] + arr[j] + arr[k] = target$ 的三元组数量。

由于数组元素范围较小（$0 \le arr[i] \le 100$），我们可以使用哈希表统计每个数字的出现次数，然后枚举所有可能的三元组：

1. **统计频次**：使用哈希表 $count$ 统计每个数字的出现次数。
2. **枚举三元组**：枚举所有可能的 $(i, j, k)$ 组合，其中 $i \le j \le k$：
   - 如果 $i + j + k = target$，计算该组合的方案数。
   - 方案数的计算需要考虑三个数是否相同：
     - 如果三个数都相同：$C(count[i], 3) = \frac{count[i] \times (count[i] - 1) \times (count[i] - 2)}{6}$
     - 如果两个数相同：$C(count[i], 2) \times count[k] = \frac{count[i] \times (count[i] - 1)}{2} \times count[k]$
     - 如果三个数都不同：$count[i] \times count[j] \times count[k]$
3. 返回总方案数对 $10^9 + 7$ 取模的结果。

#### 代码

```python
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10**9 + 7
        from collections import Counter
        
        # 统计每个数字的出现次数
        count = Counter(arr)
        res = 0
        
        # 枚举所有可能的三元组 (i, j, k)，其中 i <= j <= k
        for i in range(101):
            for j in range(i, 101):
                k = target - i - j
                if k < 0 or k > 100:
                    continue
                
                if i == j == k:
                    # 三个数都相同：C(count[i], 3)
                    res += count[i] * (count[i] - 1) * (count[i] - 2) // 6
                elif i == j:
                    # 前两个数相同：C(count[i], 2) * count[k]
                    if k > j:
                        res += count[i] * (count[i] - 1) // 2 * count[k]
                elif j == k:
                    # 后两个数相同：count[i] * C(count[j], 2)
                    if k > i:
                        res += count[i] * count[j] * (count[j] - 1) // 2
                else:
                    # 三个数都不同
                    if k > j:
                        res += count[i] * count[j] * count[k]
                
                res %= MOD
        
        return res
```

#### 复杂度分析

- **时间复杂度**：$O(n + C^2)$，其中 $n$ 是数组长度，$C = 101$ 是数字的范围。统计频次需要 $O(n)$，枚举三元组需要 $O(C^2)$。
- **空间复杂度**：$O(C)$，需要哈希表存储每个数字的频次。
