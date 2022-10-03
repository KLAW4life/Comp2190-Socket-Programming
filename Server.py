import socket
import datetime as dt
import threading
import Verify as av
import logging #imports the log library for the program's use

# Selected an appropriate port number. 
PORT = 5420
# Setting up the Server's IP Address
SERVER_IP = "192.168.56.1"
# Seting up the Server's Address
ADDR = (SERVER_IP, PORT)
FORMAT = 'utf-8'

# Logging Code that identifies which file to store the log information and the information format.
logging.basicConfig(filename = "ServerLogFile.txt",  level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p')

#Code to initialize the socket        
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Code to bind Address to the server socket.
server.bind(ADDR)

 # This function processes messages that are read through the Socket.
def clientHandler(conn, addr): 
    print(f"[NEW CONNECTION] {addr} connected.")
    logging.info('Server connection established for {addr}')

    while True:
        # Write Code that allows the Server to receive a connection code from an Agent. 
        print(f"[REQUESTING CODE CONNECTION]")
        logging.info('Request connection code from {addr}')
        message = conn.recv(1024).decode(FORMAT) #decodes the connectionmessage from bytes into a string.
        print(f"[CONNECTION CODE RECEIVED]")
        logging.info('Connection code received from {addr}')
        #print(f"[{addr}] {message}") #prints the address and the message sent

         
        #Logging code that prints to the Server Log File the text in brackets to the Server Log FIle.
        logging.info('Verifying Connection code received from {addr}')
        # Write Code that allows the Server to check if the connection code received is valid.
        agent = av.check_conn_codes(message)
        print(f"[VERIFYING CONNECTION CODE]")
        if (agent == -1):
            print(f"{addr} [CONNECTION TERMINATED]")
            #Logging code that prints to the Server Log File the text in brackets to the Server Log FIle.
            logging.warning('Unauthorized Connection Code from {addr}')
            logging.info('Connection TERMINATED.')
            break
        else:
            print(f"[CONNECTION CODE VERIFIED]")
            #Logging code that prints to the Server Log File the text in brackets to the Server Log FIle.
            logging.info('Connection code from {addr} verified')

        # Write Code that allows the Server to retrieve a random secret question.
        print(f"[ACTIVATING SECURITY PROTOCOL........]")
        #Logging code that prints to the Server Log File the text in brackets to the Server Log FIle.
        logging.info('Randoom Secret Question Generated for {addr}')
        ques = av.getSecretQuestion()
        s_quest = ques[0]
        print(f"[PROTOCOL COMPLETE]")
        print(s_quest)

        # Write Code that allows the Server to send the random secret question to the Client.
        print(f"[USER CONFIRMATION REQUESTED.]")
        conn.send(bytes(s_quest, FORMAT))
        #Logging code that prints to the Server Log File the text in brackets to the Server Log FIle.
        logging.info('Secret Question Sent to {addr}')

        # Write Code that allows the Server to receive an answer from the Client.

        answer = conn.recv(1024).decode(FORMAT)
        #Logging code that prints to the Server Log File the text in brackets to the Server Log FIle.
        logging.info('Secret Question Answer received from {addr}')
        print(f"[PROCESSING.......]")

        # Write Code that allows the Server to check if the answer received is correct.
        result = av.getSecretAnswer(ques,answer)
        #Logging code that prints to the Server Log File the text in brackets to the Server Log FIle.
        logging.info('Validating Secret Question Answer from {addr}')
        if result != True:
            print(f"[CONNECTION TERMINATED]")
            #Logging code that prints to the Server Log File the text in brackets to the Server Log FIle.
            logging.warning('Unauthorized Answer from {addr}')
            #Logging code that prints to the Server Log File the text in brackets to the Server Log FIle.
            logging.info('Connection TERMINATED.')
            break
        else:
            # Write Code that allows the Server to Send Welcome message to agent -> "Welcome Agent X"
            time = dt.datetime.now()
            time2 = str(time)
            open = "Welcome "
            agent2 = str(agent)
            open2 = " Time Logged - "
            wel = open + agent2 + open2 + time2
            print(f"[AGENT VERIFIED]")
            #welcome = ("Welcome",agent,"Time Logged -",time)
            conn.send(bytes(wel, FORMAT))
            #print(f"Welcome",agent,"Time Logged -",time)   
            #Logging code that prints to the Server Log File the text in brackets to the Server Log FIle.
            logging.info('{agent} Successfully Verified')     
            break
    #Logging code that prints to the Server Log File the text in brackets to the Server Log FIle.    
    logging.info('Server Offline')
    print(f"[CONNECTION TERMINATED]")
    conn.close()
def runServer():
    server.listen() #Server is listening for connection sockets
    print(f"[LISTENING] Server is listening on {SERVER_IP}")
    #Logging code that prints to the Server Log File the text in brackets to the Server Log FIle.
    logging.info('Server listening for possible connections')
    while True:
        conn, addr = server.accept() 
        #server is waiting to accept incomming connections

        thread = threading.Thread(target=clientHandler, args=(conn,addr) ) 
        #passing the connection to clientHandler to execute the code.

        thread.start()
        print(f"[ACTIVE CONNECTIONS]{threading.active_count() - 1}") 
        #Tells how many threads or active clients that are connected to the server. 

print("[STARTING] The Server is Starting...")
#Logging code that prints to the Server Log File when the Server is Online.
logging.info('Server Online')
runServer()