# [1441. 用栈操作构建数组](https://leetcode.cn/problems/build-an-array-with-stack-operations/)

- 标签：栈、数组、模拟
- 难度：中等

## 题目链接

- [1441. 用栈操作构建数组 - 力扣](https://leetcode.cn/problems/build-an-array-with-stack-operations/)

## 题目大意

**描述**：给定一个整数数组 $target$ 和一个整数 $n$。有一个栈，初始为空。从 $1$ 到 $n$ 的顺序依次将整数推入栈中。同时可以执行以下操作：
- `"Push"`：将一个整数推入栈中。
- `"Pop"`：将栈顶元素弹出。

**要求**：返回一个操作序列，使得栈中的元素（从栈底到栈顶）等于 $target$。

**说明**：
- $1 \le target[i] \le n \le 100$。
- $target$ 严格递增。

**示例**：

- 示例 1：

```python
输入：target = [1,3], n = 3
输出：["Push","Push","Pop","Push"]
解释：一开始栈为空。最后一个元素是栈顶。
从流中读取 1 并推入数组。s = [1]。
从流中读取 2 并推入数组。s = [1,2]。
从栈顶删除整数。s = [1]。
从流中读取 3 并推入数组。s = [1,3]。
```

- 示例 2：

```python
输入：target = [1,2,3], n = 3
输出：["Push","Push","Push"]
解释：一开始栈为空。最后一个元素是栈顶。
从流中读取 1 并推入数组。s = [1]。
从流中读取 2 并推入数组。s = [1,2]。
从流中读取 3 并推入数组。s = [1,2,3]。
```

## 解题思路

### 思路 1：模拟

#### 1. 核心思想

模拟从 $1$ 到 $n$ 的推入过程。对于每个数字 $x = 1 \to n$：
1. 如果 $x$ 在 $target$ 中，只需要 `"Push"`。
2. 如果 $x$ 不在 $target$ 中，需要先 `"Push"` 再 `"Pop"`（因为必须推入才能跳过）。
3. 如果已经处理完 $target$ 的最后一个元素，可以提前停止。

#### 2. 具体步骤

**第 1 步**：将 $target$ 转换为集合 $set\_target$ 方便 $O(1)$ 判断。

**第 2 步**：遍历 $i = 1 \to n$：
- 如果 $i$ 在 $target$ 中，$ans.append("Push")$。
- 否则，$ans.append("Push")$ 和 $ans.append("Pop")$。
- 如果已经构建完 $target$ 的所有元素（$i == target[-1]$），提前结束。

#### 3. 举例说明

以 $target = [1, 3]$，$n = 3$ 为例：

| 遍历 | 操作 | 栈 | ans |
| --- | ---- | - | --- |
| 1    | Push | [1] | [Push] |
| 2    | Push, Pop | [] | [Push, Push, Pop] |
| 3    | Push | [3] | [Push, Push, Pop, Push] |

结果：`["Push", "Push", "Pop", "Push"]`。

### 思路 1：代码

```python
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        target_set = set(target)
        ans = []
        last = target[-1]

        for i in range(1, n + 1):
            if i in target_set:
                ans.append("Push")
            else:
                ans.append("Push")
                ans.append("Pop")
            if i == last:
                break

        return ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，最多遍历到 $n$。
- **空间复杂度**：$O(n)$，存储操作序列和集合。
