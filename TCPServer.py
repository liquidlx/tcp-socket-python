#importa o modulo de socket nativo do python
import socket
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('0.0.0.0', 8080))
#Deixa o servidor escutando por novas conexoes no socket.
#O parametro define a quantidade de conexoes que podem estar na fila.
serv.listen(5)

while True:
    #accept() - aceita uma nova conexao e guarda as informacoes de conexao na variavel conn e do cliente na variavel addr
    conn, client = serv.accept()
    #Imprime o endereco IP do cliente
    print "Cliente IP", client
    #conn.send() - Envia uma mensagem para o cliente
    conn.send("Eu sou o servidor.")
    #Imprimindo no console
    print "\nMensagem: 'Eu sou o servidor' enviada.\n"
    #Imprimindo no console
    print "Aguardando resposta\n"
    #Entra em loop para enviar/receber mensagens
    while True:
        #Variavel que guarda a mensagem vinda do cliente atraves do metodo conn.recv()
        #O primeiro parametro da funcao conn.recv() restringe o tamanho permitido, em bytes, da mensagem.
        data = conn.recv(4096)
                
        #Verifica se o cliente nao enviou mensagem.
        if not data: 
            break
        else:
            #Imprime no console a mensagem
            print "Mensagem: '"+data+"' recebida.\n"
    #Fecha conexao com cliente
    conn.close()
    
    print 'Cliente desconectado\n'
