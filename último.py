#LÊ OS DADOS DE ENTRADA
import numpy as np
leitura = open('teste.txt','r')
arquivo = leitura.readlines()
nunp = int(arquivo[1])
index = arquivo[2].split(',')
pl = [arquivo[i].split(',') for i in range(3,3+nunp)]
for i in range(0,len(pl)):
    for j in range(0,len(pl[0])):
        pl[i][j] = pl[i][j].strip('\n')
        pl[i][j] = float(pl[i][j]) 

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

count_pro = []
aux1 = []
aux2 = []
count_pro.append(pl[0][0])
for i in range(3,6):
    v_pro = pl[0][i] + 0.1*m_res[0][i-3]/pl[0][8]
    s_pro = pl[0][i-3] + 0.1*v_pro
    aux1.append(s_pro)
    aux2.append(v_pro)
for i in range(0,3):
    count_pro.append(aux1[i])
for i in range(0,3):
    count_pro.append(aux2[i])
for i in range(7,9):
    count_pro.append(pl[0][i])
    
    
    
        


    
    
        
     