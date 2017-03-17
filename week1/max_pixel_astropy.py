# Write your load_fits function here.
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
import math

def load_fits(file_name):
  hdulist = fits.open(file_name)
  data = hdulist[0].data 
  length = (hdulist[0].data.shape)
  num_data = np.array(data)
  row = np.argmax(data)%length[1]
  col = math.floor((np.argmax(data)/length[1]))
  return (col,row)

  #plt.imshow(data,cmap = plt.cm.viridis)  
  #plt.show()

if __name__ == '__main__':
  
  # Run your `load_fits` function with examples:
  bright = load_fits('image0.fits')
  print(bright)

  # You can also confirm your result visually:
  #from astropy.io import fits
  #import matplotlib.pyplot as plt

  #hdulist = fits.open('image1.fits')
  #data = hdulist[0].data

  # Plot the 2D image data
  #plt.imshow(data.T, cmap=plt.cm.viridis)
  #plt.colorbar()
  #plt.show()

 
