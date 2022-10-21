def creat(words_list):
    m_list = list()
    for i in range(0,len(words_list)):
        m_list.append(len(words_list[i]))
    print(m_list)
    return m_list
def search_min(m_list):
    min_word = m_list[0]
    for i in range(1,len(m_list)):
        if min_word > m_list[i]:
            min_word = m_list[i]
    return min_word
def search_max(m_list):
    max_word = m_list[0]
    for i in range(1,len(m_list)):
        if max_word < m_list[i]:
            max_word = m_list[i]
    return max_word
words = ['Дом','Клоп','Тираннозавр','Тромб','Монета','Пустота','Зима']
my_list = creat(words)
print("Сумма максимального и минимального элемента: " + str(search_min(my_list) + search_max(my_list)))