basic_disctionary={1:'a',2:'b',3:'p',4:'l',5:'e'}
index=len(basic_disctionary)
decode=[]
#print(index)
with open('encoded.lzw','rb')as f:
    recieved=f.read()
n=len(recieved)
entry=''
for i in range(n):
    recieved_int=chr(recieved[i])
    recieved_int=int(recieved_int)
    print(recieved_int)
    #print(index)
    #print(partial)
    partial=basic_disctionary[recieved_int]
    decode.append(partial)
    if i==0:
        entry=entry+partial[0]
    else:
        entry=entry+partial[0]
        index=index+1
        basic_disctionary[index]=entry
        entry=partial[0]

print(decode)
n=len(decode)
i=0
decode_text=''
for i in range(n):
    decode_text=decode_text+str(decode[i])
print(decode_text)

with open('dencoded.txt','wb')as f:
    f.write(str.encode(decode_text))
