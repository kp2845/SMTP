from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    # mailserver = 'smtp.google.com'
    
    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start - Open TCP Socket and connect to mail server port
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    #print(recv)
    if recv[:3] != '220':
       print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    if recv1[:3] != '250':
       print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    # Fill in start - Setup and encode from address
    mailFrom = 'MAIL FROM:<kairipurnell@gmail.com>\r\n'
    clientSocket.send(mailFrom.encode())
    receivemail = clientSocket.recv(1024).decode()
    # print(receivemail)
    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start - Send receipt address
    receipt = 'RCPT TO:<kairipurnell@gmail.com>\r\n'
    clientSocket.send(receipt.encode())
    receivereceipt = clientSocket.recv(1024).decode()
    # print(recceiverreceipt)
    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    dataCommand = 'DATA\r\n'
    clientSocket.send(dataCommand.encode())
    senddata = clientSocket.recv(1024).decode()
    # print(senddata)
    # Fill in end

    # Send message data.
    # Fill in start
    # message_data = 'Subject This is not SPAM\r\n''
    clientSocket.send(msg.encode())
    # Fill in end

    # Message ends with a single period.
    # Fill in start
    clientSocket.send(endmsg.encode())
    message_end = clientSocket.recv(1024).decode()
    # print(message_end)
    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    quit_command = 'QUIT\r\n'
    clientSocket.send(quit_command.encode())
    send_quit = clientSocket.recv(1024).decode()
    # print(send_quit)
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
