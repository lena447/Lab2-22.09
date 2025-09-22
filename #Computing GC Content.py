#Computing GC Content


with open("/Users/user/downloads/rosalind_gc-5.txt", 'r') as file:
    lines = file.readlines()

sequences = {}                     #Создаём словарь для хранения ID и последовательностей
current_id = ''

for line in lines:
    line = line.strip()
    if line.startswith('>'):        #Начинаем новая запись, сохраняем новый ID без '>'
        current_id = line[1:]
        sequences[current_id] = ''
    else:                           #Продолжаем добавлять нуклеотиды к текущей последовательности
        sequences[current_id] += line

def gc_content(dna):                 #Расчёта GC-содержания
    gc_count = 0
    for nucleotide in dna:
        if nucleotide == 'G' or nucleotide == 'C':
            gc_count += 1
    return (gc_count / len(dna)) * 100

max_id = ''                          # Поиск последовательности с максимальным GC-содержанием
max_gc = 0.0

for seq_id, dna_seq in sequences.items():
    current_gc = gc_content(dna_seq)
    if current_gc > max_gc:
        max_gc = current_gc
        max_id = seq_id
        
print(max_id)
print(f"{max_gc:.6f}")