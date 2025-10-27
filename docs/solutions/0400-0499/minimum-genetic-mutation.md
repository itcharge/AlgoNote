# [0433. 最小基因变化](https://leetcode.cn/problems/minimum-genetic-mutation/)

- 标签：广度优先搜索、哈希表、字符串
- 难度：中等

## 题目链接

- [0433. 最小基因变化 - 力扣](https://leetcode.cn/problems/minimum-genetic-mutation/)

## 题目大意

**描述**：

基因序列可以表示为一条由 $8$ 个字符组成的字符串，其中每个字符都是 `'A'`、`'C'`、`'G'` 和 `'T'` 之一。

假设我们需要调查从基因序列 $start$ 变为 $end$ 所发生的基因变化。一次基因变化就意味着这个基因序列中的一个字符发生了变化。

- 例如，`"AACCGGTT"` --> `"AACCGGTA"` 就是一次基因变化。

另有一个基因库 $bank$ 记录了所有有效的基因变化，只有基因库中的基因才是有效的基因序列。（变化后的基因必须位于基因库 $bank$ 中）

给定两个基因序列 $start$ 和 $end$，以及一个基因库 $bank$。

**要求**：

请你找出并返回能够使 $start$ 变化为 $end$ 所需的最少变化次数。如果无法完成此基因变化，返回 $-1$。

**说明**：

- 注意：起始基因序列 $start$ 默认是有效的，但是它并不一定会出现在基因库中。
- $start.length == 8$。
- $end.length == 8$。
- $0 \le bank.length \le 10$。
- $bank[i].length == 8$。
- $start$、$end$ 和 $bank[i]$ 仅由字符 `['A', 'C', 'G', 'T']` 组成。

**示例**：

- 示例 1：

```python
输入：start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]
输出：1
```

- 示例 2：

```python
输入：start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
输出：2
```

## 解题思路

### 思路 1：广度优先搜索

这是一个最短路径问题。我们需要找到从 $start$ 到 $end$ 的最少基因变化次数。

**核心思想**：
- 每次基因变化只能修改一个字符，且变化后的基因必须在基因库 $bank$ 中。
- 使用广度优先搜索（BFS）逐层遍历所有可能的基因变化。
- 使用哈希集合记录已访问过的基因，避免重复访问。
- 当找到目标基因 $end$ 时，返回变化次数。

**算法步骤**：

1. 如果 $start$ 等于 $end$，直接返回 $0$。
2. 将 $bank$ 转换为哈希集合 $bank\_set$，方便查找。
3. 如果 $end$ 不在 $bank\_set$ 中，返回 $-1$。
4. 初始化队列 $queue$，将 $(start, 0)$ 加入队列，表示从 $start$ 开始，变化次数为 $0$。
5. 初始化集合 $visited$，记录已访问的基因。
6. 定义字符集 $chars = ['A', 'C', 'G', 'T']$。
7. 从队列中取出当前基因 $current$ 和变化次数 $level$。
8. 遍历当前基因的每个位置 $i$，遍历每个字符 $c$：
   - 如果 $current[i] \neq c$，生成新基因 $new\_gene$。
   - 如果 $new\_gene$ 在 $bank\_set$ 中且未被访问过：
     - 如果 $new\_gene == end$，返回 $level + 1$。
     - 否则将 $new\_gene$ 加入队列和 $visited$ 集合。
9. 如果队列为空仍未找到目标，返回 $-1$。

### 思路 1：代码

```python
from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # 如果起始基因和目标基因相同，直接返回 0
        if startGene == endGene:
            return 0
        
        # 将基因库转换为集合，方便查找
        bank_set = set(bank)
        
        # 如果目标基因不在基因库中，无法完成变化，返回 -1
        if endGene not in bank_set:
            return -1
        
        # 定义可能的基因字符
        chars = ['A', 'C', 'G', 'T']
        
        # 初始化队列，使用 BFS 遍历
        queue = deque([(startGene, 0)])
        visited = {startGene}
        
        # BFS 遍历
        while queue:
            current, level = queue.popleft()
            
            # 尝试改变基因的每一个位置
            for i in range(len(current)):
                # 尝试将当前位置的字符替换为其他字符
                for c in chars:
                    if current[i] != c:
                        # 生成新的基因序列
                        new_gene = current[:i] + c + current[i+1:]
                        
                        # 如果新基因在基因库中且未被访问过
                        if new_gene in bank_set and new_gene not in visited:
                            # 如果找到了目标基因，返回变化次数
                            if new_gene == endGene:
                                return level + 1
                            
                            # 将新基因加入队列和已访问集合
                            queue.append((new_gene, level + 1))
                            visited.add(new_gene)
        
        # 无法完成基因变化，返回 -1
        return -1
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(N \times 8 \times 4) = O(N)$，其中 $N$ 为基因库中有效基因序列的数量。对于每个基因序列，我们需要遍历其 $8$ 个位置，每个位置有 $4$ 种可能的字符替换。在最坏情况下，需要遍历所有有效基因序列。
- **空间复杂度**：$O(N)$。主要开销包括：$O(N)$ 的哈希集合 $bank\_set$，$O(N)$ 的已访问集合 $visited$，以及 $O(N)$ 的队列空间。
