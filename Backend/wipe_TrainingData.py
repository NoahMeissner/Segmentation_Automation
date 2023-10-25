import os
import sys
class Wipe:
    def __init__(self):
        pass

    def Wipe_Data(self):
        path = 'Model/'
        categories = ['Test','Train', 'Validate']
        subfolders = ['images', 'labels']

        base_path = '../Model/'

        for category in categories:
            category_path = os.path.join(base_path, category)

            if os.path.exists(category_path):
                for subfolder in subfolders:
                    subfolder_path = os.path.join(category_path, subfolder)

                    if os.path.exists(subfolder_path):
                        for filename in os.listdir(subfolder_path):
                            file_path = os.path.join(subfolder_path, filename)
                            if os.path.isfile(file_path):
                                os.remove(file_path)

                    else:
                        for filename in os.listdir(subfolder_path):
                            file_path = os.path.join(category_path, filename)
                            if os.path.isfile(file_path):
                                os.remove(file_path)