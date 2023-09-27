
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


east = input(f'Traffic is east: ')
west = input(f'Traffic is west: ')
if east and west == 'true':
     print('false')
if east and west == 'false':
     print('true')
if east == 'true' and west == 'false':
     print('true')
if east == 'false' and west == 'true':
     print('true')








