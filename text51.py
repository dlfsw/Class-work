count = 0
total = 0
while True:
    test = input("Enter a number: ")
    if test == "done" : 
        break
    try:
        num = float(test)
    except:
        print("Invalid input")
        continue
    count = count + 1
    total = total + num
print("")
print("Sum is", total)
print("Count is", count)
print("Average is", total/count)