# [0690. 员工的重要性](https://leetcode.cn/problems/employee-importance/)

- 标签：深度优先搜索、广度优先搜索、哈希表
- 难度：中等

## 题目链接

- [0690. 员工的重要性 - 力扣](https://leetcode.cn/problems/employee-importance/)

## 题目大意

给定一个公司的所有员工信息。其中每个员工信息包含：该员工 id，该员工重要度，以及该员工的所有下属 id。

再给定一个员工 id，要求返回该员工和他所有下属的重要度之和。

## 解题思路

利用哈希表，以「员工 id: 员工数据结构」的形式将员工信息存入哈希表中。然后深度优先搜索该员工以及下属员工。在搜索的同时，计算重要度之和，最终返回结果即可。

## 代码

```python
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employee_dict = dict()
        for employee in employees:
            employee_dict[employee.id] = employee

        def dfs(index: int) -> int:
            total = employee_dict[index].importance
            for sub_index in employee_dict[index].subordinates:
                total += dfs(sub_index)
            return total

        return dfs(id)
```

