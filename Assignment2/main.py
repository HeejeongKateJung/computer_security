from numpy.core.defchararray import index
import pandas as pd
from math import log
import os


class Datas:
    _path_dir = ''
    _isRansome = False
    _file_list = ''
    _4grams = []
    _docs = []
    _terms_list = set()

    def __init__(self,name):
        self.name = name



def get_file_list(path_dir, datas):

    print('get file list from '+path_dir + '...')
    file_list = []
    for i in os.listdir(path_dir):
        if i.endswith('.txt'):
            file_list.append(i)
    
    datas._file_list = file_list
    return datas


def docs_from_filelist(datas):
    docs = []
    file_list = datas._file_list
    path_dir = datas._path_dir

    for f in file_list:
        file = open(path_dir+f, 'r')
        doc = file.read()
        file.close()
        docs.append(doc)

    datas._docs = docs
    return datas


def get_4gram_terms(datas):

    datas = docs_from_filelist(datas)

    _4grams = []   # 4gram 화 된 doc 이 들어있는 list
    terms_list = set()   # 4gram 종류들이 담긴 set

    docs = datas._docs
    
    for doc in docs:
        list_api = doc.splitlines()
        seq = []
        for i in range(len(list_api)-3):
            seq.append(list_api[i]+list_api[i+1]+list_api[i+2]+list_api[i+3])
        _4grams.append(seq)
        terms_list = terms_list.union(set(seq))

    datas._4grams = _4grams
    datas._terms_list = terms_list

    return datas
    
def tf(d, term):
    #doc 안의 특정 term 등장 확률을 리턴한다.
    return d.count(term)

def get_malware_feature_terms(datas):
    _4grams = datas._4grams
    terms_list = datas._terms_list
    file_list = datas._file_list

    df = pd.DataFrame(columns=terms_list)
    
    print('df 만듬')

    df.insert(0, 'file_name', file_list)
    
    i = 0
    
    # 파일이 커서 이부분이 오래걸림
    for term in terms_list:
        i+=1
        tf_list = []
        #docs 들안에 term이 몇개 들어가있는지 반환.
        for d in _4grams:
            tf_list.append(d.count(term))
        df[term] = tf_list

        if(i%100 == 0):
            print(i)

    
    df.to_csv('term_frequency.csv', mode='w')



def preprocess(path_dir, isRansome):
    datas = Datas('ransome')
    if(isRansome == False):
        datas = Datas('normal')
    
    datas._path_dir = path_dir
    datas._isRansome = isRansome
    datas = get_file_list(path_dir, datas)

    # file_list 로부터 파일들을 읽어와 datas._docs 에 저장한다.
    datas = docs_from_filelist(datas)

    # 변환된 파일을 4gram 화하여 datas._4grams 에 저장한다.
    datas = get_4gram_terms(datas)

    # <get_malware_featue_terms(datas)>
    # term_frequency.csv file 을 만든다.
    # term_frequency.csv 파일 구조는 다음과 같다.
    # columns: unique code 로 변환된 api call 을 4-gram 화 하여 나타낸 'term'의 모든 종류.
    # rows: 파일 별로 나타낸 각 'term' 별 term frequency (count 형태)
    # 큰 용량의 csv file 을 만드는 것이 오래걸리므로 미리 만들어서 첨부
    # get_malware_feature_terms(datas)

    return datas



def analysis(r_datas, n_datas):

    print('악성코드 분석을 시작합니다')

    # 분석코드
    df_r = pd.read_csv(r_datas._path_dir[:-2]+'term_frequency_1.csv')
    df_n = pd.read_csv(n_datas._path_dir[:-2]+'term_frequency_0.csv')

    r_4grams = r_datas._4grams  #4gram으로 묶인 파일 내용
    n_4grams = n_datas._4grams

    ran_seq = []    #ransome 특징 서열
    nor_seq = []

    for i in range(len(r_4grams)):
        doc = r_4grams[i]
        for w in doc:
            TFs = df_r[w]
            if(TFs[i]/len(doc) > 0.06):
                ran_seq.append(w)
                break

    ran_seq = set(ran_seq)
    
    for j in range(len(n_4grams)-1):
        doc = n_4grams[j]
        for w in doc:
            TFs = df_n[w]
            if(TFs[j]/len(doc) > 0.05):
                nor_seq.append(w)
                break
    nor_seq = set(nor_seq)
    ran_seq = set.difference(ran_seq, nor_seq)

    print('ransom sequence 추출: ',len(list(ran_seq)))

    count = 0
    for i in range(len(r_4grams)):
        r_doc = r_4grams[i]
        for rs in ran_seq:
            if (rs in r_doc and df_r[rs][i] > 1):
                count+=1
                break

    n_count = 0
    for j in range(len(n_4grams)-1):
        n_doc = n_4grams[j]
        for rs in ran_seq:
            if (rs in n_doc and df_n[rs][j] > 1):
                n_count+=1
                break

    print('ransom sample 분류 결과: ', count/len(r_4grams))
    print('normal sample 분류 결과: ', n_count/len(n_4grams))


    

# path_dir = 'C:/Users/hee/Desktop/computer_security/Assignment2/'

path_dir = input('Sample file 경로를 입력하세요')

for s in path_dir:
    if(s == "\\"):
        s.replace('\\', '/')
path_dir = path_dir+'/'



r_datas = preprocess(path_dir+'1/', True)
n_datas = preprocess(path_dir+'0/', False)
analysis(r_datas, n_datas)




