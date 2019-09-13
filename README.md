# bt-miner
在同一个价位反复买卖达到挖矿目的。可以在此程序上扩展达到程序化交易的目的

# 依赖
1. 使用eos官方钱包并导入私钥[https://developers.eos.io/eosio-home/docs/setting-up-your-environment](https://developers.eos.io/eosio-home/docs/setting-up-your-environment)
2. python2.7

# 步骤
1. 使用自己的账号替换代码中的alitechgroup
2. 使用自己钱包的名称替换mainnet，使用自己钱包的密码替换PW5J7Vh3CNGMaAjXMj4cDuzb9ai945QwceekiYTaTvr6XB3EpV9b3
2. python mining.py

# 说明
* BTEX的挂单全部都是转账，在MEMO中备注挂单信息
  * 买单备注
  ```javascript
  order:1-表示买单,订单号,交易对ID,价格,价格小数位数
  ```
  * 卖单备注
  ```javascript
  order:2-表示卖单,订单号,交易区0-EOS/1-USDT,价格,价格小数位数
  ```
* 查看合约的交易对ID
  存储在btexexchange合约的tokenpairs表里面,id=154114185766125772是BT/EOS交易对的,自己上的币需要在表中查询。其中base_id:0是eos交易区，base_id:1是usdt交易区
  ```javascript
    {
    "id": "154114185766125772",
    "base_id": 0,
    "contract": "eosbtextoken",
    "sym": 21570,
    "sym_name": "BT",
    "precision": 4,
    "creator": "eosbtexfunds",
    "create_time": "1541141872000",
    "pledge": "5000.0000 BT",
    "price": "0.00511200000000000",
    "open_price": "0.00511100000000000",
    "open_date": "1546822127500"
  }
  ```
