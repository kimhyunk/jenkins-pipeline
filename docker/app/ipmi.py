import socket
from sre_parse import State
import jsons


def get_power(type):
    filePath = "./log/ipmi/power.log"
    f = open(filePath, 'r')
    lines = f.readlines()

    result = []

    if type == "dashboard":
        for line in lines:
            if line.find("System Power") != -1:
                if line.find("on"):
                    result.append(True)
                else:
                    result.append(False)

    if type == "node":
        str1 = "System Power"
        str2 = ": "
        object_array = []

        for index, line in enumerate(lines):
            if line.find(str1) != -1:
                node_line = lines[index-1].strip("\n")
                node_len = node_line.find(str2) + 2
                node_str = node_line[node_len:len(node_line)].strip()
                state_len = line.find(str2) + 2
                state_str = line[state_len:len(line)].strip()
                object_array.append(
                    {"node": node_str, "state": state_str})
        result = object_array
    f.close()

    return result


def set_power(host, state):

    msgFromClient = jsons.dumps(
        {'cmd': "setpower", "host": host, "state": state})

    # msgFromClient = "test!!!"

    bytesToSend = str.encode(msgFromClient)
    serverAddressPort = ("mas.supreme-k.org", 9300)
    # bufferSize = 1024

    # 클라이언트 쪽에서 UDP 소켓 생성
    UDPClientSocket = socket.socket(
        family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # 생성된 UDP 소켓을 사용하여 서버로 전송
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)

    # msgFromServer = UDPClientSocket.recvfrom(bufferSize)

    # msg = "Message from Server {}".format(msgFromServer[0])
    # print(msg)
    UDPClientSocket.close()

    return {"power": "ok"}

    # return {'cmd': "setpower", "host": host, "state": state}
