# -*- coding: utf-8 -*-
import time
import commands
import sys
sys.setrecursionlimit(10000)

commands.getoutput('cleos wallet open -n mainnet')
commands.getoutput('cleos wallet lock_all')
commands.getoutput('cleos wallet unlock -n mainnet --password PW5J7Vh3CNGMaAjXMj4cDuzb9ai945QwceekiYTaTvr6XB3EpV9b3')

def buy(price, amount):
    qty = amount/price
    print('buy:',price,qty,amount)
    cmd = '''cleos -u http://api.eosnewyork.io push action eosio.token transfer '["alitechgroup","btexexchange","%.4f EOS","order:1,%s000,154114185766125772,%d,6"]' -p alitechgroup''' % (
        amount, int(time.time() * 100000), price*1000000)
    output = commands.getoutput(cmd)
    print(output)
    time.sleep(1)
    sell(price,qty)

def sell(price,qty):
    amount = price*qty
    print('sell:',price,qty,amount)
    cmd = '''cleos -u http://api.eosnewyork.io push action eosbtextoken transfer '["alitechgroup","btexexchange","%.4f BT","order:2,%s000,0,%d,6"]' -p alitechgroup''' % (
        qty, int(time.time() * 100000), price * 1000000)
    output = commands.getoutput(cmd)
    print(output)
    time.sleep(1)
    buy(price,amount)

buy(0.0055,1000)