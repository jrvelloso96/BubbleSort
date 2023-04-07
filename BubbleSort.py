import random


def bubble_sort(v):
    fim = len(v)
    while fim > 0:
        i = 0
        print(v, "\n")
        while i < fim-1:
            if v[i] < v[i+1]:
                temp = v[i]
                v[i] = v[i+1]
                v[i+1] = temp
            i += 1
        fim -= 1


vetor = list(range(0, 10))
random.shuffle(vetor)
print("Não ordenado \n", vetor, "\n")
bubble_sort(vetor)
print("Ordenado \n", vetor)
