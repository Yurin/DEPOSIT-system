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
        # TODO: balancesを更新
        balances[user] = balances.get(user, 0) + amount
    elif cmd == "BALANCE":
        # TODO: userの残高を出力
        print(balances.get(user, 0))