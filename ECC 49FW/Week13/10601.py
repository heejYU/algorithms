# 백준 10601 30
N = input()
check_zero = False
result = 0
sum = 0

for i in range(len(N)):
    sum += int(N[i])
    if N[i] == '0':
        check_zero = True
    
if sum % 3 == 0 and check_zero == True:
    result = ''.join(sorted(N, reverse=True))
else:
    result = -1

print(result)