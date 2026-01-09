# [0981. 基于时间的键值存储](https://leetcode.cn/problems/time-based-key-value-store/)

- 标签：设计、哈希表、字符串、二分查找
- 难度：中等

## 题目链接

- [0981. 基于时间的键值存储 - 力扣](https://leetcode.cn/problems/time-based-key-value-store/)

## 题目大意

**描述**：

设计一个基于时间的键值数据结构，该结构可以在不同时间戳存储对应同一个键的多个值，并针对特定时间戳检索键对应的值。

**要求**：

实现 TimeMap 类：

- `TimeMap()` 初始化数据结构对象
- `void set(String key, String value, int timestamp)` 存储给定时间戳 $timestamp$ 时的键 $key$ 和值 $value$。
- `String get(String key, int timestamp)` 返回一个值，该值在之前调用了 `set`，其中 $timestamp\_prev \le timestamp$。如果有多个这样的值，它将返回与最大  $timestamp\_prev$ 关联的值。如果没有值，则返回空字符串（`""`）。

**说明**：

- $1 \le key.length, value.length \le 10^{3}$。
- key 和 value 由小写英文字母和数字组成。
- $1 \le timestamp \le 10^{7}$。
- `set` 操作中的时间戳 timestamp 都是严格递增的。
- 最多调用 `set` 和 `get` 操作 $2 \times 10^{5}$ 次。

**示例**：

- 示例 1：

```python
输入：
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
输出：
[null, null, "bar", "bar", null, "bar2", "bar2"]

解释：
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // 存储键 "foo" 和值 "bar" ，时间戳 timestamp = 1   
timeMap.get("foo", 1);         // 返回 "bar"
timeMap.get("foo", 3);         // 返回 "bar", 因为在时间戳 3 和时间戳 2 处没有对应 "foo" 的值，所以唯一的值位于时间戳 1 处（即 "bar"） 。
timeMap.set("foo", "bar2", 4); // 存储键 "foo" 和值 "bar2" ，时间戳 timestamp = 4  
timeMap.get("foo", 4);         // 返回 "bar2"
timeMap.get("foo", 5);         // 返回 "bar2"
```

## 解题思路

### 思路 1：哈希表 + 二分查找

使用哈希表存储每个键对应的时间戳和值的列表，由于时间戳是递增的，可以使用二分查找。

1. 使用哈希表 $data$，键为字符串 $key$，值为列表，列表中每个元素是 $(timestamp, value)$ 元组。
2. `set` 操作：将 $(timestamp, value)$ 添加到 $data[key]$ 的列表末尾。
3. `get` 操作：在 $data[key]$ 的列表中二分查找小于等于 $timestamp$ 的最大时间戳。

### 思路 1：代码

```python
class TimeMap:

    def __init__(self):
        # 哈希表，key -> [(timestamp, value), ...]
        self.data = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # 直接添加到列表末尾（时间戳递增）
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        
        pairs = self.data[key]
        # 二分查找小于等于 timestamp 的最大时间戳
        left, right = 0, len(pairs) - 1
        result = ""
        
        while left <= right:
            mid = (left + right) // 2
            if pairs[mid][0] <= timestamp:
                result = pairs[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        
        return result


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
```

### 思路 1：复杂度分析

- **时间复杂度**：`set` 操作为 $O(1)$，`get` 操作为 $O(\log n)$，其中 $n$ 是该键对应的时间戳数量。
- **空间复杂度**：$O(N)$，其中 $N$ 是所有 `set` 操作的总次数。
