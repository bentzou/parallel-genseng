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

echo 'STARTING'
cd test
/usr/bin/time -o timestats.log ./GENSENG reviseddata4hmm_300bpSlides_chr1.txt 1 0.01 0.01 1 1 1 0 0 1 1
cd ..
echo