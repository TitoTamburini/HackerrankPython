
#Python If-Else
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if(n%2!=0):
        print("Weird")
    else:
        if ( n>=2 and n<=5):
            print("Not Weird")
        elif(n>=6 and n<=20):
            print("Weird")
        elif(n>20):
            print("Not Weird")


#Say "Hello, World!" With Python
if __name__ == '__main__':
    print("Hello, World!")

#Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a + b)
    print(a-b)
    print(a*b)

#Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)

#Loops
if __name__ == '__main__':
    n = int(input())
    for i in range(0,n):
        print(i**2)





#Write a function
def is_leap(year):
    leap = False
    if(year%4==0 and year%100!=0):
        leap = True
    elif(year%4==0 and year%100==0 and year%400==0):
        leap =  True
    return leap


#Print Function
if __name__ == '__main__':
    n = int(input())
    x =""
    for i in range(1,n+1):
         x += str(i)
    print(x)
    

#List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    mylist  = [[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) ]
    newlist  = [ elem for elem in mylist if elem[0]+elem[1]+elem[2 ]!=n]
    print(newlist)


#Find the Runner-Up Score!  
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    oldmax = max(arr)
    arr.remove(max(arr))
    newmax = max(arr)
    while(newmax == oldmax):
        arr.remove(max(arr))
        newmax = max(arr)
    print(newmax)








#Nested Lists
if __name__ == '__main__':
    mylist= list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        mylist.append([name,score])
    oldmin = min(x[1] for x in mylist)
    "print(oldmin)"
    mylist = [ x for x in mylist if x[1] > oldmin]
    newmin  = min(x[1] for x in mylist)
    "print(newmin)"
    output = [ x[0] for x in mylist if x[1] == newmin]
    output.sort()
    for elem in output : 
        print(elem)

#Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    marks = [x for x in student_marks[query_name]]
    output = 0
    for mark in marks:
        output+=mark
    print("{:.2f}".format(output/3))

#sWAP cASE
def swap_case(s):
    output =""
    for char in s:
        if( char.islower()):
            output += char.upper()
        else:
            output += char.lower()
    return output


#String Split and Join


def split_and_join(line):
    output=""
    mylist  = line.split()
    output += mylist[0]
    for i in range(1,len(mylist)):
        output+= "-"+mylist[i]
    return output

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

#Lists
    
if __name__ == '__main__':
    N = int(input())
    i=0
    commands =[]
    output  = []
    while i <N:
        commands.append(str(input()))
        i+=1
    for line in commands:
        command = line.split()
        if(command[0] == "insert"):
            output.insert(int(command[1]),int(command[2]))
        elif(command[0]=="print"):
            print(output)
        elif(command[0] == "remove"):
            output.remove(int(command[1]))
        elif(command[0] == "append"):
            output.append(int(command[1]))
        elif(command[0] == "sort"):
            output.sort()
        elif(command[0] == "pop"):
            output.pop(len(output)-1)
        elif(command[0]=="reverse"):
            output.reverse()
        else:
            print("command not valid")
    
                

#Tuples 
if __name__ == '__main__':
    n = int(input())
    integer_list = list(map(int, input().split()))
    t = tuple(integer_list)
    print(hash(t))

#What's Your Name?
#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    print("Hello "+first+" " + last +"! You just delved into python.")


#Mutations
def mutate_string(string, position, character):
    output=""
    for i in range(0,len(string)):
        if( i == position):
            output+=character
        else:
            output += string[i]
    return output


#Find a string
def count_substring(string, sub_string):
    i=0
    j=0
    count = 0
    while  i < len(string):
        if( string[i] == sub_string[j]):
            j+=1
            if(j == len(sub_string)):
                count+=1
                j=0
            if( string[i] == sub_string[0]):
                continue
        i+=1
                
        
            
    return count


#String Validators
def anyalnum(s):
    for char in s:
        if(char.isalnum()):
            return True
    return False

def anyalpha(s):
    for char in s:
        if(char.isalpha()):
            return True
    return False

def anydigit(s):
    for char in s:
        if(char.isdigit()):
            return True
    return False

def anylower(s):
    for char in s:
        if(char.islower()):
            return True
    return False

def anyupper(s):
    for char in s:
        if(char.isupper()):
            return True
    return False

    
if __name__ == '__main__':
    s = input()
    print(anyalnum(s))
    print(anyalpha(s))
    print(anydigit(s))
    print(anylower(s))
    print(anyupper(s))
    

#Text Alignment
#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

#Text Wrap


def wrap(string, max_width):
    output=[]
    i=0
    cnt=0
    elem=""
    while i <len(string):
        if(cnt == max_width):
            cnt=0
            elem += "\n"
        elem += string[i]
        cnt+=1
        i+=1
    return elem



#String Formatting
def print_formatted(number):
    lens = len(str(bin(number)))-2
    for i in range(1,n+1):
        output=[]
        dec = i
        octal = tooctal(i,"")
        hexadecimal = tohexal(i,"")
        binary = tobin(i,"")
        output.append(str(dec))
        output.append(str(octal))
        output.append(str(hexadecimal))
        output.append(str(binary))
        #print("  ".join(output))
        #print(dec.rjust(lens," "),octal.rjust(lens," "),hexadecimal.rjust(lens," "),binary.rjust(lens," "))
        print("{0:>{l}} {1:>{l}} {2:>{l}} {3:>{l}}".format(dec,octal,hexadecimal,binary,l=lens))
        
        
def tooctal(n,result):
    if(n<8):
        return   str(n)+result
    else:
        string = str(n%8)+result
        return tooctal(n//8,string)
    
def tohexal(n,result):
    if(n<16):
        return toletter(n) + result
    else:
        string = toletter(n%16) +result
        return tohexal(n//16,string)
    
def toletter(n):
    if(n==10):
        return "A"
    elif(n==11):
        return "B"
    elif(n==12):
        return "C"
    elif(n==13):
        return "D"
    elif(n==14):
        return "E"
    elif(n==15):
        return "F"
    else:
        return str(n)
        

def tobin(n,result):
    if(n<2):
        return str(n)+result
    else:
        string  = str(n%2) +result
        return tobin(n//2,string)


#Designer Door Mat
# Enter your code here. Read input from STDIN. Print output to STDOUT
stdin = input().split()
N  = int(stdin[0])
M  = int(stdin[1])
mat=""
for i in range(0,N//2):
    string =".|."*((2*(i+1)-1))
    print(string.center(M,"-"))

print("-"*((M-7)//2)+"WELCOME" + "-"*((M-7)//2))

for i in range(0,N//2):
    h = N//2-i
    string = ".|."*((2*h)-1)
    print(string.center(M,"-"))


#Alphabet Rangoli
def print_rangoli(size):
    j=1
    if(size==1):
        print("a")
    else:
        for i in range(0,size):
            string=""
            idx = (((size*2)-1)*2)-1
            for k in range(0,j):
                string += chr(96+size-k)+"-"
            rev  = string[::-1]
            string += rev[3:]
            print(string.center(idx,"-"))
            j+=1
        j=size
        for i in range(size,1,-1):
            string = ""
            idx = (((size*2)-1)*2)-1
            for k in range(1,j):
                string += chr(96+size-k+1)+"-"
            rev  = string[::-1]
            string += rev[3:]
            print(string.center(idx,"-"))
            j-=1
            
            #print(string.center(idx,"-"))
    



#Capitalize!


# Complete the solve function below.
def solve(s):
    mylist = s.split()
    string=""
    for i in range(0,len(s)):
        if( i==0 and s[i].isalpha()):
            string += s[i].upper()
        elif (s[i-1]==" " and s[i].isalpha()) :
            string += s[i].upper()
        else:
            string += s[i]
    return string
            
    ##for name in mylist:
    #    for i in range(0,len(name)):
    #       if(i==0 and name[i].isalpha()):
    #           string+= name[0].upper()
    #       else:
    #           string+= name[i]
    #   string += " "
        





#The Minion Game
def minion_game(string):
    player1 = 0
    player2 =0 
    len_s = len(string)
    for char in string:
        if(isVowel(char)==True):
            player2 += len_s
        else:
            player1 += len_s
        len_s-=1
    if(player1>player2):
        print("Stuart "+str(player1))
    elif(player1<player2): 
         print("Kevin "+str(player2))      
    else:
        print("Draw")

def isVowel(char):
    if("AEIOU".find(char)>-1):
        return True
    return False



#Merge the Tools!
def merge_the_tools(string, k):
    # your code goes here
    i=0
    cnt = 0
    substrings = []
    while(cnt< len(string)/k):
        elem = string[i:i+k]
        substrings.append(elem)
        cnt +=1
        i+=k
    for sub in substrings:
        elem =""
        for c in sub:
            if(elem.find(c)<0):
               elem += c 
        print(elem)       
                
    



#Introduction to Sets
def average(array):
    
    myset = set(array)
    n = len(myset)
    output  = 0
    for elem in myset:
        output += elem
    return  str(output/n)
    # your code goes here


#Symmetric Difference
# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
M = set(list(map(int,input().split())))
n = int(input())
N = set(list(map(int,input().split())))
result = (M.union(N)).difference(N.intersection(M))
mylist = [x for x in result]
mylist.sort()
for x in mylist:
    print(x)



#No Idea!
# Enter your code here. Read input from STDIN. Print output to STDOUT
def contains(myset,elem):
    for x in myset:
        if(x==elem):
            return True
    return False

dimensions = list(map(int,input().split()))
array_list = list(map(int,input().split()))
A = set( list(map(int,input().split())))
B = set( list(map(int,input().split())))
happiness = 0
for elem in array_list:
    if elem in A:
        happiness +=1
    elif elem in B:
        happiness -=1
print(happiness)

#Set .add() 
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
result = set()
for i in range(0,n):
    result.add(input())

print(len(result))





#Set .discard(), .remove() & .pop()
size = int(input())
s = set(map(int, input().split()))
n = int(input())
command = list()
for i in range(0,n):
    string   = input().split()
    command.append(string)

for c in command:
    #if len(c) > 1:
    #  print(c[0],c[1])
    #print(c[0])
    if(c[0] == "pop"):
        s.pop()
    elif(c[0]=="remove"):
        s.remove(int(c[1]))
        
    elif(c[0]=="discard"):
        s.discard(int(c[1]))
    else:
        continue
l = 0
for n in s:
    l += n
print(l)
    

#Set .intersection() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
eng = int(input())
english =  set(list(map(int,input().split())))
fr  = int(input())
french = set(list(map(int,input().split())))
print(len(english.intersection(french)))



#Set .difference() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
eng  = int(input())
english = set(list(map(int,input().split())))
fr = int(input())
french = set(list(map(int,input().split())))

inters = english.intersection(french)
print(len(english.difference(inters)))

#Set .symmetric_difference() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
eng  = int(input())
english = set(list(map(int,input().split())))
fr = int(input())
french = set(list(map(int,input().split())))
print(len(english.symmetric_difference(french)))

#Set Mutations
# Enter your code here. Read input from STDIN. Print output to STDOUT
n  = int(input())
N = set(list(map(int,input().split())))
number_sets = int(input())
commands = list()
for i in range(0,number_sets):
    commands= input().split()
    op_set = set(list(map(int,input().split())))
    if( commands[0] == "intersection_update"):
        N.intersection_update(op_set)
    elif(commands[0] == "update"):
        N.update(op_set)
    elif(commands[0] == "symmetric_difference_update"):
        N.symmetric_difference_update(op_set)
    elif(commands[0] == "difference_update"):
        N.difference_update(op_set)
    else:
        print("Command not valid")
sum_N = 0
for elem in N:
    sum_N += elem
print(sum_N)
        






#The Captain's Room 
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
k = int(input())
input_list = list(map(int,input().split()))
c = Counter(input_list)
print(c.most_common()[-1][0])

#Check Subset
# Enter your code here. Read input from STDIN. Print output to STDOUT
test = int(input())
i = 0
while i < test : 
    n = int(input())
    A =  set(list(map(int,input().split())))
    b = int(input())
    B = set(list(map(int,input().split())))
    if( len(A.intersection(B)) == len(A)):
        print(True)
    else:
        print(False)
    i+=1  

#Check Strict Superset
# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(list(map(int,input().split())))
N = int(input())
i= 0 
res = True
while(i<N):
    B  = set(list(map(int,input().split())))
    if(len(A.intersection(B)) != len(B) or (len (A.intersection(B)) == len(B) and len(A) <= len(A.intersection(B)))):
        res = False
    i+=1
print(res)
    


#Find Angle MBC
# Enter your code here. Read input from STDIN. Print output to STDOUT
import math as m
ab = int(input())
bc = int(input())
res= m.atan(ab/bc)
print(str(int(m.degrees(res)))+"°")



#Set .union() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
eng = int(input())
english = set(list(map(int,input().split())))
fr  =  int(input())
french = set(list(map(int,input().split())))
print(len(english.union(french)))

#collections.Counter()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n =  int(input())
store =  Counter(list(map(int,input().split())))
clients = int(input())
output= 0
i = 0
while i < clients :
    order = list(map(int,input().split()))
    size = order[0]
    price = order[1]
    if ( store[size] > 0 ):
        output += price
        store[size] -=1 
    i+= 1
print(output)



#DefaultDict Tutorial
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
dim = list(map(int,input().split()))
n = dim[0]
m= dim[1]
i=0
a= list()
b =list()
while(i < n+m):
    if(i < n):
        a.append(str(input()))
    if(i >=n):
        b.append(str(input()))
    i+=1
for elem in b:
    if elem in a:
        output = []
        for j in range(0,len(a)):
            if(a[j]==elem):
                output.append(j+1)
        print(*output,sep= " ")
        output =[]
    else:
        print(-1)
                

#Collections.namedtuple()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
n = int(input())
columns = list(input().split())
idx =0 
for i in range(len(columns)):
        if (columns[i]  == "MARKS"):
            idx = i
average= 0
for i in range(n):
    stdin = list(input().split())
    average += int(stdin[idx])

output = average/n
print(f"{output:.2f}")

            

#Collections.OrderedDict()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
n = int(input())
dicts = OrderedDict()
for i in range(n):
    stdin = list(input().split())
    if(len(stdin)<3):
        key =  stdin[0]
    else:
        key = stdin[0]+" "+stdin[1]
    value  = int(stdin[len(stdin)-1])
    if(key not in dicts.keys()):
        dicts[key] = int(value)
    else:
        dicts[key] += int(value)
for elem in dicts : 
    print(elem+" "+str(dicts[elem]))


#Word Order
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n = int(input())
strings = []
for i in range(n):
    strings.append(str(input()))
    
output = Counter(strings)
res =""
print(len(output))
for i in output:
    res += str(output[i])
    res+=" "
print(res)

#Collections.deque()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
n = int(input())
d = deque()
for i in range(n):
    command = input().split()
    if( command[0] ==  "append"):
        d.append(int(command[1]))
    elif(command[0] ==  "appendleft"):
          d.appendleft(int(command[1]))
    elif(command[0] ==  "pop"):
          d.pop()
    elif(command[0] ==  "popleft"):
        d.popleft()
res =""
for elem in d:
    res += str(elem)
    res += " "
print(res)



#Piling Up!
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
n = int(input())

for i in range(n):
    dim =  int(input())
    cubes = deque(list(map(int,input().split())))
    temp = max(cubes)
    output = "Yes"
    for i in range(dim):
        if cubes[0]<= cubes[-1]:
            max_elem = cubes[-1]
            cubes.pop()
        else:
            max_elem = cubes[0]
            cubes.popleft()
        if temp >= max_elem :
            temp = max_elem
        else: 
            output = "No"
            break
    print(output)



#Company Logo
#!/bin/python3

import math
import os
import random
import re
import sys
import collections



if __name__ == '__main__':
    s = sorted(input())
    [print(x,y) for x,y in collections.Counter(s).most_common(3) ]
    #output = counter.most_common(3)
    #for i in output:
    #    print(str(i[0])+" "+str(counter[i[0]]))
    

        


#Calendar Module
# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
date  = list(map(int,input().split()))
day = date[1]
month  = date[0]
year =  date[2]
res = calendar.weekday(year,month,day)
if( res == 0):
    print("MONDAY")
elif( res == 1):
    print("TUEDAY")
elif( res == 2):
    print("WEDNESDAY")
elif( res == 3):
    print("THURSDAY")
elif( res == 4):
    print("FRIDAY")
elif( res == 5):
    print("SATURDAY")
elif( res == 6):
    print("SUNDAY")


#Time Delta
#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    date_time1 = datetime.strptime(t1,'%a %d %b %Y %H:%M:%S %z' )
    date_time2 = datetime.strptime(t2,'%a %d %b %Y %H:%M:%S %z')
    difference = abs(date_time1.timestamp() - date_time2.timestamp())
    return str(int(difference))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

#Exceptions
# Enter your code here. Read input from STDIN. Print output to STDOUT-
n = int(input())
for _ in range(n):
    try:
        a, b = map(int,input().split())
        print(a//b)
    except Exception as e:
        print("Error Code:",e)
        continue


#Zipped!
# Enter your code here. Read input from STDIN. Print output to STDOUT
cols,rows = map(int,input().split())
mat = []
for _ in range(rows):
    row = []
    line  = list(input().split())
    for value in line:
        row.append(value)
    mat.append(row)
l = list(zip(*mat))

for x in l:
    average = 0
    for i in range(rows):
        average += float(x[i])
    print(average/rows)

#Athlete Sort
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    l = sorted(arr, key =lambda x :x[k])
    for elem in l:
        print(" ".join(map(str,elem)))


#ginortS
# Enter your code here. Read input from STDIN. Print output to STDOUT
s = str(input())
s_sort=""
lower = [str(x) for x in list(s) if x.islower() and x.isalpha()]
upper  =[str(x) for x in list(s) if x.isupper() and x.isalpha()]
odd = [int(x) for x in list(s) if x.isdigit() and int(x)%2!=0]
even = [int(x) for x in list(s) if x.isdigit() and int(x)%2==0]

for i  in sorted(lower):
    s_sort += i
for i  in sorted(upper):
     s_sort += i
for i  in sorted(odd):
     s_sort += str(i)
for i  in sorted(even):
     s_sort += str(i)
print(s_sort)




#Map and Lambda Function
cube = lambda x:x**3 # complete the lambda function 

def fibonacci(n):
    next_num = lambda x,y:x+y
    if(n>1):
        res = [0,1]
    elif(n==0):
        res= []
    else:
        res= [0]
    for i in range(2,n):
        res.append(next_num(res[i-2],res[i-1]))
    return res


#Detect Floating Point Number
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
for _ in range(n):
    s_float = input()
    print(bool(re.match('^[+-.]?[0-9]*\.{1}[0-9]+$',s_float)))

#Re.split()
regex_pattern = r"\D"	# Do not delete 'r'.



#Group(), Groups() & Groupdict()
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
string = input()
m =  re.search(r'([A-Za-z0-9])\1+',string)
if m:
    print(m.group(1))
else:
    print(-1)


#Re.findall() & Re.finditer()
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
string = input()

m = re.finditer(r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([AEIOUaeiou]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])',string)
res = list(map(lambda x :x.group(),m))
if(res):
    for elem in res:
        print(elem)
else:
    print(-1)









#Re.start() & Re.end()
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
string =input()
substring = input()
m =  re.finditer(rf'(?={substring})',string)
res = []
for elem in m:
    res.append(elem)

if(len(res)>0):
    for elem in res:
        print("("+str(elem.start())+", "+str(elem.end()+len(substring)-1)+")")
else:
    print("(-1, -1)")






#Regex Substitution
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
string = ""
for _ in range(n):
    string += input()
    string += "\n"
def andor(match):
    if(match.group(0) == "&& "):
        return "and "
    if(match.group(0) == "|| "):
        return "or "
print(re.sub(r"(?<= {1})&{1}&{1} {1}|(?<= {1})\|{1}\|{1} {1}",andor,string))




#Validating Roman Numerals
regex_pattern = r"^(M{0,3})(C[DM]|D?C{0,3})(X[LC]|L?X{0,3})(I[VX]|V?I{0,3})$"	# Do not delete 'r'.






#Validating phone numbers
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
for _ in range(n):
    tel = input()
    if(len(tel) == 10 and re.match("^[789][0-9]{9}",tel)):
        print("YES")
    else:
        print("NO")




#Validating and Parsing Email Addresses
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import email.utils

n = int(input())
for _ in range(n):
    t =  email.utils.parseaddr(str(input()))
    res= re.match(r"[a-z][A-Za-z0-9\.\_\-]+\@[A-Za-z]+\.[A-Za-z]{1,3}" ,t[1])
    if(res):
        if( res.group() ==  t[1]):
            print(email.utils.formataddr(t))


#HTML Parser - Part 1
# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        for name,value in attrs:
            print(f"-> {name} > {value}")

    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        for name,value in attrs:
            print(f"-> {name} > {value}")

    def handle_endtag(self, tag):
        print(f"End   : {tag}")
n =int(input())   
parser = MyHTMLParser()
for _ in range(n):
    parser.feed(input())
parser.close()

#HTML Parser - Part 2
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self,data):
        if data != '\n':
            if '\n' in data:
                print(">>> Multi-line Comment")
                print(data)
            else:
                print(">>> Single-line Comment")
                print(data)
    def handle_data(self, data):
        if not data =='\n':
            print(f">>> Data")
            print(data)
  

html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()          

#Detect HTML Tags, Attributes and Attribute Values
# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        [print('-> {} > {}'.format(*attr)) for attr in attrs]
        
html = '\n'.join([input() for _ in range(int(input()))])
parser = MyHTMLParser()
parser.feed(html)
parser.close()

#Validating UID 
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
reg =r'^(?=(?:[a-z\d]*[A-Z]){2})(?=(?:\D*\d){3})(?:([a-zA-Z\d])(?!.*\1)){10}$'
for _ in range(n):
    t = input()
    if( re.fullmatch(reg,t)):
        print("Valid")
    else:
        print("Invalid")



#Validating Credit Card Numbers
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
regex1  = r'^[456](\d{15}|[\d]{3}(-\d{4}){3})$'
regex2 = r'(\d)\1\1\1'
for _ in range(int(input())) :
    number = input()
    if( re.match(regex1,number) and not re.search(regex2,number)):
        print("Valid")
    else:
        print("Invalid")
    


#Hex Color Code
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
reg  =r'[\s:,()](#([0-9a-fA-F]{3}){1,2})'
for _ in range(n):
    line=  input()
    result = re.findall(reg,line)
    if(result == []):
        continue
    else:
        for i in result:
            print(i[0])



#Validating Postal Codes
regex_integer_in_range = r"[1-9][0-9]{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r'(?=(\d)\d\1)'







#Matrix Script
#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
# (#  @i U)
sol = []
for j in range(m):
    line=""
    for i in range(n):
         line+=matrix[i][j]
    sol.append(line)
print(re.sub(r'(?<=[A-Za-z0-9])[\W\s]{1,}(?=[A-Za-z0-9])',' ',"".join(sol)))

#XML 1 - Find the Score


def get_attr_number(node):
    cnt = len(node.attrib.values())
    for child in node:
        cnt += get_attr_number(child)
    return cnt



#XML2 - Find the Maximum Depth


maxdepth = 0
def depth(elem, level):
    global maxdepth 
    level +=1
    if(maxdepth<level):
        maxdepth = level
    for child in elem:
        depth(child,level)



#Standardize Mobile Number Using Decorators
def wrapper(f):
    def fun(l):
        for i in range(len(l)):
            ult = l[i][len(l[i])-10:len(l[i])-5]+" "+l[i][len(l[i])-5:]
            l[i] = '+91 '+ult
        l= f(l)
        return l
    return fun



#Decorators 2 - Name Directory


def person_lister(f):
    def inner(people):
        for p in people:
            p[2] =int(p[2])
        return map(f,sorted(people,key= operator.itemgetter(2)))
    return inner



#Arrays


def arrays(arr):
    return numpy.array(arr[::-1],float)


#Shape and Reshape
import numpy
inp = list(map(int,input().split()))
inp = numpy.array(inp)
print(numpy.reshape(inp,(3,3)))



#Transpose and Flatten
import numpy
n,m = map(int,input().split())

l = []
for _ in range(n):
    l.append(list(map(int,input().split())))
print(numpy.transpose(numpy.array(l)))
print(numpy.array(l).flatten())
    


#Concatenate
import numpy
n,m,p = map(int,input().split())
N = []
M=[]
for _ in range(n):
    N.append(list(map(int,input().split())))
for _ in range(m):
    M.append(list(map(int,input().split())))
arr_n = numpy.array(N)
arr_m = numpy.array(M)
#print(arr_n,'\n',arr_m)

print(numpy.concatenate((arr_n,arr_m)))



#Zeros and Ones
import numpy
t = tuple(map(int,input().split()))
print(numpy.zeros(t,dtype=numpy.int))
print(numpy.ones(t,dtype=numpy.int))



#Eye and Identity
import numpy
numpy.set_printoptions(legacy='1.13')
n,m = map(int,input().split())
print(numpy.eye(n,m,k=0))



#Array Mathematics
import numpy
numpy.set_printoptions(legacy = "1.13")
n,m = map(int, input().split())
lN  = list(map(int,input().split()))
lM  = list(map(int,input().split()))
N = numpy.array(lN)
M = numpy.array(lM)
print("["+str(numpy.add(N,M))+"]")
print("["+str(numpy.subtract(N,M))+"]")
print("["+str(numpy.multiply(N,M))+"]")
print("["+str(numpy.array(numpy.divide(N,M),int))+"]")
print("["+str(numpy.mod(N,M))+"]")
print("["+str(numpy.power(N,M))+"]")



#Floor, Ceil and Rint
import numpy
numpy.set_printoptions(legacy="1.13")
a = numpy.array(list(map(float,input().split())))
print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))


#Sum and Prod
import numpy
n,m = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
sum_  = numpy.sum(numpy.array(arr),axis =0)
print(numpy.prod(sum_))

#Min and Max
import numpy
n,m = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

print(numpy.max(numpy.min(numpy.array(arr),axis=1)))


#Mean, Var, and Std
import numpy
numpy.set_printoptions(legacy="1.13")
n,m = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
print(numpy.mean(numpy.array(arr),axis = 1))
print(numpy.var(numpy.array(arr),axis = 0))
print(numpy.std(numpy.array(arr)))


#Dot and Cross
import numpy
#numpy.set_printoptions(legacy = "1.13")
n = int(input())
a = []
b = []
for _  in range(n):
    a.append(list(map(int,input().split())))
for _ in range(n):
    b.append(list(map(int,input().split())))
A =numpy.array(a)
B = numpy.array(b)
print(numpy.dot(A,B))

#Inner and Outer
import numpy
A = numpy.array(list(map(int,input().split())))
B = numpy.array(list(map(int,input().split())))
print(numpy.inner(A,B))
print(numpy.outer(A,B))



#Polynomials
import numpy
cff = list(map(float,input().split()))
x = float(input())
print(numpy.polyval(cff,x))




#Linear Algebra
import numpy.linalg
m = []
for _ in range(int(input())):
    m.append(list(map(float,input().split())))
print (round(numpy.linalg.det(m),2))



#Birthday Cake Candles
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    maxi = max(candles)
    return len([x for x in candles if x == maxi])
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

#Number Line Jumps
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    if( v1>v2):
        while (x1 <x2):
            x1 += v1
            x2 += v2
        if(x1 == x2):
                return "YES"
    return "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

#Viral Advertising
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    likes = 0
    
    recipients = 5
    for i in range(n):
        daylikes = 0
        daylikes += recipients//2 
        likes +=daylikes
        recipients = daylikes * 3
    
    return likes
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()



#Recursive Digit Sum
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#
def superDigitAux(s):
    if(len(s)==1):
        return s
    else:
        res = 0
        for c in s:
            res += int(c)
        return superDigitAux(str(res))
    
def superDigit(n, k):
        s = str(n)
        res  = 0
        for c in s:
            res += int(c)
        res = res * k
        res  = superDigitAux(str(res))
        return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()





#Insertion Sort - Part 1
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    elem  = arr[n-1] 
    for i in range(n-2,-1,-1):
        if(arr[i]> elem and i!=0):
            arr[i+1]  = arr[i]
        elif(arr[i]>elem and i==0):
            arr[i+1]  = arr[i]
            print(" ".join([str(x) for x in arr]))
            arr[i] = elem
        else:
            arr[i+1]=elem
            print(" ".join([str(x) for x in arr]))
            break
        print(" ".join([str(x) for x in arr]))
    return arr
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

#Insertion Sort - Part 2
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    for i in range(1,n):
        j = i-1
        temp =  arr[i]
        while( j>=0 and arr[j]>temp):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp
        print(" ".join([str(x) for x in arr]))

        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)

