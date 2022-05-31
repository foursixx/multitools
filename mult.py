from http import client
from importlib.metadata import requires
import discord
from discord.ext import commands
import requests
import time
from operator import indexOf
import os
import socket 

os.system("cls")

root = input("Digite um nome para o seu root: ")
print("\n")

print("Carregando aguarde....")
time.sleep(1)


os.system("cls")
time.sleep(1)

print("Criador: 4six\n")

print("""


                ---------------------------------------------------------------------------------------------
                |                                                                                           |
                |       portscanner - Verificar as portas abertas/fechadas do site    !                     |
                |       cleardiscord - Apagar mensagem do discord  !                                        |
                |       discordtoken - Gerar varios token do discord !                                      |    
                |       cep - Ver as informações do cep informado !                                         |
                |       ip - Ver as informações do ip informado!                                            |
                |       pingip - Pingar o ip !                                                              |
                |                                                                                           |
                |                                                                                           |
                |                                                                                           |
                |                                                                                           |
                |                                                                                           |
                |                                                                                           |
                |                                                                                           |
                ---------------------------------------------------------------------------------------------






""")

msg = input(f"[root@{root}] $ ")

if msg == "portscanner":
    site = input("Digite a url do site: ")
    os.system("cls")
    portas = [80, 443, 21, 22, 23, 25, 3306]
    for i in portas:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.1)
        codigo = client.connect_ex((site, i))
        if codigo == 0:
            print(i, "[+] Porta Aberta")
        else:
            print(i, "[+] Porta Fechada")
if msg == "cep":
    os.system("cls")
    cep = input("Informe o CEP: ")
    r = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    data = r.json()

    print('CEP: {}'.format(data['cep']))
    print('Bairro: {}'.format(data['bairro']))
    print('Cidade: {}'.format(data['localidade']))
    
if msg == "discordtoken":
    os.system("cls")
    rr = requests.get('https://some-random-api.ml/bottoken')
    dataa = rr.text
    print(dataa)

if msg == "ip":
    os.system("cls")
    import urllib.request, json
    ip = input("Digite o ip: ")
    with urllib.request.urlopen(f"https://ipinfo.io/{ip}/json") as url:
        dados = json.loads(url.read().decode())

    print("\n")
    print("-"*35)
    print('IP: ' + dados['ip'])
    print("\n")
    print('Cidade: ' + dados['city'] + ' | Região: ' + dados['region'] + ' | País: ' + dados['country'])
    print("-"*35)
    print("\n")
    print('Endereço Postal: ' + dados['postal'])
    print("-"*35)
    print("\n")
    print('TimeZone: ' + dados['timezone'])
    print("-"*35)

if msg == "pingip":
    os.system("cls")
    pingip = input("Digite o ip que quer pingar: ")
    os.system(f"ping -t {pingip}")
    
if msg == "cleardiscord":
    os.system("cls")
    print("[+] Clear Discord\n")

    token = input("[-] Digite seu token: ")
    prefix = input("[-] Digite o prefixo: ")

    os.system("cls")


    bot  = commands.Bot(command_prefix=prefix, self_bot=True)
    bot .remove_command("help")

    @bot.event
    async def on_ready():
        print("[+] Seja bem vindo")

        print(f"        Usuario: {bot.user.name}         ")

    @bot.command()
    async def clear(ctx, limit: int=None):
        passed = 0
        failed = 0
        async for msg in ctx.message.channel.history(limit=limit):
            if msg.author.id == bot.user.id:
                try:
                    await msg.delete()
                    passed += 1
                except:
                    failed += 1
                    print(f"[Completado] Removi {passed} Mensagens com sucesso! ")

    bot.run(token, bot=False)

