
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
    

def multply(bill, tip):
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

def gcf(x, y):
    XList = mommamia(x)
    YList = mommamia(y)
    GCF = 1

    for i in XList:
        if i in YList:
            GCF = max(GCF, i)
    print(GCF)



mommamia(10)
gcf(40,10)








