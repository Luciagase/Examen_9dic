from ast import main

String = "BANANA"

# Program that creates a dictionary with substrings of the word as Keys and the number of times they appear as values
def Dic(String):
    Dict = {}
    for i in range(len(String)):
        for j in range(i+1, len(String)+1):
            if String[i:j] in Dict:
                Dict[String[i:j]] += 1
            else:
                Dict[String[i:j]] = 1
    return Dict

# Program that returns the sum of the values of the dictionary whose keys start with vowels 
def Sum(Dict):
    Sum1 = 0
    for i in Dict:
        if i[0] in "AEIOU":
            Sum1 += Dict[i]
    return Sum1

# Program that sum all the values of the dictionary
def SumAll(Dict):
    Sum = 0
    for i in Dict:
        Sum += Dict[i]
    return Sum


def puntuation(Sum1, Sum):
    if Sum1 < (Sum-Sum1):
        print("Stuart", Sum1)
    elif Sum1 > (Sum-Sum1):
        print("Kevin", Sum1)
    elif Sum1 == (Sum-Sum1):
        print("Draw")
    else:
        print("Error")

puntuation(Sum(Dic(String)), SumAll(Dic(String)))


if __name__ =='__main__':
    main()