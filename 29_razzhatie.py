
f = open('dataset_3363_2.txt', 'r')
result = list(f.read())
f.close()
res = []
integ = []
l = len(result)

for i in result:
   if i.isdigit() == False:
        res += i

i = 0
while i < l:
    s_int = ''
    a = result[i]
    while '0' <= a <= '9':
        s_int += a
        i += 1
        if i < l:
            a = result[i]
        else:
            break
    i += 1
    if s_int != '':
        integ.append(int(s_int))

answer=[]
answer = [res[i]*integ[i] for i in range(len(res)-1)]
myString = ''.join(answer)
f1 = open('answer.txt', 'w')
f1.write(myString)
f1.close()