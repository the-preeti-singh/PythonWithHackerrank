import roman
x=input()
try:
    if (roman.fromRoman(x)>0 and roman.fromRoman(x)<4000):
        print("True")
    else:
        print("False")
except:
    print("False")
