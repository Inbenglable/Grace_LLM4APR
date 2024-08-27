import os
import pickle

def get_line(index):
    with open('Chart.pkl', 'rb') as f:
        data = pickle.load(f)
    lines= data[0]['lines']
    for line in lines:
        if lines[line]==index:
            file_path=line.replace('.','/').split(':')[0]+'.java'
            loc=int(line.replace('.','/').split(':')[1])
            print(f'line {loc} is in {file_path}')
            break

def get_method(index):
    with open('Chart.pkl', 'rb') as f:
        data = pickle.load(f)
    methods= data[0]['methods']
    for method in methods:
        if methods[method]==index:
            method_name=method.split(":")[1]
            method_name=method_name.split("(")[0]
            print(f'method {method_name} is in {method.split(":")[0]}.java')
            break

with open('Chart.pkl', 'rb') as f:
    data = pickle.load(f)
edge=data[1]['edge']

max=0
for tuple in edge:
    max=max if max>tuple[0] else tuple[0]

lines=[0]*(max+1)
for tuple in edge:
    if lines[tuple[0]]==0:
        lines[tuple[0]]=1
    else:
        print('line repetition:',tuple)

for i in range(len(lines)):
    if lines[i]==0:
        print(f'line {i} is not in the graph')
