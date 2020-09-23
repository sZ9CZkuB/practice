name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = {}
time = list()
hr_list =list()
for line in handle:
    if not line.startswith("From"): continue
    if line.startswith("From:"): continue
    words = line.split()
    time.append(words[5])
for digit in time:
    time_split = digit.split(":")
    hr_list.append(time_split[0])
for name in hr_list:
    counts[name] = counts.get(name, 0) + 1
lst = list()
for hour, count in counts.items():
    tup = (hour, count)
    lst.append(tup)
lst = sorted(lst)

for hour, count in lst:
    print(hour, count)