import pandas as kungfupanda
import io

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = '\033[0m'  # Reset the color to default

running = 1

print(f"\n")
print(f"{CYAN}### CONTROLS ###{RESET}")
print(f"p = setup path")
print(f"a = decimal. approx")
print(f"q = quit")
print(f"m = mode")

print(f"\n")
print(f"{CYAN}### START SETUP ###{RESET}")
mode = input(f"{RESET}Insert mode (frex = from excel, frpy = from python, topy = to python): {YELLOW}")
folder = input(f"{RESET}Inserisci il nome del progetto: {YELLOW}")
approx = input(f"{RESET}Approssimazione cifre dopo la virgola: {YELLOW}")
print(f"{CYAN}### END SETUP ###{RESET}")

print(f"{RESET}\nInizio main loop...\n\n")

while running:
    path = input(f"{RESET}Nome tabella: {RED}")

    match path:
        case "q": 
            running = 0
            print(f"{GREEN}\nGrazie e alla prossima!\n{RESET}")
        case "a": 
            approx = input(f"{RESET}Approssimazione cifre dopo la virgola: {YELLOW}")
        case "p": 
            folder = input(f"{RESET}Inserisci folder path: {YELLOW}")
        case "m":
            mode = input(f"{RESET}(frex = from excel, frpy = from python, topy = to python) {YELLOW}")
        case _:

            path_completo = f"./progetti/{folder}/latex_subfile/{path}.tex"

            df = kungfupanda.read_clipboard(sep="\t")

            if mode == "frex":
                df.to_latex(path_completo, index=False, float_format=f'%.{approx}f')	
                print(f"{GREEN}Salvato con successo in: {path_completo}!\n{RESET}")
            
            elif mode == "frpy":

                # import data as string
                data_string = df.to_string(index=False)
                
                # remove blank spaces
                data_string = data_string.strip()
                
                # divide in columns
                columns = data_string.split("\n")

                # divide in name and values
                names = [column.split("=")[0] for column in columns]
                values = [column.split("=")[1] for column in columns]

                # format values : remove blank spaces
                names = [name.strip() for name in names]
                values = [value.strip() for value in values]
                
                # format values : remove brackets and np.array()
                values = [value.replace(")", "") for value in values if "np.array" in value]
                values = [value.replace("np.array(", "") for value in values if "np.array" in value]
                values = [value[1:-1] for value in values]

                # format values : divide values
                values = [value.split(",") for value in values]

                # format values : transposing data
                values = list(zip(*values))

                output = ""
                for index, name in enumerate(names):
                    if index != len(names) - 1: output += f"{name}\t"
                    elif index == len(names) - 1: output += f"{name}\n"
                
                # formatted data
                for value in values:
                    for index, elemento in enumerate(value):
                        if index != len(value) - 1: output += f"{float(elemento) if '.' in elemento else int(elemento)}\t"
                        elif index == len(value) - 1: output += f"{float(elemento) if '.' in elemento else int(elemento)}\n"

                print(output)
                df = kungfupanda.read_csv(io.StringIO(output), sep="\t")
                df.to_latex(path_completo, index=False, float_format=f'%.{approx}f')	
                print(f"{GREEN}Salvato con successo in: {path_completo}!\n{RESET}")

            elif mode == "topy":
                df.replace(",", ".", regex=True, inplace=True)
                data = df.to_numpy(float)
                len_data = data.shape[1]
                
                titoli = str(df).split("\n")[0].split()
                
                for i in range(len_data):
                    print(f"{titoli[i]} = np.array({list(data[:,i])})")
