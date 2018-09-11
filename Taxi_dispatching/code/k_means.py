import random
import math
import csv
class Cluster(object):
    def __init__(self,samples):
        if len(samples) == 0:
            raise Exception("错误，这是一个空的聚类！")
        self.samples = samples
        print(samples)
        self.n_dim = samples[0].n_dim
        for sample in samples:
            if sample.n_dim != self.n_dim:
                raise Exception("错误，聚类样本点的维度不一样")
        self.centroid = self.cal_centroid()

    def __repr__(self):
        """
            输出对象信息
        """
        return str(self.samples)

    def cal_centroid(self):
        n_samples = len(self.samples)
        coords = [sample.coords for sample in self.samples]
        unzipped = zip(*coords)
        centroid_coords =  [math.fsum(d_list)/n_samples for d_list in unzipped]
        return Sample(centroid_coords)
    def update(self,samples):
        old_centroid = self.centroid
        self.samples = samples
        self.centroid = self.cal_centroid()
        shift = get_distance(old_centroid, self.centroid)
        return shift

def get_distance(a, b):
    """
        返回样本点a, b的欧式距离
        参考：https://en.wikipedia.org/wiki/Euclidean_distance#n_dimensions
    """
    if a.n_dim != b.n_dim:
        # 如果样本点维度不同
        raise Exception("错误: 样本点维度不同，无法计算距离！")

    acc_diff = 0.0
    for i in range(a.n_dim):
        square_diff = pow((a.coords[i]-b.coords[i]), 2)
        acc_diff += square_diff
    distance = math.sqrt(acc_diff)

    return distance



class Sample(object):
    def __init__(self,coords):
        self.coords = coords
        self.n_dim = len(coords)
    def __repr__(self):
        return str(self.coords)

def get_data():
    with open("../data/data_format/data.csv") as datac:
        sample = []
        reader = csv.reader(datac)
        data = []
        for item in reader:
            data.append(item)
        for item in data:
            for index in range(len(item)):
                item[index] = float(item[index])
        for item in data:
            sample.append(Sample(item))
    return sample
def gen_random_sample(n_dim,lower,upper):
    sample = Sample([random.uniform(lower,upper) for _ in range(n_dim)])
    return sample
