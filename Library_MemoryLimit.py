


import resource


def Main(Bytes = None):
    #Kilobytes = Bytes/1000.0

    print 'Changing Memory Limit To : ' + str(Bytes) + " Bytes"

    MemoryLimitBytes = resource.RLIMIT_AS
    soft, hard = resource.getrlimit(MemoryLimitBytes)
    print 'Soft limit starts as     :', soft

    resource.setrlimit(MemoryLimitBytes, (Bytes, hard)) #limit to one kilobyte

    soft, hard = resource.getrlimit(MemoryLimitBytes)
    print 'Soft limit changed to    :', soft
