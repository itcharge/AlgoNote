# [1603. 设计停车系统](https://leetcode.cn/problems/design-parking-system/)

- 标签：设计、计数、模拟
- 难度：简单

## 题目链接

- [1603. 设计停车系统 - 力扣](https://leetcode.cn/problems/design-parking-system/)

## 题目大意

给一个停车场设计一个停车系统。停车场总共有三种尺寸的车位：大、中、小，每种尺寸的车位分别有固定数目。

现在要求实现 `ParkingSystem` 类：

-  `ParkingSystem(big, medium, small)`：初始化 ParkingSystem 类，三个参数分别对应三种尺寸车位的数目。
- `addCar(carType) -> bool:`：检测是否有 `carType` 对应的停车位，如果有，则将车停入车位，并返回 `True`，否则返回 `False`。

## 解题思路

使用不同成员变量存放车位数目。并根据给定操作进行判断。

## 代码

```python
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.park = [0, big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.park[carType] == 0:
            return False
        self.park[carType] -= 1
        return True
```

