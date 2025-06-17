# [1108. IP 地址无效化](https://leetcode.cn/problems/defanging-an-ip-address/)

- 标签：字符串
- 难度：简单

## 题目链接

- [1108. IP 地址无效化 - 力扣](https://leetcode.cn/problems/defanging-an-ip-address/)

## 题目大意

**描述**：给定一个有效的 IPv4 的地址 `address`。。

**要求**：返回这个 IP 地址的无效化版本。

**说明**：

- **无效化 IP 地址**：其实就是用 `"[.]"` 代替了每个 `"."`。

**示例**：

- 示例 1：

```python
输入：address = "255.100.50.0"
输出："255[.]100[.]50[.]0"
```

## 解题思路

### 思路 1：字符串替换

依次将字符串 `address` 中的 `"."` 替换为 `"[.]"`。这里为了方便，直接调用了 `replace` 方法。

### 思路 1：字符串替换代码

```python
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')
```
