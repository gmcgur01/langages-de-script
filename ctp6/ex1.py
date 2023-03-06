#! /usr/bin/env python3

import re

"""
Motif: A.C 
Chaîne:
  -  "abc": Ça ne correspond pas
  -  "AZZC": Ça ne correspond pas
  -  "AC": Ça ne correspond pas
  -  "ABC": Ça correspond exactement

Motif: [ABC]
Chaîne:
  -  "A": Ça correspond exactement
  -  "B": Ça correspond exactement
  -  "AC": Le debut correspond
  -  "ABC": Le debut correspond

Motif: [a-k].*[1-5]
Chaîne:
  -  "a2": Ça correspond exactement
  -  "A05": Ça ne correspond pas
  -  "ab12": Ça correspond exactement
  -  "k1k": Le debut correspond

Motif: [^a-k].*[1-5]
Chaîne:
  -  "a2": Ça ne correspond pas
  -  "A05": Ça correspond exactement
  -  "ab12": Ça ne correspond pas
  -  "k1k": Ça ne correspond pas

Motif: [a-k].[1-5]{,3}
Chaîne:
  -  "ak1234": Le debut correspond
  -  "a123": Ça correspond exactement
  -  "ad12bd123": Le debut correspond
  -  "z1k": Ça ne correspond pas

Motif: (a?b)+
Chaîne: 
  -  "ababab": Ça correspond exactement
  -  "aaaab": Ça contient une sou-chaîne qui correspond
  -  "bbbbba": Le debut correspond
  -  "bbbab": Ça correspond exactement

Motif: (a|[AB]*)[0-9]
Chaîne:
  -  "aAB0": Ça contient une sou-chaîne qui correspond
  -  "AAB0": Ça correspond exactement
  -  "0": Ça correspond exactement
  -  "A-Z9": Ça contient une sou-chaîne qui correspond

Motif: .\^[^^]+.
Chaîne:
  -  "a^0^0": Le debut correspond
  -  "aa^0^": Ça contient une sou-chaîne qui correspond
  -  "0^^^0": Ça ne correspond pas
  -  "A^Z9": Ça correspond exactement
"""

def main():
    if match := re.fullmatch(r".\^[^^]+.", "A^Z9"):
        print("yes")
        print(match.group(0))
    else:
        print("no")

if __name__ == "__main__":
    main()