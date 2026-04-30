from collections import Counter,defaultdict,namedtuple,deque
# counter
nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
counter = Counter(nums)
print(counter)

# defaultdict
d = defaultdict(int)
print(d)
d['key1'] += 1
d['key2'] = "Hello"
print(d)

# namedtuple
Point = namedtuple('Point', ['x', 'y'])
p1 = Point(1, 2)
print(p1)

# deque
q = deque([1, 2, 3, 4, 5])
q.append(6)
print(f'After append(6): {q}')
q.appendleft(0)
print(f'After appendleft(0): {q}')
q.pop()
print(f'After pop(): {q}')
q.popleft()
print(f'After popleft(): {q}')