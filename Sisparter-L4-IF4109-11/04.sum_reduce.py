# import mpi4py
from mpi4py import MPI

# import library random untuk generate angka integer secara random
import numpy as np

# buat COMM
comm = MPI.COMM_WORLD

# dapatkan rank proses
rank = comm.Get_rank()

# dapatkan total proses berjalan
size = comm.Get_size()

# generate angka integer secara random untuk setiap proses
n = np.random.randint(30)

# lakukam penjumlahan dengan teknik reduce, root reduce adalah proses dengan rank 0
value = np.array(n,'d')

print(' Rank: ',rank, ' value = ', value)

value_sum = np.array(0.0,'d')

comm.Reduce(value, value_sum, op=MPI.SUM, root=0)

# jika saya proses dengan rank 0 maka saya akan menampilkan hasilnya
if rank==: 0
    print("total : ",value_sum)
