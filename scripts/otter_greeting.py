"""Otter Greeting Generator

This script allows you to greet otters with different levels of enthusiasm.
"""

import click

@click.command()
@click.option('--count', default=1, help='Number of otter greetings.')
@click.option('--name', prompt='Your name', help='The person to greet.')
@click.option('--enthusiasm', type=click.Choice(['low', 'medium', 'high']), 
              default='medium', help='How enthusiastic should the otters be?')
def greet_otters(count, name, enthusiasm):
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
    
    Returns
    -------
    None
        Outputs greetings directly to the console using click.echo().
    
    Examples
    --------
    Run from command line:
    
    >>> python otter_greeting.py --name "Oyster" --count 3 --enthusiasm high
    
    This will display 3 highly enthusiastic otter greetings for Oyster.
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
    
    click.echo(f"\n{emojis[enthusiasm]} Otter Greetings Incoming! {emojis[enthusiasm]}\n")
    
    for i in range(count):
        click.echo(f"  Otter #{i+1}: {messages[enthusiasm]}")
    
    click.echo(f"\n🦦 You've been greeted by {count} friendly otter(s)! 🦦\n")

if __name__ == '__main__':
    greet_otters()