import socket
import binascii
import struct
import math
import array
import time
import _thread 

TCP_IP = '192.168.132.1'
TCP_PORT = 9800
BUFFER_SIZE = 5000000
d = 35
n = 221
      
def RSA_decrypt(msg,length,file_count):
    lock = _thread.allocate_lock()
    lock.acquire()
    decrypt_msg = bytearray(length)
    i = int(0)
    pt = int(0)
    ct = int(0)
    k = int(1)
    while i < length-1:
        ct = msg[i]
        ct = ct - 96
        k = 1
        for j in range(0,d):
            k = k * ct
            k = math.fmod(k,n)
        pt = k + 96
        decrypt_msg[i] = int(pt)
        i = i + 1
    file_img = open("C:\Users\X-Calibre\Downloads"+str(file_count)+".bmp","wb")
    file_img.write(decrypt_msg)
    file_img.close();
    lock.release()
    
if __name__ == '__main__':
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.bind((TCP_IP, TCP_PORT))
    
    while 1:
        recv_index = 0
        file_counter = 0
        time_start = 0
        time_end = 0
        time_frame = 0
        first_byte_flag = 1
        message_length = BUFFER_SIZE
        tcp_socket.listen(1)
        
        conn, addr = tcp_socket.accept()
        print('Connection address:', addr)
        
        buf = bytearray(BUFFER_SIZE)
        view = memoryview(buf)
        
        while recv_index < message_length:
            nbytes = conn.recv_into(view)
            if nbytes:
                recv_index = recv_index + nbytes
                if first_byte_flag:
                    message_length = int.from_bytes(buf[0:4], byteorder='little', signed=False)
                    first_byte_flag = 0
                    
                if recv_index > message_length and first_byte_flag == 0:
                    print("Frame at Time = ",time.time())
                    
                    size = int((message_length-4)/2)
                    
                    data_int16 = struct.unpack('h'*size ,buf[4:message_length])
                    buf[0:(recv_index-message_length)] = buf[message_length:recv_index]
                    view = memoryview(buf[(recv_index-message_length):])

                    _thread.start_new_thread(RSA_decrypt,(data_int16,size,file_counter))
                    
                    file_counter = file_counter + 1
                    message_length = BUFFER_SIZE
                    recv_index = 0
                    first_byte_flag = 1
                    
                else:
                    view = view[nbytes:]
                
        
    conn.close()

