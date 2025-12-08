"""Greeting Counter

This script reads a greetings file and records who was greeted 
and the word count of each greeting message.
"""

import click

@click.command()
@click.option('--input', default='greetings.txt', help='Input greetings file to read.')
@click.option('--output', default='greeting_count.csv', help='Output CSV file for greeting counts.')
def count_greetings(input, output):
    """Count otter greetings and word counts
    
    Reads a greetings text file and records each greeting with
    the person's name and the word count of the message.
    
    Parameters
    ----------
    input : str
        Path to the input greetings text file.
        Default is 'greetings.txt'.
    output : str
        Path to the output CSV file for greeting counts.
        Default is 'greeting_count.csv'.
    
    Examples
    --------
    >>> python count_greetings.py --input greetings.txt --output greeting_count.csv
    """
    
    try:
        with open(input, 'r', encoding='utf-8') as f_in:
            with open(output, 'w', encoding='utf-8') as f_out:
                # Write header
                f_out.write('name,word_count\n')
                
                for line in f_in:
                    # Parse lines in format: name,enthusiasm,message
                    if ',' in line:
                        parts = line.strip().split(',', 2)
                        if len(parts) >= 3:
                            name = parts[0].strip()
                            message = parts[2].strip()
                            word_count = len(message.split())
                            f_out.write(f'{name},{word_count}\n')
        
        print(f'Greeting counts saved to {output}')
        
    except FileNotFoundError:
        print(f'Error: Input file {input} not found!')

if __name__ == '__main__':
    count_greetings()

