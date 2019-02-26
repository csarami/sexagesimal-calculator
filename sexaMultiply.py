def scalar60(mult, s):
    res = []
    n = len(s); t60 = 0;
    for i in range(len(s)):     
        temp = mult*s[n-i-1]
        res = [t60 + temp % 60]+ res
        t60 = temp // 60
        if  i== n-1:
            res = [t60]+ res
    return res



#print(scalar60(41,[37,11,7]))
p = [37,11,7]; q = [16,13,41]
x= scalar60(41,[0,0,37,11,7])
y = scalar60(13,[0,37,11,7,0])
z = scalar60(16,[37,11,7,0,0])
print(x,y,z)
prod = list(map(sum, zip(x,y,z)))
print(prod)
def LD(a):
    return (a//60, a%60)


def convert2Dec(s):
    d = 0
    for i in range(len(s)):
        d += s[i]*60**(len(s)-1-i)
    return d

print(convert2Dec( prod) == convert2Dec(p)*convert2Dec(q))

'''
def simpleMult60(mult,s):
    n = len(s)
    for i in range(len(s)):     
        s[i] = mult*s[i]
    return s

simpleMult60(41,[37,11,7]))


'''

def sum60(A, B):
    if len(A) != len(B):
        print('inputs must have same length')
        return
    else:
        res = len(A)*[0]
        carry = 0
        for i in range(len(A)-1,-1,-1):
              res[i] = (A[i]+B[i]) % 60 + carry
              carry = (A[i]+B[i])// 60
        if carry > 0:
              res = [carry] + res
    return res

print(sum60([12,31],[50,50]) == [1, 3, 21])

def sum60Array(arrOfArrays):
    N = len(arrOfArrays[0])
    res = arrOfArrays[0]
    for i in range(1, len(arrOfArrays)):
                   if len(arrOfArrays[i]) != N:
                       print('arrays must have same length')
                   res = sum60(res, arrOfArrays[i])
    return res

print(sum60Array([x,y,z]))
                   
    
def sexaMultiply(A,B):
    res = len(B)*[(len(A)+len(B))*[0]]
    for i in range(len(B)):
        res[i] = (len(B)-i)*[0] + scalar60(B[len(B)-i-1],A) + i*[0]
    return sum60Array(res)

def sexaMultiplyShowWork(A,B):
    res = len(B)*[(len(A)+len(B))*[0]]
    for i in range(len(B)):
        res[i] = (len(B)-i)*[0] + scalar60(B[len(B)-i-1],A) + i*[0]
        print(res[i])
    return sum60Array(res)

# Example        
print(sexaMultiply([10,30,40], [1,20]))      
                   
# 37 ; 11 ,  7 times  6 ,  13 ; 41 th              
print('///////'*5)
print(sexaMultiplyShowWork([37,11,7], [6,13,41]))               
