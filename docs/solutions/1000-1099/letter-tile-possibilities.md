# [1079. 活字印刷](https://leetcode.cn/problems/letter-tile-possibilities/)

- 标签：哈希表、字符串、回溯、计数
- 难度：中等

## 题目链接

- [1079. 活字印刷 - 力扣](https://leetcode.cn/problems/letter-tile-possibilities/)

## 题目大意

**描述**：给定一个代表活字字模的字符串 $tiles$，其中 $tiles[i]$ 表示第 $i$ 个字模上刻的字母。

**要求**：返回你可以印出的非空字母序列的数目。

**说明**：

- 本题中，每个活字字模只能使用一次。
- $1 <= tiles.length <= 7$。
- $tiles$ 由大写英文字母组成。

**示例**：

- 示例 1：

```python
输入："AAB"
输出：8
解释：可能的序列为 "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA"。
```

- 示例 2：

```python
输入："AAABBC"
输出：188
```

## 解题思路

### 思路 1：哈希表 + 回溯算法

1. 使用哈希表存储每个字符的个数。
2. 然后依次从哈希表中取出对应字符，统计排列个数，并进行回溯。
3. 如果当前字符个数为 $0$，则不再进行回溯。
4. 回溯之后将状态回退。

### 思路 1：代码

```python
class Solution:
    ans = 0
    def backtrack(self, tile_map):
        for key, value in tile_map.items():
            if value == 0:
                continue
            self.ans += 1
            tile_map[key] -= 1
            self.backtrack(tile_map)
            tile_map[key] += 1

    def numTilePossibilities(self, tiles: str) -> int:
        tile_map = dict()
        for tile in tiles:
            if tile not in tile_map:
                tile_map[tile] = 1
            else:
                tile_map[tile] += 1

        self.backtrack(tile_map)

        return self.ans
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n \times n!)$，其中 $n$ 表示 $tiles$  的长度最小值。
- **空间复杂度**：$O(n)$。

