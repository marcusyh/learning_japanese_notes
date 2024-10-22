import sys
import os
import config

def process_markdown():
    input_file = os.path.join(config.LEARNING_DIR, f'{config.ONYOMI_FILENAME}.md')
    output_file = os.path.join(config.NOTEBOOK_DIR, f'{config.ONYOMI_FILENAME}.md')

    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            columns = line.strip().split('|')
            if len(columns) >= 8:  # Ensure there are at least 7 columns (plus the leading empty column)
                selected_columns = columns[:1] + columns[2:8]  # Keep the first empty column and columns 2-7
                outfile.write('|'.join(selected_columns) + '|\n')
            else:
                outfile.write(line)  # Write unchanged if not enough columns

if __name__ == "__main__":
    process_markdown()
