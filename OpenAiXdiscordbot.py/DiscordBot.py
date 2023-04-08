import os 
import discord
import openai

from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents = intents.all()

TOKEN = os.getenv('DISCORD_TOKEN')
openai.api_key = os.getenv('API_KEY')    # You have to put your api key here

# list engines
engines = openai.Engine.list()

client = discord.Client(intents=intents)


# Global Variable 
prefix = ";"
@client.event   
async def on_ready():
    print(f'{client.user} had connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    if(message.content.startswith(prefix)):
        if message.author == client.user:
            return
        else:
            # Code that need response
            if(message.content.startswith(';prompt')):
                prompt = message.content[7:]
                completion = openai.Completion.create(engine="text-davinci-003",
                                                         prompt=prompt,
                                                         temperature=0.4,
                                                         max_tokens=300,
                                                         top_p=1, 
                                                         frequency_penalty=0,
                                                         presence_penalty=0,
                                                         echo=False)
               
                    
                print(completion.choices[0].text)
                await message.channel.send("```"+completion.choices[0].text+"```")

            elif(message.content.startswith(';image')):
                prompt = message.content[6:]
                ShowImage=openai.Image.create(
                prompt=prompt,
                n=1,
                size="1024x1024")

                print(ShowImage)
                await message.channel.send(ShowImage["data"][0]["url"])
            else:
                response = str(message.content[1:])   # reponse = question !
                print("Message send  : "+str(message.content[1:]))
                choose = "Here is a list of all available command : ``` \n ;promt  \n ;image ``` "
                await message.channel.send(choose)     ## 1
            

            def choix(m):
                prompt = message.content[1:]
                completion = openai.Completion.create(engine="text-davinci-003",
                                                         prompt=prompt,
                                                         temperature=0.4,
                                                         max_tokens=180,
                                                         top_p=1, 
                                                         frequency_penalty=0,
                                                         presence_penalty=0,
                                                         echo=False)
               
                    
                print("Response = "+completion.choices[0].text)
                return completion.choices[0].text

            #msg = await client.wait_for('message',check=choix)
            #await message.channel.send(msg.content)

client.run(TOKEN)
