import numpy as np
import matplotlib.pyplot as plt

#DECLARAÇÃO DAS CONSTANTES UTILIZADAS
nome = input('Digite o nome do arquivo: ')
leitura = open(nome,'r')
arquivo = leitura.readlines()
nunp = int(arquivo[1])
nunc = int(arquivo[4+nunp])
index = arquivo[2].split(',')
parada = 0

#MÓDULO DE ENTRADA DE DADOS

#DADOS DOS PLANETAS
pl = [arquivo[i].split(',') for i in range(3,3+nunp)] 
for i in range(0,len(pl)):
    for j in range(0,len(pl[0])):
        pl[i][j] = pl[i][j].strip('\n')
        pl[i][j] = float(pl[i][j])

#DADOS DA MATRIZ DE ÍNDICES DE COLISÃO
ch_mat = [arquivo[i].split(' ') for i in range(6+nunp+nunc,6+2*nunp+nunc)]
for i in range(0,len(ch_mat)):
    for j in range(0,len(ch_mat)):
        ch_mat[i][j] = int(ch_mat[i][j])
        
#DADOS DO VETOR DE CONSTANTES DE COLISÃO
ch_vet = [arquivo[i].split(',') for i in range(5+nunp,5+nunp+nunc)]
for i in range(0,len(ch_vet)):
    for j in range(0,len(ch_vet)):
        ch_vet[i][j] = int(ch_vet[i][j])

#DADOS DE TEMPO
timer = [arquivo[i].split(',') for i in range(7+2*nunp+nunc,8+2*nunp+nunc)]
for i in range(0,3):
    timer[0][i] = float(timer[0][i])
leitura.close()
  
#MÓDULO DE ANÁLISE      

def iteral(pl,count,dt):
    #CALCULA RECURSIVAMENTE OS PONTOS DO PASSO DADO        
    m_for = []
    #CRIA A MATRIZ DE FORÇA
    for i in range(0,len(pl)):    
        aux2 = []
        for j in range(0,len(pl)):            
            aux = []
            raio = ((pl[i][1]-pl[j][1])**2+(pl[i][2]-pl[j][2])**2+(pl[i][3]-pl[j][3])**2)**(1/2) #DISTÂNCIA ENTRE OS PLANETAS DA ITERAÇÃO
            for k in range(1,4):
                if i == j: 
                    aux = [0 for i in range(0,3)]
                    break    
                if raio < pl[i][7] or raio < pl[j][7]: #VERIFICAÇÃO DE COLISÃO
                    dx = abs(raio - pl[i][7] - pl[j][7])
                    f_ch = (-1)*dx*ch_vet[ch_mat[i][j]-1][1]*(pl[j][k]-pl[i][k])/raio
                    aux.append((6.67*10**(-11)*(pl[i][8])*(pl[j][8])*(pl[j][k]-pl[i][k]))/raio**3 + f_ch)                     
                else:
                    aux.append((6.67*10**(-11)*(pl[i][8])*(pl[j][8])*(pl[j][k]-pl[i][k]))/raio**3)
            aux2.append(aux)
        m_for.append(aux2)
    
    #CRIA O VETOR DE FORÇA RESULTANTE    
    m_res = []
    for i in range(0,len(pl)):
        aux = np.array(m_for[i][i])
        for j in range(0,len(pl)):         
            aux = aux + np.array(m_for[i][j])
        m_res.append(aux)
    
    #CALCULA O PRÓXIMO VALOR DE POSIÇÃO E VELOCIDADE  
    pl_pro = []
    for j in range(0,len(pl)):
        count_pro = []
        aux1 = []
        aux2 = []
        count_pro.append(pl[j][0])
        
        #MÉTODO DE EULER
        for i in range(4,7):
            v_pro = pl[j][i] + dt*m_res[j][i-4]/pl[j][8]
            s_pro = pl[j][i-3] + dt*v_pro
            aux1.append(s_pro)
            aux2.append(v_pro)
        
        #PREPARA O FORMATO DE SAÍDA DO PONTO PARA A PRÓXIMA ITERAÇÃO
        for i in range(0,3):
            count_pro.append(aux1[i])
        for i in range(0,3):
            count_pro.append(aux2[i])
        for i in range(7,9):
            count_pro.append(pl[j][i])
        pl_pro.append(count_pro)
    
    #VERIFICA O FIM DO PASSO
    if count == 100:
        return pl_pro
    count += 1
    
    return iteral(pl,count,dt)      

#PREPADA O ÍNDICE DOS VALORES DE SAÍDA
result = [[] for i in range(0,len(pl))]
for i in range(0,len(pl)):
    result[i].append(index)

#FAZ A CHAMADA DA DEF QUE CALCULA OS PRÓXIMOS VALORES
while parada < timer[0][2]:
    aux = iteral(pl,timer[0][0],timer[0][1])
    for i in range(0,len(pl)):
        result[i].append(aux[i])
    pl = aux
    parada += timer[0][1]*timer[0][0]

#MÓDULO DE VISUALIZAÇÃO    

#IMPRESSÃO DO HISTÓRICO DE PONTOS    
historico = open('historico.txt','w')
for i in range(0,len(result)):
    for j in range(0,len(result[0])):
        historico.writelines(str(result[i][j]))
        historico.write('\n')
historico.close()

#PLOT DOS PONTOS EM 2D
for j in range(0,len(pl)):
    x = [result[j][i][1] for i in range(1,len(result[0]))]
    y = [result[j][i][2] for i in range(1,len(result[0]))]
    z = [result[j][i][3] for i in range(1,len(result[0]))]    
    plt.plot(x,y)
plt.show()

#PLOT DE CADA PLANETA EM 3D
for j in range(0,len(pl)):
    x = [result[j][i][1] for i in range(1,len(result[0]))]
    y = [result[j][i][2] for i in range(1,len(result[0]))]
    z = [result[j][i][3] for i in range(1,len(result[0]))]    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = '3d')
    ax.scatter(x, y, z)
    plt.show()
    
    
    











