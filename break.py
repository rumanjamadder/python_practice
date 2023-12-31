for i in range(12):
    if(i==10):
        break
print("5 x",i+1,"=",5*(i+1))
print("Loop se bar nikhal gaya")

# another example of break statement
print()
for i in range(1,101,1):
     print(i, end="")
     if(i==20):
            break
     else:
          print("Mississppi")
          print("Thank You")

# example of continue statement
          print()
          for i in range(12):
            if(i==10):
                 print("skip the iteration")
                 continue
            print("5 x", i, "=", 5*1)

# example of continue and break statement together in a for loop 
for i in range(1, 200):
    if(i>=50 and i<=60):
        print("ami ekhane")
        continue
    if(i==50):
        break
    print(i)
