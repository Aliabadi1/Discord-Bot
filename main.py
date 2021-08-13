import discord
import praw
import random
import os
import requests
import json
client = discord.Client()

reddit = praw.Reddit(client_id ="_MqTuOmbgl0cvv4FoG1Gug", client_secret="lwwRKQJjTeug7rfyKrN2wLhVYNO7fQ", username = "fordiscordbot", password = "password", user_agent = "blank")


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("!meme"):
        subreddit = reddit.subreddit("memes")
        subs = []
        recents = subreddit.top(limit=50)
        for post in recents:
            subs.append(post)
        random_sub = random.choice(subs)
        title = random_sub.title
        url = random_sub.url
        em = discord.Embed(title = title)
        em.set_image(url = url)
        await message.channel.send(embed=em)
        return
    if message.content.startswith('!motivate'):
        quote = generate_quote()
        await message.channel.send(quote + message.author.mention)
    if message.content.startswith('!joke'):
        joke = generate_joke()
        await message.channel.send(joke + message.author.mention)
    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')
        return
    if message.content.startswith('!youtube'):
        await message.channel.send('https://youtube.com/c/' + message.content[9:])
        return
    sad_words = ['sad', 'down bad', 'depressed', 'unhappy', 'miserable', 'angry']
    for x in sad_words:
        if x in message.content and ("im" in message.content or "Im" in message.content or "i'm" in message.content or "I'm" in message.content or "I am" in message.content or "i am" in message.content):
            await message.channel.send("Sometimes you must hurt in order to know, fall in order to grow, lose in order to gain because life’s greatest lessons are taught through pain :slight_smile:")
            return
    if message.content.startswith("!emoji"):
        await message.channel.send(":fire:")
    
    bad_words = ['fuck', 'shit', 'bitch', 'cunt', 'retard', 'ingrate']
    for x in bad_words:
        if x in message.content:
            await message.delete()
            await message.channel.send("Please refrain from using profane language " + message.author.mention + ", message has been taken down")
            return


def generate_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)

def generate_joke():
    response = requests.get(
        'https://api.chucknorris.io/jokes/random')
    joke = json.loads(response.text)
    return(joke['value'])

client.run('ODc1NzUyMTU3Mzg5OTE0MTYz.YRaFwQ.4RwDE7L0akKCU0kF6udLtR2Zq84')