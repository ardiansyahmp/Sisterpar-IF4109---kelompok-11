# import mpi4py
from mpi4py import MPI

# buat COMM
comm = MPI.COMM_WORLD

# dapatkan rank proses
rank = comm.Get_rank()

# dapatkan total proses berjalan
size = comm.Get_size()

# jika saya rank 0 maka saya akan melakukan broadscast
if rank == 0 :
     for i in range(1, size):
        sendMsg = "Broadcast message from "+str(rank)+" to rank "+str(i)
        comm.send(sendMsg, dest=i)

	
# jika saya bukan rank 0 maka saya menerima pesan
else:
    recvMsg = comm.recv(source=0)
    print(recvMsg)
	
