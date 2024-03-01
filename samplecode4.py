i = 100
str = 'this is'
print(str,'apple', i, 0.123, sep='-')
# this is-apple-100-0.123

print(str,'apple', i, 0.123, sep='\n')
# apple
# 100
# 0.123 

list2 = [1,2,3,4]

print(*list2, sep='')
# 1234

print(*list2, sep='-')
# 1-2-3-4