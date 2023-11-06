import os
import numpy as np
import healpy as hp
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.use('TkAgg')
frequency = np.arange(0,30,1)
j = 0
while(j<30):
    data0 = np.load('/home/lzl/Desktop/BINGO_files/0/real_'+str(frequency[j])+".npy")
#data1 = np.load('/home/lzl/Desktop/BINGO_files/0/red_0.npy')
#data2 = np.load('/home/lzl/Desktop/BINGO_files/0/red2_0.npy')
    hp.mollview(data0)
#hp.mollview(data1)
#hp.mollview(data2)
#fig , ((fig0), (fig1), (fig2)) = plt.subplots(1, 3)
    plt.savefig('/home/lzl/Desktop/figures0/real_'+str(frequency[j]))
    plt.close()
    j += 1

j = 0
while(j<30):
    data1 = np.load('/home/lzl/Desktop/BINGO_files/0/red_'+str(frequency[j])+".npy")
    hp.mollview(data1)
    plt.savefig('/home/lzl/Desktop/figures0/red_'+str(frequency[j]))
    plt.close()
    j += 1

j = 0
while(j<30):
    data2 = np.load('/home/lzl/Desktop/BINGO_files/0/red2_'+str(frequency[j])+".npy")
    hp.mollview(data2)
    plt.savefig('/home/lzl/Desktop/figures0/red2_'+str(frequency[j]))
    plt.close()
    j += 1