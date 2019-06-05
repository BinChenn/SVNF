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