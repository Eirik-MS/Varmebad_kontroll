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

t = np.array(df.t)
U = np.array(df.U)
Ufb = np.array(df.Ufb)
T_målt = np.array(df.T_målt)
T_a = np.array(df.T_a)
D = np.array(df.D)
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

plt.plot(t, T_a, label=f'Satt temperatur {T_a[-1]:.2f}')
plt.plot(t, T_målt, label='Målt temperatur med målestøy', alpha = 0.5)
plt.plot(t, T_målt_filtrert, label='Filtrert måling')
plt.plot(t, T_real, label='Faktisk temperatur')

plt.ylim(19, None)
plt.legend()
plt.xlabel('Index')
plt.ylabel('Values')
plt.title('System Data')
plt.show()