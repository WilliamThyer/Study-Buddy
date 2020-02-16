import os
import shutil


os.chdir('frames')

if not os.path.isdir('train'):
    os.mkdir('train')

if not os.path.isdir('valid'):
    os.mkdir('valid')

os.mkdir('train/attend')
os.mkdir('train/nonattend')
os.mkdir('valid/attend')
os.mkdir('valid/nonattend')

for d in os.listdir('.'):
    if os.path.isdir(d) and d not in ('train', 'valid', 'pilot'):
        dataset = 'valid' if int(d) <= 6 else 'train'
        folder = 'nonattend' if int(d) % 2 == 0 else 'attend'

        for f in os.listdir(d):
            if not f.startswith('.DS'):
                shutil.copy(os.path.join(d, f), os.path.join(dataset, folder, f'{d}_{f}'))
