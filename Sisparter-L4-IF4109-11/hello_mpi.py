# gunakan library mpi4py
from mpi4py import MPI

# definisikan communicator
comm = MPI.COMM_WORLD

# dapatkan rank proses
# setiap proses akan mempunyai rank yan unik
rank = comm.Get_rank()

# dapatkan total proses yang berjalan
# total proses ditentukan menggunakan parameter -n pada mpiexec.exe
# mpiecex.exe -n 5 berarti akan ada total 5 proses yang berjalan
size = comm.Get_size()

# setiap proses akan menampilkan rank-nya masing-masing dan total proses yang berjalan
print ("hello world from process %d/%d\n" %(rank,size))

# pada cmd jalankan perintah:
# mpiexec.exe -n 7 python hello_mpi.py