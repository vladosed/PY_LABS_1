from string import ascii_letters, ascii_lowercase, digits, ascii_lowercase, ascii_uppercase

#generate 2 sets with not unique numbers
set1 = set(ascii_uppercase + ascii_letters + ascii_lowercase + digits)
set2 = set(ascii_uppercase + ascii_letters + ascii_lowercase + digits)
print("SET1:", set1)

#create tuple from intersection of first and second set
tpl_intersec = tuple(set1.intersection(set2))
print("tuple  intersection:", tpl_intersec)

#create tuple from difference first and second set
tpl_difference = tuple(set1.difference(set2)) 
print("tuple difference:", set2)

#slice first 3 symbols from 1st tuple
slc_three_symb = tpl_intersec[:3]
print("slice first three symbols:", slc_three_symb)

#print only symbols with numbers from second set
print("only digits:", set(digits).intersection(set2))

#reverse tuple using slice
print("reverse:", tpl_intersec[::-1])

#convert both tuples to list
print(''.join(tpl_intersec))