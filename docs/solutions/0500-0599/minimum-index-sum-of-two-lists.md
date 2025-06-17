# [0599. 两个列表的最小索引总和](https://leetcode.cn/problems/minimum-index-sum-of-two-lists/)

- 标签：数组、哈希表、字符串
- 难度：简单

## 题目链接

- [0599. 两个列表的最小索引总和 - 力扣](https://leetcode.cn/problems/minimum-index-sum-of-two-lists/)

## 题目大意

Andy 和 Doris 都有一个表示最喜欢餐厅的列表 list1、list2，每个餐厅的名字用字符串表示。

找出他们共同喜爱的餐厅，要求两个餐厅在列表中的索引和最小，如果答案不唯一，则输出所有答案。

## 解题思路

遍历 list1，建立一个哈希表 list1_dict，以 list1[i] : i 键值对的方式，将 list1 的下标存储起来。

然后遍历 list2，判断 list2[i] 是否在哈希表中，如果在，则根据 i + list1_dict[i] 和 min_sum 的比较，判断是否需要更新最小索引和。如果 i + list1_dict[i] < min_sum，则更新最小索引和，并清空答案数据，添加新的答案。如果 i + list1_dict[i] == min_sum，则更新最小索引和，并添加答案。

## 代码

```python
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list1_dict = dict()
        len1 = len(list1)
        len2 = len(list2)
        for i in range(len1):
            list1_dict[list1[i]] = i

        min_sum = len1 + len2
        res = []
        for i in range(len2):
            if list2[i] in list1_dict:
                sum = i + list1_dict[list2[i]]
                if sum < min_sum:
                    res = [list2[i]]
                    min_sum = sum
                elif sum == min_sum:
                    res.append(list2[i])
        return res
```

