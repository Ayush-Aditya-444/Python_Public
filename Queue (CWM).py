from collections import deque


queue=deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.appendleft(1)
queue.appendleft(3)
print(queue)
print(*queue)
queue.pop()
queue.popleft()
print(queue)
queue.popleft()
queue.popleft()
queue.popleft()
queue.popleft()
print(queue)
if not queue:
    print("Empty Queue")
