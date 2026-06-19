# [1396. 设计地铁系统](https://leetcode.cn/problems/design-underground-system/)

- 标签：设计、哈希表、字符串
- 难度：中等

## 题目链接

- [1396. 设计地铁系统 - 力扣](https://leetcode.cn/problems/design-underground-system/)

## 题目大意

**描述**：实现地铁系统 $UndergroundSystem$：
- $checkIn(id, stationName, t)$：乘客 $id$ 在 $t$ 时刻进站 $stationName$。
- $checkOut(id, stationName, t)$：乘客 $id$ 在 $t$ 时刻出站 $stationName$。
- $getAverageTime(startStation, endStation)$：返回从 $startStation$ 到 $endStation$ 的平均用时。

**示例**：

- 示例 1：

```python
输入
["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]
[[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]

输出
[null,null,null,null,null,null,null,14.00000,11.00000,null,11.00000,null,12.00000]

解释
UndergroundSystem undergroundSystem = new UndergroundSystem();
undergroundSystem.checkIn(45, "Leyton", 3);
undergroundSystem.checkIn(32, "Paradise", 8);
undergroundSystem.checkIn(27, "Leyton", 10);
undergroundSystem.checkOut(45, "Waterloo", 15);  // 乘客 45 "Leyton" -> "Waterloo" ，用时 15-3 = 12
undergroundSystem.checkOut(27, "Waterloo", 20);  // 乘客 27 "Leyton" -> "Waterloo" ，用时 20-10 = 10
undergroundSystem.checkOut(32, "Cambridge", 22); // 乘客 32 "Paradise" -> "Cambridge" ，用时 22-8 = 14
undergroundSystem.getAverageTime("Paradise", "Cambridge"); // 返回 14.00000 。只有一个 "Paradise" -> "Cambridge" 的行程，(14) / 1 = 14
undergroundSystem.getAverageTime("Leyton", "Waterloo");    // 返回 11.00000 。有两个 "Leyton" -> "Waterloo" 的行程，(10 + 12) / 2 = 11
undergroundSystem.checkIn(10, "Leyton", 24);
undergroundSystem.getAverageTime("Leyton", "Waterloo");    // 返回 11.00000
undergroundSystem.checkOut(10, "Waterloo", 38);  // 乘客 10 "Leyton" -> "Waterloo" ，用时 38-24 = 14
undergroundSystem.getAverageTime("Leyton", "Waterloo");    // 返回 12.00000 。有三个 "Leyton" -> "Waterloo" 的行程，(10 + 12 + 14) / 3 = 12
```

- 示例 2：

```python
输入
["UndergroundSystem","checkIn","checkOut","getAverageTime","checkIn","checkOut","getAverageTime","checkIn","checkOut","getAverageTime"]
[[],[10,"Leyton",3],[10,"Paradise",8],["Leyton","Paradise"],[5,"Leyton",10],[5,"Paradise",16],["Leyton","Paradise"],[2,"Leyton",21],[2,"Paradise",30],["Leyton","Paradise"]]

输出
[null,null,null,5.00000,null,null,5.50000,null,null,6.66667]

解释
UndergroundSystem undergroundSystem = new UndergroundSystem();
undergroundSystem.checkIn(10, "Leyton", 3);
undergroundSystem.checkOut(10, "Paradise", 8); // 乘客 10 "Leyton" -> "Paradise" ，用时 8-3 = 5
undergroundSystem.getAverageTime("Leyton", "Paradise"); // 返回 5.00000 ，(5) / 1 = 5
undergroundSystem.checkIn(5, "Leyton", 10);
undergroundSystem.checkOut(5, "Paradise", 16); // 乘客 5 "Leyton" -> "Paradise" ，用时 16-10 = 6
undergroundSystem.getAverageTime("Leyton", "Paradise"); // 返回 5.50000 ，(5 + 6) / 2 = 5.5
undergroundSystem.checkIn(2, "Leyton", 21);
undergroundSystem.checkOut(2, "Paradise", 30); // 乘客 2 "Leyton" -> "Paradise" ，用时 30-21 = 9
undergroundSystem.getAverageTime("Leyton", "Paradise"); // 返回 6.66667 ，(5 + 6 + 9) / 3 = 6.66667
```


## 解题思路

### 思路 1：哈希表

#### 1. 核心思想

用 $check\_in$ 字典记录每个乘客的进站信息（车站+时间）。出站时查找对应的进站信息，计算用时，累加到 $travel\_times$ 字典中。

$travel\_times$ 的键为 $(start, end)$，值为 $(总用时, 次数)$。

#### 2. 具体步骤

**第 1 步**：$checkIn$：存入 $check\_in[id] = (stationName, t)$。

**第 2 步**：$checkOut$：查找 $check\_in[id]$，计算用时，累加到 $travel\_times$ 并删除 $check\_in[id]$。

**第 3 步**：$getAverageTime$：从 $travel\_times$ 获取总用时和次数，相除。

### 思路 1：代码

```python
class UndergroundSystem:
    def __init__(self):
        self.check_in = {}           # id → (station, time)
        self.travel_times = {}       # (start, end) → [total_time, count]

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.check_in.pop(id)
        key = (start_station, stationName)
        total, cnt = self.travel_times.get(key, (0.0, 0))
        self.travel_times[key] = (total + (t - start_time), cnt + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, cnt = self.travel_times[(startStation, endStation)]
        return total / cnt
```

### 思路 1：复杂度分析
- **时间复杂度**：$O(1)$ 每次操作。
- **空间复杂度**：$O(N)$，$N$ 是乘客数 + 路线数。
