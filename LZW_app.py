import json

def primary_index_entry(input_str):
    primary_index_values={}
    key_val=1
    for i in input_str:
        if i not in list(primary_index_values.values()):
            primary_index_values[key_val]=i
            key_val+=1
    with open('compressed_file.json','w')  as f:
        f.write(json.dumps(primary_index_values))
    return primary_index_values

def get_final_index_entry(input_str,initial_LZW_dictionary):
    s_index=0
    e_index=1
    key=len(initial_LZW_dictionary)+1
    e_flag=0
    for i in range(len(input_str)):
        while True: 
            if input_str[s_index:e_index] in list(initial_LZW_dictionary.values()):
                e_index+=1
                if e_index>=len(input_str):
                    e_flag==1
                    break

            else: 
                initial_LZW_dictionary[key]=input_str[s_index:e_index]
                key+=1
                s_index=e_index-1
                break
       
        if e_flag==1:
            break
    #print(initial_LZW_dictionary)
    return initial_LZW_dictionary

def compress_from_dictionary(input_str,start_from,Final_LZW_dictionary):
    final_compressed_val=''
    values=list(Final_LZW_dictionary.values())
    values.append(input_str[-1])
    for i in range(start_from,len(values)):
        if len(values[i])==1:
            to_check=values[i]
        else: 
            to_check=values[i][0:-1]

        encoded_val=[j for j in Final_LZW_dictionary if Final_LZW_dictionary[j]==to_check]
        final_compressed_val+=str(encoded_val[0])
    
    
    print(f'Final Compressed Form: {final_compressed_val}')
    with open('compressed_file.txt','w') as f:
        f.write(final_compressed_val)

    return final_compressed_val

def get_text_from_file(file_name,flag):
    with open(file_name,'r') as f:
        input_str=f.readlines()
    if flag==0:
        return input_str[0]
    else: 
        with open(file_name.replace('.txt','.json'),'r') as f:
            input_dct=json.load(f)
        return input_str[0],input_dct

def LZW_Compress(file_name):
    input_str=get_text_from_file(file_name,0)
    print(f'Initial String: {input_str}')
    initial_LZW_dictionary=primary_index_entry(input_str)
    t_initial_dictionary=initial_LZW_dictionary.copy()
    Final_LZW_dictionary=get_final_index_entry(input_str,t_initial_dictionary)
    compress_from_dictionary(input_str,len(initial_LZW_dictionary),Final_LZW_dictionary)

def decompress(string_val,dictionary_val):
    uncompressed_str=[]
    start_from_val=len(dictionary_val)+1
    partial=''
    for c,i in enumerate(string_val):
        print(i)
        if c==0:
            decode_inst=dictionary_val[i]
            partial=decode_inst
        else: 
            decode_inst=dictionary_val[i]
            print(partial,decode_inst)
            entry=partial+decode_inst[0]
            partial=decode_inst
            dictionary_val[str(start_from_val)]=entry
            start_from_val+=1
        #print(dictionary_val)
        uncompressed_str.append(decode_inst)
    
    uncompressed_str=''.join(uncompressed_str)
    print(uncompressed_str)
    return uncompressed_str
def LZW_Decompress(file):
    input_str,initial_LZW_dictionary=get_text_from_file(file,1)
    uncompressed_txt=decompress(input_str,initial_LZW_dictionary)
    

#LZW_Compress('Initial_File.txt')
LZW_Decompress('compressed_file.txt')