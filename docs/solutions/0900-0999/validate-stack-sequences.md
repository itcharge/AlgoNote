# [0946. 验证栈序列](https://leetcode.cn/problems/validate-stack-sequences/)

- 标签：栈、数组、模拟
- 难度：中等

## 题目链接

- [0946. 验证栈序列 - 力扣](https://leetcode.cn/problems/validate-stack-sequences/)

## 题目大意

**描述**：给定两个整数序列 `pushed` 和 `popped`，每个序列中的值都不重复。

**要求**：如果第一个序列为空栈的压入顺序，而第二个序列 `popped` 为该栈的压出序列，则返回 `True`，否则返回 `False`。

**说明**：

- $1 \le pushed.length \le 1000$。
- $0 \le pushed[i] \le 1000$。
- $pushed$ 的所有元素互不相同。
- $popped.length == pushed.length$。
- $popped$ 是 $pushed$ 的一个排列。

**示例**：

- 示例 1：

```python
输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
输出：true
解释：我们可以按以下顺序执行：
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
```

- 示例 2：

```python
输入：pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
输出：false
解释：1 不能在 2 之前弹出。
```

## 解题思路

### 思路 1：栈

借助一个栈来模拟压入、压出的操作。检测最后是否能模拟成功。

### 思路 1：代码

```python
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        index = 0
        for item in pushed:
            stack.append(item)
            while (stack and stack[-1] == popped[index]):
                stack.pop()
                index += 1

        return len(stack) == 0
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$。
- **空间复杂度**：$O(n)$。

