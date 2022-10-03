from ctypes import FormatError
import socket
import logging

# Select an appropriate port number. 
PORT = 5420
# Set The Server's IP Address
SERVER_IP = "192.168.56.1"
# Set up the Server's Address
ADDR =  (SERVER_IP, PORT)
FORMAT = 'utf-8'

logging.basicConfig(filename = "AgentChatLog.txt",  level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p')

logging.info('Client Online')
# Add code to initialize the Socket.
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)
logging.info('Client Connected to Server using {ADDR}')

# Write Code that will allow the Client (Agent) to send messages to the server. 
# The Function accepts the message as a String (msg) and sends that message to the Server through a connection established.
def send(msg):
    print(f"[MESSAGE SENT]")
    logging.info('Message sent to Server')
    client.send(msg.encode(FORMAT))

# Write code to Prompts the Agent to enter their connection code and returns the code given.
def getConCode():
    print(f"[AWAITING CONNECTION....]")
    code = input("Enter your connection code:\n")
    logging.info('Client Code Requested')
    return(code)

# Write code to Prompts the Agent to enter an answer and returns the answer given.
def getAnswer(question):
    print(f"[QUESTION RECEIVED]")
    ans = input("What's the answer?:\n")
    return(ans)

# Get Connection Code.
connCode = getConCode()
logging.info('Client Code Retrieved')

# Send Connection Code to Server.
send(connCode)

# Receive question from server.
question = client.recv(1024).decode(FORMAT)
logging.info('Server Secret Question Received')

# Get Answer from Agent.
answer = getAnswer(question)
logging.info('Server Secret Question Answered')

# Send Answer to Server.
send(answer)

# Recive and print response from the server.
welcome = client.recv(1024).decode(FORMAT) #decodes the response received from the server.
print(f"{welcome}")
print(f"[CONNECTION TERMINATED]")
logging.info('Client Connection Terminated')

#closes the client connection
client.close()