''' x = int(input('Enter an integer: '))
ans = 0
while ans**3 < abs(x):
 ans = ans + 1
# print(x, 'is a cube root.')
if ans**3 != abs(x):
    print(x, 'is not a perfect cube')
else:
  if x < 0:
    ans = -ans
    print('Cube root of', x, 'is', ans)
  else:
    # ans = ans
    print('cube root of', x, 'is', ans)'''

'''x = 4
for j in range(x):
  # for k in range(x):
  print(j)
  x = 2'''

'''# sum of FLOAT
s = duble('1.23,2.4,3.123')
x=s[0]+s[1]+s[2]
print(x)'''

print('My favorite professor--John G.--rocks'.split(' '))
print('My favorite professor--John G.--rocks'.split('-'))
print('My favorite professor--John G.--rocks'.split('--'))
x = 25
epsilon = 0.01
numGuesses = 0
low: float = 0.0
high = max(1.0, x)
ans: float = (high + low)/ 2.0
while abs(ans**2 - x) >= epsilon:
  numGuesses += 1
  if ans**2 < x:
      low = ans
  else:
     high = ans
     ans = (high + low)/ 2.0
print('numGuesses =' + numGuesses)
print(ans, 'is close to square root of', x)
