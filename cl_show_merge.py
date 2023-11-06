import numpy as np
import healpy as hp
import matplotlib.pyplot as plt

#multi_num = np.arange(0,100,1,dtype=int)
frequency = np.arange(0,30,1)
l = np.arange(1,769,1)
j=0
while(j<30):
#ref = np.load('/home/lzl/Desktop/BINGO_files/0'+str(frequency[j])+"Mhz.npy")
#ref_cl = hp.anafast(ref)
#ref2 = np.load('../test/HR4_masscut/real/'+str(frequency[j])+"Mhz.npy")
#ref2_cl = hp.anafast(ref2)
    real_cl = np.load('/home/lzl/Desktop/BINGO_files/0/real_'+str(frequency[j])+".npy")
    real_cl = hp.anafast(real_cl)
    red_cl = np.load('/home/lzl/Desktop/BINGO_files/0/red_'+str(frequency[j])+".npy")
    red_cl = hp.anafast(red_cl)
    red2_cl = np.load('/home/lzl/Desktop/BINGO_files/0/red2_'+str(frequency[j])+".npy")
    red2_cl = hp.anafast(red2_cl)
    plt.figure()
#for multi_i in multi_num:
    plt.plot(l,real_cl,color='blue',alpha=0.2,lw=1)
    plt.plot(l,red_cl,color='red',lw=1)
    plt.plot(l,red2_cl,color='yellow',ls='--',lw=1)
    plt.xlim(2,768)
    plt.ylim(1e-9,1e-4)
    plt.xlabel('l')
    plt.ylabel('$Cl/mK^{2}$')
    plt.loglog()
    plt.savefig('/home/lzl/Desktop/figures0/multi_cl_'+str(frequency[j]))
    plt.close()
    j += 1
'''
j=0
while(j<30):
	ref = np.load('../../../HR4_fof/10Mhz/red/'+str(frequency[j+1])+"Mhz.npy")
	ref_cl = hp.anafast(ref)
	ref2 = np.load('../test/HR4_masscut/red/'+str(frequency[j+1])+"Mhz.npy")
	ref2_cl = hp.anafast(ref2)
	multi_cl = np.load('../cls/red/'+str(frequency[j+1])+"Mhz.npy")
	plt.figure()
	for multi_i in multi_num:
		plt.plot(l,multi_cl[multi_i],color='blue',alpha=0.2,lw=1)
	plt.plot(l,ref_cl,color='red',lw=1)
	plt.plot(l,ref2_cl,color='red',ls='--',lw=1)
	plt.xlim(2,768)
	plt.ylim(1e-9,1e-4)
	plt.xlabel('l')
	plt.ylabel('$Cl/mK^{2}$')
	plt.loglog()
	plt.savefig('../figure/red/'+str(frequency[j+1])+"Mhz.png")
	plt.close()
	j += 1

j=0
while(j<30):
	ref = np.load('../../../HR4_fof/10Mhz/red2/'+str(frequency[j+1])+"Mhz.npy")
	ref_cl = hp.anafast(ref)
	ref2 = np.load('../test/HR4_masscut/red2/'+str(frequency[j+1])+"Mhz.npy")
	ref2_cl = hp.anafast(ref2)
	multi_cl = np.load('../cls/red2/'+str(frequency[j+1])+"Mhz.npy")
	plt.figure()
	for multi_i in multi_num:
		plt.plot(l,multi_cl[multi_i],color='blue',alpha=0.2,lw=1)
	plt.plot(l,ref_cl,color='red',lw=1)
	plt.plot(l,ref2_cl,color='red',ls='--',lw=1)
	plt.xlim(2,768)
	plt.ylim(1e-9,1e-4)
	plt.xlabel('l')
	plt.ylabel('$Cl/mK^{2}$')
	plt.loglog()
	plt.savefig('../figure/red2/'+str(frequency[j+1])+"Mhz.png")
	plt.close()
	j += 1
'''