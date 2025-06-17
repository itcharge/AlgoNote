# [LCR 113. 课程表 II](https://leetcode.cn/problems/QA2IGt/)

- 标签：深度优先搜索、广度优先搜索、图、拓扑排序
- 难度：中等

## 题目链接

- [LCR 113. 课程表 II - 力扣](https://leetcode.cn/problems/QA2IGt/)

## 题目大意

给定一个整数 `numCourses`，代表这学期必须选修的课程数量，课程编号为 `0` 到 `numCourses - 1`。再给定一个数组 `prerequisites` 表示先修课程关系，其中 `prerequisites[i] = [ai, bi]` 表示如果要学习课程 `ai` 则必须要学习课程 `bi`。

要求：返回学完所有课程所安排的学习顺序。如果有多个正确的顺序，只要返回其中一种即可。如果无法完成所有课程，则返回空数组。

## 解题思路

拓扑排序。这道题是「[0207. 课程表](https://leetcode.cn/problems/course-schedule/)」的升级版，只需要在上一题的基础上增加一个答案数组即可。

1. 使用列表 `edges` 存放课程关系图，并统计每门课程节点的入度，存入入度列表 `indegrees`。

2. 借助队列 `queue`，将所有入度为 `0` 的节点入队。

3. 从队列中选择一个节点，并将其加入到答案数组 `res` 中，再让课程数 -1。
4. 将该顶点以及该顶点为出发点的所有边的另一个节点入度 -1。如果入度 -1 后的节点入度不为 `0`，则将其加入队列 `queue`。
5. 重复 3~4 的步骤，直到队列中没有节点。
6. 最后判断剩余课程数是否为 `0`，如果为 `0`，则返回答案数组 `res`，否则，返回空数组。

## 代码

```python
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0 for _ in range(numCourses)]
        edges = collections.defaultdict(list)
        res = []
        for x, y in prerequisites:
            edges[y].append(x)
            indegrees[x] += 1
        queue = collections.deque([])
        for i in range(numCourses):
            if not indegrees[i]:
                queue.append(i)
        while queue:
            y = queue.popleft()
            res.append(y)
            numCourses -= 1
            for x in edges[y]:
                indegrees[x] -= 1
                if not indegrees[x]:
                    queue.append(x)
        if not numCourses:
            return res
        else:
            return []
```

