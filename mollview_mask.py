import os

import matplotlib.pyplot as plt
import numpy as np
import healpy as hp
from astropy.io import fits
'''
data1 = fits.open('/home/lzl/Desktop/BINGO_files/mask/mask_larissa_w.fits')
data1 = fits.open('/home/lzl/Desktop/BINGO_files/mask/mask_bingo_Ns256_2d.fits')
data1.info()
toshow = data1[1].data.field(0)
hp.mollview(toshow)
plt.imshow(toshow)
plt.title("mask_bingo_Ns256_2d")
plt.savefig('/home/lzl/Desktop/figures0/mask_bingo_Ns256_2d.png')
plt.show()
'''
data1 = hp.read_map('/home/lzl/Desktop/BINGO_files/mask/mask_bingo_Ns256_2d.fits')
#data1 = hp.read_map('/home/lzl/Desktop/BINGO_files/mask/mask_larissa_w.fits')
hp.mollview(data1, title='mask_larissa_w')
#plt.savefig('/home/lzl/Desktop/figures0/mask_larissa_w_mollview')
plt.show()

