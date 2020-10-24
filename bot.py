import discord
from secreto import auth
from velha import Velha
from dado import Dado
from forca import Forca

client = discord.Client()
NewGame = Velha()
JogoDaForca = Forca()


@client.event
async def on_ready():
    print("Hello World")
    print(client.user.name)
    print(client.user.id)


@client.event
async def on_message(message):
    if message.content.startswith('.teste'):
        channel = message.channel
        await channel.send("Teste")

    if message.content.startswith(".dado"):
        await message.channel.send(Dado())

    if message.content.lower().find("beco sem saida") != -1:
        await message.channel.send("De novo essa merda")

    if message.content.lower().startswith(".velha"):
        await message.channel.send(NewGame.NovoJogo())

    if message.content.startswith("##"):
        try:
            position = message.content[2:4].upper()
            jogador = message.author.name
            await message.channel.send(NewGame.NovaJogada(position, jogador))
        except:
            await message.channel.send("Deu alguma merda!")

    if message.content.lower().startswith("salve"):
        await message.channel.send("Salvado")
    if message.content.lower().startswith(".forca"):
        await message.channel.send(JogoDaForca.sendTemplate())


@client.event
async def on_message_delete(message):
    await message.channel.send("Pq apagou " + message.author.name + "?")

client.run(auth())
