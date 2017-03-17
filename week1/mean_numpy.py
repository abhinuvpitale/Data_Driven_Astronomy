# Write your mean_datasets function here
import numpy as np
def mean_datasets(arr_list):
  itm = np.loadtxt(arr_list[0],delimiter = ',')
  itm = itm - itm
  length = len(arr_list)
  for item in arr_list:
    itm = itm + (np.loadtxt(item,delimiter = ','))
  return (itm/length).round(1)
  



if __name__ == '__main__':
  # Run your function with examples from the question:
  
  print(mean_datasets(['data1.csv', 'data2.csv', 'data3.csv']))
