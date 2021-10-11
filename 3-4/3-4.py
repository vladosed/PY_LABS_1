#create random string with lower and upper case and with numbers
str_var = "asdjhJVYGHV42315gvghvHGV214HVhjjJK"
print(str_var)

#find first symbol of string
first_symbol = str_var[0]
print(first_symbol)

#find the last symbol of string
last_symbol = str_var[-1]
print(last_symbol)

#slice first 8 symbols
print(str_var[slice(8)])

#print only symbols with index which divides on 3 without remaining
list_of_str_var = list(str_var.strip(" "))
every_third_elem = list_of_str_var[::3]
list_to_str = ''.join(str(x) for x in every_third_elem)
print(list_to_str)

#print the symbol of the middle of the string text
middle = str_var[int(len(str_var) / 2)] #len(str_var) / 2 
print(middle)

#reverse text using slice
print(str_var [::-1])