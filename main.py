# -*- condig: utf-8 -*-
import random
import lxml
from bs4 import BeautifulSoup
import requests
import discord

url = "https://stats.altfs.ru/hlstats.php"

headers = {
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.47"
}
req = requests.get(url, headers = headers)
src = req.text
soup = BeautifulSoup(src, "lxml")

ip = []
server_info = soup.find(class_ = "data-table").find_all("b")
server_name = server_info[7:]

server_infoip = soup.find_all(class_ = "game-table-row toggler")
for item1 in server_infoip:
    item = item1.find("a").get("href")
    ip.append(item)

players = soup.find_all(class_ = "game-table-cell")
players_count = players[4::8]
server1 = server_name[0].text + "  " + ip[0] + "  " + players_count[0].text
server2 = server_name[1].text + "  " + ip[1] + "  " + players_count[1].text
server3 = server_name[2].text + "  " + ip[2] + "  " + players_count[2].text
server4 = server_name[3].text + "  " + ip[3] + "  " + players_count[3].text
server5 = server_name[4].text + "  " + ip[4] + "  " + players_count[4].text
server6 = server_name[5].text + "  " + ip[5] + "  " + players_count[5].text

servers = []
servers.append(server1)
servers.append(server2)
servers.append(server3)
servers.append(server4)
servers.append(server5)
servers.append(server6)

client = discord.Client()
sinn = ["hello world"]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$lmao'):
        for it in range(10):
            await message.channel.send('test')
    if message.content.startswith('hwtest'):
        for item2 in range(len(sinn)):
            await message.channel.send(sinn[item2])
    if message.content.startswith('altfs'):
        for i in range(len(servers)):
            await message.channel.send(servers[i])

client.run("") # your bot's token