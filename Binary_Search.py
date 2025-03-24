def is_possible(A, n, p, max_time):
  painters.current_time = 1,0
  for length in A:
    if current_time+length>max_time:
      painters += 1
      current_time = 0
      if painters > p:
        return False
      current_time += length
  return True
      
def min_time_to_paint(n, p, A):
  low, high = max(A), sum(A)
  while low < high:
    mid = (low+high) // 2
    if is_possible(A,n,p, mid):
      high = mid
    else:
      low = mid + 1
  return low
  
t = int(input())
for _ in range(t):
  n,p = map(int, input().split())
  A = list(map(int, input().split()))
  print(min_time_to_paint(n,p,A))