import random

pontos_eu = 0
aleatorio = ['pedra', 'papel', 'tesoura']
pc =  random.choice(aleatorio)
pontos_pc = 0
jogo = 0

'''
if eu not in aleatorio:
print('Resposta inválida, tente novamente')
eu = input('pedra, papel ou tesoura?: ')  
estudar mais sobre listas  
'''
for vezes in range(5):
    eu = input('pedra, papel ou tesoura?: ')

    if (eu == 'pedra'and pc == 'tesoura') or (eu == 'papel'and pc == 'pedra') or (eu == 'tesoura'and pc == 'papel'):
     print (pc)
     print ('Eu ganhei uhuuu')
     pontos_eu += 1
     jogo += 1


    elif eu == pc:
      print (pc)
      print('EMPATE')
      jogo += 1

    else:
      print (pc)
      print('PC ganhou!!!')
      pontos_pc += 1
      jogo += 1


    
    if pontos_pc ==3:
         print('O COMPUTADOR FEZ 3 PONTOS')
         break
    elif pontos_eu ==3:
        print('EU FIZ 3 PONTOS')
        break
    elif jogo == 5:
        print('FIM DAS RODADAS')
    else:
        print()
