
def odd(number):
    if number%2 == 0:
       print("even")
    else:
        print("odd")


def factor(number, number2):
    print(f"the factors of {number} and {number2} is: ")
    for i in range (1, number + 1):
        if number%i == 0:
            print(i)
    for i in range (1, number2 + 1):
        if number%i == 0:
            print(i)
    

def multiply(bill):
    service = input(f"How's the service?: ")  
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

def mommamia(num):
    list = []
    for i in range(1, num + 1):
        if num%i == 0:
            list.append(i)

    return(list)

#list = [] makes a list
#list.append(i) puts stuff in a list
#return(list) returns anything

def gcf(x, y):
    XList = mommamia(x)
    YList = mommamia(y)
    GCF = 1

    for i in XList:
        if i in YList:
            GCF = max(GCF, i)
    print(GCF)




def XY(x,y):
    if type(x) != bool or type(x) != bool:
        print("it's wrong")
    else:
         if x == y:
             print('false')
         if not(x == y):
             print('true')

XY(True,False)




