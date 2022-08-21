# Python code used solve the cipher
#gcd using Euclid's Algorithm
def gcd(a,b): 
  
    if(b == 0): 
        return a 
    else: 
        return gcd(b, a % b) 
      
# To calculate a^q taking p mod 
def mod_power(a,q,p): 
  
    if (q == 0): 
        return 1
    c = mod_power(a, q // 2, p) % p 
    c = (c * c) % p 
    return c if(q % 2 == 0) else  (a * c) % p 
  
# To find inverse of a under modulo p(prime)
def find_inverse(a,p): 
  
    if (gcd(a, p) != 1): #A condition in Fermat's theorem
        print("Invalid argument") 
   
    else: 
   
        return mod_power(a, p - 2, p) 

# To find g              
def find_g(a,k1,b,k2,p):
    if(a == 1):
        return k1
    
    k2 = (find_inverse(k1,p)*k2)%p
    b = b-a
    
    if(a<=b):
        return find_g(a,k1,b,k2,p)
    else:
        return find_g(b,k2,a,k1,p)
  
# Driver code 
  
y1 = 11226815350263531814963336315
y2 = 9190548667900274300830391220
y3 = 4138652629655613570819000497
p = 19807040628566084398385987581

k1 = (find_inverse(y1,p)*y2)%p
k2 = (find_inverse(y2,p)*y3)%p

a = 2021
b = 7168

g = find_g(a,k1,b,k2,p)
print("Value of g is",g)

g324 = mod_power(g,324,p)
x = (find_inverse(g324,p)*y1)%p
print("Password is",x)