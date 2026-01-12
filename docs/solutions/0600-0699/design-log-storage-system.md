# [0635. 设计日志存储系统](https://leetcode.cn/problems/design-log-storage-system/)

- 标签：设计、哈希表、字符串、有序集合
- 难度：中等

## 题目链接

- [0635. 设计日志存储系统 - 力扣](https://leetcode.cn/problems/design-log-storage-system/)

## 题目大意

**描述**：

你将获得多条日志，每条日志都有唯一的 $id$ 和 $timestamp$，$timestamp$ 是形如 `Year:Month:Day:Hour:Minute:Second` 的字符串，例如 `2017:01:01:23:59:59`，所有值域都是零填充的十进制数。

**要求**：

实现 LogSystem 类：

- `LogSystem()` 初始化 `LogSystem` 对象
- `void put(int id, string timestamp)` 给定日志的 $id$ 和 $timestamp$，将这个日志存入你的存储系统中。
- `int[] retrieve(string start, string end, string granularity)` 返回在给定时间区间 $[start, end]$（包含两端）内的所有日志的 $id$。$start$、$end$ 和 $timestamp$ 的格式相同，$granularity$ 表示考虑的时间粒度（例如，精确到 `Day`、`Minute` 等）。例如 `start = "2017:01:01:23:59:59"`、`end = "2017:01:02:23:59:59"` 且 `granularity = "Day"` 意味着需要查找从 Jan. 1st 2017 到 Jan. 2nd 2017 范围内的日志，可以忽略日志的 `Hour`、`Minute` 和 `Second`。

**说明**：

- $1 \le id \le 500$。
- $2000 \le Year \le 2017$。
- $1 \le Month \le 12$。
- $1 \le Day \le 31$。
- $0 \le Hour \le 23$。
- $0 \le Minute, Second \le 59$。
- $granularity$ 是这些值 `["Year", "Month", "Day", "Hour", "Minute", "Second"]` 之一。
- 最多调用 $500$ 次 `put` 和 `retrieve`。

**示例**：

- 示例 1：

```python
输入：
["LogSystem", "put", "put", "put", "retrieve", "retrieve"]
[[], [1, "2017:01:01:23:59:59"], [2, "2017:01:01:22:59:59"], [3, "2016:01:01:00:00:00"], ["2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year"], ["2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour"]]
输出：
[null, null, null, null, [3, 2, 1], [2, 1]]

解释：
LogSystem logSystem = new LogSystem();
logSystem.put(1, "2017:01:01:23:59:59");
logSystem.put(2, "2017:01:01:22:59:59");
logSystem.put(3, "2016:01:01:00:00:00");

// 返回 [3,2,1]，返回从 2016 年到 2017 年所有的日志。
logSystem.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year");

// 返回 [2,1]，返回从 Jan. 1, 2016 01:XX:XX 到 Jan. 1, 2017 23:XX:XX 之间的所有日志
// 不返回日志 3 因为记录时间 Jan. 1, 2016 00:00:00 超过范围的起始时间
logSystem.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour");
```

## 解题思路

### 思路 1：哈希表 + 字符串处理

#### 思路 1：算法描述

这道题目要求设计一个日志存储系统，支持存储日志和根据时间粒度检索日志。

我们可以使用哈希表来存储日志，键为日志 ID，值为时间戳。在检索时，根据时间粒度截取时间戳的相应部分进行比较。

**算法步骤**：

1. **初始化**：创建一个哈希表 `logs`，用于存储日志 ID 和时间戳。

2. **put(id, timestamp)**：将日志 ID 和时间戳存入哈希表。

3. **retrieve(start, end, granularity)**：
   - 根据时间粒度确定需要比较的时间戳长度。
   - 截取 `start` 和 `end` 的相应部分。
   - 遍历所有日志，截取时间戳的相应部分，判断是否在 `[start, end]` 范围内。
   - 返回符合条件的日志 ID 列表。

时间粒度对应的截取长度：

- Year: 4
- Month: 7
- Day: 10
- Hour: 13
- Minute: 16
- Second: 19

#### 思路 1：代码

```python
class LogSystem:

    def __init__(self):
        self.logs = {}  # 存储日志 ID 和时间戳
        # 时间粒度对应的截取长度
        self.granularity_map = {
            "Year": 4,
            "Month": 7,
            "Day": 10,
            "Hour": 13,
            "Minute": 16,
            "Second": 19
        }

    def put(self, id: int, timestamp: str) -> None:
        self.logs[id] = timestamp

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        # 根据时间粒度确定截取长度
        length = self.granularity_map[granularity]
        
        # 截取 start 和 end 的相应部分
        start_prefix = start[:length]
        end_prefix = end[:length]
        
        result = []
        
        # 遍历所有日志
        for log_id, timestamp in self.logs.items():
            # 截取时间戳的相应部分
            timestamp_prefix = timestamp[:length]
            
            # 判断是否在范围内
            if start_prefix <= timestamp_prefix <= end_prefix:
                result.append(log_id)
        
        return result


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)
```

#### 思路 1：复杂度分析

- **时间复杂度**：
  - `put()`：$O(1)$。
  - `retrieve()`：$O(n)$，其中 $n$ 是日志的数量。需要遍历所有日志。
- **空间复杂度**：$O(n)$。需要存储 $n$ 条日志。
