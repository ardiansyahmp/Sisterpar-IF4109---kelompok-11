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


# jika saya adalah proses dengan rank 0 maka:
# saya menerima nilai dari proses 1 s.d proses dengan rank terbesar
# menjumlah semua nilai yang didapat (termasuk nilai proses saya)
if rank ==  0:
    nilai = [n]
    print("value in rank 0 : ",nilai[0])
    for i in range(1, size):
        recvMsg = comm.recv(source=i)
        print("receive value : ",recvMsg)
        nilai.append(recvMsg)
    print("total : ",np.sum(nilai))
	
# jika bukan proses dengan rank 0, saya akan mengirimkan nilai proses saya ke proses dengan rank=0
else:
    sendMsg = n
    comm.send(sendMsg, dest=0)
