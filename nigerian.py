
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



sentence = input('write a sentence: ')
broken = sentence.split()

print(len(broken))



#.split splits the sentence into strings
#len() tells the length of the sentence 













