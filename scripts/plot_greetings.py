"""Greeting Visualizer

This script reads greeting count data and creates a simple bar plot 
showing the total number of times each person was greeted.
"""

import click
import matplotlib.pyplot as plt

@click.command()
@click.option('--input', default='greeting_count.csv', help='Input CSV file with greeting counts.')
@click.option('--output', default='greeting_plot.png', help='Output file for the bar plot.')
def plot_greetings(input, output):
    """Create a bar plot of total greetings per person
    
    Reads a greeting counts CSV file and creates a simple bar plot
    showing the total number of times each person was greeted.
    
    Parameters
    ----------
    input : str
        Path to the input CSV file with greeting counts.
        Expected columns: name, word_count
        Default is 'greeting_count.csv'.
    output : str
        Path to save the output plot image.
        Default is 'greeting_plot.png'.
    
    Examples
    --------
    >>> python plot_greetings.py --input greeting_count.csv --output greeting_plot.png
    """
    
    try:
        # Read the CSV file
        names = []
        with open(input, 'r', encoding='utf-8') as f:
            next(f)  # Skip header
            for line in f:
                parts = line.strip().split(',')
                if len(parts) >= 1:
                    names.append(parts[0])
        
        # Count greetings per person
        name_counts = {}
        for name in names:
            name_counts[name] = name_counts.get(name, 0) + 1
        
        # Create bar plot
        plt.figure(figsize=(8, 6))
        plt.bar(name_counts.keys(), name_counts.values())
        plt.xlabel('Name')
        plt.ylabel('Number of Greetings')
        plt.title('Total Otter Greetings per Person')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig(output)
        plt.close()
        
        print(f'Bar plot saved to {output}')
        
    except FileNotFoundError:
        print(f'Error: Input file {input} not found!')

if __name__ == '__main__':
    plot_greetings()

