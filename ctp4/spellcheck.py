#! /usr/bin/env python3

import sys

def main():
    if len(sys.argv) != 3:
        sys.exit(f"Usage: {sys.argv[0]} <nomdico> <fichetexte>")
    
    dico = populate_dico(sys.argv[1])

    spell_check(dico, sys.argv[2])

def populate_dico(nomdico):
    try:
        with open(nomdico) as file:
            return {line.lower().strip() for line in file}
    except FileNotFoundError:
        sys.exit(f"{nomdico}: Unable to open file")

def spell_check(dico, fichetexte):
    try:
        with open(fichetexte) as file:

            *file_name, file_type = fichetexte.split(".")
            output = open(file_name[0] + "\_corrige." + file_type, "w")

            for line in file:
                new_line = []
                curr_word = ""
                for char in line:
                    # probably still some bugs but I'm over it
                    if char.isalpha():
                        curr_word += char
                    elif char == "'":
                        curr_word += char
                        if curr_word.lower() in dico:
                            output.write(curr_word)
                        else:
                            output.write(f"**{curr_word}**")
                        curr_word = ""
                    else:
                        if curr_word != "":
                            if curr_word.lower() in dico:
                                output.write(curr_word)
                            else:
                                output.write(f"**{curr_word}**")
                            curr_word = ""
                        output.write(char)

            output.close()

    except FileNotFoundError:
        sys.exit(f"{fichetexte}: Unable to open file")

if __name__ == "__main__":
    main()