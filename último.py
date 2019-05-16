#LÊ OS DADOS DE ENTRADA
import numpy as np
import matplotlib.pyplot as plt
leitura = open('teste.txt','r')
arquivo = leitura.readlines()
nunp = int(arquivo[1])
index = arquivo[2].split(',')
pl = [arquivo[i].split(',') for i in range(3,3+nunp)]
for i in range(0,len(pl)):
    for j in range(0,len(pl[0])):
        pl[i][j] = pl[i][j].strip('\n')
        pl[i][j] = float(pl[i][j]) 
leitura.close()
        
def iteral(pl,count,dt):
    m_for = []
    for i in range(0,len(pl)):    
        aux2 = []
        for j in range(0,len(pl)):            
            aux = []
            raio = ((pl[i][1]-pl[j][1])**2+(pl[i][2]-pl[j][2])**2+(pl[i][3]-pl[j][3])**2)**(1/2)
            for k in range(1,4):
                if i == j:
                    aux = [0 for i in range(0,3)]
                    break    
                aux.append((6.67*10**(-11)*(pl[i][8])*(pl[j][8])*(pl[j][k]-pl[i][k]))/raio**3)
            aux2.append(aux)
        m_for.append(aux2)
        
    m_res = []
    for i in range(0,len(pl)):
        aux = np.array(m_for[i][i])
        for j in range(0,len(pl)):         
            aux = aux + np.array(m_for[i][j])
        m_res.append(aux)
        
    pl_pro = []
    for j in range(0,len(pl)):
        count_pro = []
        aux1 = []
        aux2 = []
        count_pro.append(pl[j][0])
        for i in range(4,7):
            v_pro = pl[j][i] + dt*m_res[j][i-4]/pl[j][8]
            s_pro = pl[j][i-3] + dt*v_pro
            aux1.append(s_pro)
            aux2.append(v_pro)
        for i in range(0,len(pl)):
            count_pro.append(aux1[i])
        for i in range(0,len(pl)):
            count_pro.append(aux2[i])
        for i in range(7,9):
            count_pro.append(pl[j][i])
        pl_pro.append(count_pro)
    
    if count == 100:
        return pl_pro
    count += 1
    return iteral(pl,count,dt)   
   

result = [[] for i in range(0,len(pl))]
for i in range(0,len(pl)):
    result[i].append(index)
parada = 0
passo = int(input('Digite o tamanho do passo: '))
dt = float(input('Digite o tamanho do dt: '))
periodo = int(input('Digite a quantidade de tempo em segundos: '))
while parada < periodo:
    a = iteral(pl,passo,dt)
    for i in range(0,len(pl)):
        result[i].append(a[i])
    pl = a
    parada += dt*passo
    
historico = open('historico.txt','w')
for i in range(0,len(result)):
    for j in range(0,len(result[0])):
        historico.writelines(str(result[i][j]))
        historico.write('\n')
historico.close()

#x = [result[0][i][1] for i in range(1,len(result[0]))]
#y = [result[0][i][2] for i in range(1,len(result[0]))]
#plt.plot(x,y,'r-')
x = [result[1][i][1] for i in range(1,len(result[0]))]
y = [result[1][i][2] for i in range(1,len(result[0]))]
plt.plot(x,y)
#x = [result[2][i][1] for i in range(1,len(result[0]))]
#y = [result[2][i][2] for i in range(1,len(result[0]))]
#plt.plot(x,y,'g-')
plt.show()
    
    













