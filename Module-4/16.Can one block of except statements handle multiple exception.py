try:
    name = 'Bob'
    name += 5
except (NameError, TypeError) as error:
    print(error)

try:
    name = 'Bob'
    name =+ 5
except NameError as ne:
    
    print(ne)
except TypeError as te:
    
    print(te)