for i in range(1,101):
    if i%5==0:
        print("Fizz")
    if i%7==0:
        print("Buzz")
    if i%5!=0 and i%7!=0:
        print(i)
 
for i in range(1,101):
    if i%5==0 and i%7!=0:
        print("Fizz")
    if i%7==0 and i%5!=0:
        print("Buzz")
    if i%7==0 and i%5==0:
        print("FizzBuzz")
    if i%5!=0 and i%7!=0:
        print(i)
        
        
for i in range(1,101):
    outp = ""
    if i%3==0: outp+="Jazz"
    if i%5==0: outp+="Fizz"
    if i%7==0: outp+="Buzz"
    if not(outp): outp=str(i)
    print(outp)

mapper = {3:"Jazz",5:"Fizz",7:"Buzz"}
for i in range(1,101):
    outp = ""
    for key in mapper:
        if i%key==0: outp+=mapper[key]
    if not(outp): outp=str(i)
    print(outp)
