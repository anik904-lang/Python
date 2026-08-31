def normalize(s):
    result = ""

    for c in s:
        c = c.lower()

        if c == 'o' or c == '0':
            result += '0'
        elif c == '1' or c == 'l' or c == 'i':
            result += '1'
        else:
            result += c

    return result


s = normalize(input())

n = int(input())

found = False

for i in range(n):
    login = normalize(input())

    if login == s:
        found = True

if found:
    print("No")
else:
    print("Yes")