# 线段树的节点类
class SegTreeNode:
    def __init__(self, left=-1, right=-1, val=False, lazy_tag=None, leftNode=None, rightNode=None):
        self.left = left                            # 区间左边界
        self.right = right                          # 区间右边界
        self.mid = left + (right - left) // 2
        self.leftNode = leftNode                    # 区间左节点
        self.rightNode = rightNode                  # 区间右节点
        self.val = val                              # 节点值（区间值）
        self.lazy_tag = lazy_tag                    # 区间问题的延迟更新标记
        
        
# 线段树类
class SegmentTree:
    # 初始化线段树接口
    def __init__(self, function):
        self.tree = SegTreeNode(0, int(1e9))
        self.function = function                    # function 是一个函数，左右区间的聚合方法
    
    # 单点更新接口：将 nums[i] 更改为 val
    def update_point(self, i, val):
        self.__update_point(i, val, self.tree)
    
    # 区间更新接口：将区间为 [q_left, q_right] 上的元素值修改为 val
    def update_interval(self, q_left, q_right, val):
        self.__update_interval(q_left, q_right, val, self.tree)
    
    # 区间查询接口：查询区间为 [q_left, q_right] 的区间值
    def query_interval(self, q_left, q_right):
        return self.__query_interval(q_left, q_right, self.tree)
    
    # 获取 nums 数组接口：返回 nums 数组
    def get_nums(self, length):
        nums = [0 for _ in range(length)]
        for i in range(length):
            nums[i] = self.query_interval(i, i)
        return nums
            
    
    # 以下为内部实现方法
    
    # 单点更新实现方法：将 nums[i] 更改为 val。node 节点的区间为 [node.left, node.right]
    def __update_point(self, i, val, node):
        if node.left == node.right:
            node.val = val                          # 叶子节点，节点值修改为 val
            return
        
        if i <= node.mid:                           # 在左子树中更新节点值
            self.__update_point(i, val, node.leftNode)
        else:                                       # 在右子树中更新节点值
            self.__update_point(i, val, node.rightNode)
        self.__pushup(node)                         # 向上更新节点的区间值
        
    # 区间更新实现方法
    def __update_interval(self, q_left, q_right, val, node):
        if node.left >= q_left and node.right <= q_right:  # 节点所在区间被 [q_left, q_right] 所覆盖
            node.lazy_tag = val                     # 将当前节点的延迟标记增加 val
            interval_size = (node.right - node.left + 1)    # 当前节点所在区间大小
            node.val = val * interval_size          # 当前节点所在区间每个元素值改为 val
            return
        if node.right < q_left or node.left > q_right:  # 节点所在区间与 [q_left, q_right] 无关
            return
    
        self.__pushdown(node)                       # 向下更新节点所在区间的左右子节点的值和懒惰标记
    
        if q_left <= node.mid:                      # 在左子树中更新区间值
            self.__update_interval(q_left, q_right, val, node.leftNode)
        if q_right > node.mid:                      # 在右子树中更新区间值
            self.__update_interval(q_left, q_right, val, node.rightNode)
            
        self.__pushup(node)
    
    # 区间查询实现方法：在线段树的 [left, right] 区间范围中搜索区间为 [q_left, q_right] 的区间值
    def __query_interval(self, q_left, q_right, node):
        if node.left >= q_left and node.right <= q_right:   # 节点所在区间被 [q_left, q_right] 所覆盖
            return node.val                         # 直接返回节点值
        if node.right < q_left or node.left > q_right:  # 节点所在区间与 [q_left, q_right] 无关
            return 0
                                  
        self.__pushdown(node)                       # 向下更新节点所在区间的左右子节点的值和懒惰标记
        
        res_left = 0                                # 左子树查询结果
        res_right = 0                               # 右子树查询结果
        if q_left <= node.mid:                      # 在左子树中查询
            res_left = self.__query_interval(q_left, q_right, node.leftNode)
        if q_right > node.mid:                      # 在右子树中查询
            res_right = self.__query_interval(q_left, q_right, node.rightNode)
        return self.function(res_left, res_right)   # 返回左右子树元素值的聚合计算结果
    
    # 向上更新实现方法：更新 node 节点区间值 等于 该节点左右子节点元素值的聚合计算结果
    def __pushup(self, node):
        if node.leftNode and node.rightNode:
            node.val = self.function(node.leftNode.val, node.rightNode.val)
            
    # 向下更新实现方法：更新 node 节点所在区间的左右子节点的值和懒惰标记
    def __pushdown(self, node):
        if node.leftNode is None:
            node.leftNode = SegTreeNode(node.left, node.mid)
        if node.rightNode is None:
            node.rightNode = SegTreeNode(node.mid + 1, node.right)
            
        lazy_tag = node.lazy_tag
        if node.lazy_tag is None:
            return
            
        node.leftNode.lazy_tag = lazy_tag           # 更新左子节点懒惰标记
        left_size = (node.leftNode.right - node.leftNode.left + 1)
        node.leftNode.val = lazy_tag * left_size    # 更新左子节点值
        
        node.rightNode.lazy_tag = lazy_tag          # 更新右子节点懒惰标记
        right_size = (node.rightNode.right - node.rightNode.left + 1)
        node.rightNode.val = lazy_tag * right_size  # 更新右子节点值
        
        node.lazy_tag = None                        # 更新当前节点的懒惰标记

# 线段树使用方法
class Solution:
    # 初始化线段树
    def __init__(self):
        self.STree = SegmentTree(lambda x, y: x + y)
        
    # 将区间 [left, right] 上的元素值全部修改为 val
    def update(self, left: int, right: int, val) -> None:
        self.STree.update_interval(left, right, val)
        
    # 查询区间 [left, right] 的区间值
    def sumRange(self, left: int, right: int) -> int:
        return self.STree.query_interval(left, right)