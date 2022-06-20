# Codificação em Imagens
###### Código desenvolvido na disciplina MC920 - Introdução ao Processamento de Imagem Digital


O projeto tem como objetivo codificar e decoficar uma mensagem textual em um plano de bit de uma imagem. Para codificação cada caractere da mensagem é convertido pro inteiro correspondendo no código Unicode e depois passado pra binário. No final da mensagem é adicionado o binário equivalente à '\0' para sinalizar  o fim da mensagem. Cada bit da nova sequência é então substituído nos bits da imagem no plano de bits escolhido. Além de retornar a imagem contendo a mensagem codificada o programa também salva imagens do plano de bits 0, 1, 2 e 7 para observação.
Para decodificação, dada uma imagem contendo uma mensagem e o plano de bits que essa mensagem está contida, o programa retorna a mensagem já descodificada. 

## Parametros 
#### Codificação 
*py codificar.py [imagem] [arquivo com a mensagem a ser codificada] [plano de bits(0-7)] [nome da imagem resultante]*
#### Decodificação
*py decodificar.py [imagem com texto codificado] [plano de bits da mensagem(0-7)] [arquivo para salvar a mensagem descodificada]*
