import h5py
import numpy as np
import healpy as hp
import matplotlib.pyplot as plt

f = h5py.File('/home/lzl/Desktop/BINGO_files/z0/halo.z0_11.4_11.5.hdf5')

print(f.keys())
key = ""
for k in f.keys():
    key = k
    d = f[key]
    print(d)
    a = np.ones(d.shape)
    d.read_direct(a)
    print(a)
f.close()
