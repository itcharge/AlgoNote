# [0838. 推多米诺](https://leetcode.cn/problems/push-dominoes/)

- 标签：双指针、字符串、动态规划
- 难度：中等

## 题目链接

- [0838. 推多米诺 - 力扣](https://leetcode.cn/problems/push-dominoes/)

## 题目大意

**描述**：

$n$ 张多米诺骨牌排成一行，将每张多米诺骨牌垂直竖立。在开始时，同时把一些多米诺骨牌向左或向右推。

每过一秒，倒向左边的多米诺骨牌会推动其左侧相邻的多米诺骨牌。同样地，倒向右边的多米诺骨牌也会推动竖立在其右侧的相邻多米诺骨牌。

如果一张垂直竖立的多米诺骨牌的两侧同时有多米诺骨牌倒下时，由于受力平衡，「该骨牌仍然保持不变」。

就这个问题而言，我们会认为一张正在倒下的多米诺骨牌不会对其它正在倒下或已经倒下的多米诺骨牌施加额外的力。

给定一个字符串 $dominoes$ 表示这一行多米诺骨牌的初始状态，其中：

- $dominoes[i] = 'L'$，表示第 $i$ 张多米诺骨牌被推向左侧，
- $dominoes[i] = 'R'$，表示第 $i$ 张多米诺骨牌被推向右侧，
- $dominoes[i] = '.'$，表示没有推动第 $i$ 张多米诺骨牌。

**要求**：

返回表示最终状态的字符串。

**说明**：

- $n == dominoes.length$。
- $1 \le n \le 10^{5}$。
- $dominoes[i]$ 为 `'L'`、`'R'` 或 `'.'`。

**示例**：

- 示例 1：

```python
输入：dominoes = "RR.L"
输出："RR.L"
解释：第一张多米诺骨牌没有给第二张施加额外的力。
```

- 示例 2：

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/05/18/domino.png)

```python
输入：dominoes = ".L.R...LR..L.."
输出："LL.RR.LLRRLL.."
```

## 解题思路

### 思路 1：双指针 + 模拟

多米诺骨牌的最终状态取决于相邻的 `R` 和 `L` 之间的关系。我们可以用双指针来标记相邻的两个非 `.` 字符,然后根据它们的组合来决定中间部分的状态。

1. 在字符串首尾分别添加虚拟的 `L` 和 `R`,方便处理边界情况。
2. 使用两个指针 $left$ 和 $right$,分别指向相邻的两个非 `.` 字符。
3. 根据 $dominoes[left]$ 和 $dominoes[right]$ 的组合,分四种情况处理:
   - `R...R`:中间全部变为 `R`
   - `L...L`:中间全部变为 `L`
   - `R...L`:中间部分向两边倒,中心位置保持不变(如果距离为奇数)
   - `L...R`:中间部分保持不变

### 思路 1:代码

```python
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # 在首尾添加虚拟字符,方便处理边界
        dominoes = 'L' + dominoes + 'R'
        n = len(dominoes)
        res = []
        left = 0  # 左指针
        
        for right in range(1, n):
            # 找到下一个非 '.' 的字符
            if dominoes[right] == '.':
                continue
            
            # 计算中间 '.' 的个数
            middle = right - left - 1
            
            # 添加左边界字符(跳过最开始的虚拟 'L')
            if left > 0:
                res.append(dominoes[left])
            
            # 根据左右字符的组合处理中间部分
            if dominoes[left] == dominoes[right]:
                # R...R 或 L...L,中间全部变为相同字符
                res.append(dominoes[left] * middle)
            elif dominoes[left] == 'R' and dominoes[right] == 'L':
                # R...L,向中间倒
                res.append('R' * (middle // 2))
                if middle % 2 == 1:
                    res.append('.')  # 中心位置保持不变
                res.append('L' * (middle // 2))
            else:
                # L...R,中间保持不变
                res.append('.' * middle)
            
            left = right
        
        return ''.join(res)
```

### 思路 1:复杂度分析

- **时间复杂度**:$O(n)$,其中 $n$ 是字符串 $dominoes$ 的长度。只需遍历一次字符串。
- **空间复杂度**:$O(n)$,需要存储结果字符串。
