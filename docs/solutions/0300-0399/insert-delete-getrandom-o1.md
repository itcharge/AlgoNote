# [0380. 常数时间插入、删除和获取随机元素](https://leetcode.cn/problems/insert-delete-getrandom-o1/)

- 标签：设计、数组、哈希表、数学、随机化
- 难度：中等

## 题目链接

- [0380. 常数时间插入、删除和获取随机元素 - 力扣](https://leetcode.cn/problems/insert-delete-getrandom-o1/)

## 题目大意

设计一个数据结构 ，支持时间复杂度为 O(1) 的以下操作：

- insert(val)：当元素 val 不存在时，向集合中插入该项。
- remove(val)：元素 val 存在时，从集合中移除该项。
- getRandom：随机返回现有集合中的一项。每个元素应该有相同的概率被返回。

## 解题思路

普通动态数组进行访问操作，需要线性时间查找解决。我们可以利用哈希表记录下每个元素的下标，这样在访问时可以做到常数时间内访问元素了。对应的插入、删除、后去随机元素需要做相应的变化。

- 插入操作：将元素直接插入到数组尾部，并用哈希表记录插入元素的下标位置。
- 删除操作：使用哈希表找到待删除元素所在位置，将其与数组末尾位置元素相互交换，更新哈希表中交换后元素的下标值，并将末尾元素删除。
- 获取随机元素：使用` random.choice` 获取。

## 代码

```python
import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = dict()
        self.list = list()


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dict:
            idx = self.dict[val]
            last = self.list[-1]
            self.list[idx] = last
            self.dict[last] = idx
            self.list.pop()
            self.dict.pop(val)
            return True
        return False


    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.list)
```

