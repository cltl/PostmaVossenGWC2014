java -Xmx812m -cp ../lib/WordnetTools-1.0-jar-with-dependencies.jar vu.wntools.wnsimilarity.main.Similarity --lmf-file "../resources/wneng-30.lmf.xml" --input "/home/marten/Dropbox/aaVU/Spinoza/Papers/GWC_2014/Github/Code/WT_input/WT_INPUT__GS_MC_EN.txt" --method all --pairs words --depth 15 --subsumers "../resources/ic-semcor.dat.lower-case-cum" --relations "../resources/relations.txt"