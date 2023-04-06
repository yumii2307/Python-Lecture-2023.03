import datetime as dt
# 이름과 금액을 입력으로 받아서 account에 새로운 항목을 추가
def create_account(account):
    cmd = input('이름 금액> ').split()
    name, amount = cmd[0], int(cmd[1])
    now = dt.datetime.now()
    ano = now.strftime('%H%M%S')
    account.append({'계좌번호': ano, '소유주': name, '잔액': amount})

# 계좌번호와 금액을 입력으로 받아서 계좌의 금액을 추가
def deposit(account):
    cmd = input('계좌번호 금액> ').split()
    ano, amount = cmd[0], int(cmd[1])
    for acc in account:
        if ano == acc['계좌번호']:
            acc['잔액'] += amount
            return

# 계좌번호와 금액을 입력으로 받아서 계좌의 금액을 인출
def withdraw(account):
    cmd = input('계좌번호 금액> ').split()
    ano, amount = cmd[0], int(cmd[1])
    for acc in account:
        if ano == acc['계좌번호']:
            acc['잔액'] -= amount
            return