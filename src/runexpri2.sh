python traffic.py -c 200 -k 10 -Tm 10 -al 2.1 -s 20  -r 2 -x 2 

python mvsh.py -k 10 -c 200 -s 20 -n -x 2
python resultAnalysis.py -c 200 -k 10 -c 200 -s 20 -a mvsh -x 2
python plr.py -c 200 -k 10 -s 20 -a mvsh -x 2

python svnfp.py -k 10 -c 200 -s 20 -n -x 2
python resultAnalysis.py -c 200 -k 10 -s 20  -a svnf -x 2
python plr.py -c 200 -k 10  -s 20  -a svnf -x 2

python clbp2.py -k 10 -c 200 -s 20 -n -x 2
python resultAnalysis.py -c 200 -k 10 -s 20 -a clbp -x 2
python plr.py -c 200 -k 10 -s 20 -a clbp -x 2

python draw.py -c 200 -s 20 -x 2