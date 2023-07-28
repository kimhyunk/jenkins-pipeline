import os
# import subprocess


def make_directory(dirs, dir_path):
    result = []

    for dir in dirs:
        data = {}
        if os.path.exists(dir_path + "/" + dir):
            files = os.listdir(dir_path + "/" + dir)
            data["name"] = dir
            data["files"] = files

            result.append(data)
        else:
            data["name"] = dir

            result.append(data)

    return result


def get_file():
    dir_path = "./log/slurm_out"

    dirs = os.listdir(dir_path)
    result = make_directory(dirs, dir_path)

    if len(result) == 0:
        result = {"err": "파일이 존재하지 않음"}

    # filename = './log/slurm_out/HPL/output.1231.out'
    # stats = os.stat(filename)
    # print(stats.st_size)
    # print(stats.st_mtime)
    
    return result


def read_file(dir, file):
    dir_path = "./log/slurm_out"
    result = {"err": "파일이 존재하지 않음"}

    if os.path.exists(dir_path + "/" + dir + "/" + file + ".txt"):
        filePath = dir_path + "/" + dir + "/" + file + ".txt"
        f = open(filePath, 'r')
        result = f.read()

    if os.path.exists(dir_path + "/" + dir + "/" + file + ".out"):
        filePath = dir_path + "/" + dir + "/" + file + ".out"
        f = open(filePath, 'r')
        result = f.read()

    # subprocess.run("./scripts/test.sh")

    return result
