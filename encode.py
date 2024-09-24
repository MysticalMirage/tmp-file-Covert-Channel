import os
# Shared secrets
os.chdir("/home/ubuntu/covertComms/channel")
# Define the message you want to send
message = "Hello, world!"
# Encode the message within permissions:
fileIteration = 0
for char in message:
    fileNum = str(fileIteration + 1000)
    filename = "file_" + fileNum + "cc"
    f = open(filename, 'w')
    f.close()

    binary = format(ord(char), '08b')

    #print(f"{binary}")
    changeVal = 0o0
    for index, bit in enumerate(binary):
        if bit =='1':
            if index == 0:
                changeVal += 0o400
            elif index == 1:
                changeVal += 0o200
            elif index == 2:
                changeVal += 0o100
            elif index == 3:
                changeVal += 0o40
            elif index == 4:
                changeVal += 0o20
            elif index == 5:
                changeVal += 0o10
            elif index == 6:
                changeVal += 0o4
            elif index == 7:
                changeVal += 0o2
    #print(f"{changeVal}")
    
    # Set end of message
    if fileIteration == len(message) - 1:
        changeVal += 0o1
    
    # Commit character
    os.chmod(filename, changeVal)

    fileIteration += 1
    