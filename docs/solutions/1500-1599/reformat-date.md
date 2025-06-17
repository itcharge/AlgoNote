# [1507. 转变日期格式](https://leetcode.cn/problems/reformat-date/)

- 标签：字符串
- 难度：简单

## 题目链接

- [1507. 转变日期格式 - 力扣](https://leetcode.cn/problems/reformat-date/)

## 题目大意

**描述**：给定一个字符串 $date$，它的格式为 `Day Month Year` ，其中：

- $Day$ 是集合 `{"1st", "2nd", "3rd", "4th", ..., "30th", "31st"}` 中的一个元素。
- $Month$ 是集合 `{"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}` 中的一个元素。
- $Year$ 的范围在 $[1900, 2100]$ 之间。

**要求**：将字符串转变为 `YYYY-MM-DD` 的格式，其中：

- $YYYY$ 表示 $4$ 位的年份。
- $MM$ 表示 $2$ 位的月份。
- $DD$ 表示 $2$ 位的天数。

**说明**：

- 给定日期保证是合法的，所以不需要处理异常输入。

**示例**：

- 示例 1：

```python
输入：date = "20th Oct 2052"
输出："2052-10-20"
```

- 示例 2：

```python
输入：date = "6th Jun 1933"
输出："1933-06-06"
```

## 解题思路

### 思路 1：模拟

1. 将字符串分割为三部分，分别按照以下规则得到日、月、年：
   1. 日：去掉末尾两位英文字母，将其转为整型数字，并且进行补零操作，使其宽度为 $2$。
   2. 月：使用哈希表将其映射为对应两位数字。
   3. 年：直接赋值。
2. 将得到的年、月、日使用 `"-"` 进行链接并返回。

### 思路 1：代码

```python
class Solution:
    def reformatDate(self, date: str) -> str:
        months = {
            "Jan" : "01", "Feb" : "02", "Mar" : "03", "Apr" : "04", "May" : "05", "Jun" : "06", 
            "Jul" : "07", "Aug" : "08", "Sep" : "09", "Oct" : "10", "Nov" : "11", "Dec" : "12"
        }
        date_list = date.split(' ')
        day = "{:0>2d}".format(int(date_list[0][: -2]))
        month = months[date_list[1]]
        year = date_list[2]
        return year + "-" + month + "-" + day
```

### 思路 1：复杂度分析

- **时间复杂度**：$O(1)$。
- **空间复杂度**：$O(1)$。

