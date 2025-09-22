#Majority Element
def majority_element(arr,n): #arr - список чисел, n - размер массива
    count = {} #словарь для подсчета
    for num in arr:
        count[num] = count.get(num, 0) + 1 #ищем ключ при переборе и считает кол-во вхождений ключа
    for num, count in count.items(): #После подсчета всех элементов запускаем счетчик для сравнения ключей
        if count > n / 2:
            return num
    return -1 #Мажористый элемент или -1 если не сущ
def main():
    with open('/Users/user/downloads/rosalind_maj-3.txt', 'r') as file:
        data = file.read().split()
    k = int(data[0])
    n = int(data[1])
    results = []
    index = 2 #Первые 2 элемента мы уже рассмотрели, начинаем с 3 элемента


    for i in range(k):
        count_array = list(map(int, data[index:index+n]))
        index += n 
        result = majority_element(count_array, n)
        results.append(str(result))
    print(' '.join(results))
if __name__ == "__main__":
    main()

    
