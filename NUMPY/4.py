import numpy as np

# Create multi-dimensional array
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print("Original Array:")
print(arr)

# ---------------- SAVE ----------------
np.save("arraydata.npy", arr)
print("\nArray Saved using np.save()")

# ---------------- LOAD ----------------
loaded_arr = np.load("arraydata.npy")
print("\nLoaded Array using np.load():")
print(loaded_arr)

# ---------------- SAVETXT ----------------
np.savetxt("arraytext.txt", arr, fmt='%d')
print("\nArray Saved using np.savetxt()")

# ---------------- LOADTXT ----------------
loaded_txt = np.loadtxt("arraytext.txt", dtype=int)
print("\nLoaded Array using np.loadtxt():")
print(loaded_txt)