from valclient.client import Client

#client = Client(region="ap")
#client.activate()

#data = client.fetch_presence()
#print(str(data))

import psutil
#dict_pids = {
#    p.info["pid"]: p.info["name"]
#    for p in psutil.process_iter(attrs=["pid", "name"])
#}

required_processes = ['Discord.exe']
processes = []
for proc in psutil.process_iter():
    processes.append(proc.name())
print(str(set(required_processes).issubset(processes)))

#print(str(dict_pids))