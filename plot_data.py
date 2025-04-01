import h5py
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Path to the .mat file
file_path = r"C:\Users\ivers\Documents\GitHub\Varmebad_kontroll\system_data.mat"

# Check if the file exists
if not os.path.exists(file_path):
    raise FileNotFoundError(f"The file {file_path} does not exist.")

# Load the .mat file and read the data
with h5py.File(file_path, 'r') as mat:
    # Assuming the data is stored in the first dataset
    dataset_name = list(mat.keys())[0]
    data = np.array(mat[dataset_name])  # Convert to numpy array

# Define column names
column_names = ['t', 'U', 'Ufb', 'T_målt', 'T_a', 'D', 'T_målt_filtrert', 'T_real']

# Convert the data to a pandas DataFrame with column names
df = pd.DataFrame(data, columns=column_names)

t = np.array(df.t)/60
U = np.array(df.U)/0.0125
Ufb = np.array(df.Ufb)/0.0125
T_målt = np.array(df.T_målt)
T_a = np.array(df.T_a)
D = np.array(df.D)/10
T_målt_filtrert = np.array(df.T_målt_filtrert)
T_real = np.array(df.T_real)

"""
# Plot the data
plt.plot(t, T_real, label='Temperatur')
plt.plot(t, U, label='U')
plt.plot(t, Ufb, label='Ufb')
plt.plot(t, T_målt, label='T_målt')
plt.plot(t, T_a, label='T_a')
plt.plot(t, D, label='D')
plt.plot(t, T_målt_filtrert, label='T_målt_filtrert')
"""
"""
# find time where T_real first goes over 37.7 degrees (just one number)
index37_7 = np.argmax(T_real > 37.7)
print(f'Tid til 38 - 0.3 grader: {t[index37_7]:.2f} min')


plt.subplot(2, 1, 1)
plt.title('Temperatur i vannbadet', size = 17)
plt.axhline(y=T_a[-1], color='black', label=f'Satt temperatur {T_a[-1]:.2f}')
plt.axvline(x=t[index37_7], color='red', label=f'Tid til 38 - 0.3 grader: {t[index37_7]:.2f} min', linestyle='--')
plt.plot(t, T_målt, label='Målt temperatur med målestøy', alpha = 0.5)
plt.plot(t, T_målt_filtrert, label='Filtrert måling')
plt.plot(t, T_real, label='Faktisk temperatur')
plt.ylim(19, None)
plt.ylabel('Tempertur (C)')

plt.subplot(2, 1, 2)
plt.title('Zoomet inn rundt Ta', size = 12)
plt.axhline(y=T_a[-1], color='black', label=f'Satt temperatur {T_a[-1]:.2f} +- 0.3')

plt.axhline(y=T_a[-1] - 0.3, color='black', linestyle='--')
plt.axhline(y=T_a[-1] + 0.3, color='black', linestyle='--')

plt.axvline(x=t[index37_7], color='red', label=f'Tid til 38 - 0.3 grader: {t[index37_7]:.2f} min', linestyle='--')

plt.plot(t, T_målt, label='Målt temperatur med målestøy', alpha = 0.5)
plt.plot(t, T_målt_filtrert, label='Filtrert måling')
plt.plot(t, T_real, label='Faktisk temperatur')
plt.ylim(T_a[-1] - 0.5, T_a[-1] + 0.5)

plt.legend(loc = 'lower right')
plt.xlabel('Tid (min)')
plt.ylabel('Tempertur (C)')"
"""

colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

timespan1 = [8, 9]
timespan2 = [15, 16]

plt.subplot(3, 1, 1)
plt.title("Sammenheng mellom Ufb og pulsbredde", size = 17)
plt.axvline(x=timespan1[0], color='red', linestyle='--')
plt.axvline(x=timespan1[1], color='red', linestyle='--')

plt.axvline(x=timespan2[0], color='orange', linestyle='--')
plt.axvline(x=timespan2[1], color='orange', linestyle='--')

plt.plot(t, Ufb, label='Ufb', color = colors[1])
plt.plot(t, U, label='U', color = colors[0])
plt.plot(t, Ufb, color = colors[1])
plt.plot(t, D, label='D', color = colors[2])
plt.ylim(None, U[-1] *1.2)
plt.xlim(-0.1, 60)
plt.legend()

plt.subplot(3, 1, 2)
plt.axvline(x=timespan1[0], color='red', linestyle='--')
plt.axvline(x=timespan1[1], color='red', linestyle='--')

plt.axvline(x=timespan2[0], color='orange', linestyle='--')
plt.axvline(x=timespan2[1], color='orange', linestyle='--')

#plt.plot(t, U, label='U')
#plt.plot(t, Ufb, label='Ufb')
plt.plot(t, D, label='D', color = colors[2])


# change y ticks to be in percent from 0-1
plt.yticks(np.arange(0, 1.1, 0.2), [f'{i}%' for i in np.arange(0, 101, 20)])


plt.ylim(-0.2, 1.2)
plt.xlim(-0.1, 60)


plt.subplot(3,2,5)
plt.plot(t, U, label='U', color = colors[0])
plt.plot(t, D*800, label='D', color = colors[2])

plt.axvline(x=timespan1[0], color='red', linestyle='--')
plt.axvline(x=timespan1[1], color='red', linestyle='--')

plt.xlim(timespan1[0] * 0.995, timespan1[1] * 1.005)
plt.ylim(-U[-1] *1.2 + U[-1], U[-1] *1.2)
# change y ticks to be in percent from 0-800
plt.yticks(np.arange(0, 801, 200), [f'{i}%' for i in np.arange(0, 101, 25)])


plt.subplot(3,2,6)
plt.plot(t, U, label='U', color = colors[0])
plt.plot(t, D*800, label='D', color = colors[2])

plt.axvline(x=timespan2[0], color='orange', linestyle='--')
plt.axvline(x=timespan2[1], color='orange', linestyle='--')

plt.xlim(timespan2[0] * 0.995, timespan2[1] * 1.005)
plt.ylim(-U[-1] *1.2 + U[-1], U[-1] *1.2)

# change y ticks to be in percent from 0-800
plt.yticks(np.arange(0, 801, 200), [f'{i}%' for i in np.arange(0, 101, 25)])

plt.show()