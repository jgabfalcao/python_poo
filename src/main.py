from frota import *

def selectcar(carro: Carro):
    print('1- Ligar motor')
    print('2- Desligar motor')
    print('3- Acelerar')

    op = 0
    while op not in (1, 2, 3):
        op = int(input("Selecione a opção[1-3]: "))

    if op == 1:
        carro.ligar()
    elif op == 2:
        carro.desligar()
    elif op == 3:
        v = float(input("Informe a velocidade: "))
        t = float(input("Informe o tempo: "))
        carro.acelerar(v, t)

    print('Infos atuais do carro')
    print(carro)




if __name__ == "__main__":
    print('Cadastre o carro 1')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')

    print('Cadastre o carro 2')
    nm_modelo2 = input('Digite o modelo: ')
    nm_marca2 = input('Digite a marca: ')
    nm_cor2 = input('Digite a cor: ')

    carro1 = Carro(nm_modelo, nm_marca, nm_cor, odometro=0, motor = False)
    carro2 = Carro(nm_modelo2, nm_marca2, nm_cor2, odometro=0, motor=False)

    '''
    Controlando o carro até ele atingir 600 Km
    '''

    while carro1.odometro < 600 and carro2.odometro < 600:
        try:
            opcar = 0
            while opcar not in (1, 2):
                opcar = int(input("Selecione o carro[1-2]: "))

                if opcar == 1:
                    selectcar(carro1)
                elif opcar == 2:
                    selectcar(carro2)

        except Exception as e:
            print("Erro!")
            print(e)

    carro1.desligar()
    carro2.desligar()

    if(carro1.odometro > carro2.odometro):
        print('Carro 1 Vencedor!')
        print(carro1)
    else:
        print('Carro 2 Vencedor!')
        print(carro2)
    print('Parar para trocar óleo!!!')



