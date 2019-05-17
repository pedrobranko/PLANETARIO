Criado por: Pedro Igor Ferreira Amorim; Graduando em Engenharia Civil; e-mail: pedro.amorim@ctec.ufal.br

[INTRODU��O]

Este script tem por finalidade o c�lculo de valores de posi��o e velocidade de corpos ap�s sofrerem intera��o gravitacional. 
Este script tem como base a Lei da gravita��o universal e o m�todo de Euler.

[INSTALA��O]

Foram utilizadas as bibliotecas Numpy e matplotlib.pyplot, caso n�o as tenha instaladas, faz-se necess�ria a instala��o:

pip install numpy

pip install matplotlib.pyplot

[ENTRADA DE DADOS]

Segue um arquivo modelo de entrada de dados junto ao reposit�rio.

!!!ATEN��O, N�O UTILIZAR PASSOS MAIORES QUE 100 POIS ULTRAPASSA O LIMITE DE ITERA��ES!!!

[SA�DA DE DADOS]

O script plota um gr�fico em 2D para o conjunto de planetas e um gr�fico 3D individual. Al�m disto, 
� criado um arquivo com o hist�rico de pontos calculados.

O tamanho do arquivo de hist�rico vai variar dependendo dos dados de tempo fornecidos.
 