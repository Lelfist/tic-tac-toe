print("!Игра Крестики-нолики!\nВведите имя клетки, чтобы поставить крестик или нолик")
def name(n_kl, a):
    if n_kl not in ["a", "b", "c", "d", "e", "f", "g", "h", "i"]:
        print("Неверное имя клетки!\nВведите имя клетки ещё раз.")
        n_kl = input("Введите имя клетки: ")
        n_kl = name(n_kl, a)
        return n_kl
    elif n_kl in a[0]:
        return n_kl
    elif n_kl in a[1]:
        return n_kl
    elif n_kl in a[2]:
        return n_kl
    else:
        print("Клетка уже занята!\nВведите имя клетки ещё раз.")
        n_kl = input("Введите имя клетки: ")
        n_kl = name(n_kl, a)
        return n_kl
def tochka(n_kl, player, a):
    for i in range(3):
        for j in range(3):
            if n_kl == a[i][j]:
                if player%2 == 0:
                    a[i][j] = "X"
                else:
                    a[i][j] = "O"
    return a
def view(a):
    print("_" * 7)
    for i in a:
        print("|" , "|".join(i) , "|", sep="")
        print("-" * 7)
def win(a):
    for i in range(3):
        if a[i][0] == a[i][1] == a[i][2]:
            return True
        if a[0][i] == a[1][i] == a[2][i]:
            return True
    if a[0][0] == a[1][1] == a[2][2]:
        return True
    if a[0][2] == a[1][1] == a[2][0]:
        return True
    return False
def nichaya(a):
    for i in a:
        for j in i:
            if j in "abcdefghi":
                return False
    return True
