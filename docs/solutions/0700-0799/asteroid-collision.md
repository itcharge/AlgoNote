# [0735. 小行星碰撞](https://leetcode.cn/problems/asteroid-collision/)

- 标签：栈、数组
- 难度：中等

## 题目链接

- [0735. 小行星碰撞 - 力扣](https://leetcode.cn/problems/asteroid-collision/)

## 题目大意

给定一个整数数组 `asteroids`，表示在同一行的小行星。

数组中的每一个元素，其绝对值表示小行星的大小，正负表示小行星的移动方向（正表示向右移动，负表示向左移动）。每一颗小行星以相同的速度移动。小行星按照下面的规则发生碰撞。

-  碰撞规则：两个行星相互碰撞，较小的行星会爆炸。如果两颗行星大小相同，则两颗行星都会爆炸。两颗移动方向相同的行星，永远不会发生碰撞。

要求：找出碰撞后剩下的所有小行星，将答案存入数组并返回。

## 解题思路

用栈模拟小行星碰撞，具体步骤如下：

- 遍历数组 `asteroids`。
- 如果栈为空或者当前元素 `asteroid` 为正数，将其压入栈。
- 如果当前栈不为空并且当前元素 `asteroid` 为负数：
  - 与栈中元素发生碰撞，判断当前元素和栈顶元素的大小和方向，如果栈顶元素为正数，并且当前元素的绝对值大于栈顶元素，则将栈顶元素弹出，并继续与栈中元素发生碰撞。
  - 碰撞完之后，如果栈为空并且栈顶元素为负数，则将当前元素 `asteroid` 压入栈，表示碰撞完剩下了 `asteroid`。
  - 如果栈顶元素恰好与当前元素值大小相等、方向相反，则弹出栈顶元素，表示碰撞完两者都爆炸了。
- 最后返回栈作为答案。

## 代码

```python
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if not stack or asteroid > 0:
                stack.append(asteroid)
            else:
                while stack and 0 < stack[-1] < -asteroid:
                    stack.pop()
                if not stack or stack[-1] < 0:
                    stack.append(asteroid)
                elif stack[-1] == -asteroid:
                    stack.pop()

        return stack
```

