
CAMINHO = r'lista_clientes.csv'

def read_csv(file):
    with open(file,  newline = '',encoding = 'utf-8') as f:
        lines = f.readlines()[1:]
        person_info = [line.strip().split(",") for line in lines]

        print(person_info)
    
    

if __name__ == '__main__':
    print(read_csv(CAMINHO))



