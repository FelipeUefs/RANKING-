##/*******************************************************************************
#Autor: Felipe Gomes da Silva
#Componente Curricular: Algoritmos I
#Concluido em: 17/09/2024
#Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
#trecho de código de outro colega ou de outro autor, tais como provindos de livros e
#apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
#de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
#do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
#******************************************************************************************/
#SISTEMA OPERACIONAL: WINDOWS 10

#ENTRADA DE PESO DAS QUESTÕES E NOMES DAS EQUIPES QUE IRÃO PARTICIPAR DO TORNEIO:
print('Defina a pontuação dos Desafios e Nomes das Equipes:')
peso_faceis = float(input('Digite o peso da questão fácil: '))
peso_medias = float(input('Digite o peso da questão média: '))
peso_dificeis = float(input('Digite o peso da questão difícil: '))
equipe1 = input('\nNome da EQUIPE 1: \n')
equipe2 = input('Nome da EQUIPE 2: \n')
equipe3 = input('Nome da EQUIPE 3: \n')
equipe4 = input('Nome da EQUIPE 4: \n')
equipe5 = input('Nome da EQUIPE 5: \n')

#DEFINIÇÃO DAS VARIAVEIS PARA DEFINIR O RANKING E SUAS DEVIDAS PONTUAÇÕES:
rank1 = rank2 = rank3 = rank4 = rank5 = ''
pontos_rank1 = pontos_rank2 = pontos_rank3 = ''
pontos_rank4 = pontos_rank5 = ''
faceis_rank1 = faceis_rank2 = faceis_rank3 = ''
faceis_rank4 = facies_rank5 = ''
medias_rank1 = medias_rank2 = medias_rank3 = ''
medias_rank4 = medias_rank5 = ''

#CRITERIOS DE DESEMPATE, CASO HAJA ALGUM EMPATE EM PONTUAÇÕES OU QUESTÕES DIFICEIS
dificeis_rank1 = dificeis_rank2 = dificeis_rank3 = dificeis_rank4 = dificeis_rank5 = int()
time_rank1 = time_rank2 = time_rank3 = time_rank4 = time_rank5 = int()
mais_dif = ''
rank_dif = ''
#MENU DE SELEÇÃO DAS EQUIPES, PARA ADICIONAR AS INFORMAÇÕES DE CADA EQUIPE BASTA SELECIONAR UM NÚMERO:
num = 0
while num != '6':
    num = input(f'\nSelecione qual equipe deseja inserir os dados:\n'
                f'[1] EQUIPE 1: {equipe1}\n'
                f'[2] EQUIPE 2: {equipe2}\n'
                f'[3] EQUIPE 3: {equipe3}\n'
                f'[4] EQUIPE 4: {equipe4}\n'
                f'[5] EQUIPE 5: {equipe5}\n'
                f'[6] ENCERRAR\n')
    
    #EQUIPE 1 E TODAS AS INFORMAÇÕES PARA O RANK SER GERADO:
    if num == '1': 
        print(f'EQUIPE [{equipe1}]')
        quest_faceis = int(input('Questões fáceis corretas: '))
        quest_medias = int(input('Questões médias corretas: '))
        quest_dificil = int(input('Questões difíceis corretas: '))
        time1 = int(input('Tempo gasto pra finalizar (em min): '))
        pontos1 = (quest_faceis * peso_faceis + quest_medias * peso_medias + quest_dificil * peso_dificeis)
        rank1, pontos_rank1, faceis_rank1, medias_rank1, dificeis_rank1, time_rank1  = equipe1, pontos1, quest_faceis, quest_medias, quest_dificil, time1
    
    #EQUIPE 2 E TODAS AS INFORMAÇÕES PARA O RANK SER GERADO:
    if num == '2':
        print(f'EQUIPE [{equipe2}]')
        quest_faceis_2 = int(input('Questões fáceis corretas: '))
        quest_medias_2 = int(input('Questões médias corretas: '))
        quest_dificil_2 = int(input('Questões difíceis corretas: '))
        time2 = int(input('Tempo gasto pra finalizar (em min): '))
        pontos2 = (quest_faceis_2 * peso_faceis + quest_medias_2 * peso_medias + quest_dificil_2 * peso_dificeis)
        rank2 = '' 
        if pontos2 > pontos_rank1  or (pontos2 == pontos_rank1 and (dificeis_rank2 > dificeis_rank1 or (pontos2 == pontos_rank1 and dificeis_rank2 == dificeis_rank1 and time2 < time_rank1))):
            rank2, pontos_rank2, faceis_rank2, medias_rank2, dificeis_rank2, time_rank2 = rank1, pontos_rank1,faceis_rank1, medias_rank1, dificeis_rank1, time_rank1
            rank1, pontos_rank1, faceis_rank1, medias_rank1, dificeis_rank1, time_rank1  = equipe2, pontos2, quest_faceis_2, quest_medias_2, quest_dificil_2, time2
        else:
            rank2, pontos_rank2, faceis_rank2 , medias_rank2, dificeis_rank2, time_rank2 = equipe2, pontos2, quest_faceis_2, quest_medias_2, quest_dificil_2, time2

    #EQUIPE 3 E TODAS AS INFORMAÇÕES PARA O RANK SER GERADO: 
    if num == '3':
        print(f'EQUIPE [{equipe3}]')
        quest_faceis_3 = int(input('Questões fáceis corretas: '))
        quest_medias_3 = int(input('Questões médias corretas: '))
        quest_dificil_3 = int(input('Questões difíceis corretas: '))
        time3 = int(input('Tempo gasto pra finalizar (em min): '))
        pontos3 = (quest_faceis_3 * peso_faceis + quest_medias_3 * peso_medias + quest_dificil_3 * peso_dificeis)
        rank3 = ''
        if pontos3 > pontos_rank1 or (pontos3 == pontos_rank1 and (dificeis_rank3 > dificeis_rank1 or (pontos3 == pontos_rank1 and dificeis_rank3 == dificeis_rank1 and time3 < time_rank1))):
            rank3, pontos_rank3, faceis_rank3, medias_rank3, dificeis_rank3, time_rank3 = rank2, pontos_rank2, faceis_rank2 , medias_rank2, dificeis_rank2, time_rank2
            rank2, pontos_rank2, faceis_rank2, medias_rank2, dificeis_rank2, time_rank2 = rank1, pontos_rank1, faceis_rank1, medias_rank1, dificeis_rank1, time_rank1
            rank1, pontos_rank1, faceis_rank1, medias_rank1, dificeis_rank1, time_rank1 = equipe3, pontos3, quest_faceis_3, quest_medias_3, quest_dificil_3, time3
        elif pontos3 > pontos_rank2 or (pontos3 == pontos_rank2 and (dificeis_rank3 > dificeis_rank2 or (pontos3 == pontos_rank2 and dificeis_rank3 == dificeis_rank2 and time3 < time_rank2))):
            rank3, pontos_rank3, faceis_rank3, medias_rank3, dificeis_rank3, time_rank3 = rank2, pontos_rank2, faceis_rank2 , medias_rank2, dificeis_rank2, time_rank2
            rank2, pontos_rank2, faceis_rank2, medias_rank2, dificeis_rank2, time_rank2 = equipe3, pontos3, quest_faceis_3, quest_medias_3, quest_dificil_3, time3
        else:
            rank3, pontos_rank3, faceis_rank3, medias_rank3, dificeis_rank3, time_rank3 = equipe3, pontos3, quest_faceis_3, quest_medias_3, quest_dificil_3, time3
    
    #EQUIPE 4 E TODAS AS INFORMAÇÕES PARA O RANK SER GERADO:
    if num == '4':
        print(f'EQUIPE [{equipe4}]')
        quest_faceis_4 = int(input('Questões fáceis corretas: '))
        quest_medias_4 = int(input('Questões médias corretas: '))
        quest_dificil_4 = int(input('Questões difíceis corretas: '))
        time4 = int(input('Tempo gasto pra finalizar (em min): '))
        pontos4 = (quest_faceis_4 * peso_faceis + quest_medias_4 * peso_medias + quest_dificil_4 * peso_dificeis)
        rank4 = ''

        if pontos4 > pontos_rank1 or (pontos4 == pontos_rank1 and (dificeis_rank4 > dificeis_rank1 or (pontos4 == pontos_rank1 and dificeis_rank4 == dificeis_rank1 and time4 < time_rank1))):
            rank4, pontos_rank4, faceis_rank4, medias_rank4, dificeis_rank4, time_rank4 = rank3, pontos_rank3, faceis_rank3, medias_rank3, dificeis_rank3, time_rank3
            rank3, pontos_rank3, faceis_rank3, medias_rank3, dificeis_rank3, time_rank3 = rank2, pontos_rank2, faceis_rank2, medias_rank2, dificeis_rank2, time_rank2
            rank2, pontos_rank2, faceis_rank2, medias_rank2, dificeis_rank2, time_rank2 = rank1, pontos_rank1, faceis_rank1, medias_rank1, dificeis_rank1, time_rank1
            rank1, pontos_rank1, faceis_rank1, medias_rank1, dificeis_rank1, time_rank1 = equipe4, pontos4, quest_faceis_4, quest_medias_4, quest_dificil_4, time4
        elif pontos4 > pontos_rank2 or (pontos4 == pontos_rank2 and (dificeis_rank4 > dificeis_rank2 or (pontos4 == pontos_rank2 and dificeis_rank4 == dificeis_rank2 and time4 < time_rank2))):
            rank4, pontos_rank4, faceis_rank4, medias_rank4, dificeis_rank4, time_rank4 = rank3, pontos_rank3, faceis_rank3, medias_rank3, dificeis_rank3, time_rank3
            rank3, pontos_rank3, faceis_rank3, medias_rank3, dificeis_rank3, time_rank3 = rank2, pontos_rank2, faceis_rank2, medias_rank2, dificeis_rank2, time_rank2
            rank2, pontos_rank2, faceis_rank2, medias_rank2, dificeis_rank2, time_rank2 = equipe4, pontos4, quest_faceis_4, quest_medias_4, quest_dificil_4, time4
        elif pontos4 > pontos_rank3 or (pontos4 == pontos_rank3 and (dificeis_rank4 > dificeis_rank3 or (pontos4 == pontos_rank3 and dificeis_rank4 == dificeis_rank3 and time4 < time_rank3))):
            rank4, pontos_rank4, faceis_rank4, medias_rank4, dificeis_rank4, time_rank4 = rank3, pontos_rank3, faceis_rank3, medias_rank3, dificeis_rank3, time_rank3
            rank3, pontos_rank3, faceis_rank3, medias_rank3, dificeis_rank3, time_rank3 = equipe4, pontos4, quest_faceis_4, quest_medias_4, quest_dificil_4, time4
        else:
            rank4, pontos_rank4, faceis_rank4, medias_rank4, dificeis_rank4, time_rank4 = equipe4, pontos4, quest_faceis_4, quest_medias_4, quest_dificil_4, time4
    
    #EQUIPE 5 E TODAS AS INFORMAÇÕES PARA O RANK SER GERADO: 
    if num == '5':
        print(f'EQUIPE [{equipe5}]')
        quest_faceis_5 = int(input('Questões fáceis corretas: '))
        quest_medias_5 = int(input('Questões médias corretas: '))
        quest_dificil_5 = int(input('Questões difíceis corretas: '))
        time5 = int(input('Tempo gasto pra finalizar (em min): '))
        pontos5 = (quest_faceis_5 * peso_faceis + quest_medias_5 * peso_medias + quest_dificil_5 * peso_dificeis)
        rank5 = ''
        if pontos5 > pontos_rank1 or (pontos5 == pontos_rank1 and (dificeis_rank5 > dificeis_rank1 or (pontos5 == pontos_rank1 and dificeis_rank5 == dificeis_rank1 and time5 < time_rank1))):
            rank5, pontos_rank5, faceis_rank5, medias_rank5, dificeis_rank5, time_rank5 = rank4, pontos_rank4, faceis_rank4, medias_rank4, dificeis_rank4, time_rank4
            rank4, pontos_rank4, faceis_rank4, medias_rank4, dificeis_rank4, time_rank4 = rank3, pontos_rank3, faceis_rank3, medias_rank3, dificeis_rank3, time_rank3
            rank3, pontos_rank3, faceis_rank3, medias_rank3, dificeis_rank3, time_rank3 = rank2, pontos_rank2, faceis_rank2, medias_rank2, dificeis_rank2, time_rank2
            rank2, pontos_rank2, faceis_rank2, medias_rank2, dificeis_rank2, time_rank2 = rank1, pontos_rank1, faceis_rank1, medias_rank1, dificeis_rank1, time_rank1
            rank1, pontos_rank1, faceis_rank1, medias_rank1, dificeis_rank1, time_rank1 = equipe5, pontos5, quest_faceis_5, quest_medias_5, quest_dificil_5, time5
        elif pontos5 > pontos_rank2 or (pontos5 == pontos_rank2 and (dificeis_rank5 > dificeis_rank2 or (pontos5 == pontos_rank2 and dificeis_rank5 == dificeis_rank2 and time5 < time_rank2))):
            rank5, pontos_rank5, faceis_rank5, medias_rank5, dificeis_rank5, time_rank5 = rank4, pontos_rank4, faceis_rank4, medias_rank4, dificeis_rank4, time_rank4
            rank4, pontos_rank4, faceis_rank4, medias_rank4, dificeis_rank4, time_rank4 = rank3, pontos_rank3, faceis_rank3, medias_rank3, dificeis_rank3, time_rank3
            rank3, pontos_rank3, faceis_rank3, medias_rank3, dificeis_rank3, time_rank3 = rank2, pontos_rank2, faceis_rank2, medias_rank2, dificeis_rank2, time_rank2
            rank2, pontos_rank2, faceis_rank2, medias_rank2, dificeis_rank2, time_rank2 = equipe5, pontos5, quest_faceis_5, quest_medias_5, quest_dificil_5, time5
        elif pontos5 > pontos_rank3 or (pontos5 == pontos_rank3 and (dificeis_rank5 > dificeis_rank3 or (pontos5 == pontos_rank3 and dificeis_rank5 == dificeis_rank3 and time5 < time_rank3))):
            rank5, pontos_rank5, faceis_rank5, medias_rank5, dificeis_rank5, time_rank5 = rank4, pontos_rank4, faceis_rank4, medias_rank4, dificeis_rank4, time_rank4
            rank4, pontos_rank4, faceis_rank4, medias_rank4, dificeis_rank4, time_rank4 = rank3, pontos_rank3, faceis_rank3, medias_rank3, dificeis_rank3, time_rank3
            rank3, pontos_rank3, faceis_rank3, medias_rank3, dificeis_rank3, time_rank3 = equipe5, pontos5, quest_faceis_5, quest_medias_5, quest_dificil_5, time5
        elif pontos5 > pontos_rank4 or (pontos5 == pontos_rank4 and (dificeis_rank5 > dificeis_rank4 or (pontos5 == pontos_rank4 and dificeis_rank5 == dificeis_rank4 and time5 < time_rank4))):
            rank5, pontos_rank5, faceis_rank5, medias_rank5, dificeis_rank5, time_rank5 = rank4, pontos_rank4, faceis_rank4, medias_rank4, dificeis_rank4, time_rank4
            rank4, pontos_rank4, faceis_rank4, medias_rank4, dificeis_rank4, time_rank4 = equipe5, pontos5, quest_faceis_5, quest_medias_5, quest_dificil_5, time5
        else:
            rank5, pontos_rank5, faceis_rank5, medias_rank5, dificeis_rank5, time_rank5 = equipe5, pontos5, quest_faceis_5, quest_medias_5, quest_dificil_5, time5
            
#BLOCOS DE IF PARA DEFINIR A EQUIPE COM MAIS ACERTOS DIFICEIS
if quest_dificil == quest_dificil:
        rank_dif = equipe1
        mais_dif = quest_dificil
if quest_dificil_2 > quest_dificil and quest_dificil_2 > quest_dificil_3 and quest_dificil_2 > quest_dificil_4 and quest_dificil_2 > quest_dificil_5:
        rank_dif = equipe2
        mais_dif = quest_dificil_2
if quest_dificil_3 > quest_dificil and quest_dificil_3 > quest_dificil_2 and quest_dificil_3 > quest_dificil_4 and quest_dificil_3 > quest_dificil_5:
        rank_dif = equipe3
        mais_dif = quest_dificil_3
if quest_dificil_4 > quest_dificil and quest_dificil_4 > quest_dificil_2 and quest_dificil_4 > quest_dificil_3 and quest_dificil_4 > quest_dificil_5:
        rank_dif = equipe4
        mais_dif = quest_dificil_4
if quest_dificil_5 > quest_dificil and quest_dificil_5 > quest_dificil_2 and quest_dificil_5 > quest_dificil_3 and quest_dificil_5 > quest_dificil_4:
        rank_dif = equipe5
        mais_dif = quest_dificil_5

#CALCULO DA MÉDIA DE PONTOS DAS EQUIPES
media = ((pontos1 + pontos2 + pontos3 + pontos4 + pontos5) / 5)

#TABELA DE RANKING DAS EQUIPES 
print('\nTABELA DE RANKING DAS EQUIPES')
print('\nRanking\tEquipe\tPontos\tTempo\tFaceis\tMédias\tDificeis')
print(f'[1º]\t{rank1}\t{pontos_rank1}\t{time_rank1} min\t{faceis_rank1}\t{medias_rank1}\t{dificeis_rank1}')
print(f'[2º]\t{rank2}\t{pontos_rank2}\t{time_rank2} min\t{faceis_rank2}\t{medias_rank2}\t{dificeis_rank2}')
print(f'[3º]\t{rank3}\t{pontos_rank3}\t{time_rank3} min\t{faceis_rank3}\t{medias_rank3}\t{dificeis_rank3}')
print(f'[4º]\t{rank4}\t{pontos_rank4}\t{time_rank4} min\t{faceis_rank4}\t{medias_rank4}\t{dificeis_rank4}')
print(f'[5º]\t{rank5}\t{pontos_rank5}\t{time_rank5} min\t{faceis_rank5}\t{medias_rank5}\t{dificeis_rank5}')
print(f'\nMedia por equipe: {media}')
print(f"\nA equipe {rank_dif}, teve mais acertos Dificeis, totalizando {mais_dif} questões corretas.")
print(f'\nA EQUIPE VENCEDORA É A EQUIPE [{rank1}] COM {pontos_rank1} PONTOS E {dificeis_rank1} QUESTÕES DIFICEIS ACERTADAS!')