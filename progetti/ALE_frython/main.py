# def ricerca(lines, nome, n_righe_prec, n_righe_succ,):
#     for indice, line in enumerate(lines):
#         if nome in line:

#             for i in range(0,n_righe_prec, -1):    
#                 print(lines[indice + i])
            
#             for i in range(n_righe_succ):
#                 print(lines[indice + i])

            
#                 print("\n-------------------------------------\n")
    


# path = "data/cristallo.out"

# lines: list[str] = []

# with open(path, 'r') as file:
#     for line in file:
#         lines.append(line)

# ricerca(lines, "DIPOLE MOMENT", 3, 2)

# ricerca di ENTROPY
# for indice, line in enumerate(lines):
#     if "ENTROPY" in line and not "TEMPERATURE" in line:
#         print (lines[indice - 1])
#         print (lines[indice])

# best_index = 0
# for indice, line in enumerate(lines):
#     if "HF ENERGY" in line:
#         if indice > best_index:
#             best_index = indice


# print (lines[best_index])
# print (lines[best_index + 1])




def ricerca(lines: list[str], parola: str, n_righe_prec: int, n_righe_succ: int, escludi: str = None):
    risultato = []
    for indice, line in enumerate(lines):
        if parola in line:
            for i in range(-n_righe_prec, 0):
                risultato.append(lines[indice + i][:-2])
            for i in range(n_righe_succ + 1):
                risultato.append(lines[indice + i][:-2])

            risultato.append("------------")

    return risultato


def salvataggio(file_name: str, linee: list[str]):
    with open(file_name, 'w') as file:
        for linea in linee:
            file.write(f"{linea}\n")

path = "data/cristallo.out"

lines: list[str] = []

with open(path, 'r') as file:
    for line in file:
        lines.append(line)

risultati = ricerca(lines, "DIPOLE MOMENT", 2, 2)
salvataggio("data/ris.txt", risultati)
