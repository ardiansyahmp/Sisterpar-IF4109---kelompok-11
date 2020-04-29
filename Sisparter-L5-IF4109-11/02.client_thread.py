# import socket dan sys
import socket, sys
# fungsi utama
def main():
    # buat socket bertipe TCP
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # tentukan IP server target
    ip = "192.168.100.13" #ip local laptop
    
    # tentukan por server
    port = 8080

    # lakukan koneksi ke server
    try:
        soc,connect((ip, port))
    except:
        # print error
        print("Koneksi error")
        # exit
        sys.exit()
    
    # tampilkan menu, enter quit to exit
    print("Masukkan 'quit' untuk keluar")
    message = input(" -> ")

    # selama pesan bukan "quit", lakukan loop forever
    while message != 'quit':
        # kirimkan pesan yang ditulis ke server
        s.send(massage.encode('test'))
        
        # menu (user interface)
        message = input(" -> ")

    # send "quit" ke server
    soc.send(b'--quit--')

# panggil fungsi utama
if __name__ == "__main__":
    main()
