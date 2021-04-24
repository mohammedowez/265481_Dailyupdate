
n = int(input())
result = []
for _ in range(n):
    s = input().split(' ')
    command = s[0]
    if command == 'print':
        print (result)
        continue

    ar = map(int, s[1:])
    getattr(result, command)(*ar)
