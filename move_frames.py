import os
import shutil

os.chdir('frames')

if not os.path.isdir('attend'):
    os.mkdir('attend')

if not os.path.isdir('nonattend'):
    os.mkdir('nonattend')

for d in os.listdir('.'):
    if os.path.isdir(d) and d not in ('attend', 'nonattend'):
        folder = 'nonattend' if int(d) % 2 == 0 else 'attend'

        for f in os.listdir(d):
            if not f.startswith('.DS'):
                shutil.copy(os.path.join(d, f), os.path.join(folder, f'{d}_{f}'))
