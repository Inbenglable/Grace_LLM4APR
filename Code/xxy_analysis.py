import os
import shutil
import json
import pickle

def analyse_pkl(pkl_path):
    with open(pkl_path, 'rb') as f:
        data = pickle.load(f)
    print(type(data[0]))
    os.makedirs(f'../Pkl_Structure/{pkl_path}', exist_ok=True)
    for proj in data:
        proj_name=proj['proj']       
        os.makedirs(f'../Pkl_Structure/{pkl_path}/{proj_name}', exist_ok=True)
        for key in proj: 
            with open(f'../Pkl_Structure/{pkl_path}/{proj_name}/{key}.json', 'w') as f:
                f.write(f'{proj[key]}\n')


def get_line(index):
    with open('Chart.pkl', 'rb') as f:
        data = pickle.load(f)
    lines= data[0]['lines']
    for line in lines:
        if lines[line]==index:
            file_path=line.replace('.','/').split(':')[0]+'.java'
            loc=int(line.replace('.','/').split(':')[1])
            print(f'index:{index}, line {loc} is in {file_path}')
            break


def analyse_edge2():
    with open('Chart.pkl', 'rb') as f:
        data = pickle.load(f)

    lines= data[0]['lines']
    line_by_index={}

    for line in lines:
        line_by_index[lines[line]]=line


    edge2= data[0]['edge2']
    min_1=10
    max_1=10
    min_2=10
    max_2=10
    for tuple in edge2:
        min_1=min(min_1, tuple[0])
        max_1=max(max_1, tuple[0])
        min_2=min(min_2, tuple[1])
        max_2=max(max_2, tuple[1])
    
    element_1=[0]*(max_1+1)
    element_2=[0]*(max_2+1)
    for tuple in edge2:
        if element_1[tuple[0]]==0:
            element_1[tuple[0]]=1
        # else:
        #     print('method repetition:',tuple)
        if element_2[tuple[1]]==0:
            element_2[tuple[1]]=1
        else:
            print('line repetition:',tuple)

    for i in range(len(element_1)):
        if element_1[i]==0:
            print('method missing:',i)
    for i in range(len(element_2)):
        if element_2[i]==0:
            print('line missing:',i)
    # tuples_76=[]
    # for tuple in edge2:
    #     if tuple[0]==76:
    #         tuples_76.append((tuple[0], line_by_index[tuple[1]].split(':')[1]))
    # tuples_76.sort(key=lambda x:x[1])
    # for tuple in tuples_76:
    #     print(tuple)


def check_edge2_allHasType():
    with open('Chart.pkl', 'rb') as f:
        data = pickle.load(f)
    edge2= data[0]['edge2']
    ltype= data[0]['ltype']
    for tuple in edge2:
        if tuple[1] not in ltype:
            print(tuple)

    for line_idx in ltype:
        if ltype[line_idx]=="Empty" or ltype[line_idx] is None:
            print(line_idx)


def analyse_edge10():
    with open('Chart.pkl', 'rb') as f:
        data = pickle.load(f)
    edge10= data[0]['edge10']
    max_1=10
    max_2=10
    for tuple in edge10:
        max_1=max(max_1, tuple[0])
        max_2=max(max_2, tuple[1])
    
    print(max_1, max_2)
    element_1=[0]*(max_1+1)
    element_2=[0]*(max_2+1)
    for tuple in edge10:
        if element_1[tuple[0]]==0:
            element_1[tuple[0]]=1
        # else:
        #     print('line repetition:',tuple)
        if element_2[tuple[1]]==0:
            element_2[tuple[1]]=1
        # else:
        #     print('test repetition:',tuple)
    
    for i in range(len(element_1)):
        if element_1[i]==0:
            print('line missing:',i)
    for i in range(len(element_2)):
        if element_2[i]==0:
            print('test missing:',i)

def get_line_method_test_num(index):
    with open('Chart.pkl', 'rb') as f:
        data = pickle.load(f)
    methods= data[index]['methods']
    method_num=len(methods)
    test_num= len(data[index]['rtest'])+len(data[index]['ftest'])
    line_num=len(data[index]['lines'])
    print(f'project {index} has {method_num} methods, {test_num} tests, {line_num} lines')
    ftest_num=len(data[index]['ftest'])
    print(f'project {index} has {ftest_num} failed tests')


def analyse_correctnum(index):
    with open('Chart.pkl', 'rb') as f:
        data = pickle.load(f)
    correctnum= data[index]['correctnum']
    lcorrectnum= data[index]['lcorrectnum']
    correctnum_max_value=0
    lcorrectnum_max_value=0
    for method_index in correctnum:
        correctnum_max_value=max(correctnum_max_value, correctnum[method_index])

    print(f'correctnum max value: {correctnum_max_value}')

    for line_index in lcorrectnum:
        lcorrectnum_max_value=max(lcorrectnum_max_value, lcorrectnum[line_index])
    
    print(f'lcorrectnum max value: {lcorrectnum_max_value}')

def analyse_test(index):
    with open('Chart.pkl', 'rb') as f:
        data = pickle.load(f)
    ftest= data[index]['ftest']
    rtest= data[index]['rtest']

    with open('rtests', 'r') as f:
        test_all_list = f.readlines()
    test_classes=[]
    for line in test_all_list:
        test_classes.append(line.strip())

    
    test_extract=[]
    for test in ftest:
        test_extract.append(test[:test.rfind('.')])

    for test in rtest:
        test_extract.append(test[:test.rfind('.')])
    
    # for test in test_extract:
    #     if test not in test_classes:
    #         print(test)

    for test_class in test_classes:
        if test_class not in test_extract:
            print(test_class)        


def analyse_edge(index):
    with open('Chart.pkl', 'rb') as f:
        data = pickle.load(f)
    edge= data[index]['edge']
    max_1=-1
    max_2=-1
    for tuple in edge:
        max_1=max(max_1, tuple[0])
        max_2=max(max_2, tuple[1])
    
    print(max_1, max_2)
    element_1=[0]*(max_1+1)
    element_2=[0]*(max_2+1)

    buggy_line_in_edge=[]
    buggy_method=20

    buggy_lines=[]
    
    edge2= data[index]['edge2']
    edge10= data[index]['edge10']

    for tuple in edge2:
        if tuple[0]==buggy_method:
            # get_line(tuple[1])
            buggy_lines.append(tuple[1])

    for tuple in edge:
        # if tuple[1]==0 and tuple[0] in buggy_lines:
        if tuple[1]==0:
            buggy_line_in_edge.append(tuple[0])
        if element_1[tuple[0]]==0:
            element_1[tuple[0]]=1
        # else:
        #     print('line repetition:',tuple)
        if element_2[tuple[1]]==0:
            element_2[tuple[1]]=1
        # else:
        #     print('test repetition:',tuple)

    # for i in range(len(element_1)):
    #     if element_1[i]==0:
    #         print('line missing:',i)
    # for i in range(len(element_2)):
    #     if element_2[i]==0:
    #         print('pos2 missing:',i) 


    buggy_line_in_edge10=[]
    for tuple in edge10:
        # if tuple[1]==0 and tuple[0] in buggy_lines:
        if tuple[1]==0:
            buggy_line_in_edge10.append(tuple[0])
    

    
    # for buggy_line in buggy_lines:
    #     print(f'buggy_line {buggy_line} ')

    # for buggy_line in buggy_line_in_edge:
    #     print(f'buggy_line {buggy_line} in edge')

    # for buggy_line in buggy_line_in_edge10:
    #     print(f'buggy_line {buggy_line} in edge10')
            
    for line in buggy_line_in_edge10:
        get_line(line)
        print(f'buggy_line {line} in edge10')
        # if line not in buggy_line_in_edge:
        #     print(f'buggy_line {line} in edge10 but not in edge')

            
analyse_edge(0)