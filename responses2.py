import random
import openai

openai.api_key = "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"


def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hey there!'

    if message == 'roll':
        return str(random.randint(1, 6))

    if p_message == '!help':
        return '`This is a help message that you can modify.`'
    else:
        response = openai.Completion.create(engine="text-davinci-001",prompt=p_message,max_tokens=6)
        return response
