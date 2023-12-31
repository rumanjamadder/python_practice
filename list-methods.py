l = [11, 45, 1, 1, 1, 2, 4, 6]
print(l)
# append = add something new at the end of the list
l.append(7) 
# sort = sort by asending way and also sort bye decending way
l.sort(reverse=True)
# It reverse the main list
l.reverse()
# prints index
print(l.index(1))
# It counts how many (1) has in the list like this we can count any number from the list
print(l.count(1))
# reference [don't use this as a beginner]
# m = l
m = l.copy() 
m[0] = 0
print(l)