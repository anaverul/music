def catalan(n): 
    if n <=1 : 
        return 1 
    res = 0 
    for i in range(n): 
        res += catalan(i) * catalan(n-i-1) 
  
    return res

def catalan_to_sonic(num):
    int_note_dict={0:"Eb3", 1:"E3", 2:"Gb3", 3:"Ab4", 4:"A4", 5:"B4", 6:"Db4", 7:"Eb4", 8:"E4", 9:"Gb4"}    
    catalan_str=""
    notes_list=[]
    sonic_code=""
    for i in range(num):
        catalan_str+=(str(catalan(i)))
    for digit in catalan_str:
        notes_list.append(int_note_dict[int(digit)])
    for i in notes_list:
        sonic_code+="play :"+i+"\n"+"sleep 0.2" + "\n"
    print(sonic_code)   
#run the output in Sonic pi