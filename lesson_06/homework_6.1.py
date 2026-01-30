unique_symbols = []
string_to_check = input("Enter a string for checking the unique symbols: \n")

for el in string_to_check:
    if el not in unique_symbols:
        unique_symbols.append(el)

if len(unique_symbols) > 10:
    print("True")
else:
    print("False")

