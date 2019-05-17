Criado por: Pedro Igor Ferreira Amorim; Graduando em Engenharia Civil; e-mail: pedro.amorim@ctec.ufal.br

[INTRODUÇÃO]

Este script tem por finalidade o cálculo de valores de posição e velocidade de corpos após sofrerem interação gravitacional. 
Este script tem como base a Lei da gravitação universal e o método de Euler.

[INSTALAÇÃO]

Foram utilizadas as bibliotecas Numpy e matplotlib.pyplot, caso não as tenha instaladas, faz-se necessária a instalação:

pip install numpy

pip install matplotlib.pyplot

[ENTRADA DE DADOS]

Segue um arquivo modelo de entrada de dados junto ao repositório.

!!!ATENÇÃO, NÃO UTILIZAR PASSOS MAIORES QUE 100 POIS ULTRAPASSA O LIMITE DE ITERAÇÕES!!!

[SAÍDA DE DADOS]

O script plota um gráfico em 2D para o conjunto de planetas e um gráfico 3D individual. Além disto, 
é criado um arquivo com o histórico de pontos calculados.

O tamanho do arquivo de histórico vai variar dependendo dos dados de tempo fornecidos.
 