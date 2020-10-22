def primes(n):
    primes_str ="2"
    for num in range(3, n+1, 2):
        if all(num % i != 0 for i in range(2, int(num**.5 ) + 1)):
            primes_str+=str(num)
    return primes_str

def primes_to_sonic(num):
    mydict={0:"Eb3", 1:"E3", 2:"Gb3", 3:"Ab4", 4:"A4", 5:"B4", 6:"Db4", 7:"Eb4", 8:"E4", 9:"Gb4"}    
    notes=[]
    sonic_code=""
    for i in primes(num):
        notes.append(mydict[int(i)])
    for i in notes:
        sonic_code+="play :"+i+"\n"+"sleep 0.2" + "\n"
    print(sonic_code) 
#run the output in Sonic pi     
