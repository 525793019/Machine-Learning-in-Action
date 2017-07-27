# auther: Hanhe
import numpy as np
import operator

def createDataset():
    dataset = np.array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return dataset, labels


def classify(new_m, dataset, labels, k):
    """
    ###input
    new_m: 待分类对象
    dataset: 特征集
    labels: 数据集对应的标签
    k: k个近邻点判断待分类对象

    ###return
    返回：待分类对象标签
    """
    #Construct a mat by repeating new_m
    l_dataset = dataset.shape[0]

    #calculate distance from new_m to dataset member
    new_mat = np.tile(new_m, (l_dataset, 1)) - dataset
    new_mat = new_mat**2
    new_mat = np.sum(new_mat, axis=1)
    new_mat = new_mat**0.5

    #get sorted distance indices
    distances = new_mat.argsort()

    #calculate max k
    cla = {}
    for i in range(k):
        vote = labels[distances[i]]
        cla[vote] = cla.get(vote,0) + 1
    cla = sorted(cla.items(), key=operator.itemgetter(1),reverse=True)
    print(cla[0][0])

def file2matrix(filename):
    """
    #input
    filename: 数据集路径

    #return
    dataset: 特征集矩阵
    labels: 数据集对应的分类标签
    """
    f = open(filename)
    text = f.readlines()
    dataset = np.zeros((len(text),len(text[0].strip().split('\t'))-1))
    labels = []
    index = 0
    for line in text:
        line = line.strip()
        line = line.split('\t')
        dataset[index:]=line[:-1]
        labels.append(line[-1])
        index+=1
    return dataset, labels

#dataset, labels = createDataset()
#classify([1, 0], dataset, labels, 3)
file2matrix('datingTestSet2.txt')












