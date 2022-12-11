num = [1,2,3,4,5,6,7,8,9]
print(len(num))
#now we print array sum
print(sum(num))
result = 0
for i in range (0,len(num)+1):
    result = i + result
r = [num[i+1]+num[i] for i in range(8)]










print(r)

