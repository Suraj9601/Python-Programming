# input = 'abcaba'
# output = 'a-bb-ccc-a-bb-a'

string = 'abcaba'
print('Original String : ',string)
ch_idx = {}
ch_list = []

for i,ch in enumerate(string, start=1):
    if ch not in ch_idx:
        ch_idx[ch] = i
    ch_list.append(ch * ch_idx[ch])


result = '-'.join(ch_list)
print('Output String : ',result)