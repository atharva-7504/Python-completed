#Here's a basic Python code for a text-based adventure game:
def describe_room(room):
    print(room['description'])

def get_input():
    return input("> ")

def main():
    rooms = {
        'hall': {
            'description': 'You are in a dimly lit hall.',
            'exits': {'east': 'kitchen', 'west': 'bedroom'}
        },
        'kitchen': {
            'description': 'You are in a messy kitchen.',
            'exits': {'west': 'hall'}
        },
        'bedroom': {
            'description': 'You are in a cozy bedroom.',
            'exits': {'east': 'hall'}
        }
    }

    current_room = 'hall'

    while True:
        describe_room(rooms[current_room])

        action = get_input()

        if action in rooms[current_room]['exits']:
            current_room = rooms[current_room]['exits'][action]
        else:
            print("You can't do that.")




 
