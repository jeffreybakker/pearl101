import subprocess


file = open('traces.txt', 'r')

trace_list = []

file.readline()

highest = -1

for line in file:
    item = []
    contents = line.split()

    item.append(contents[0])

    name = ""
    for i in range(1, len(contents) - 2):
        if i > 1:
            name += " "
        name += contents[i]

    item.append(name)

    item.append(contents[len(contents) - 2].split("//")[1].split("/")[0])
    item.append(contents[len(contents) - 1])

    # print(str(item[2]))
    # print(item)

    res = str(subprocess.check_output(["traceroute", str(item[2])])).split("\\n")
    hops = 0
    for i in range(1, len(res) - 1):
        # print(res[i])
        hop_list = res[i].split()
        if hop_list[1] != "*":
            hops += 1

    item.append(hops)

    if highest == -1:
        highest = len(trace_list)
        print("new highest hops", item[4])
    elif item[4] > trace_list[highest][4]:
        highest = len(trace_list)
        print("new highest hops", item[4])

    trace_list.append(item)

print(trace_list[highest])
