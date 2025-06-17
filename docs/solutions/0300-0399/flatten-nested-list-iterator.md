# [0341. 扁平化嵌套列表迭代器](https://leetcode.cn/problems/flatten-nested-list-iterator/)

- 标签：栈、树、深度优先搜索、设计、队列、迭代器
- 难度：中等

## 题目链接

- [0341. 扁平化嵌套列表迭代器 - 力扣](https://leetcode.cn/problems/flatten-nested-list-iterator/)

## 题目大意

给定一个嵌套的整数列表 `nestedList` 。列表中元素类型为 NestedInteger 类。每个元素（NestedInteger 对象）要么是一个整数，要么是一个列表；该列表的元素也可能是整数或者是其他列表。

NestedInteger 类提供了三个方法：

- `isInteger()`，判断当前存储的对象是否为 int；
- `getInteger()` ，如果当前存储的元素是 int 型的，那么返回当前的结果 int，否则调用会失败；
- `getList()`，如果当前存储的元素是 `List<NestedInteger>` 型的，那么返回该 List，否则调用会失败。

要求：实现一个迭代器将其扁平化，使之能够遍历这个列表中的所有整数。

实现扁平迭代器类 NestedIterator：

- `NestedIterator(List<NestedInteger> nestedList)` 用嵌套列表 `nestedList` 初始化迭代器。
- `int next()` 返回嵌套列表的下一个整数。
- `boolean hasNext()` 如果仍然存在待迭代的整数，返回 `True`；否则，返回 `False`。

## 解题思路

初始化时不对元素进行预处理。而是将所有的 `NestedInteger` 逆序放到栈中，当需要展开的时候才进行展开。

## 代码

```python
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        size = len(nestedList)
        for i in range(size - 1, -1, -1):
            self.stack.append(nestedList[i])
        
    
    def next(self) -> int:
        cur = self.stack.pop()
        return cur.getInteger()
        
    
    def hasNext(self) -> bool:
        while self.stack:
            cur = self.stack[-1]
            if cur.isInteger():
                return True
            self.stack.pop()
            for i in range(len(cur.getList()) - 1, -1, -1):
                self.stack.append(cur.getList()[i])
        return False
```

