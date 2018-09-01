'''
Concatenate all files from data folder to one two files with one file containing movie titles per line and other containing the movie descriptions per file.
'''

from glob import glob
import os

DATA_PATH = './data/*.txt'
OUT_FOLDER = './processed_data/'
OUT_TITLES = OUT_FOLDER + 'titles.txt'
OUT_DESCRIPTIONS = OUT_FOLDER + 'descriptions.txt'

if not os.path.exists(OUT_FOLDER):
    os.makedirs(OUT_FOLDER)

def load_files(path=DATA_PATH):
    for fname in glob(path):
        with open(fname, 'r') as f:
            yield f.read()

with open(OUT_TITLES, 'w+') as out_titles, open(OUT_DESCRIPTIONS, 'w+') as out_descriptions:
    for f in load_files():
        data = f.split('\n')
        title = data[0]
        description = data[-2]
        if description == "No overview found.":
            print('No overview found! Skipping...')
        else:
            out_titles.write(title + '\n')
            out_descriptions.write(description + '\n')

print('Done')
