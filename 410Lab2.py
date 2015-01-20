import socket
import sys
try:
	import thread
except ImportError:
	import _thread as thread

def clientthread(conn):

	while 1:
		data = conn.recv(1024)

		if not data:	
			return

	
		data2 = str(data)
		data2 = data2[0:len(data2)-2]
		reply = '<Hello ' + data2 + ' >\r\n'

		conn.sendall(reply.encode("UTF-8"))
	
	


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
    sys.exit()
print('Socket created.')

host = ''
port = 8888
try:
	s.bind((host, port))
except socket.error as msg:
	sys.exit()

s.listen(3)


while 1:
	conn, addr = s.accept()
	thread.start_new_thread(clientthread, (conn,))
	
	
conn.close()
s.close()

	

