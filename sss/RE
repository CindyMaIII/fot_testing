**Demo Dataset**
===================
該文件是WASA測試用的Dataset，其中包含兩個data及一個Python檔案。

----------

**main_Manual_ChainSpot.py**
----------------
main_Manual_ChainSpot.py為打Web access log假資料至ES，適用Webhound、ChainSpot、CWAF。

**"__main__"**
>  * 是主程式，由此控制所有方法，所以變數都會在裡面 
>  * 資料拆成(1-10)、(10-21)、（21-26)及(26-31)四段打到ES裡
>  * 1日到20日：正常資料，21日到25日：日期的順序改變，25日到30日：增大uri

**Param**

| Param | Describe |
| ------ | ------ |
| [path_source] | 資料來源的路徑 |
| [path_source_anomaly] | 整合資料的路徑 |
| [readfile_forURI] | 讀取整合資料 |
| [URI_List] | 提出URI存成URI List |
| [replacestring] | 置換LogTime與@LogTime的時間|
| [readfile] | 重新讀入資料避免資料置換時間後被keep的問題 |

 
----------

geoip_ip_to_location.py
----------------
此程式將ip轉換成json格式的geoip，並將geoip與原ip combine

要執行此程式需要先有
*  install geoip
*  下載Databases：https://dev.maxmind.com/geoip/legacy/geolite/
*  需準備一個存有ip的檔案

**geoip_city()**
> * path指向使用的geoip database檔案位置
> * csv指向檔案的位置

----------

transform_insert_ip.py
----------------
此程式會將ip.txt中的ip與geoip以Random的方式插入mic.mv.6.19.txt的原始檔案中，並會將原本在mic.mv.6.19.txt檔案中的SrcIP置換成新的

> * filetxt指向mic.mv.6.19.txt檔案位置
> * filecvs指向藉由geoip_ip_to_location.py轉換出來的txt檔案位置

----------

mic.mv.6.19.txt
----------------
mic.mv.6.19.txt為原始RAW DATA

----------

inter.result.txt
----------------
inter.result.txt為URI的RAW DATA

----------

ip_only.csv
----------------
ip_only.csv為只有ip的RAW DATA

----------

ip.txt
----------------
ip.txt是以geoip_ip_to_location.py轉換存取的ip及geoip的檔案

----------