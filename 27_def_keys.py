s = input()
count=1
for i in range(len(s) - 1):
    if s[i]== s[i+1]:
        count+=1
    elif s[i]!=s[i+1]:
        print(s[i] + str(count), end='')
        count=1
print(s[-1:] + str(count))


