"""Otter Greeting Generator

This script allows you to greet otters with different levels of enthusiasm.
"""

import click

@click.command()
@click.option('--count', default=1, help='Number of otter greetings.')
@click.option('--name', prompt='Your name', help='The person to greet.')
@click.option('--enthusiasm', type=click.Choice(['low', 'medium', 'high']), 
              default='medium', help='How enthusiastic should the otters be?')
@click.option('--output', default='greetings.txt', help='Output file to append greetings to.')
def greet_otters(count, name, enthusiasm, output):
    """ Otter greeting generator
    
    Simple program that has adorable otters greet NAME for COUNT times. 🦦
    
    Parameters
    ----------
    count : int
        Number of otter greetings to display. Must be a positive integer.
        Default is 1.
    name : str
        The name of the person to greet. Will be prompted if not provided
        via command line.
    enthusiasm : {'low', 'medium', 'high'}
        The enthusiasm level of the otter greetings:
        - 'low': Simple, calm greeting
        - 'medium': Friendly greeting with some emojis
        - 'high': Very excited greeting with lots of emojis and caps
        Default is 'medium'.
    output : str
        Path to the output file where greetings will be appended.
        Default is 'greetings.txt'.
    
    Returns
    -------
    None
        Appends greetings to the specified output file.
    
    Examples
    --------
    Run from command line:
    
    >>> python otter_greeting.py --name "Oyster" --count 3 --enthusiasm high --output greetings.txt
    
    This will append 3 highly enthusiastic otter greetings for Oyster to greetings.txt.
    """
    # Different enthusiasm levels
    emojis = {
        'low': '🦦',
        'medium': '🦦✨',
        'high': '🦦🎉🌊'
    }
    
    messages = {
        'low': f"hello {name}.",
        'medium': f"Hello {name}! 🌊",
        'high': f"HELLO {name.upper()}!!! Who is that lovely, amazing, genius friend over there?? The otters are SO excited to see you! 🎊"
    }
    
    # Open file in append mode, create if it doesn't exist
    with open(output, 'a', encoding='utf-8') as f:

        for i in range(count):
            # Write each greeting as: name,enthusiasm,message
            f.write(f"{name},{enthusiasm},{messages[enthusiasm]}\n")
        
if __name__ == '__main__':
    greet_otters()
