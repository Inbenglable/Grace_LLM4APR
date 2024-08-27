import subprocess
from tqdm import tqdm
import time
import os, sys
import pickle
import shutil
# project = sys.argv[1]

singlenums = {'Time':5, 'Math':2, "Lang":10, "Chart":3, "Mockito":4, "Closure":1}
for project in singlenums:
    card = [0]
    lst = list(range(len(pickle.load(open(project + '.pkl', 'rb')))))

    singlenum = singlenums[project]
    totalnum = len(card) * singlenum
    lr = 1e-2
    seed = 0
    batch_size = 60
    for i in tqdm(range(int(len(lst) / totalnum) + 1)):
        jobs = []
        for j in range(totalnum):
            if totalnum * i + j >= len(lst):
                continue
            cardn =int(j / singlenum)
            p = subprocess.Popen("CUDA_VISIBLE_DEVICES="+str(card[cardn]) + " python run.py %d %s %f %d %d"%(lst[totalnum * i + j], project, lr, seed, batch_size), shell=True)
            jobs.append(p)
            time.sleep(10)
        for p in jobs:
            p.wait()
    p = subprocess.Popen("python sum.py %s %d %f %d"%(project, seed, lr, batch_size), shell=True)
    p.wait()
    subprocess.Popen("python watch.py %s %d %f %d"%(project, seed, lr, batch_size),shell=True)

    for file in os.listdir('.'):
        if file.startswith(project+'res') or file.startswith(project+'result'):
            shutil.move(file,f'../Result/{project}')
            
