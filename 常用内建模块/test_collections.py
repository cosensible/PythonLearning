# namedtuple 创建自定义tuple对象
from collections import namedtuple
Point=namedtuple('Point',['x','y'])
p=Point(1,2)
print(p.x,p.y)
print(isinstance(p,tuple))	#Point是tuple的子类

# deque	实现高效插入和删除的双向列表
from collections import deque
q=deque(['a','b','c'])
q.popleft()
q.append('x')
q.appendleft('y')
print(q)

# defaultdict key不存在时返回默认值
from collections import defaultdict
dd=defaultdict(lambda:'no such key')
dd['key1']='abc'
print(dd['key1'],dd['key2'])

# OrderedDict 保持key的顺序
from collections import OrderedDict
od=OrderedDict([('a',1),('b',2),('c',3)])
print(list(od.keys()))

# Counter 统计字符出现的次数
from collections import Counter
c=Counter()
for char in 'programming':
	c[char]=c[char]+1
print(c)