def create_phone_number(lst: list) -> str:
    """Решение для Задачи 1"""
    return f'({str(lst[0]) + str(lst[1]) + str(lst[2])}) {str(lst[3]) + str(lst[4]) + 
    str(lst[5])}-{str(lst[6]) + str(lst[7]) + str(lst[8]) + str(lst[9])}'

def duplicate_encode(text: str) -> str:
    """Решение для Задачи 2"""
    string = text.lower()
    lst_text = list(string)
    result = []
    for i in lst_text:
        count = lst_text.count(i)
        if count == 1:
            result.append('(')
        else:
            result.append(')')
    return (''.join(result))

def is_valid_walk(walk: list) -> bool:
    """Решение для Задачи 3"""
    if len(walk) != 10:
        return False
    n, s, w, e = 0, 0, 0, 0
    
    for direction in walk:
         if direction == 'n':
             n += 1
         elif direction == 's':
             s += 1
         elif direction == 'w':
             w += 1
         elif direction == 'e':
             e += 1
    return n == s and w == e


def move_zeros(lst: list) -> list:
    """Решение для Задачи 4"""
    list1 = []
    list2 = []
    for i in lst:
        if i == 0:
            list2.append(0)
        else:
            list1.append(i)
    return list1 + list2

def find_uniq(lst: list):
    """Решение для Задачи 5"""
    if lst[0] != lst[1]:
        if lst[0] == lst[2]:
            return lst[1]
        else:
            lst[0]
    else:
        a = lst[0]
        for item in lst:
            if item != a:
                return item
                
