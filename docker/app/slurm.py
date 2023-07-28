from typing import Union

from typing import Union

def get_nodes(type: Union[str, None] = None):
    filePath = "./log/slurm/nodes.log"

    with open(filePath, 'r') as f:
        lines = f.readlines()

    result = None
    str1 = ''
    str2 = ''
    text_array = []
    use = 0

    if type == "text":
        total = sum(1 for line in lines if "NodeName" in line)
        idle = sum(1 for line in lines if "IDLE" in line)
        result = {"total": total, "idle": idle}

    if type == "state":
        str1 = 'State='
        str2 = ' ThreadsPerCore='
        object_array = []

        name_str1 = 'NodeName='
        name_str2 = ' Arch='

        for index, line in enumerate(lines):
            if str1 in line:
                text_str1 = line.index(str1)
                text_str2 = line.index(str2)
                state = line[text_str1 + 6:text_str2].strip()

                name_line = lines[index-8]
                name_num1 = name_line.index(name_str1)
                name_num2 = name_line.index(name_str2)
                name = name_line[name_num1 + 9:name_num2].strip()

                object_array.append({"node": name, "state": state})

        object_array.pop(1)
        result = object_array

    if type == "cpu":
        str1 = 'CPUAlloc='
        str2 = ' CPUTot='
        cpus = []

        for line in lines:
            if str1 in line:
                text_array.append(line)

        text_array.pop(1)

        for text in text_array:
            text_str1 = text.index(str1)
            text_str2 = text.index(str2)
            cpu = text[text_str1 + 9:text_str2].strip()
            cpus.append(int(cpu))

        use = sum(cpus)
        cjade_cpu = cpus[0]
        csnow_cpu = cpus[1] + cpus[2]
        thunder_cpu = cpus[3] + cpus[4]

        result = {"cjade": cjade_cpu, "csnow": csnow_cpu, "thunder": thunder_cpu, "use": use}

    if type == "free":
        str1 = 'FreeMem='
        str2 = ' Sockets='
        frees = []

        for line in lines:
            if str1 in line:
                text_array.append(line)

        text_array.pop(1)

        for text in text_array:
            text_str1 = text.index(str1)
            text_str2 = text.index(str2)
            free_mem = text[text_str1 + 8:text_str2].strip()
            free_mem = 0 if free_mem == "N/A" else int(free_mem)
            frees.append(free_mem)

        use = sum(frees)
        cjade_mem = frees[0]
        csnow_mem = frees[1] + frees[2]
        thunder_mem = frees[3] + frees[4]

        result = {"cjade": round(cjade_mem/1000), "csnow": round(csnow_mem/1000), "thunder": round(thunder_mem/1000), "use": round(use/1000)}

    return result



def _get_nodes(type: Union[str, None] = None):
    filePath = "./log/slurm/nodes.log"
    f = open(filePath, 'r')
    lines = f.readlines()

    result = None
    str1 = ''
    str2 = ''
    text_array = []
    use = 0

    if type == "text":
        total = 0
        idle = 0

        name_str1 = 'NodeName='
        name_str2 = ' Arch='

        for line in lines:
            if line.find("NodeName") != -1:
                total = total + 1
            if line.find("IDLE") != -1:
                idle = idle + 1

        result = {"total": total, "idle": idle}

    if type == "state":
        str1 = 'State='
        str2 = ' ThreadsPerCore='
        object_array = []

        name_str1 = 'NodeName='
        name_str2 = ' Arch='

        for index, line in enumerate(lines):
            if line.find(str1) != -1:
                text_str1 = line.index(str1)
                text_str2 = line.index(str2)
                state = line[text_str1 + 6:text_str2].strip()

                name_line = lines[index-8]
                name_num1 = name_line.index(name_str1)
                name_num2 = name_line.index(name_str2)
                name = name_line[name_num1 + 9:name_num2].strip()

                object_array.append(
                    {"node": name, "state": state})

        object_array.pop(1)
        result = object_array

    if type == "cpu":
        str1 = 'CPUAlloc='
        # str2 = ' CPUErr='
        str2 = ' CPUTot='
        cpus = []
        use = 0

        for line in lines:
            if line.find(str1) != -1:
                text_array.append(line)

        # text_array = text_array[1:len(text_array)]
        text_array.pop(1)

        for text in text_array:
            text_str1 = text.index(str1)
            text_str2 = text.index(str2)
            cpu = text[text_str1 + 9:text_str2].strip()
            cpus.append(int(cpu))

        for cpu in cpus:
            use = use + cpu

        cjade_cpu = cpus[0]
        csnow_cpu = cpus[1] + cpus[2]
        thunder_cpu = cpus[3] + cpus[4]

        result = {"cjade": cjade_cpu, "csnow": csnow_cpu,
                  "thunder": thunder_cpu, "use": use}

    if type == "free":
        str1 = 'FreeMem='
        str2 = ' Sockets='
        frees = []
        use = 0

        for line in lines:
            if line.find(str1) != -1:
                text_array.append(line)

        # text_array = text_array[1:len(text_array)] # maas 노드 제거 안함
        text_array.pop(1)

        for text in text_array:
            text_str1 = text.index(str1)
            text_str2 = text.index(str2)
            free_mem = text[text_str1 + 8:text_str2].strip()
            if free_mem == "N/A":
              free_mem = 0
            frees.append(int(free_mem))

        for free in frees:
            use = use + free

        cjade_mem = frees[0]
        csnow_mem = frees[1] + frees[2]
        thunder_mem = frees[3] + frees[4]

        result = {"cjade": round(cjade_mem/1000), "csnow": round(csnow_mem/1000),
                  "thunder": round(thunder_mem/1000), "use": round(use/1000)}

    f.close()

    return result


def get_squeue():
    logs = []
    filePath = "./log/slurm/squeue.log"
    f = open(filePath, 'r')
    lines = f.readlines()
    lines.pop(0)

    # return {"logs": lines}

    for log in lines:
        logString = log.strip("").strip("\n").split()
        logObject = {
            "jobid": logString[0],
            "partition": logString[1],
            "name": logString[2],
            "user": logString[3],
            "st": logString[4],
            "time": logString[5],
            "nodes": logString[6],
            "nodelist": logString[7]
        }

        logs.append(logObject)

    return {"logs": logs}
    # if len(lines) == 1:
    #     return {"squeue": len(lines) - 1}
    # else:
    #     return {"squeue": len(lines) - 2}


def get_runtime():
    filePath = "./log/slurm/runtime.log"
    f = open(filePath, 'r')
    lines = f.readlines()

    return {'runtime': lines[0].strip()}


def get_job_history(type):
    result = None
    jobs = []

    filePath = "./log/slurm/jobhistory_bar"
    f = open(filePath, 'r')
    lines = f.readlines()

    if type == "system":
        for line in lines:
            if line.find("JobID") == -1:
                if line.find("---") == -1:
                    datas = line.split()
                    if datas[0] != "" and datas[0] != None:
                        jobs.append({"id": int(datas[0]), "partition": datas[1], "cpu": int(
                            datas[4]), "second": round(int(datas[4]) / int(datas[0]))})
                    result = jobs

    return result
