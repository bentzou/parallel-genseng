cd test
rm *.log
rm Jinger*.dat
cd ..
cd parallel
make
cd ..
mv parallel/GENSENG test/
cd test
/usr/bin/time -o timestats.log ./GENSENG reviseddata4hmm_300bpSlides_chr1.txt 1 0.01 0.01 1 1 1 0 0 1 1
