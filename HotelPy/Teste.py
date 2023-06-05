from model import *
from service import *

def reservar(rsvEdfc, rsvAnd, rsvQat, quartosReservados, listaDeReservas):
    reservado = True
    
    hotel[rsvEdfc - 1][rsvAnd - 1][rsvQat - 1] = reservado
    quartosReservados[1] = (rsvEdfc)
    quartosReservados[3] = (rsvAnd)
    quartosReservados[5] = (rsvQat)
    listaAuxiliar = quartosReservados[:]
    listaDeReservas.append(listaAuxiliar)
    return (quartosReservados, listaDeReservas)




hotel = [[[ False for _ in range(5)] for _ in range(5)] for _ in range(3)]
#print(hotel)
print()

objCliente = clienteService.cadastrarCliente()
objTelefone = telefoneService.cadastrarTelefoneCliente(objCliente)

print(objTelefone.getCliente == objCliente)
print(objTelefone)
primeiroNome = objCliente.getNome().split(None, 1)[0]





qtdReservar = int(input("Olá {nome}, quantos quartos deseja reservar hoje? ".format(nome = primeiroNome)))

quartosReservados = ["Edifício:", 0, "Andar:", 0, "Quarto:", 0]
listaDeReservas = []
reservados = 0
totalQuartos = len(hotel) * len(hotel[0]) * len(hotel[0][0])
quartosDisponiveis = 0
loop = 0

print() 
while loop < qtdReservar:
    quartosDisponiveis = totalQuartos - reservados 
    print()
    print("Quartos já reservados: ", reservados)
    print("Quartos disponíveis: ", quartosDisponiveis)
    print()
    rsvEdfc = int(input("Em qual edifício gostaria de alugar o quarto? (1 à {edificio}): ".format(edificio=len(hotel))))
    rsvAnd  = int(input("Em qual andar gostaria de alugar o quarto? (1 à {andar}): ".format(andar=len(hotel[0]))))
    rsvQat  = int(input("Em qual quarto gostaria de se alojar? (1 à {quarto}): ".format(quarto=len(hotel[0][0]))))
    
    if hotel[rsvEdfc - 1][rsvAnd - 1][rsvQat - 1] == True :
        print("Desculpe, este quarto não está disponível no momento, tente algum outro.")
        continue
    reservar(rsvEdfc, rsvAnd, rsvQat, quartosReservados, listaDeReservas)
    reservados += 1
    loop+=1
    
print("Quartos reservados: ")
for i in listaDeReservas:
    print(i)
    

