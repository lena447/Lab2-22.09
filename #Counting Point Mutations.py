#Counting Point Mutations
with open('/Users/user/downloads/rosalind_hamm-3.txt', 'r') as file:
    s = file.readline().strip() 
    t = file.readline().strip() 
count_distance = 0
for i in range(len(s)): #проходим по всем индексам от 0 до конца строки
    if s[i] != t[i]: #На каждом индексе сравниваем сравниваем символы двух строк на одной и той же позиции
     count_distance += 1
print(count_distance)
