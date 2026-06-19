# [1356. 根据数字二进制下 1 的数目排序](https://leetcode.cn/problems/sort-integers-by-the-number-of-1-bits/)

- 标签：位运算、数组、哈希表、排序
- 难度：简单

## 题目链接

- [1356. 根据数字二进制下 1 的数目排序 - 力扣](https://leetcode.cn/problems/sort-integers-by-the-number-of-1-bits/)

## 题目大意

**描述**：给定一个整数数组 $arr$。

**要求**：按数组中每个数字的二进制表示中 $1$ 的数目升序排序。如果 $1$ 的数目相同，按十进制数值升序排序。返回排序后的数组。

**说明**：
- $0 \le arr.length \le 500$。
- $0 \le arr[i] \le 10^4$。

**示例**：

- 示例 1：

```python
输入：arr = [0,1,2,3,4,5,6,7,8]
输出：[0,1,2,4,8,3,5,6,7]
解释：[0] 是唯一一个有 0 个 1 的数。
[1,2,4,8] 都有 1 个 1 。
[3,5,6] 有 2 个 1 。
[7] 有 3 个 1 。
按照 1 的个数排序得到的结果数组为 [0,1,2,4,8,3,5,6,7]
```

- 示例 2：

```python
输入：arr = [1024,512,256,128,64,32,16,8,4,2,1]
输出：[1,2,4,8,16,32,64,128,256,512,1024]
解释：数组中所有整数二进制下都只有 1 个 1 ，所以你需要按照数值大小将它们排序。
```


## 解题思路

### 思路 1：自定义排序

#### 1. 核心思想

用 Python 的 `sorted` 函数，自定义排序 key。对于每个元素 $x$，排序 key 为 $\text{(bit\_count}(x), x)$。

其中 $\text{bit\_count}(x)$ 表示 $x$ 的二进制中 $1$ 的个数。

#### 2. 具体步骤

**第 1 步**：定义函数计算二进制中 $1$ 的个数（可以用 Python 内置 `bin(x).count('1')` 或 `x.bit_count()`）。

**第 2 步**：用 `sorted()` 排序，$key = (bit\_count(x), x)$。

**第 3 步**：返回排序后的数组。

#### 3. 举例说明

以 $arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]$ 为例：

| 数字 | 二进制 | bit_count | 排序键 |
| --- | ----- | --------- | ----- |
| 0   | 0     | 0         | (0,0) |
| 1   | 1     | 1         | (1,1) |
| 2   | 10    | 1         | (1,2) |
| 3   | 11    | 2         | (2,3) |
| 4   | 100   | 1         | (1,4) |
| 5   | 101   | 2         | (2,5) |
| 6   | 110   | 2         | (2,6) |
| 7   | 111   | 3         | (3,7) |
| 8   | 1000  | 1         | (1,8) |

排序后：$[0, 1, 2, 4, 8, 3, 5, 6, 7]$。

### 思路 1：代码

```python
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (x.bit_count(), x))
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \log n)$，排序耗时。
- **空间复杂度**：$O(n)$，排序需要额外空间。

---

### 思路 2：手动计算 bit_count

如果面试中不允许使用 `int.bit_count()`，可以自己实现：

```python
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def bit_count(x):
            count = 0
            while x:
                x &= x - 1  # 清除最低位的 1
                count += 1
            return count

        return sorted(arr, key=lambda x: (bit_count(x), x))
```

`x & (x - 1)` 是 Brian Kernighan 算法，每次将最低位的 $1$ 置为 $0$，循环次数等于 $1$ 的个数。
