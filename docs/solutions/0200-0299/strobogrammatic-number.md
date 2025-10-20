# [0246. 中心对称数](https://leetcode.cn/problems/strobogrammatic-number/)

- 标签：哈希表、双指针、字符串
- 难度：简单

## 题目链接

- [0246. 中心对称数 - 力扣](https://leetcode.cn/problems/strobogrammatic-number/)

## 题目大意

**描述**：

中心对称数是指一个数字在旋转了 180 度之后看起来依旧相同的数字（或者上下颠倒地看）。

**要求**：

写一个函数来判断该数字是否是中心对称数，其输入将会以一个字符串的形式来表达数字。

**示例**：

- 示例 1：

```python
输入: num = "69"
输出: true
```

- 示例 2：

```python
输入: num = "88"
输出: true
```

## 解题思路

### 思路 1：哈希表 + 双指针

中心对称数是指旋转 180 度后看起来相同的数字。只有特定的数字在旋转后有意义：
- $0$ 旋转后还是 $0$。
- $1$ 旋转后还是 $1$。
- $6$ 旋转后变成 $9$。
- $8$ 旋转后还是 $8$。
- $9$ 旋转后变成 $6$。

其他数字（如 $2, 3, 4, 5, 7$）旋转后没有意义。

使用哈希表存储每个数字的旋转对应关系，然后用双指针从两端向中间检查：

- 如果字符串中包含不能旋转的数字，直接返回 $false$。
- 如果两端字符的旋转对应关系不匹配，返回 $false$。
- 如果所有字符都满足中心对称条件，返回 $true$。

### 思路 1：代码

```python
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        # 定义中心对称数字的映射关系
        strobogrammatic_map = {
            '0': '0',
            '1': '1', 
            '6': '9',
            '8': '8',
            '9': '6'
        }
        
        # 双指针从两端向中间检查
        left, right = 0, len(num) - 1
        
        while left <= right:
            # 如果当前字符不能旋转，返回 False
            if num[left] not in strobogrammatic_map:
                return False
            if num[right] not in strobogrammatic_map:
                return False
            
            # 检查旋转后的对应关系
            if strobogrammatic_map[num[left]] != num[right]:
                return False
            
            left += 1
            right -= 1
        
        return True
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是字符串长度。需要遍历字符串一次。
- **空间复杂度**：$O(1)$。哈希表大小固定为 $5$，不随输入规模变化。
