#importa o modulo de socket nativo do python
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#variavel para guardar o ip do servidor.
ip_server = "127.0.0.1"

#conectando ao servidor com o ip guardado na variavel ip_server na porta 8080.
client.connect((ip_server, 8080))

print "Conectado ao servidor IP", ip_server, "\n"

print "Aguardando resposta do servidor\n"

#Guarda em uma variavel a mensagem do servidor.
from_server = client.recv(4096)

#Imprime no console a mensagem vinda do servidor
print "Mensagem: '"+from_server+"' recebida.\n"

#Envia mensagem ao servidor.
client.send("Eu sou o cliente.")

#Imprime mensagem no console.
print "Mensagem 'Eu sou o cliente' enviada.\n"

#Disconecta do servidor
client.close()