from collections import Counter
def find_repeated_char(s):
    counts=Counter(s)
    repeted = {char:count for char,count in counts.items() if count>1}
    return repeted
input_string='aaanccnnssccc'
result = find_repeated_char(input_string)
print( result)
fruits = [("apple",1), ("banana",2), ("cherry",3)]
for name,count in fruits:
    print( name,count)
#Convert to Dictionary
fruits_dict=dict(fruits)
print(fruits_dict)
student=[("Govardhan",100),("Ramesh",90),("Mahesh",70),("Kumar",50),("Sai",34)]
high_score = [students for students in student if students[1]>90]
print(high_score)
