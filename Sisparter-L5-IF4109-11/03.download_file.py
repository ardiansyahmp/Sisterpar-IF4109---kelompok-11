import os
import requests
import threading
import urllib.request, urllib.error, urllib.parse
import time

# file yang akan di download oleh sistem berupa url
url = "https://apod.nasa.gov/apod/image/1901/LOmbradellaTerraFinazzi.jpg"

# melakukan split data yang akan di download
def buildRange(value, numsplits):
    lst = []
    for i in range(numsplits):
        if i == 0:
            lst.append('%s-%s' % (i, int(round(1 + i * value/(numsplits*1.0) + value/(numsplits*1.0)-1, 0))))
        else:
            lst.append('%s-%s' % (int(round(1 + i * value/(numsplits*1.0),0)), int(round(1 + i * value/(numsplits*1.0) + value/(numsplits*1.0)-1, 0))))
    return lst

class SplitBufferThreads(threading.Thread):
    """ Splits the buffer to ny number of threads
        thereby, concurrently downloading through
        ny number of threads.
    """
    def __init__(self, url, byteRange):
        super(SplitBufferThreads, self).__init__()
        self.__url = url
        self.__byteRange = byteRange
        self.req = None

    def run(self):
        self.req = urllib.request.Request(self.__url,  headers={'Range': 'bytes=%s' % self.__byteRange})

    def getFileData(self):
        return urllib.request.urlopen(self.req).read()


def main(url=None, splitBy=3):
    start_time = time.time()
    # mengecek yang di input merupakan url atau bukan
    if not url:
        print("Please Enter some url to begin download.")
        return
    #Mengisi variabel file name dengan url yang di split
    fileName = url.split('/')[-1]
    #mengecek besar file yang akan di download dalam byte
    sizeInBytes = requests.head(url, headers={'Accept-Encoding': 'identity'}).headers.get('content-length', None)
    print("%s bytes to download." % sizeInBytes)
    if not sizeInBytes:
        print("Size cannot be determined.")
        return

    dataLst = []
    for idx in range(splitBy):
        # Mendapatkan range dari total bytes
        byteRange = buildRange(int(sizeInBytes), splitBy)[idx]
        #Melakukan split terhadap buffer
        bufTh = SplitBufferThreads(url, byteRange)
        bufTh.start()
        bufTh.join()
        dataLst.append(bufTh.getFileData())

    content = b''.join(dataLst)
# Mesave data tersebut ke directory dan mengecek data tersebut apakah sudah terdownload dengan nama yang sesuai terdefinisi di file name 
    if dataLst:
        if os.path.exists(fileName):
            os.remove(fileName)
        print("--- %s seconds ---" % str(time.time() - start_time))
        with open(fileName, 'wb') as fh:
            fh.write(content)
        print("Finished Writing file %s" % fileName)

if __name__ == '__main__':
    main(url)
