import discord
import responses
import asyncio
import openai

openai.api_key = "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"


async def send_message(message, user_message, is_private):

    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    token = 'MTA5NTA2NzQyMTg2MzMxNzU3NA.GvUj6Z.IvRGby3EsBBgLEPlueRFGmTG0Tehau6U_YPp8E'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            response = responses.get_response(user_message)
            if response == '':
                response = openai.Completion.create(engine="text-davinci-001", prompt=user_message, max_tokens=6).choices[0].text
            await message.channel.send(response)

    @client.event
    async def on_message(message):
        if message.content.startswith('!remindme'):
            # Parse the message to extract the time and reminder message
            try:
                time, reminder = message.content.split(' ', 2)[1:]
                time = int(time)
            except:
                await message.channel.send('Invalid format. Use `!remindme <time in seconds> <reminder>`')
                return

            # Wait for the specified time
            await asyncio.sleep(time)

            # Send the reminder message
            await message.channel.send(f'Reminder: {reminder}')

    client.run(token)

