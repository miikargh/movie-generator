from textgenrnn import textgenrnn
import subprocess

AUTO_SHUTDOWN = False

textgen = textgenrnn()
textgen.train_from_file('./processed_data/descriptions_small.txt', num_epochs=1)

print('done')
if AUTO_SHUTDOWN:
    subprocess.call(['halt'])
