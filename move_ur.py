mport socket

HOST = "10.5.18.172"

PORT = 30002

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))

cmd = "movej([0,1.57,-1.57,3.14,-1.57,1.57],a=1.4, v=1.05, t=0, r=0)" + "\n"

s.send(cmd.encode('utf-8'))

s.close()

print('Received',repr(data))
