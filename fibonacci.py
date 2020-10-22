def fibonacci(n):
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))
       
def fibonacci_to_sonic(num):
    mydict={0:"Eb3", 1:"E3", 2:"Gb3", 3:"Ab4", 4:"A4", 5:"B4", 6:"Db4", 7:"Eb4", 8:"E4", 9:"Gb4"}    
    notes=[]
    sonic_code=""
    fibonacci_str=""
    for i in range(1,num):
        fibonacci_str+=str(fibonacci((i)))
    for digit in fibonacci_str:
        notes.append(mydict[int(digit)])
    for i in notes:
        sonic_code+="play :"+i+"\n"+"sleep 0.2" + "\n"
    print(sonic_code)    
#run the output in Sonic pi
