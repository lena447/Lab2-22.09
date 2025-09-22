#Mendel's First Law

with open('/Users/user/downloads/rosalind_iprb-6.txt', 'r') as file:
    data = file.read().split()
    
    k = int(data[0])  #Гомозигота АА
    m = int(data[1])  #Гетерозигота Аа
    n = int(data[2])  #Гомозигота аа
    total = n + k + m #Всего особей в популяции

    recessive_probability = 0.0 
    if n >= 2:
        recessive_probability += (n / total) * ((n - 1) / (total - 1)) #Пары гомозиготы аа и аа
    if m >= 2:
        recessive_probability += (m / total) * ((m - 1) / (total - 1)) * 0.25 #Пары гетерозиготы Аа и Аа. Умножение на 0.25 по закону Менделя
    if m >= 1 and n >= 1:
        recessive_probability += 2 * (m / total) * (n / (total - 1)) * 0.5 #Пары гетерозиготы Аа и аа. 0.5 по закон Менделя
dominant_probility = 1 - recessive_probability
print(f"{dominant_probility:.5f}")