import glob


def browar(name):

    print("Pracuje nad " + name)
    plik = open(name, "r")

    # n - liczba miast do analizy
    n = int(plik.readline())
    dane = plik.read().splitlines()
    tab = []
    flat_tab = []
    for element in dane:
        tab.append(element.split(" "))
    for sublist in tab:
        for item in sublist:
            flat_tab.append(item)

    # z[i] - zapotrzebowanie na piwo w mieście i
    # d[i] - odleglosc od miasta i do kolejnego miasta
    z = []
    d = []
    index = 0
    for element in flat_tab:
        if index % 2 == 0:
            z.append(int(element))
        else:
            d.append(int(element))
        index += 1

    dl, dr, l, r, zl, zr, c = 0, 0, 0, 0, 0, 0, 0
    j = 1
    while j < n:
        if dl+d[(l+n-1) % n] < dr+d[r]:
            dl = dl + d[(l + n - 1) % n]
            l = (l + n - 1) % n
            c = c + dl * z[l]
            zl = zl + z[l]

        else:
            dr = dr + d[r]
            r = (r + 1) % n
            c = c + dr * z[r]
            zr = zr + z[r]
        j += 1

    min = c
    min_n = 0

    for i in range(1, n):
        zl = zl + z[i - 1]
        cc = d[(i + n - 1) % n]
        cc = cc * (zl - zr)
        c = c + cc
        zr = zr - z[i]
        dl = dl + d[(i + n - 1) % n]
        dr = dr - d[(i + n - 1) % n]

        while dl > dr + d[r]:
            dr = dr + d[r]
            r = (r + 1) % n
            l = (l + 1) % n
            zr = zr + z[r]
            zl = zl - z[r]
            c = c + z[r] * (dr - dl)
            dl = dl - d[r]
        if c < min:
            min = c
            min_n = i

    plik.close()
    nameout = name.replace("in\\broin", "out\\broout")
    plikout = open(nameout, "w")
    plikout.write(str(min) + " " + str(min_n))
    plikout.close()


def main():
    pliki = glob.glob("in/*.txt")
    for plik in pliki:
        browar(plik)


if __name__ == "__main__":
    main()
