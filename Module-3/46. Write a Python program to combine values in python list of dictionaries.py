from collections import Counter
item_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
result = Counter()

for d in item_list:
    result[d['item']] += d['amount']

print (f"Original items list is : {item_list}")
print (f"output is : {result}") 