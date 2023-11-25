
def odd(number):
    if number%2 == 0:
       print("even")
    else:
        print("odd")


def factor(number):
    print(f"the factors of {number}: ")
    for i in range (1, number + 1):
        if number%i == 0:
            print(i)

def commonfactor(a,b):
     A = factor(a)
     B = factor(b)
     for i in range(1, a + b):
          if A[i] == B[i]:
               print(i)
               break
commonfactor(15,48)          
    

def multiply(bill):
    service = (input(f"How's the service?: ")).lower()
    if service == "bad":
            tip = 0
    if service == "okay":
            tip = 15
    if service == "good":
            tip = 20
    if service == "excellent":
            tip = 25
                           
    finaltip = tip/100
    totalpay = bill*finaltip + bill

    print(totalpay)

#sentence = input('write a sentence: ')
#broken = sentence.split()

#.split splits the sentence into strings
#len() tells the length of the sentence 



#list = [] makes a list
#list.append(i) puts stuff in a list
#return(list) returns anything






def XY(x,y):
    if type(x) != bool or type(y) != bool:
        print("it's wrong")
    else:
         if x == y:
             print('false')
         if not(x == y):
             print('true')

GCF = [1,3,4,8]
b = max(GCF)

def math(x,y):
    if x + y > 10:
         a = x*y
         print(a)
    elif x + y < 10:
         b = x/y
         print(b)
    else:
         print(69420)



    

          

