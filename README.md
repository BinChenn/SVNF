# Scalable Virtual Network Function Placement

## 说明

转载或引用请联系本项目作者：周伟林 izhouwl@163.com
如果对你有帮助，麻烦加个star吧！

## 依赖库

请安装python3、argparse、numpy等依赖库，推荐用pip3安装。

## 运行说明

1. 生成流量

python3 traffic.py -c 1000 -k 20 -Tm 10 -al 2.1 -s 10 -o output/traffic.txt

-c 指定生成的流量条数，默认1000条
-k 指定拓扑基于 k-阶胖树 拓扑。决定了服务器编号的起始地址和终止地址 [(5k^2)/4 , (5k^2)/4 + (3k^3)/4 -1 ]
-Tm 指定最小流速率
-al 指定tr与Tm的关系因子
-s 指定随机数的起始随机种子
-o 指定输出结果存储到的文件名

2. 运行SVNFP算法，进行VNF放置

python3 svnfp.py -k 20 -i output/traffic.txt -o output/result.txt
或简写如下：
python3 svnfp.py -k 20 -n

-i 指定读入文件名
-o 指定输出文件名

3. 分析结果，统计总流路径长度、平均流路径长度、接受率等

python3 resultAnalysis.py -k 20 -i output/result.txt -o output/analysis.txt
或简写如下：
python3 resultAnalysis.py -k 20

-i 指定读入文件名
-o 指定输出文件名
