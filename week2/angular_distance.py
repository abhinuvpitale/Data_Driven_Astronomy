# Write your angular_dist function here.
import numpy as np

def angular_dist(r1_deg,d1_deg,r2_deg,d2_deg):
  r1 = np.radians(r1_deg)
  r2 = np.radians(r2_deg)
  d1 = np.radians(d1_deg)
  d2 = np.radians(d2_deg)
  
  delta_1 = d1 - d2
  if delta_1<0:
    delta_1 = - delta_1
  delta_1 = (delta_1)/2
  a = (np.sin(delta_1))*(np.sin(delta_1))
  b = np.cos(d1)*np.cos(d2)*np.sin(np.abs(r1 - r2)/2)**2
  d = 2*np.arcsin(np.sqrt(a + b)) 
  return np.degrees(d)


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with the first example in the question.
  print(angular_dist(21.07, 0.1, 21.15, 8.2))

  # Run your function with the second example in the question
  print(angular_dist(10.3, -3, 24.3, -29))
