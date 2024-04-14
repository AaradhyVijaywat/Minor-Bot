from random import choice, randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

# All This logic has to be changed or we have to edit it according to our responses
    if lowered == '':
        return 'Well, you\'re awfully silent....'

    elif 'hello' in lowered:
        return 'Hello there!'

    elif 'how are you' in lowered:
        return 'Good, Thanks !'

    elif 'bye' in lowered:
        return 'See you !'

    elif 'roll dice' in lowered:
        return f'You Rolled:{randint(1,6)}'

    else:
        return choice(['I do not Understand...',
                       'What are you talking about ?',
                       'Do you mind rephraseing that?'])
