import sys

lines = sys.stdin.read().splitlines() #["DEPOSIT 100", "BALANCE"]
balance = 0
for line in lines:
    # if line == "":
    #     continue
    if not line:
        continue

    parts = line.split()
    cmd = parts[0]
    if cmd == "DEPOSIT":
        amount = int(parts[1])
        balance = amount + balance
    elif cmd == "BALANCE":
        print(balance)