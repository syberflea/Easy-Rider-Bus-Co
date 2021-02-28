passwords = input().split()

passwords.sort(key=len)
for each in passwords:
    print(each, len(each), sep=" ")
