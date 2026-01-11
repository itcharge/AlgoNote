# [0582. 杀掉进程](https://leetcode.cn/problems/kill-process/)

- 标签：树、深度优先搜索、广度优先搜索、数组、哈希表
- 难度：中等

## 题目链接

- [0582. 杀掉进程 - 力扣](https://leetcode.cn/problems/kill-process/)

## 题目大意

**描述**：

给定一个进程 ID 列表 $pid$ 和对应的父进程 ID 列表 $ppid$，其中 $pid[i]$ 是第 $i$ 个进程的 ID，$ppid[i]$ 是第 $i$ 个进程的父进程 ID。

在给定一个要杀掉的进程 ID $kill$。

当一个进程被杀掉时，它的所有子进程和后代进程也会被杀掉。

**要求**：

返回被杀掉的所有进程的 ID 列表（包括 $kill$ 本身）。

**说明**：

- $n == pid.length$。
- $n == ppid.length$。
- $1 \le n \le 5 \times 10^4$。
- $1 \le pid[i] \le 5 \times 10^4$。
- $0 \le ppid[i] \le 5 \times 10^4$。
- 只有一个进程的父进程 ID 为 0，表示根进程。
- 所有 $pid$ 都是唯一的。
- 题目数据保证 $kill$ 在 $pid$ 中。

**示例**：

- 示例 1：

![](https://assets.leetcode.com/uploads/2021/02/24/ptree.jpg)

```python
输入：pid = [1,3,10,5], ppid = [3,0,5,3], kill = 5
输出：[5,10]
解释：
进程树：
     3
   /   \
  1     5
       /
      10
杀掉进程 5，同时杀掉其子进程 10。
```

- 示例 2：

```python
输入：pid = [1], ppid = [0], kill = 1
输出：[1]
```

## 解题思路

### 思路 1：构建进程树 + DFS

给定进程 ID 列表和父进程 ID 列表，以及要杀掉的进程 ID，需要返回该进程及其所有子进程。

**解题步骤**：

1. 使用哈希表构建进程树：$parent\_to\_children[parent\_id] = [child\_id1, child\_id2, ...]$。
2. 从要杀掉的进程 $kill$ 开始，使用 DFS 或 BFS 遍历所有子进程。
3. 将遍历到的所有进程 ID 加入结果列表。

### 思路 1：代码

```python
from collections import defaultdict

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        # 构建进程树：parent -> children
        tree = defaultdict(list)
        for i in range(len(pid)):
            tree[ppid[i]].append(pid[i])
        
        result = []
        
        # DFS 遍历所有子进程
        def dfs(process_id: int):
            result.append(process_id)
            # 递归处理所有子进程
            for child in tree[process_id]:
                dfs(child)
        
        dfs(kill)
        return result
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 是进程数量。需要遍历所有进程构建树，然后遍历要杀掉的进程的所有子进程。
- **空间复杂度**：$O(n)$，哈希表存储进程树，递归栈的深度最多为 $n$。
