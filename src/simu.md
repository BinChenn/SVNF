# 实验



## 说明
**拓扑**
例如，取k=6, 共54台服务器  编号为[45,98]。
6个pod         [45-98]
每个pod3个tor   [45-53] ...
每个tor3台serv  [45-47] [48-50] [51-53] ...

**环境**
Windows10， Anaconda，PowerShell

## 实验1   (exp: 1~2)

```shell
# 初始化expri1所需目录结构
chmod a+x init.sh clear.sh
./clear.sh expri1
./init.sh expri1
# --- k=10 c=500 s=20 x=1---
# 生成流量
python traffic.py -c 500 -k 10 -Tm 10 -al 2.1 -s 20 -o expri1/traffic/traffic-c500s20.txt -x 1

python mvsh.py -k 10 -i expri1/traffic/traffic-c500s20.txt -o expri1/placeResult/result_mvsh-c500s20.txt -n
python resultAnalysis.py -c 500 -k 10 -i expri1/placeResult/result_mvsh-c500s20.txt -o expri1/staticAnalysis/analysis_mvsh-c500s20.txt -a mvsh -x 1
python plr.py -c 500 -k 10 -i expri1/placeResult/result_mvsh-c500s20.txt -s 20 -o expri1/evaluation/plr_mvsh-c500s20.txt -a mvsh -x 1

python svnfp.py -k 10 -i expri1/traffic/traffic-c500s20.txt -o expri1/placeResult/result_svnf-c500s20.txt -n
python resultAnalysis.py -c 500 -k 10 -i expri1/placeResult/result_svnf-c500s20.txt -o expri1/staticAnalysis/analysis_svnf-c500s20.txt  -a svnf -x 1
python plr.py -c 500 -k 10 -i expri1/placeResult/result_svnf-c500s20.txt -s 20 -o expri1/evaluation/plr_svnf-c500s20.txt -a svnf -x 1

python clbp2.py -k 10 -i expri1/traffic/traffic-c500s20.txt -o expri1/placeResult/result_clbp-c500s20.txt -n
python resultAnalysis.py -c 500 -k 10 -i expri1/placeResult/result_clbp-c500s20.txt -o expri1/staticAnalysis/analysis_clbp-c500s20.txt -a clbp -x 1
python plr.py -c 500 -k 10 -i expri1/placeResult/result_clbp-c500s20.txt -s 20 -o expri1/evaluation/plr_clbp-c500s20.txt -a clbp -x 1

python draw.py -c 500 -s 20 -x 1
```

| 算法       | AR    | FLP（跳数） | AVG SU  |
| ---       | ---   | ---        | ---     |
| sVNFP     | 100%  |  5.090     |49.697%  |
| sVNFP-adv | 100%  |  2.370     |49.697%  |
| CLBP      | 100%  |  2.082     |92.032%  |

## 实验2 (exp: 2~3)

```shell
# 初始化expri2所需目录结构
chmod a+x init.sh clear.sh
./clear.sh expri2
./init.sh expri2
# --- k=10 c=500 s=20 x=2---
# 生成流量
python traffic.py -c 500 -k 10 -Tm 10 -al 2.1 -s 20 -o expri2/traffic/traffic-c500s20.txt -x 2

python mvsh.py -k 10 -i expri2/traffic/traffic-c500s20.txt -o expri2/placeResult/result_mvsh-c500s20.txt -n
python resultAnalysis.py -c 500 -k 10 -i expri2/placeResult/result_mvsh-c500s20.txt -o expri2/staticAnalysis/analysis_mvsh-c500s20.txt -a mvsh -x 2
python plr.py -c 500 -k 10 -i expri2/placeResult/result_mvsh-c500s20.txt -s 20 -o expri2/evaluation/plr_mvsh-c500s20.txt -a mvsh -x 2

python svnfp.py -k 10 -i expri2/traffic/traffic-c500s20.txt -o expri2/placeResult/result_svnf-c500s20.txt -n
python resultAnalysis.py -c 500 -k 10 -i expri2/placeResult/result_svnf-c500s20.txt -o expri2/staticAnalysis/analysis_svnf-c500s20.txt  -a svnf -x 2
python plr.py -c 500 -k 10 -i expri2/placeResult/result_svnf-c500s20.txt -s 20 -o expri2/evaluation/plr_svnf-c500s20.txt -a svnf -x 2

python clbp2.py -k 10 -i expri2/traffic/traffic-c500s20.txt -o expri2/placeResult/result_clbp-c500s20.txt -n
python resultAnalysis.py -c 500 -k 10 -i expri2/placeResult/result_clbp-c500s20.txt -o expri2/staticAnalysis/analysis_clbp-c500s20.txt -a clbp -x 2
python plr.py -c 500 -k 10 -i expri2/placeResult/result_clbp-c500s20.txt -s 20 -o expri2/evaluation/plr_clbp-c500s20.txt -a clbp -x 2

python draw.py -c 500 -s 20 -x 2
```
| 算法       | AR    | FLP（跳数） | AVG SU  |
| ---       | ---   | ---        | ---     |
| sVNFP     | 100%  |  5.119     |49.697%  |
| sVNFP-adv | 100%  |  2.371     |49.697%  |
| CLBP      | 100%  |  2.205     |79.136%  |



## 100组实验

```console
# 100组实验
run 100 python plr.py -c 500 -k 10 -i shiyan1/result_mvsh-c100s20.txt -s 30 -o shiyan1/plr_mvsh-c100s20.txt -a mvsh -x 3 >> test1.txt
run 100 python plr.py -c 500 -k 10 -i shiyan1/result_svnf-c100s20.txt -s 30 -o shiyan1/plr_svnf-c100s20.txt -a svnf -x 3 >> test2.txt
run 100 python plr.py -c 500 -k 10 -i shiyan1/result_clbp-c100s20.txt -s 30 -o shiyan1/plr_clbp-c100s20.txt -a clbp -x 3 >> test3.txt
```

结果详见我的论文（ICC已录用）: W.  Zhou,  Y.  Yang,  and  M.  Xu, Hao Chen,  “Accommodating  dynamic  trafficimmediately:  a  VNF  placement  approach,”.
