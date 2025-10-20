# [0293. 翻转游戏](https://leetcode.cn/problems/flip-game/)

- 标签：字符串
- 难度：简单

## 题目链接

- [0293. 翻转游戏 - 力扣](https://leetcode.cn/problems/flip-game/)

## 题目大意

**描述**：

你和朋友玩一个叫做「翻转游戏」的游戏。游戏规则如下：

给定一个字符串 $currentState$ ，其中只含 `'+'` 和 `'-'`。你和朋友轮流将「连续」的两个 `"++"` 反转成 `"--"`。当一方无法进行有效的翻转时便意味着游戏结束，则另一方获胜。

**要求**：

计算并返回「一次有效操作」后，字符串 $currentState$ 所有的可能状态，返回结果可以按任意顺序 排列。如果不存在可能的有效操作，请返回一个空列表 $[]$。

**说明**：

- $1 \le currentState.length \le 500$。
- $currentState[i]$ 不是 `'+'` 就是 `'-'`。

**示例**：

- 示例 1：

```python
输入：currentState = "++++"
输出：["--++","+--+","++--"]
```

- 示例 2：

```python
输入：currentState = "+"
输出：[]
```

## 解题思路

### 思路 1：遍历模拟

这是一个简单的字符串模拟问题。我们需要遍历字符串，找到所有连续的 `"++"` 位置，然后将每个位置翻转成 `"--"`，生成所有可能的下一个状态。

核心思想是：

- 遍历字符串 $currentState$，寻找所有可以翻转的位置 $i$，满足 `currentState[i] = '+'` 且 `currentState[i+1] = '+'`。
- 对于每个有效位置 $i$，生成新状态：`newState = currentState[:i] + "--" + currentState[i+2:]`。
- 将所有生成的新状态收集到结果列表中。

具体算法步骤：

1. 初始化结果列表 $result = []$。
2. 遍历字符串从位置 $0$ 到 $len(currentState) - 2$。
3. 检查当前位置 $i$ 和 $i+1$ 是否都为 `'+'`。
4. 如果是，则生成新状态并添加到结果中。
5. 返回结果列表。

### 思路 1：代码

```python
class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        result = []
        # 遍历字符串，寻找可以翻转的 "++" 位置
        for i in range(len(currentState) - 1):
            # 检查当前位置和下一个位置是否都是 '+'
            if currentState[i] == '+' and currentState[i + 1] == '+':
                # 生成新状态：将 "++" 替换为 "--"
                new_state = currentState[:i] + "--" + currentState[i + 2:]
                result.append(new_state)
        return result
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是字符串长度。我们需要遍历字符串一次，每次检查两个相邻字符，生成新状态的时间复杂度为 $O(n)$。
- **空间复杂度**：$O(k \times n)$，其中 $k$ 是可能的下一个状态数量。最坏情况下，如果字符串中每两个相邻字符都是 `"++"`，则 $k = O(n)$，每个状态需要 $O(n)$ 空间存储。
