# ./GENSENG readcountdata round mc1 mc2 map autor mixture tran init human postprocessing.

# readcountdata: the window count data generted from the bam file. One example is the reviseddata4hmm_300bpSlides_chr1.txt. The input data preparation pipeline has been uploaded as GENSENG_data_generation_pipelines.zip.
# round: the em inference rounds [1-]
# mc1: the mixture component parameter for the normal state [0-1]
# mc2: the mixture component parameter for the CNV state [0-1]
# map: whether corrects the mapability bias (1), or not (0)
# autor: whether uses the auto regressive component (1), or not (0)
# mixture: whether uses the mixture component (1), or not (0)
# tran: whether re-estimate the transition probability of HMM (1), or not (0)
# init: whether re-estimate the intial probablity of HMM (1), or not (0)
# human: the input data is human (1), or mouse (0). If the value for this field is larger than 2, it will be the given largest state (by default, the largest state will be 6).
# postprocessing: whether the postprocessing step will be executed (1) , or not (0).

ROUND=10
TRANS=1
INIT=1

cd test
echo 'REMOVING OLD FILES...'
rm *.log
rm Jinger*.dat
rm GENSENG
cd ..
echo

echo 'CREATING NEW FILES...'
cd parallel
make
mv GENSENG ../test/
cd ..
echo

# ./GENSENG readcountdata round mc1 mc2 map autor mixture tran init human postprocessing.
# ./GENSENG reviseddata4hmm_300bpSlides_chr1.txt 10 0.01 0.01 1 1 1 0 0 1 1


echo 'STARTING'
cd test
/usr/bin/time -o timestats.log ./GENSENG reviseddata4hmm_300bpSlides_chr1.txt $ROUND 0.01 0.01 1 1 1 $TRANS $INIT 1 1
cd ..
echo