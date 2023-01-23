#! /usr/bin/env python3

def main():

    matrice = [[1,4,9,1,4],[4,8,1,2,5],[4,1,3,4,6],[5,0,4,7,6],[2,4,9,1,5]]
    print(taille(matrice))

def taille(matrice):
    taille = len(matrice[0])

    ret = 0
    for i, row in enumerate(matrice):
        for j, elem in enumerate(row):
            if i == 0 or j == 0 or i == taille - 1 or j == taille - 1:
                continue
            # checks underneath
            if matrice[i + 1][j] >= elem:
                continue
            # checks above
            if matrice[i - 1][j] >= elem:
                continue
            # check left
            if matrice[i][j - 1] >= elem:
                continue
            # check right
            if matrice[i][j + 1] >= elem:
                continue
            ret += 1
    return ret

if __name__ == "__main__":
    main()