s = input()
ans = ""

for c in s:
    if c == 'z':
        ans += 'a'
    else:
        ans += chr(ord(c) + 1)

print(ans)