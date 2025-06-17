# [0468. 验证IP地址](https://leetcode.cn/problems/validate-ip-address/)

- 标签：字符串
- 难度：中等

## 题目链接

- [0468. 验证IP地址 - 力扣](https://leetcode.cn/problems/validate-ip-address/)

## 题目大意

**描述**：给定一个字符串 `queryIP`。

**要求**：如果是有效的 IPv4 地址，返回 `"IPv4"`；如果是有效的 IPv6 地址，返回 `"IPv6"`；如果不是上述类型的 IP 地址，返回 `"Neither"`。

**说明**：

- **有效的 IPv4 地址**：格式为 `"x1.x2.x3.x4"` 形式的 IP 地址。 其中：
  -  $0 \le xi \le 255$。
  - $xi$ 不能包含前导零。

- 例如: `"192.168.1.1"` 、 `"192.168.1.0"` 为有效 IPv4 地址，`"192.168.01.1"` 为无效 IPv4 地址，`"192.168.1.00"` 、 `"192.168@1.1"` 为无效 IPv4 地址。
- **有效的 IPv6 地址**： 格式为`"x1:x2:x3:x4:x5:x6:x7:x8"` 的 IP 地址，其中:
  - $1 \le xi.length \le 4$。
  - $xi$ 是一个十六进制字符串，可以包含数字、小写英文字母（`'a'` 到 `'f'`）和大写英文字母（`'A'` 到 `'F'`）。
  - 在 $xi$ 中允许前导零。
- 例如：`"2001:0db8:85a3:0000:0000:8a2e:0370:7334"` 和 `"2001:db8:85a3:0:0:8A2E:0370:7334"` 是有效的 IPv6 地址，而 `"2001:0db8:85a3::8A2E:037j:7334"` 和 `"02001:0db8:85a3:0000:0000:8a2e:0370:7334"` 是无效的 IPv6 地址。
- `queryIP` 仅由英文字母，数字，字符 `'.'` 和 `':'` 组成。

**示例**：

- 示例 1：

```python
输入：queryIP = "172.16.254.1"
输出："IPv4"
解释：有效的 IPv4 地址，返回 "IPv4"
```

- 示例 2：

```python
输入：queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
输出："IPv6"
解释：有效的 IPv6 地址，返回 "IPv6"
```

## 解题思路

### 思路 1：模拟

根据题意以及有效的 IPV4 地址规则、有效的 IPv6 地址规则，我们可以分两步来做：第一步，验证是否为有效的 IPV4 地址。第二步，验证是否为有效的 IPv6 地址。

#### 1. 验证是否为有效的 IPv4 地址

1. 将字符串按照 `'.'` 进行分割，将不同分段存入数组 `path` 中。
2. 如果分段数组 `path` 长度等于 $4$，则说明该字符串为 IPv4 地址，接下里验证是否为有效的 IPv4 地址。
3. 遍历分段数组 `path`，去验证每个分段 `sub`。
   1. 如果当前分段 `sub` 为空，或者不是纯数字，则返回 `"Neither"`。
   2. 如果当前分段 `sub` 有前导 $0$，并且长度不为 $1$，则返回 `"Neither"`。
   3. 如果当前分段 `sub` 对应的值不在 $0 \sim 255$ 范围内，则返回 `"Neither"`。
4. 遍历完分段数组 `path`，扔未发现问题，则该字符串为有效的 IPv4 地址，返回 `IPv4`。

#### 2. 验证是否为有效的 IPv6 地址

1. 将字符串按照 `':'` 进行分割，将不同分段存入数组 `path` 中。
2. 如果分段数组 `path` 长度等于 $8$，则说明该字符串为 IPv6 地址，接下里验证是否为有效的 IPv6 地址。
3. 定义一个代表十六进制不同字符的字符串 `valid = "0123456789abcdefABCDEF"`，用于验证分段的每一位是否为 $16$ 进制数。
4. 遍历分段数组 `path`，去验证每个分段 `sub`。
   1. 如果当前分段 `sub` 为空，则返回 `"Neither"`。
   2. 如果当前分段 `sub` 长度超过 $4$，则返回 `"Neither"`。
   3. 如果当前分段 `sub` 对应的每一位的值不在 `valid` 内，则返回 `"Neither"`。
5. 遍历完分段数组 `path`，扔未发现问题，则该字符串为有效的 IPv6 地址，返回 `IPv6`。

如果通过上面两步验证，该字符串既不是有效的 IPv4 地址，也不是有效的 IPv6 地址，则返回 `"Neither"`。

### 思路 1：代码

```python
class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        path = queryIP.split('.')
        if len(path) == 4:
            for sub in path:
                if not sub or not sub.isdecimal():
                    return "Neither"
                if sub[0] == '0' and len(sub) != 1:
                    return "Neither"
                if int(sub) > 255:
                    return "Neither"
            return "IPv4"

        path = queryIP.split(':')
        if len(path) == 8:
            valid = "0123456789abcdefABCDEF"
            for sub in path:
                if not sub:
                    return "Neither"
                if len(sub) > 4:
                    return "Neither"
                for digit in sub:
                    if digit not in valid:
                        return "Neither"
            return "IPv6"

        return "Neither"
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 为字符串 `queryIP` 的长度。
- **空间复杂度**：$O(n)$。
