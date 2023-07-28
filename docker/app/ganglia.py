import xmltodict
import jsons
from decimal import *
from datetime import datetime as dt


def get_line():
    filePath = "./log/ganglia/ganglia.xml"

    with open(filePath, "r") as f:
        xmlString = f.read()
  
    json_string = jsons.dumps(xmltodict.parse(xmlString), indent=4)
    json_object = jsons.loads(json_string)
    cjade = 0
    csnow = 0
    thunder = 0
    clusters = json_object["GANGLIA_XML"]["GRID"]["CLUSTER"]
    for cluster in clusters:
        find_jade = cluster["HOST"]
        if type(find_jade) == dict:
            if find_jade["@NAME"] == "supreme-jade01":
                # print(find_jade)
                for metric in find_jade["METRIC"]:
                    if metric["@NAME"] == "load_one":
                        cjade = cjade + Decimal(metric["@VAL"])

        for hosts in cluster["HOST"]:
            if type(hosts) == dict:
                if hosts["@NAME"] == "supreme-snow01":
                    for metric in hosts["METRIC"]:
                        if metric["@NAME"] == "load_one":
                            csnow = csnow + Decimal(metric["@VAL"])
                if hosts["@NAME"] == "supreme-snow02":
                    for metric in hosts["METRIC"]:
                        if metric["@NAME"] == "load_one":
                            csnow = csnow + Decimal(metric["@VAL"])
                if hosts["@NAME"] == "supreme-thunder01":
                    for metric in hosts["METRIC"]:
                        if metric["@NAME"] == "load_one":
                            thunder = thunder + Decimal(metric["@VAL"])
                if hosts["@NAME"] == "supreme-thunder02":
                    for metric in hosts["METRIC"]:
                        if metric["@NAME"] == "load_one":
                            thunder = thunder + Decimal(metric["@VAL"])

    return {"cjade": round(cjade), "thunder": round(thunder), "csnow": round(csnow), "date": dt.now().minute}


def get_bar():
    filePath = "./log/ganglia/ganglia.xml"

    with open(filePath, "r") as f:
        xmlString = f.read()
    json_string = jsons.dumps(xmltodict.parse(xmlString), indent=4)
    json_object = jsons.loads(json_string)

    cjade = {"cpu": [], "user": []}
    csnow = {"cpu": [], "user": []}
    thunder = {"cpu": [], "user": []}
    clusters = json_object["GANGLIA_XML"]["GRID"]["CLUSTER"]
    for cluster in clusters:
        find_jade = cluster["HOST"]
        if type(find_jade) == dict:
            if find_jade["@NAME"] == "supreme-jade01":
                for metric in find_jade["METRIC"]:
                        if metric["@NAME"] == "cpu_system":
                            cpuSystem = metric["@VAL"]
                            cjade["cpu"].append(cpuSystem)
                        if metric["@NAME"] == "cpu_user":
                            cpuUser = metric["@VAL"]
                            cjade["user"].append(cpuUser)

        for hosts in cluster["HOST"]:
            if type(hosts) == dict:
                if hosts["@NAME"] == "supreme-snow01":
                    for metric in hosts["METRIC"]:
                        if metric["@NAME"] == "cpu_system":
                            cpuSystem = metric["@VAL"]
                            csnow["cpu"].append(cpuSystem)
                        if metric["@NAME"] == "cpu_user":
                            cpuUser = metric["@VAL"]
                            csnow["user"].append(cpuUser)
                if hosts["@NAME"] == "supreme-snow02":
                    for metric in hosts["METRIC"]:
                        if metric["@NAME"] == "cpu_system":
                            cpuSystem = metric["@VAL"]
                            csnow["cpu"].append(cpuSystem)
                        if metric["@NAME"] == "cpu_user":
                            cpuUser = metric["@VAL"]
                            csnow["user"].append(cpuUser)
                if hosts["@NAME"] == "supreme-thunder01":
                    for metric in hosts["METRIC"]:
                        if metric["@NAME"] == "cpu_system":
                            cpuSystem = metric["@VAL"]
                            thunder["cpu"].append(cpuSystem)
                        if metric["@NAME"] == "cpu_user":
                            cpuUser = metric["@VAL"]
                            thunder["user"].append(cpuUser)
                if hosts["@NAME"] == "supreme-thunder02":
                    for metric in hosts["METRIC"]:
                        if metric["@NAME"] == "cpu_system":
                            cpuSystem = metric["@VAL"]
                            thunder["cpu"].append(cpuSystem)
                        if metric["@NAME"] == "cpu_user":
                            cpuUser = metric["@VAL"]
                            thunder["user"].append(cpuUser)

    return [{"cjade": cjade, "thunder": thunder, "csnow": csnow}]
