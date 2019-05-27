# b4_thesis

## 仮想通貨取引所の情報を取得
### getExchange.py
取引所の取引量ランキングを掲載しているサイトから仮想通貨取引所の名前とURLを取得．

### GetIPAdder.py
仮想通貨取引所のURL（ドメイン名）からIPアドレス，サーバの設置国，サーバの管理会社などを取得．

## 取引所のTLS証明書について
Subjectの欄と実際にブラウザでアクセスをして，TLS証明書のEVレベルであるかを手動で判定する．
### get_subject.py
仮想通貨取引所のTLS証明書のSubjectを取得．


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
### matchIP.py
各ブロックチェーンネットワークで収集したIPアドレスと仮想通貨取引所のWebサーバのIPアドレスが一致してるか，第3オクテットまで一致してるかを判定する．
一致していればWebサーバとウォレットを同一管理しており，Webサーバが乗っ取られるとウォレットが盗まれる恐れがある．
第3オクテットまで一致していれば同一ネットワークにあり，取引所のウォレットが推測される恐れがある．
