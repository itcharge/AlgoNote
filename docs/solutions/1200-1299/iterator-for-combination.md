# [1286. 字母组合迭代器](https://leetcode.cn/problems/iterator-for-combination/)

- 标签：设计、字符串、回溯、迭代器
- 难度：中等

## 题目链接

- [1286. 字母组合迭代器 - 力扣](https://leetcode.cn/problems/iterator-for-combination/)

## 题目大意

**描述**：设计一个迭代器类 $CombinationIterator$，包含以下功能：
- `CombinationIterator(characters, combinationLength)`：构造函数，输入一个有序且字符唯一的字符串 $characters$ 和一个数字 $combinationLength$。
- `next()`：按字典序返回长度为 $combinationLength$ 的下一个字母组合。
- `hasNext()`：只有存在下一个字母组合时才返回 `true`。

**说明**：

- $1 \le combinationLength \le characters.length \le 15$。
- $characters$ 中每个字符都不同。
- 每组测试数据最多对 `next` 和 `hasNext` 调用 $10^{4}$ 次。
- 题目保证每次调用 `next` 时都存在下一个字母组合。

**示例**：

- 示例 1：

```python
输入:
["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[["abc", 2], [], [], [], [], [], []]
输出：
[null, "ab", true, "ac", true, "bc", false]
解释：
CombinationIterator iterator = new CombinationIterator("abc", 2);
iterator.next();    // 返回 "ab"
iterator.hasNext(); // 返回 true
iterator.next();    // 返回 "ac"
iterator.hasNext(); // 返回 true
iterator.next();    // 返回 "bc"
iterator.hasNext(); // 返回 false
```

## 解题思路

### 思路 1：预处理所有组合

###### 1. 核心思想

因为 $characters.length \le 15$，总的组合数最多 $C(15, 7) \approx 6435$，完全可以在构造函数中预先计算所有组合，按字典序排列好。之后 `next()` 和 `hasNext()` 就是简单的数组遍历。

生成组合用回溯法：从 $characters$ 中按顺序选取字符，选够 $combinationLength$ 个就记录一个结果。

###### 2. 具体步骤

**第 1 步：构造函数**

定义回溯函数 $backtrack(start, path)$：
- $start$：当前可选字符的起始下标。
- $path$：当前已选的字符列表。

从 $start$ 开始遍历 $characters$：
- 将 $characters[i]$ 加入 $path$。
- 如果 $path$ 长度达到 $combinationLength$，将 $path$ 转成字符串加入 $self.combinations$。
- 否则递归调用 $backtrack(i + 1, path)$。
- 回溯：将 $characters[i]$ 从 $path$ 中移除。

**第 2 步：实现 next()**

返回 $self.combinations[self.index]$，然后 $self.index += 1$。

**第 3 步：实现 hasNext()**

返回 $self.index < len(self.combinations)$。

**结合示例走一遍：**

$characters = \text{"abc"}, combinationLength = 2$

回溯过程：
- 选 `'a'`：再从 `'bc'` 中选一个
  - 选 `'a','b'` → `"ab"`
  - 选 `'a','c'` → `"ac"`
- 选 `'b'`：再从 `'c'` 中选一个
  - 选 `'b','c'` → `"bc"`

按字典序生成：`["ab", "ac", "bc"]`

### 思路 1：代码

```python
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combinations = []
        self.index = 0

        # 回溯法生成所有长度为 combinationLength 的组合
        def backtrack(start, path):
            if len(path) == combinationLength:
                self.combinations.append(''.join(path))
                return
            for i in range(start, len(characters)):
                path.append(characters[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])

    def next(self) -> str:
        res = self.combinations[self.index]
        self.index += 1
        return res

    def hasNext(self) -> bool:
        return self.index < len(self.combinations)
```

### 思路 1：复杂度分析

- **时间复杂度**：
  - 构造函数：$O(C(n, k) \times k)$，其中 $n$ 是 $characters$ 的长度，$k$ 是 $combinationLength$。需要生成所有组合，每个组合需要 $O(k)$ 时间转成字符串。
  - `next`：$O(k)$，返回字符串。
  - `hasNext`：$O(1)$。
- **空间复杂度**：$O(C(n, k) \times k)$，需要存储所有组合。在 $n \le 15$ 时最多约 $6435$ 个组合，完全可行。
