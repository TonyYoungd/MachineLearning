import scipy.io as sio
data1 = sio.loadmat("data1.mat")
data = data1.get("Xval")
