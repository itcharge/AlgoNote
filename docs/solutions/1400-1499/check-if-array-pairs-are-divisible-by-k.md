# [1497. 检查数组对是否可以被 k 整除](https://leetcode.cn/problems/check-if-array-pairs-are-divisible-by-k/)

- 标签：数组、哈希表、计数
- 难度：中等

## 题目链接

- [1497. 检查数组对是否可以被 k 整除 - 力扣](https://leetcode.cn/problems/check-if-array-pairs-are-divisible-by-k/)

## 题目大意

**描述**：给定一个长度为偶数的整数数组 $arr$ 和一个整数 $k$。

**要求**：判断能否将 $arr$ 分成 $n/2$ 对，使得每对元素之和都能被 $k$ 整除。如果可以，返回 $True$，否则 $False$。

**说明**：
- $2 \le arr.length \le 10^5$。
- $1 \le k \le 10^5$。

**示例**：

- 示例 1：

```python
输入：arr = [1,2,3,4,5,10,6,7,8,9], k = 5
输出：true
解释：划分后的数字对为 (1,9),(2,8),(3,7),(4,6) 以及 (5,10) 。
```

- 示例 2：

```python
输入：arr = [1,2,3,4,5,6], k = 7
输出：true
解释：划分后的数字对为 (1,6),(2,5) 以及 (3,4) 。
```

## 解题思路

### 思路 1：余数计数

#### 1. 核心思想

两个数之和能被 $k$ 整除，等价于它们的余数之和能被 $k$ 整除。即 $(a + b) \% k = 0$ 当且仅当 $(a \% k + b \% k) \% k = 0$。

对于余数 $r$，需要与余数 $k - r$ 或 $0$（当 $r=0$ 时）的元素配对。

#### 2. 具体步骤

**第 1 步**：统计每个余数的出现次数 $count[r]$，其中 $r = (x \% k + k) \% k$。

**第 2 步**：配对检查：
- 余数 $0$ 的元素必须成对出现，$count[0] \% 2 == 0$。
- 对于 $1 \le r \le k-1$：
  - 如果 $count[r] \ne count[k-r]$，无法配对，返回 $False$。
  - 注意 $r = k - r$（即 $k$ 为偶数且 $r = k/2$）时，也需要成对。

**第 3 步**：全部满足则返回 $True$。

#### 3. 举例说明

以 $arr = [1,2,3,4,5,6], k = 5$ 为例：

余数：$[1,2,3,4,0,1]$
- $count[0] = 1$ → 奇数，无法配对 → $False$（$5$ 需要和另一个 $5$ 配对，但没有）。

以 $arr = [1,2,3,4,5,10,6,7,8,9], k = 5$ 为例：

余数：$[1,2,3,4,0,0,1,2,3,4]$
- $count[0]=2$ ✓
- $count[1]=2, count[4]=2$ ✓
- $count[2]=2, count[3]=2$ ✓

返回 $True$。

### 思路 1：代码

```python
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        count = [0] * k
        for x in arr:
            r = (x % k + k) % k  # 处理负数
            count[r] += 1

        # 余数为 0 的元素必须成对
        if count[0] % 2 != 0:
            return False

        # 配对余数 r 和 k - r
        for r in range(1, k // 2 + 1):
            if r == k - r:
                if count[r] % 2 != 0:
                    return False
            elif count[r] != count[k - r]:
                return False

        return True
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n + k)$，遍历数组 $O(n)$，检查配对 $O(k)$。
- **空间复杂度**：$O(k)$，余数计数数组。
