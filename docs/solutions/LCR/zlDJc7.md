# [LCR 109. 打开转盘锁](https://leetcode.cn/problems/zlDJc7/)

- 标签：广度优先搜索、数组、哈希表、字符串
- 难度：中等

## 题目链接

- [LCR 109. 打开转盘锁 - 力扣](https://leetcode.cn/problems/zlDJc7/)

## 题目大意

有一把带有四个数字的密码锁，每个位置上有 0~9 共 10 个数字。每次只能将其中一个位置上的数字转动一下。可以向上转，也可以向下转。比如：1 -> 2、2 -> 1。

密码锁的初始数字为：`0000`。现在给定一组表示死亡数字的字符串数组 `deadends`，和一个带有四位数字的目标字符串 `target`。

如果密码锁转动到 `deadends` 中任一字符串状态，则锁就会永久锁定，无法再次旋转。

要求：求出最小的选择次数，使得锁的状态由 `0000` 转动到 `target`。

## 解题思路

使用宽度优先搜索遍历，将`0000` 状态入队。

- 将队列中的元素出队，判断是否为死亡字符串
- 如果为死亡字符串，则跳过该状态，否则继续执行。

- 如果为目标字符串，则返回当前路径长度，否则继续执行。
- 枚举当前状态所有位置所能到达的所有状态，并判断是否访问过该状态。

- 如果之前出现过该状态，则继续执行，否则将其存入队列，并标记访问。

## 代码

```python
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = collections.deque(['0000'])
        visited = set(['0000'])
        deadset = set(deadends)
        level = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
                if cur in deadset:
                    continue
                if cur == target:
                    return level
                for i in range(len(cur)):
                    up = self.upward_adjust(cur, i)
                    if up not in visited:
                        queue.append(up)
                        visited.add(up)
                    down = self.downward_adjust(cur, i)
                    if down not in visited:
                        queue.append(down)
                        visited.add(down)
            level += 1
        return -1

    def upward_adjust(self, s, i):
        s_list = list(s)
        if s_list[i] == '9':
            s_list[i] = '0'
        else:
            s_list[i] = chr(ord(s_list[i]) + 1)
        return "".join(s_list)

    def downward_adjust(self, s, i):
        s_list = list(s)
        if s_list[i] == '0':
            s_list[i] = '9'
        else:
            s_list[i] = chr(ord(s_list[i]) - 1)
        return "".join(s_list)
```

