def show_menu():
    print("1. Citire date.")
    print("2. Determinare cea mai lungă subsecvență cu proprietatea 1.")
    print("3. Determinare cea mai lungă subsecvență cu proprietatea 2.")
    print("x. Ieșire.")

def read_list() :
    lst=[]
    lst_str=input("dati numere separate prin spatiu ")
    lst_str_split=lst_str.split(' ')
    for num_str in lst_str_split:
        lst.append(int(num_str))
    return lst

def get_longest_all_even(st, fn, lst: list[int]) -> list[int]:
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

def numar_divizori(n):
    if n==0 : return 0
    if n==1:return 1
    d = 2
    for i in range(2,n):
        if n%i==0:d=d+1
    return  d
def get_longest_same_div_count(st,fn,lst: list[int]) -> list[int]:
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

def main():
    st=-1
    fn=-1
    while True:
        show_menu()
        opt = input("Optiune: ")
        if opt=='1':
            lst=read_list()
        elif opt=='2':
            lst2=get_longest_all_even(st, fn, lst)
            if len(lst2)==0:print("nu exista elemente pare")
            sol=''
            for x in lst2 :
                sol+=str(x)+' '
            print(sol)
        elif opt=='3':
            lst3=get_longest_same_div_count(st,fn,lst)
            sol = ''
            for x in lst3:
                sol += str(x) + ' '
            print(sol)
        elif opt=='x':
            break
        else:
            print("Optiune invalida.")
if __name__ == '__main__':
    main()