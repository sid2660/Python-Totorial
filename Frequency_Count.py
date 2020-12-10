import re
def CountFrequency(my_list):
    
##Creating an empty dictionary
    freq= {}
    for item in my_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
    print("")
    print("The frequency of all the elements of the list :")
    for key, value in freq.items():
        print("% d occurs % d times"%(key, value))

def Dash():
    print('#######################################################')
    return
def main():
    Dash()
    Element = []
    RANGE = int(input("Input the number of element to be stored in the list : "))
    print("Input", RANGE, "Elements in the list :")
    for i in range(RANGE):
        print("Element -", i, ":", end="")
        element= int(input())
        Element.append(element)
        CountFrequency(Element)
main()