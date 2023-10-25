import os
import csv
import re

input_directory = "Images"

# Iterate through files in the directory
for filename in os.listdir(input_directory):
    if filename.endswith('.csv'):
        csv_file = os.path.join(input_directory, filename)
        image_filename = filename.replace('.csv', '.jpg')
        txt_filename = image_filename.replace('.jpg', '.txt')

        # Read CSV and write TXT file
        with open(csv_file, 'r') as csv_file, open(os.path.join(input_directory, txt_filename), 'w') as txt_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                # Filter out brackets and join values with spaces
                filtered_values = [re.sub(r'[^\d ]', '', cell) for cell in row]
                numeric_values = ' '.join(filtered_values)
                txt_file.write(numeric_values + '\n')

# Iterate through TXT files in the directory
for filename in os.listdir(input_directory):
    if filename.endswith('.txt'):
        txt_file_path = os.path.join(input_directory, filename)

        # Read the contents of the TXT file
        with open(txt_file_path, 'r') as txt_file:
            txt_content = txt_file.read()

        # Replace one or two consecutive line breaks with spaces
        txt_content = re.sub(r'\n\n+', ' ', txt_content)
        txt_content = txt_content.replace('\n', ' ')

        # Write the modified content back to the TXT file
        with open(txt_file_path, 'w') as txt_file:
            txt_file.write(txt_content)