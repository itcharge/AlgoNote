# [LCR 087. 复原 IP 地址](https://leetcode.cn/problems/0on3uN/)

- 标签：字符串、回溯
- 难度：中等

## 题目链接

- [LCR 087. 复原 IP 地址 - 力扣](https://leetcode.cn/problems/0on3uN/)

## 题目大意

给定一个只包含数字的字符串，用来表示一个 IP 地址。

要求：返回所有由 `s` 构成的有效 IP 地址，可以按任何顺序返回答案。

- 有效 IP 地址：正好由四个整数（每个整数由 0~255 的数构成，且不能含有前导 0），整数之间用 `.` 分割。

例如：`0.1.2.201` 和 `192.168.1.1` 是有效 IP 地址，但是 `0.011.255.245`、`192.168.1.312` 和 `192.168@1.1` 是 无效 IP 地址。

## 解题思路

回溯算法。使用 `res` 存储所有有效 IP 地址。用 `point_num` 表示当前 IP 地址的 `.` 符号个数。

定义回溯方法，从 `start_index` 位置开始遍历字符串。

- 如果字符串中添加的 `.` 符号数量为 `3`，则判断当前字符串是否为有效 IP 地址，如果为有效 IP 地址则加入到 `res` 数组中。直接返回。
- 然后在 `[start_index, len(s) - 1]` 范围循环遍历，判断 `[start_index, i]` 范围所代表的子串是否合法。如果合法：
    - 则 `point_num += 1`。
    - 然后在 i 位置后边增加 `.` 符号，继续回溯遍历。
    - 最后 `point_num -= 1` 进行回退。
- 不符合则直接跳出循环。
- 最后返回 `res`。

## 代码

```python
class Solution:
    res = []

    def backstrack(self, s: str, start_index: int, point_num: int):
        if point_num == 3:
            if self.isValid(s, start_index, len(s) - 1):
                self.res.append(s)
            return
        for i in range(start_index, len(s)):
            if self.isValid(s, start_index, i):
                point_num += 1
                self.backstrack(s[:i + 1] + '.' + s[i + 1:], i + 2, point_num)
                point_num -= 1
            else:
                break

    def isValid(self, s: str, start: int, end: int):
        if start > end:
            return False
        if s[start] == '0' and start != end:
            return False
        num = 0
        for i in range(start, end + 1):
            if s[i] > '9' or s[i] < '0':
                return False
            num = num * 10 + ord(s[i]) - ord('0')
            if num > 255:
                return False
        return True

    def restoreIpAddresses(self, s: str) -> List[str]:
        self.res.clear()
        if len(s) > 12:
            return self.res
        self.backstrack(s, 0, 0)
        return self.res
```

