import sys

lines = sys.stdin.read().splitlines() #["DEPOSIT 100", "BALANCE"]
balances = {}
for line in lines:
    # if line == "":
    #     continue
    if not line:
        continue

    parts = line.split()
    cmd = parts[0]
    user = parts[1]
    if cmd == "DEPOSIT":
        amount = int(parts[2])
        balances[user] = balances.get(user, 0) + amount

    elif cmd == "WITHDRAW":
        amount = int(parts[2])
        if balances.get(user,0) >= amount:
            balances[user] = balances.get(user,0) -  amount
        else:
            print("INSUFFICIENT")

    elif cmd == "TRANSFER":
        amount = int(parts[3])
        from_user = parts[1]
        to_user = parts[2]
        if balances.get(from_user,0) >= amount:
            balances[user] = balances.get(from_user,0) - amount
            balances[to_user] = balances.get(to_user,0) + amount
        else:
            print("INSUFFICIENT")

    elif cmd == "BALANCE":
        print(balances.get(user, 0))