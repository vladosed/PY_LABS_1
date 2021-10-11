from numbers import Number
#generate list with lowercase and uppercase alphabet plus numbers
str_var = "FMeJSdqXEnxbYzkLSpgt4YchPgqVMghygGW4FMuS68RwLnqRAtb34kpjCm96KPGW2VwBe9tDGjycKPuwGnpgTsELNqrYJK9"
list_of_str_var = list(str_var)
print(list_of_str_var)
#print 1st symbol of list
print("first symbol of list:", list_of_str_var[0])

#print last symbol of list
print("last symbol of list:", list_of_str_var[-1])

#print 3rd from start, 3rd from the end
print("3rd from start:", list_of_str_var[2])
print("3rd from the end:", list_of_str_var[-3])

#slice first 10 symbols
slc_ten_sym_beg = slice(10)
print("slice first 10 symbols:", list_of_str_var[slc_ten_sym_beg])

#print only symbols with index which divides on 2 without remaining
all_second_elems = list_of_str_var[::2]
print("all second elements:", all_second_elems)

#print only integer values from list
int_list = [num for num in list_of_str_var if isinstance(num, (int, float))]
print("numbers:", int_list)