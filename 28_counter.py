from collections import Counter
s = input().lower().split()
cnt = Counter()
for word in s:
    cnt[word]+=1
for key, value in cnt.items():
    print(key, value, end=' ')
