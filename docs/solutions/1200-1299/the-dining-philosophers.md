# [1226. 哲学家进餐](https://leetcode.cn/problems/the-dining-philosophers/)

- 标签：多线程
- 难度：中等

## 题目链接

- [1226. 哲学家进餐 - 力扣](https://leetcode.cn/problems/the-dining-philosophers/)

## 题目大意

**描述**：有 $5$ 个哲学家围坐在一张圆桌旁，每个人面前有一盘意面。每两个相邻的哲学家之间有一把叉子。哲学家的行为是：思考 → 拿起左右两把叉子 → 进餐 → 放下叉子 → 继续思考。

**要求**：设计一个调度策略，使得不会有哲学家饿死（即每个哲学家都能在有生之年吃上饭），且尽量提高并发度。需要实现 `wantsToEat` 方法，该方法会被多线程并发调用。

**说明**：

- 每个哲学家编号为 $0$ 到 $4$。
- 哲学家 $i$ 左边叉子编号为 $i$，右边叉子编号为 $(i+1) \% 5$。
- 需要调用 `pickLeftFork`、`pickRightFork`、`eat`、`putLeftFork`、`putRightFork` 方法来记录行为。

**示例**：

- 示例：

```python
输入：n = 1
输出：[[4,2,1],[4,1,1],[0,1,1],[2,2,1],[2,1,1],[2,4,1],[0,4,1]]
解释：n 表示每个哲学家需要进餐的次数。
```

## 解题思路

### 思路 1：信号量 + 限制并发数

#### 1. 核心思想

经典"哲学家进餐问题"的解法有多种：

1. **加锁保护拿起叉子的过程**：用互斥锁保护拿起两个叉子的操作，避免死锁。
2. **限制同时就餐的人数**：最多允许 $4$ 个哲学家同时就餐，这样至少有一个哲学家能拿到两把叉子。
3. **奇数位哲学家先拿左边，偶数位先拿右边**：破坏循环等待条件。

最优雅的方式是**用信号量限制同时就餐人数为 $4$**。

#### 2. 具体步骤

**第 1 步**：创建 $5$ 个叉子的信号量（每个初始为 $1$）。

**第 2 步**：创建一个"就餐许可"信号量，初始为 $4$（最多 $4$ 人同时就餐）。

**第 3 步**：在 `wantsToEat` 中：
- 获取就餐许可。
- 拿起左边叉子。
- 拿起右边叉子。
- 进餐。
- 放下右边叉子。
- 放下左边叉子。
- 释放就餐许可。

这样，因为最多 $4$ 个哲学家同时竞争 $5$ 把叉子，至少有一个哲学家能同时拿到两把叉子。不会出现每个人都拿着一把叉子等另一把的死锁局面。

### 思路 1：代码

```python
import threading

class DiningPhilosophers:
    def __init__(self):
        # 5 把叉子，每把对应一个锁
        self.forks = [threading.Lock() for _ in range(5)]
        # 最多允许 4 个哲学家同时就餐
        self.limit = threading.Semaphore(4)

    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        left = philosopher
        right = (philosopher + 1) % 5

        # 获取就餐许可
        self.limit.acquire()

        self.forks[left].acquire()
        self.forks[right].acquire()
        pickLeftFork()
        pickRightFork()
        eat()
        putLeftFork()
        putRightFork()
        self.forks[left].release()
        self.forks[right].release()

        # 释放就餐许可
        self.limit.release()
```

### 思路 2：奇数先左后右，偶数先右后左

#### 1. 核心思想

破坏死锁的"循环等待"条件。奇数编号的哲学家先拿左边再拿右边，偶数编号的哲学家先拿右边再拿左边。这样不会形成循环等待的环。

### 思路 2：代码

```python
import threading

class DiningPhilosophers:
    def __init__(self):
        self.forks = [threading.Lock() for _ in range(5)]

    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        left = philosopher
        right = (philosopher + 1) % 5

        if philosopher % 2 == 0:
            # 偶数：先右后左
            self.forks[right].acquire()
            self.forks[left].acquire()
        else:
            # 奇数：先左后右
            self.forks[left].acquire()
            self.forks[right].acquire()

        pickLeftFork()
        pickRightFork()
        eat()
        putLeftFork()
        putRightFork()
        self.forks[left].release()
        self.forks[right].release()
```

两种思路都正确。思路 1 更通用（不依赖于奇偶编号），思路 2 更简洁。
