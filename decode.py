import os, stat
# Shared secrets
os.chdir("/home/ubuntu/covertComms/channel")
# Collect the message sent
message = ""
end = 0
fileNum = 1000
while end == 0:
    binary = ""
    filename = "file_" + str(fileNum) + "cc"
    stats = os.stat(filename)
    chmodVal = oct(stats.st_mode)[-3:]
    for val in str(chmodVal):
        num = int(val)
        if (num - 4) >= 0:
            num = num - 4
            binary = binary + "1"
        else:
            binary = binary + "0"
        if (num - 2) >= 0:
            num = num - 2
            binary = binary + "1"
        else:
            binary = binary + "0"
        if len(binary) != 8:
            if (num - 1) >= 0:
                num = num - 1
                binary = binary + "1"
            else:
                binary = binary + "0"
    
    # Cleanup
    fileNum += 1
    os.remove(filename)

    # Add character to message
    message = message + chr(int(binary, 2))
    
    # Check for end of message
    if num == 1:
        end = 1

print("The encoded message is: " + message)
