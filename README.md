# b4_thesis

## 

## Qualys SSL Server Testを利用してサーバの脆弱性診断を自動で実行
chrome driverやseleniumを用いる．
### sslpoweron.py
Qualys SSL Server Testは診断結果が出るまで5分ほど時間がかかるため，対象のWebサイトのURLを先に自動入力し診断させておく．
### ssltest.py
sslpoweronと同じパラメータの範囲をこちらで入力し，あとの診断結果は自動でCSVとスクリーンショット，htmlで保存．

## 各ブロックチェーンネットワークのIPアドレス収集
### BitTimeStamp.py
Bitnodes（最大60日前まで遡れる）でBitcoinブロックチェーンのタイムスタンプを取得しCSVに出力．
### BTCIP.py  
BitTimeStamp.pyで取得したタイムスタンプを，再度Bitnodesを利用して，BitcoinネットワークのIPアドレスを収集しCSVで出力．  
### EtherIP.py  
ethernodesのノード情報のJSONを取得し，EthereumネットワークのIPアドレスを収集しCSVで出力．    
### RippleIP.py  
Ripple公式が提供するAPIを用いて，RippleネットワークのIPアドレスを収集しCSVで出力．    
