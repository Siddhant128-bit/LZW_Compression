dictionary_init={1:'a',2:'b',3:'p',4:'l',5:'e'}
initial_length=len(dictionary_init)
encode=[]
flag=0
with open('checking.txt','rb')as f:
    bytes=f.read()
n1=len(bytes)
t=chr(bytes[0])
i=1

for i in range(1,n1):
    x=chr(bytes[i])
    #print(x)
    #print(i,' ',x)
    count=0
    n_d=len(dictionary_init)
    for j in range(1,n_d+1):
        if t==dictionary_init[j]:
            t=t+x
            #print(t)
            count=count+1
    if count<2:
        dictionary_init[n_d+1]=t
        t=x
    #print(count)



final_length=len(dictionary_init)
#print(initial_length,' ',final_length)

last_numb=dictionary_init[final_length]
print(dictionary_init)
for i in range(initial_length+1,final_length+1):
    word=dictionary_init[i]
    t=''
    for j in range(len(word)-1):
        t=t+word[j]
        #print(t)
    for index in dictionary_init:
        if t==dictionary_init[index]:
            encode.append(index)

last_char=dictionary_init[final_length]
last_char=last_char[len(last_char)-1]
print(last_char)
for index in dictionary_init:
    if last_char==dictionary_init[index]:
        encode.append(index)


n=len(encode)
i=0
encode_text=''
for i in range(n):
    encode_text=encode_text+ str(encode[i])
print(encode_text)

with open('encoded.lzw','wb')as f:
    f.write(str.encode(encode_text))
