import datetime as dt
from account import Account

# 이름과 금액을 입력으로 받아서 account에 새로운 항목을 추가
def create_account(acc_list):
    try:
        cmd = input('이름 금액 입력> ').split()
        name,amount = cmd[0],int(cmd[1])
    except:
        print('입력이 잘못되었습니다.')
        return
    now = dt.datetime.now()
    ano = now.strftime('%H%M%S')
    account = Account(ano, name, amount)
    acc_list.append(account)
    return

# 계좌번호와 금액을 입력으로 받아서 계좌의 금액을 추가
def deposit(acc_list):
    try:
        cmd = input('계좌번호 금액 입력> ').split()
        ano,amount = cmd[0],int(cmd[1])
    except:
        print('입력이 잘못되었습니다.')
    for acc in acc_list:
        if ano == acc['계좌번호']:
            acc['잔액'] += amount
            return

# 계좌번호와 금액을 입력으로 받아서 계좌의 금액을 인출
def withdraw(acc_list):
    cmd = input('계좌번호 금액> ').split()
    ano, amount = cmd[0], int(cmd[1])
    for acc in acc_list:
        if ano == acc['계좌번호']:
            if acc['잔액'] < amount:
                print('잔액이 부족합니다.')
            else:
                acc['잔액'] -= amount
            return