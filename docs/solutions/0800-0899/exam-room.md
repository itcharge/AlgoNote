# [0855. 考场就座](https://leetcode.cn/problems/exam-room/)

- 标签：设计、有序集合、堆（优先队列）
- 难度：中等

## 题目链接

- [0855. 考场就座 - 力扣](https://leetcode.cn/problems/exam-room/)

## 题目大意

**描述**：

在考场里，有 $n$ 个座位排成一行，编号为 0 到 $n - 1$。

当学生进入考场后，他必须坐在离最近的人最远的座位上。如果有多个这样的座位，他会坐在编号最小的座位上。(另外，如果考场里没有人，那么学生就坐在 0 号座位上)

**要求**：

设计一个模拟所述考场的类。

实现 ExamRoom 类：
- `ExamRoom(int n)` 用座位的数量 $n$ 初始化考场对象。
- `int seat()` 返回下一个学生将会入座的座位编号。
- `void leave(int p)` 指定坐在座位 $p$ 的学生将离开教室。保证座位 $p$ 上会有一位学生。

**说明**：

- $1 \le n \le 10^{9}$
- 保证有学生正坐在座位 $p$ 上。
- $seat$ 和 $leave$ 最多被调用 $10^{4}$ 次。

**示例**：

- 示例 1：

```python
输入：
["ExamRoom", "seat", "seat", "seat", "seat", "leave", "seat"]
[[10], [], [], [], [], [4], []]
输出：
[null, 0, 9, 4, 2, null, 5]
解释：
ExamRoom examRoom = new ExamRoom(10);
examRoom.seat(); // 返回 0，房间里没有人，学生坐在 0 号座位。
examRoom.seat(); // 返回 9，学生最后坐在 9 号座位。
examRoom.seat(); // 返回 4，学生最后坐在 4 号座位。
examRoom.seat(); // 返回 2，学生最后坐在 2 号座位。
examRoom.leave(4);
examRoom.seat(); // 返回 5，学生最后坐在 5 号座位。
```

## 解题思路

### 思路 1：有序集合 + 贪心

这道题要求设计一个考场座位系统，学生入座时要坐在离最近的人最远的位置。

关键思路：

- 使用有序集合（如 Python 的 `list` 或 `SortedList`）维护已坐学生的位置。
- 入座时，找到最大间隔的中点：
  - 检查第一个座位（0 号）到第一个学生的距离。
  - 检查相邻两个学生之间的中点到最近学生的距离。
  - 检查最后一个学生到最后一个座位（$n-1$ 号）的距离。
- 选择距离最大的位置，如果有多个，选择编号最小的。

### 思路 1：代码

```python
class ExamRoom:

    def __init__(self, n: int):
        self.n = n
        self.students = []  # 有序列表，存储已坐学生的位置

    def seat(self) -> int:
        # 如果没有学生，坐在 0 号位置
        if not self.students:
            self.students.append(0)
            return 0
        
        # 计算最大距离和对应的座位
        max_dist = self.students[0]  # 第一个座位到第一个学生的距离
        seat_pos = 0
        
        # 检查相邻学生之间的中点
        for i in range(len(self.students) - 1):
            left = self.students[i]
            right = self.students[i + 1]
            # 中点到最近学生的距离
            dist = (right - left) // 2
            if dist > max_dist:
                max_dist = dist
                seat_pos = left + dist
        
        # 检查最后一个学生到最后一个座位的距离
        if self.n - 1 - self.students[-1] > max_dist:
            seat_pos = self.n - 1
        
        # 将新学生插入有序列表
        import bisect
        bisect.insort(self.students, seat_pos)
        
        return seat_pos

    def leave(self, p: int) -> None:
        # 移除学生
        self.students.remove(p)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)
```

### 思路 1：复杂度分析

- **时间复杂度**：
  - `seat` 操作：$O(n)$，需要遍历所有已坐学生，插入操作需要 $O(n)$。
  - `leave` 操作：$O(n)$，需要查找并删除学生。
- **空间复杂度**：$O(n)$，需要存储所有已坐学生的位置。
