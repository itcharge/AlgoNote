# [1089. 复写零](https://leetcode.cn/problems/duplicate-zeros/)

- 标签：数组、双指针
- 难度：简单

## 题目链接

- [1089. 复写零 - 力扣](https://leetcode.cn/problems/duplicate-zeros/)

## 题目大意

**描述**：给定搞一个长度固定的整数数组 $arr$。

**要求**：键改改数组中出现的每一个 $0$ 都复写一遍，并将其余的元素向右平移。

**说明**：

- 注意：不要在超过该数组长度的位置写上元素。请对输入的数组就地进行上述修改，不要从函数返回任何东西。
- $1 \le arr.length \le 10^4$。
- $0 \le arr[i] \le 9$。

**示例**：

- 示例 1：

```python
输入：arr = [1,0,2,3,0,4,5,0]
输出：[1,0,0,2,3,0,0,4]
解释：调用函数后，输入的数组将被修改为：[1,0,0,2,3,0,0,4]
```

- 示例 2：

```python
输入：arr = [1,2,3]
输出：[1,2,3]
解释：调用函数后，输入的数组将被修改为：[1,2,3]
```

## 解题思路

### 思路 1：两次遍历 + 快慢指针

因为数组中出现的 $0$ 需要复写为 $00$，占用空间从一个单位变成两个单位空间，那么右侧必定会有一部分元素丢失。我们可以先遍历一遍数组，找出复写后需要保留的有效数字部分与需要丢失部分的分界点。则从分界点开始，分界点右侧的元素都可以丢失。

我们再次逆序遍历数组，

1. 使用两个指针 $slow$、$fast$，$slow$ 表示当前有效字符位置，$fast$ 表示当前遍历字符位置。一开始 $slow$ 和 $fast$ 都指向数组开始位置。
2. 正序扫描数组：
   1. 如果遇到 $arr[slow] == 0$，则让 $fast$ 指针多走一步。
   2. 然后 $fast$、$slow$ 各自向右移动 $1$ 位，直到 $fast$ 指针移动到数组末尾。此时 $slow$ 左侧数字 $arr[0]... arr[slow - 1]$ 为需要保留的有效数字部分， $arr[slow]...arr[fast - 1]$ 为需要丢失部分。
3. 令 $slow$、$fast$ 分别左移 $1$ 位，此时 $slow$ 指向最后一个有效数字，$fast$ 指向丢失部分的最后一个数字。此时 $fast$ 可能等于 $size - 1$，也可能等于 $size$（比如输入 $[0, 0, 0]$）。
4. 逆序遍历数组：
   1. 将 $slow$ 位置元素移动到 $fast$ 位置。
   2. 如果遇到 $arr[slow] == 0$，则令 $fast$ 减 $1$，然后再复制 $1$ 个 $0$ 到 $fast$ 位置。
   3. 令 $slow$、$fast$ 分别左移 $1$ 位。

### 思路 1：代码

```python
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        size = len(arr)
        slow, fast = 0, 0
        while fast < size:
            if arr[slow] == 0:
                fast += 1
            slow += 1
            fast += 1
        
        slow -= 1 # slow 指向最后一个有效数字
        fast -= 1 # fast 指向丢失部分的最后一个数字（可能在减 1 之后为 size，比如输入 [0, 0, 0]）

        while slow >= 0:
            if fast < size: # 防止 fast 越界
                arr[fast] = arr[slow] # 将 slow 位置元素移动到 fast 位置
            if arr[slow] == 0 and fast >= 0: # 遇见 0 则复制 0 到 fast - 1 位置
                fast -= 1
                arr[fast] = arr[slow]
            fast -= 1
            slow -= 1
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(n)$，其中 $n$ 为数组 $arr$ 中的元素个数。
- **空间复杂度**：$O(1)$。
