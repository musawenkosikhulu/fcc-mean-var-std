import numpy as np


def calculate(list):
    if len(list
           ) < 9:  #This checks if list have 9 numbers to generate a 3x3 matrix
        print(
            'Error :try again this list can not create a 3x3 matrix'
        )  #if the length is less than 9 which cant a 3x3 this message say "try again"
    else:

      output = np.reshape(list, (3, 3))
      mean = [np.mean(output, axis=0).tolist(), np.mean(output, axis=1).tolist(),
                np.mean(output)
          ]  #This calculates the mean for axis = 0, axis = 1 and overall
      Variance = [
            np.var(output, axis=0).tolist(), np.var(output, axis=1).tolist(), np.var(output)
          ]  #This calculates the variance for axis = 0, axis = 1 and overall
      standard_deviation = [
            np.std(output, axis=0).tolist(), np.std(output, axis=1).tolist(), np.std(output)
        ]  #This calculates a mean for axis = 0, axis = 1 and overall
      maximum = [
            np.max(output, axis=0).tolist(), np.max(output, axis=1).tolist(), np.max(output)
          ]  #This calculates the maximum for axis = 0, axis = 1 and overall
      minmum = [
            np.min(output, axis=0).tolist(), np.min(output, axis=1).tolist(), np.min(output)
          ]  #This calculates the minimum for axis = 0, axis = 1 and overall
      Total_Sum = [
            np.sum(output, axis=0).tolist(), np.sum(output, axis=1).tolist(), np.sum(output)
          ]  #This calculates the sum for axis = 0, axis = 1 and overall

      calculations = {
            'mean': mean,
            'Variance': Variance,
            'standard deviation': standard_deviation,
            'maximum': maximum,
            'minimum': minmum,
            'Sum': Total_Sum
        }  # This creates put all the results in a tuple
    return calculations
