str = input ("enter the string : ")

length_str = len (str)

mid_len = length_str // 2

mid_str = input ("enter your middle string : ")

print (str[:mid_len] + mid_str + str [mid_len :])