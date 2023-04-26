import os
import subprocess
import re

path = ["isab1PercentMax1T.py"]

a = input("Please chose the number of threads: ")

last_logs_list_prog = []
time_prog = []


for name in path:
    result = subprocess.run(["$pvpython", name, a], stdout=subprocess.PIPE,text=True)
    logs = result.stdout.strip().split("\n")
    last_log = logs[-1]
    with open("log_file_test.txt", "w") as f:
        f.write(last_log)
    print(last_log)
    with open("log_file_test.txt", "r") as f:
        lines = f.readlines()
        last_logs_list_prog.append(lines[-1])
    # if os.path.exists("log_file_test.txt"):
    #     os.remove("log_file_test.txt")



for log in last_logs_list_prog:
    line = log
    # regex = r"\[PersistenceDiagramDictEncoding\] Total time \.\.\.\.\.\.\.\.\.\.\.\.\. \[(\d+\.\d+)s\|.*\]"
    regex = r'\[(\d+\.\d+)s\|.*\]'
    match = re.search(regex, line)
    if match:
        time_str = match.group(1)
        time_seconds = float(time_str)
        time_prog.append(time_seconds)
        print(time_seconds)


dataName = ["Isabel"]

print("|{: <25}|{: <10}|".format("Data Set", "Progressive"))
for name,t_prog in zip(dataName,time_prog):
    result = {"name": name,"progressive": t_prog}
    # Affichage avec délimitations graphiques
    print("+-------------------+")
    print("|{: <25}|{: <10.3f}|".format(result["name"], result["progressive"]))
    print("+-------------------+")



