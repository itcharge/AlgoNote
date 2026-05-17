# [1111. 有效括号的嵌套深度](https://leetcode.cn/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/)

- 标签：栈、字符串
- 难度：中等

## 题目链接

- [1111. 有效括号的嵌套深度 - 力扣](https://leetcode.cn/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/)

## 题目大意

**描述**：给定一个有效括号字符串 $seq$。需要把它分到两个组 $A$ 和 $B$ 中，使得 $A$ 和 $B$ 各自仍然是有效括号字符串，并且 $\max(depth(A), depth(B))$ 尽可能小。

$depth$ 是嵌套深度，比如 `"()"` 深度为 1，`"(())"` 深度为 2。

用一个数组 $answer$ 表示分配方案，$answer[i] = 0$ 表示 $seq[i]$ 分给 $A$，$= 1$ 表示分给 $B$。

**要求**：返回任意一个满足要求的答案数组。

**说明**：

- $1 \le seq.size \le 10000$。

**示例**：

```python
输入：seq = "(()())"
输出：[0,1,1,1,1,0]
解释：A = "()", B = "()"，max(depth(A), depth(B)) = 1。
```

## 解题思路

### 思路 1：按层次奇偶分配

**关键观察**：嵌套深度本质上是连续的左括号数量。比如 `((()))` 深度为 3。

要使 $A$ 和 $B$ 的最大深度最小，就应该把每一层的括号**均匀分配到两个组**里。最直接的做法就是：**奇数层给 $A$，偶数层给 $B$**（反过来也行）。

用人话讲：想象括号的层数像楼梯的台阶，一阶给这组，一阶给那组，这样每个组都不会走得太深。

**步骤拆解：**

1. 用 $depth$ 记录当前所处的嵌套深度。
2. 遍历字符串：
   - 遇到左括号 `(`：把当前 $depth$ 的奇偶性写入答案，然后 $depth$ 加 1。
   - 遇到右括号 `)`：$depth$ 先减 1，然后把当前 $depth$ 的奇偶性写入答案。
3. 返回答案数组。

**为什么遇到右括号要先减再写？**
因为右括号对应的嵌套深度比左括号少 1。比如 `(()())` 中第 2 个字符 `(` 深度为 1，第 4 个字符 `)` 深度也为 1，它们应该分到同一组。

### 思路 1：代码

```python
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        n = len(seq)
        answer = [0] * n
        depth = 0  # 当前嵌套深度
        
        for i in range(n):
            if seq[i] == '(':
                # 左括号：按当前深度的奇偶分配
                answer[i] = depth % 2
                depth += 1
            else:  # seq[i] == ')'
                depth -= 1
                # 右括号：按减完后的深度的奇偶分配
                answer[i] = depth % 2
        
        return answer
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。遍历一次字符串。
- **空间复杂度**：$O(1)$（不计答案数组）。
