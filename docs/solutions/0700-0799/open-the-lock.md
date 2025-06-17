# [0752. 打开转盘锁](https://leetcode.cn/problems/open-the-lock/)

- 标签：广度优先搜索、数组、哈希表、字符串
- 难度：中等

## 题目链接

- [0752. 打开转盘锁 - 力扣](https://leetcode.cn/problems/open-the-lock/)

## 题目大意

**描述**：有一把带有四个数字的密码锁，每个位置上有 `0` ~ `9` 共 `10` 个数字。每次只能将其中一个位置上的数字转动一下。可以向上转，也可以向下转。比如：`1 -> 2`、`2 -> 1`。

密码锁的初始数字为：`0000`。现在给定一组表示死亡数字的字符串数组 `deadends`，和一个带有四位数字的目标字符串 `target`。

如果密码锁转动到 `deadends` 中任一字符串状态，则锁就会永久锁定，无法再次旋转。

**要求**：给出使得锁的状态由 `0000` 转动到 `target` 的最小的选择次数。如果无论如何不能解锁，返回 `-1` 。

**说明**：

- $1 \le deadends.length \le 500$
  $deadends[i].length == 4$
  $target.length == 4$
  $target$ 不在 $deadends$ 之中
  $target$ 和 $deadends[i]$ 仅由若干位数字组成。

**示例**：

- 示例 1：

```python
输入：deadends = ["0201","0101","0102","1212","2002"], target = "0202"
输出：6
解释：
可能的移动序列为 "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202"。
注意 "0000" -> "0001" -> "0002" -> "0102" -> "0202" 这样的序列是不能解锁的，
因为当拨动到 "0102" 时这个锁就会被锁定。
```

- 示例 2：

```python
输入: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
输出：-1
解释：无法旋转到目标数字且不被锁定。
```

## 解题思路

### 思路 1：广度优先搜索

1. 定义 `visited` 为标记访问节点的 set 集合变量，`queue` 为存放节点的队列。
2. 将`0000` 状态标记为访问，并将其加入队列 `queue`。
3. 将当前队列中的所有状态依次出队，判断这些状态是否为死亡字符串。
   1. 如果为死亡字符串，则跳过该状态，否则继续执行。
   2. 如果为目标字符串，则返回当前路径长度，否则继续执行。

4. 枚举当前状态所有位置所能到达的所有状态（通过向上或者向下旋转），并判断是否访问过该状态。
5. 如果之前出现过该状态，则继续执行，否则将其存入队列，并标记访问。
6. 遍历完步骤 3 中当前队列中的所有状态，令路径长度加 `1`，继续执行 3 ~ 5 步，直到队列为空。
7. 如果队列为空，也未能到达目标状态，则返回 `-1`。

### 思路 1：代码

```python
import collections

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

### 思路 1：复杂度分析

- **时间复杂度**：$O(10^d \times d^2 + m \times d)$。其中 $d$ 是数字的位数，$m$ 是数组 $deadends$ 的长度。
- **空间复杂度**：$O(10^D \times d + m)$。
