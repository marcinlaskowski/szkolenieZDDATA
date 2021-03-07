"""
6. Zbiory. Mając listy
A = [1,2,7,8,8, 10]
B = [5,6,3,2,8,10]
C= [1,2,10]
a) Podaj liczby, które występują przynajmniej w jednej z list
b) Podaj liczby, które są jednocześnie na liście A, B, C
"""

if __name__ == '__main__':
    list_A = [1, 2, 7, 8, 8, 10]
    list_B = [5, 6, 3, 2, 8, 10]
    list_C = [1, 2, 10]

    set_A = set(list_A)
    set_B = set(list_B)
    set_C = set(list_C)

    print("UNION", set_A.union(set_B, set_C))
    print("UNION", set_A | set_B | set_C)

    print("INTERSECTION", set_A.intersection(set_B, set_C))
    print("INTERSECTION", set_A & set_B & set_C)
