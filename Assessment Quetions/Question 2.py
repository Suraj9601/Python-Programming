q = [255, 543, 854 , 123, 150]
p = [101, 205, 225, 315, 512]


pq = dict(zip(q,p))


result = ''.join(str(i)+str(j) for i,j in pq.items())
print(result)