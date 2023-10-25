import os
import csv
import re
import random
import shutil
from PIL import Image

class Preprocess_Data:

    def __init__(self):
        pass
    def preprocessing(self):
        print(os.getcwd())
        input_directory = "../Model/Images"

        # Iterate through files in the directory
        for filename in os.listdir(input_directory):
            if filename.endswith('.csv'):
                csv_file = os.path.join(input_directory, filename)
                image_filename = filename.replace('.csv', '.jpg')
                txt_filename = image_filename.replace('.jpg', '.txt').replace('data', 'Image')

                # Read CSV and write TXT file
                has_hashtag = False

                with open(csv_file, 'r') as csv_file, open(os.path.join(input_directory, txt_filename),
                                                           'w') as txt_file:
                    csv_reader = csv.reader(csv_file)
                    for row in csv_reader:
                        # Filter out brackets and join values with spaces
                        filtered_values = [re.sub(r'[^\d ]', '', cell) for cell in row]
                        # kill the garbage
                        filtered_values = [cell for cell in filtered_values if
                                           not (has_hashtag and cell.strip().isdigit())]
                        has_hashtag = any('#' in cell for cell in filtered_values)

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

                # Read the input file with coordinates
                with open(txt_file_path, 'r') as f:
                    lines = f.readlines()

                # Convert the coordinates to YOLO format and write to the output file
                class_label = 0

                with open(txt_file_path, 'w') as f:
                    for line in lines:
                        coordinates = line.strip().split()
                        if len(coordinates) % 2 != 0:
                            print(f"Skipping line with incomplete coordinates: {line}")
                            continue

                        num_points = len(coordinates) // 2
                        for i in range(num_points):
                            x = float(coordinates[2 * i])
                            y = float(coordinates[2 * i + 1])

                            # Calculate the center x and y, width, and height
                            center_x = ((x + x) / 2.0) / 512
                            center_y = ((y + y) / 2.0) / 424
                            width = 1
                            height = 1

                            # Write the YOLO format line to the output file
                            yolo_line = f"{class_label} {center_x} {center_y} {width} {height}\n"
                            f.write(yolo_line)

        # Define the parent folder and subfolder names
        parent_folder = "../Model"
        subfolders = ["../Model/Train", "../Model/Validate", "../Model/Test"]

        # Define the split ratios (60-20-20)
        split_ratios = [0.6, 0.2, 0.2]
        list_paths_res = []

        # Define the source folder (Images) and destination subfolders (images and labels)
        source_folder = "../Model/Images"
        for i in subfolders:
            list_paths_res.append(i+'/'+'images')
            list_paths_res.append(i+'/'+'labels')


        print(list_paths_res)

        # Create destination subfolders if they don't exist
        for folder in list_paths_res:
            if os.access(folder, os.W_OK):
                # Directory is writable, proceed with creating directories
                os.makedirs(folder, exist_ok=True)
            else:
                print(f"Directory '{folder}' is not writable.")

        # Get a list of all .jpg and .txt files in the source folder
        jpg_files = [f for f in os.listdir(source_folder) if f.lower().endswith(".jpg")]
        txt_files = [f for f in os.listdir(source_folder) if f.lower().endswith(".txt")]

        # Sort the files based on their numeric part
        def get_numeric_part(file_name):
            return int(''.join(filter(str.isdigit, file_name)))

        jpg_files.sort(key=get_numeric_part)
        txt_files.sort(key=get_numeric_part)

        # Split the files and move them to the appropriate destination folders
        total_files = len(jpg_files)
        cumulative_split_ratios = [sum(split_ratios[:i + 1]) for i in range(len(split_ratios))]
        split_points = [int(total_files * ratio) for ratio in cumulative_split_ratios]

        for i, (start, end) in enumerate(zip([0] + split_points, split_points)):
            for file_name in jpg_files[start:end]:
                source_path = os.path.join(source_folder, file_name)
                destination_path = os.path.join(list_paths_res[i * 2], file_name)
                shutil.move(source_path, destination_path)

            for file_name in txt_files[start:end]:
                source_path = os.path.join(source_folder, file_name)
                destination_path = os.path.join(list_paths_res[i * 2 + 1], file_name)
                shutil.move(source_path, destination_path)

