import os
import subprocess
import re

# path = ["isab1PercentNaiv.py","isab1PercentMaxCompression.py"]

# path0 = ["AsteroidForTestMax1TNaiv.py","DarkMatterForTestMax1TNaiv.py","earthQuakeProgMax1TNaiv.py","ionization3DForTestProgMax1TNaiv.py",
#     "isab1PercentMax1TNaiv.py","ViscousFingers5PercProg1TNaiv.py","cloudProgMax1TNaiv.py","ionization2DForTestProgMax1TNaiv.py",
#     "SeeSurfForTest1TNaiv.py","StartingVortForTest1TNaiv.py","StreetVortForTest1TNaiv.py","Volcano1PercMax1TNaiv.py"]

path1 = ["AsteroidForTestMax1T.py","DarkMatterForTestMax1T.py","earthQuakeProgMax1T.py","ionization3DForTestProgMax1T.py",
    "isab1PercentMax1T.py","ViscousFingers5PercProg1T.py","cloudProgMax1T.py","ionization2DForTestProgMax1T.py","SeeSurfForTest1T.py",
    "StartingVortForTest1T.py","StreetVortForTest1T.py","Volcano1PercMax1T.py"]

last_logs_list_prog = []
# last_logs_list_naiv = []
time_prog = []
# time_naiv = []

a = input("Please chose the number of threads: ")


# for name in path0:
#     # if "Naiv" in name:
#     result = subprocess.run(["$pvpython", name], stdout=subprocess.PIPE,text=True)
#     logs = result.stdout.strip().split("\n")
#     last_log = logs[-1]
#     with open("log_file_test.txt", "w") as f:
#         f.write(last_log)
#     print(last_log)
#     with open("log_file_test.txt", "r") as f:
#         lines = f.readlines()
#         last_logs_list_naiv.append(lines[-1])
#     if os.path.exists("log_file_test.txt"):
#         os.remove("log_file_test.txt")
#     # else:
for name in path1:
    result = subprocess.run(["pvpython", name, a], stdout=subprocess.PIPE,text=True)
    logs = result.stdout.strip().split("\n")
    last_log = logs[-1]
    with open("log_file_test.txt", "w") as f:
        f.write(last_log)
    # print(last_log)
    with open("log_file_test.txt", "r") as f:
        lines = f.readlines()
        last_logs_list_prog.append(lines[-1])
    if os.path.exists("log_file_test.txt"):
        os.remove("log_file_test.txt")

# print(last_logs_list_naiv)
# print(last_logs_list_prog)
# print("HALLO???!!!????")

# for log in last_logs_list_naiv:
#     line = log
#     # regex = r"\[PersistenceDiagramDictEncoding\] Complete \.\.\.\.\.\.\.\.\.\. \[(\d+\.\d+)s\|.*\]"
#     regex = r'\[(\d+\.\d+)s\|.*\]'
#     match = re.search(regex, line)
#     if match:
#         time_str = match.group(1)
#         time_seconds = float(time_str)
#         time_naiv.append(time_seconds)
#         print(time_seconds)


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

print(time_prog)
dataName = ["Asteroid impact","Dark matter","Earthquake","Ionization Front 3D","Isabel","Viscous Fingering","Cloud processes",
    "Ionization Front 2D", "Sea Surface Height", "Starting Vortex", "Street Vortex","Volcanic eruptions"]
    
print("+-------------------+")
print("|{: <25}|{: <10}|".format("Data Set", "Progressive"))
for name,t_naiv,t_prog in zip(dataName,time_prog):
    result = {"name": name, "progressive": t_prog}
    # Affichage avec délimitations graphiques
    print("+-------------------+")
    print("|{: <25}|{: <10.3f}|".format(result["name"],result["progressive"]))
    print("+-------------------+")
    # print('+-----------+---------------+-----------------+')
    # print('| Ligne     | Naive (s)     | Progressive (s) |')
    # print('+-----------+---------------+-----------------+')
    # print(f"| Isabel    | {result["naive"]:>13} | {result["progressive"]:>15} |")
    # print('+-----------+---------------+-----------------+')
