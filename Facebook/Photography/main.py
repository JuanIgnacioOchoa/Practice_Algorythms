def getArtisticPhotographCount(A, B):
  # Write your code here
  As = str(A)
  Bs = str(B)
  diff = len(Bs) - len(As) - 1
  ans = 0
  if diff > 0:
    ans += diff * 9
  print(ans)
  if len(Bs) != len(As):
    print('A')
    x = len(As)
    while x + 1 != len(str(A)):
      print(A)
      ans+=1
      A += int('1' * x)
    x = len(Bs)
    while x - 1 != len(str(B)):
      print(B)
      ans+=1
      B -= int('1' * x)
  else:
    while A <= B:
      if not A % int('1' * len(str(A))):
        ans += 1
      A += 1
  return ans

getArtisticPhotographCount(75,300)