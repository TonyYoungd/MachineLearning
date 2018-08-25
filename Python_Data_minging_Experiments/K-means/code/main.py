from k_means import gen_random_sample,Cluster,get_distance,get_data
import random
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors

def kmeans(samples,k,cutoff):
    init_samples = random.sample(samples,k)
    cluster = [Cluster([sample]) for sample in init_samples]
    n_loop = 0
    while True:
        list = [[] for _ in cluster]
        n_loop += 1
        for sample in samples:
            smallest_distance = get_distance(sample, cluster[0].centroid)
            cluster_index = 0
            for i in range(k - 1):
                distance = get_distance(sample,cluster[i+1].centroid)
                if distance < smallest_distance:
                    smallest_distance = distance
                    cluster_index = i + 1
            list[cluster_index].append(sample)
        biggest_shift = 0.0
        for i in range(k):
            shift = cluster[i].update(list[i])
            biggest_shift = max(biggest_shift,shift)
        if biggest_shift < cutoff:
            print("第{}次迭代后，聚类稳定。".format(n_loop))
            print("稳定后的聚类为：")
            num = 1
            for sa in cluster:
                print("第",num,"个聚类为：",sa)
                num+=1
            break
    return cluster

def run_main():
    n_cluster = 3
    samples = get_data()
    cutoff = 0.2
    cluster = kmeans(samples,n_cluster,cutoff)

    #可视化结果

    #二维度图
    plt.subplot()
    color_names = list(mcolors.cnames)
    for i, c in enumerate(cluster):
        x = []
        y = []
        color = [color_names[i]] * len(c.samples)
        for sample in c.samples:
            x.append(sample.coords[0])
            y.append(sample.coords[1])
        plt.scatter(x, y, c=color)
    plt.show()

    """
    ax = plt.subplot()
    color_names = list(mcolors.cnames)
    for i, c in enumerate(cluster):
        x = []
        y = []
        z = []
        color = [color_names[i]] * len(c.samples)
        for sample in c.samples:
            x.append(sample.coords[0])
            y.append(sample.coords[1])
            z.append(sample.coords[2])
        plt.scatter(x, y, z, c=color)
    plt.show()
    """





if __name__ == "__main__":
    run_main()
