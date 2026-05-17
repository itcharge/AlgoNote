# [1146. 快照数组](https://leetcode.cn/problems/snapshot-array/)

- 标签：设计、数组、哈希表、二分查找
- 难度：中等

## 题目链接

- [1146. 快照数组 - 力扣](https://leetcode.cn/problems/snapshot-array/)

## 题目大意

**描述**：实现一个「快照数组」`SnapshotArray`，支持以下操作：
- `SnapshotArray(int length)`：初始化一个长度为 $length$ 的数组，初始所有元素为 $0$。
- `void set(index, val)`：将下标 $index$ 处的值设为 $val$。
- `int snap()`：对当前数组拍一张快照，返回快照编号 $snap\_id$（从 $0$ 开始，每次调用 $+1$）。
- `int get(index, snap_id)`：返回指定快照中，下标 $index$ 处的值。

**说明**：

- $1 \le length \le 50000$。
- 最多进行 $50000$ 次操作。
- $0 \le snap\_id <$ 调用 $snap()$ 的总次数。

**示例**：

```python
输入：["SnapshotArray","set","snap","set","get"]
     [[3],[0,5],[],[0,6],[0,0]]
输出：[null,null,0,null,5]
解释：
SnapshotArray snapshotArr = new SnapshotArray(3); // 初始长度为 3
snapshotArr.set(0,5);   // array[0] = 5
snapshotArr.snap();      // 拍快照，返回 snap_id = 0
snapshotArr.set(0,6);   // array[0] = 6
snapshotArr.get(0,0);   // 获取 snap_id = 0 时 array[0] 的值，返回 5
```

## 解题思路

### 思路 1：哈希表 + 二分查找

**为什么不用完整复制？** 如果一个数组长度为 $50000$，拍了 $50000$ 次快照，每次都完整复制的话会爆内存。但每个下标被修改的次数通常不多，记录变更历史更省空间。

**拆解步骤**：

1. **数据结构**：
   - `data[i]`：一个列表，存储下标 $i$ 的历史记录，每条记录是 `[snap_id, value]`。
   - `snap_id`：当前快照编号。

2. **`set(index, val)`**：
   - 如果当前快照下这个下标已经有记录（列表最后一条的 snap_id 等于当前 snap_id），直接更新值。
   - 否则，添加一条新记录 `[snap_id, val]`。

3. **`snap()`**：快照编号 $+1$，返回旧的编号。

4. **`get(index, snap_id)`**：
   - 在 `data[index]` 的历史记录中二分查找，找到最后一条 `snap_id <= target` 的记录。
   - 因为历史记录是按 $snap\_id$ 递增的，可以用二分查找加速。

### 思路 1：代码

```python
class SnapshotArray:

    def __init__(self, length: int):
        # data[i] 存储下标 i 的历史记录，每条记录 [snap_id, value]
        # 初始时每个下标的值都是 0，snap_id = 0
        self.data = [[[0, 0]] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        # 如果当前快照下已经有记录，直接更新值
        if self.data[index][-1][0] == self.snap_id:
            self.data[index][-1][1] = val
        else:
            # 否则添加一条新记录
            self.data[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        history = self.data[index]
        # 二分查找：找到最后一条 snap_id <= 目标值的记录
        left, right = 0, len(history) - 1
        while left < right:
            mid = (left + right + 1) // 2  # 右中位数，避免死循环
            if history[mid][0] <= snap_id:
                left = mid
            else:
                right = mid - 1
        return history[left][1]
```

### 思路 1：复杂度分析

- **时间复杂度**：
  - `set()`：$O(1)$，直接操作列表末尾。
  - `snap()`：$O(1)$，计数器加一。
  - `get()`：$O(\log k)$，用人话说就是二分查找的时间，$k$ 是该下标被修改的次数。
- **空间复杂度**：$O(n + m)$，$n$ 是数组长度，$m$ 是 `set()` 的调用次数（即记录的总条数）。
