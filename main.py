def show_menu():
    print("1. Citire date.")
    print("2. Determinare cea mai lungă subsecvență cu proprietatea ca toate numerele sa fie pare.")
    print("3. Determinare cea mai lungă subsecvență cu proprietatea ca toate numerele sa aiba același număr de divizori.")
    print("x. Ieșire.")

def read_list() :
    lst=[]
    lst_str=input("Dati numere separate prin spatiu: ")
    lst_str_split=lst_str.split(' ')
    for num_str in lst_str_split:
        lst.append(int(num_str))
    return lst

def get_longest_all_even(lst: list[int]) -> list[int]:
    '''
    Toate numerele sunt pare.
    :param lst: lista cu elemente
    :return: cea mai lunga subsecventa
    '''
    st = -1
    fn = -1
    lgmax=0
    i=1
    if lst[0] % 2 == 0:
        lg = 1
    else:
        lg = 0
    lst.append(1)
    while i<len(lst) :
        if lst[i]%2+lst[i-1]%2==0 :
            lg+=1
        else :
            if lg>lgmax :
                fn=i-1
                st=i-lg
                lgmax=lg
            if lst[i]%2==0 :
                lg=1
            else :
                lg=0
        i+=1
    return lst[st : fn+1]

def test_get_longest_all_even():
    assert get_longest_all_even([1, 2, 3, 4, 4])==[4, 4]
    assert get_longest_all_even([1,3,5,9,4,8])==[4, 8]
    assert get_longest_all_even([4,4,1,5,2,2,2])==[2,2,2]


def numar_divizori(n):
    if n==0 : return 0
    if n==1:return 1
    d = 2
    for i in range(2,n):
        if n%i==0:d=d+1
    return  d
def get_longest_same_div_count(lst: list[int]) -> list[int]:
    '''
    Toate numerele același număr de divizori.
    :param lst: lista cu elemente
    :return: secventa maxima de elemente cu acelasi numar de divizori
    '''
    st=-1
    fn=-1
    lgmax=0
    lg=1
    i=1
    lst.append(0)
    while i<len(lst) :
        if numar_divizori(lst[i])==numar_divizori(lst[i-1]):
            lg+=1
        else :
            if lg>lgmax :
                fn=i-1
                st=i-lg
                lgmax=lg
            lg=1
        i+=1
    return lst[st : fn+1]
def test_get_longest_same_div_count():
    assert get_longest_same_div_count([1,1,1,1,1,1,1])==[1,1,1,1,1,1,1]
    assert get_longest_same_div_count([4,4,4,6,6,6,6])==[6,6,6,6]
    assert get_longest_same_div_count([6,12,24])==[6]

def is_prime(n):
    if n==1:return 0
    d=0
    for i in range(1,n+1):
        if n%i==0:d=d+1
    if d==2: return 1
    else: return 0
def get_longest_all_primes(lst: list[int]) -> list[int]:
    '''
    Toate numerele sunt prime.
    :param lst: lsita cu elemente
    :return: lista cea mai lunga de numere prime
    '''
    st = -1
    fn = -1
    lgmax=0
    i=1
    if lst[0] % 2 == 0:
        lg = 1
    else:
        lg = 0
    lst.append(1)
    while i<len(lst) :
        if is_prime(lst[i])+is_prime(lst[i-1])==2 :
            lg+=1
        else :
            if lg>lgmax :
                fn=i-1
                st=i-lg
                lgmax=lg
            if is_prime(lst[i])==1 :
                lg=1
            else :
                lg=0
        i+=1
    if st==0 and is_prime(lst[st])==0:return "nu sunt numere prime"
    else: return lst[st : fn+1]
def test_get_longest_all_primes():
    assert get_longest_all_primes([1,2,3,4,5,6,7,8,9,10])==[2,3]
    assert get_longest_all_primes([2,3,5,7,11])==[2,3,5,7,11]
    assert get_longest_all_primes([4,8,10])=="nu sunt numere prime"

def main():

    while True:
        show_menu()
        opt = input("Optiunea dorita este: ")
        if opt=='1':
            lst=read_list()
        elif opt=='2':
            lst2=get_longest_all_even(lst)
            if len(lst2)==0:print("Nu exista elemente pare.")
            print(lst2)
        elif opt=='3':
            lst3=get_longest_same_div_count(lst)
            print(lst3)
        elif opt=='4':
            lst4=get_longest_all_primes(lst)
            print(lst4)
        elif opt=='x':
            break
        else:
            print("Optiune invalida.")


    test_get_longest_all_even()
    test_get_longest_same_div_count()
    test_get_longest_all_primes()
if __name__ == '__main__':
    main()