# [1295. 统计位数为偶数的数字](https://leetcode.cn/problems/find-numbers-with-even-number-of-digits/)

- 标签：数组、数学
- 难度：简单

## 题目链接

- [1295. 统计位数为偶数的数字 - 力扣](https://leetcode.cn/problems/find-numbers-with-even-number-of-digits/)

## 题目大意

**描述**：给你一个整数数组 $nums$。

**要求**：返回其中包含偶数个数位的数字的个数。

**说明**：

- $1 \le nums.length \le 500$。
- $1 \le nums[i] \le 10^{5}$。

**示例**：

- 示例 1：

```python
输入：nums = [12,345,2,6,7896]
输出：2
解释：
12 是 2 位数字（位数为偶数） 
345 是 3 位数字（位数为奇数）  
2 是 1 位数字（位数为奇数） 
6 是 1 位数字（位数为奇数） 
7896 是 4 位数字（位数为偶数）  
因此只有 12 和 7896 是位数为偶数的数字
```

- 示例 2：

```python
输入：nums = [555,901,482,1771]
输出：1 
解释： 
只有 1771 是位数为偶数的数字。
```

## 解题思路

### 思路 1：数字转字符串

###### 1. 核心思想

最简单的做法：把每个数字转成字符串，字符串的长度就是这个数的位数。检查长度是否为偶数即可。

###### 2. 具体步骤

**第 1 步**：初始化计数器 $ans = 0$。

**第 2 步**：遍历数组中的每个数字 $num$：
- 使用 `str(num)` 将数字转为字符串。
- 用 `len()` 获取字符串长度，即该数字的位数。
- 如果长度是偶数，$ans += 1$。

**第 3 步**：返回 $ans$。

### 思路 1：代码

```python
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            # 转成字符串，判断位数是否为偶数
            if len(str(num)) % 2 == 0:
                ans += 1
        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是数组长度。每个数字转字符串的时间与其位数成正比，但 $nums[i] \le 10^5$，最多 $6$ 位，所以可视为常数时间。
- **空间复杂度**：$O(1)$。

### 思路 2：数学方法

###### 1. 核心思想

不依赖字符串，用数学方法直接计算位数。一个十进制正整数 $num$ 的位数可以通过以下公式计算：

$$\text{digits} = \lfloor \log_{10}(num) \rfloor + 1$$

例如 $\log_{10}(100) = 2$，向下取整为 $2$，加 $1$ 得 $3$，即 $100$ 有 $3$ 位。

###### 2. 具体步骤

**第 1 步**：导入 `math` 模块。

**第 2 步**：遍历数组，对每个数字 $num$：
- 计算 $\lfloor \log_{10}(num) \rfloor + 1$ 得到位数。
- 判断位数是否为偶数。

**第 3 步**：返回计数。

### 思路 2：代码

```python
import math

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            # 用对数计算位数
            digits = int(math.log10(num)) + 1
            if digits % 2 == 0:
                ans += 1
        return ans
```

### 思路 2：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是数组长度。
- **空间复杂度**：$O(1)$。
