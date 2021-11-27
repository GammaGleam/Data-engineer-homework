# Эта функция будет выполняться на узлах
def mapper(text):
    # считает количество слов в тексте
    return len(text.split())
    
def reducer(mapped):
    return sum(mapped)


# document - входящая строка, в которой нужно посчитать количество слов
# nodes - количество рабочих узлов

# Шаг 0 - разбиваем исходный документ на N кусков, где N - количество рабочих узлов
chunks = split_by_chunks(document, chunks_count = nodes)

# Шаг 1 - просим узлы обработать куски документа, используя функцию mapper
mapped = nodes_pool.map(mapper, chunks)

# Шаг 2 - складываем результаты вычислений
reduced = reducer(mapped)

# Шаг 3 - выведем количество слов в документе
print(reduced)