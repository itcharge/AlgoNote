# [0842. 将数组拆分成斐波那契序列](https://leetcode.cn/problems/split-array-into-fibonacci-sequence/)

- 标签：字符串、回溯
- 难度：中等

## 题目链接

- [0842. 将数组拆分成斐波那契序列 - 力扣](https://leetcode.cn/problems/split-array-into-fibonacci-sequence/)

## 题目大意

**描述**：

给定一个数字字符串 $num$，比如 `"123456579"`，我们可以将它分成「斐波那契式」的序列 $[123, 456, 579]$。

形式上，「斐波那契式」序列是一个非负整数列表 $f$，且满足：

- $0 \le f[i] < 2^{31}$，（也就是说，每个整数都符合 32 位 有符号整数类型）
- $f.length \ge 3$
- 对于所有的 $0 \le i < f.length - 2$，都有 $f[i] + f[i + 1] = f[i + 2]$

另外，请注意，将字符串拆分成小块时，每个块的数字一定不要以零开头，除非这个块是数字 0 本身。

**要求**：

返回从 $num$ 拆分出来的任意一组斐波那契式的序列块，如果不能拆分则返回 []。

**说明**：

- $1 \le num.length \le 200$。
- $num$ 中只含有数字。

**示例**：

- 示例 1：

```python
输入：num = "1101111"
输出：[11,0,11,11]
解释：输出 [110,1,111] 也可以。
```

- 示例 2：

```python
输入: num = "112358130"
输出: []
解释: 无法拆分。
```

## 解题思路

### 思路 1:回溯

斐波那契序列的特点是:前两个数确定后,后续所有数都确定了。因此我们可以:

1. 枚举前两个数的所有可能划分。
2. 对于每种划分,尝试按照斐波那契规则继续划分剩余部分。
3. 如果能成功划分完整个字符串,返回结果;否则尝试下一种划分。

注意事项:

- 数字不能有前导零(除非数字本身是 0)
- 每个数必须在 32 位有符号整数范围内($< 2^{31}$)
- 序列至少要有 3 个数

### 思路 1:代码

```python
class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        n = len(num)
        
        def backtrack(index, path):
            # 如果已经遍历完字符串且序列长度 >= 3,返回 True
            if index == n and len(path) >= 3:
                return True
            
            # 枚举当前数字的长度
            for i in range(index, n):
                # 如果有前导零,只能是单独的 0
                if num[index] == '0' and i > index:
                    break
                
                # 截取当前数字
                cur_str = num[index:i+1]
                cur_num = int(cur_str)
                
                # 检查是否超过 32 位整数范围
                if cur_num >= 2**31:
                    break
                
                # 如果序列长度 < 2,直接加入
                if len(path) < 2:
                    path.append(cur_num)
                    if backtrack(i + 1, path):
                        return True
                    path.pop()
                # 如果序列长度 >= 2,检查是否满足斐波那契规则
                elif cur_num == path[-1] + path[-2]:
                    path.append(cur_num)
                    if backtrack(i + 1, path):
                        return True
                    path.pop()
                # 如果当前数字已经大于前两数之和,后面更长的数字更不可能满足
                elif cur_num > path[-1] + path[-2]:
                    break
            
            return False
        
        path = []
        if backtrack(0, path):
            return path
        return []
```

### 思路 1:复杂度分析

- **时间复杂度**:$O(n^2)$,其中 $n$ 是字符串的长度。最坏情况下需要枚举前两个数的所有可能组合,每种组合最多需要 $O(n)$ 时间验证。
- **空间复杂度**:$O(n)$,递归栈的深度最多为 $O(n)$。
