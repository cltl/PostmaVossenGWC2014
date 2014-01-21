Project: Replication Postma and Vossen (2014)
Version: 0.1
Date: January 2014
Copyright: VU University Amsterdam, Marten Postma and Piek Vossen
Email: m.c.postma@vu.nl

LICENSE:
This work is licensed under a GNU GPL version 3.0: <http://fsf.org/>. See the file LICENSESOFTWARE.TXT and COPYING-GPL.TXT that should be in the
top-directory of this distribution.

#################################################
#        Section 1: Main steps                  #
#################################################

(1) Check if all software is installed check if you have the necessary resources on your computer
	HOW: see section 2: Required software and resources

(2) Run experiment:
	HOW: run: bash Main.sh
	NOTE: this bash script is placed in the same directory as this README.
	
(3) Compare results with tables in paper "Postma_Vossen_GWC_2014.pdf", which is placed in the same folder as this README:
	HOW: go to ./Tables_paper/comparison/overview_tables.txt to inspect the results of the experiment.

######################################################
#        Section 2: Required software and resources  #
######################################################

(1) Run bash script to check if software is installed (you can re-run this script to check if all dependencies have been installed):
	HOW: go to : ./Installation_verification/
		 type: bash check_installation_software.sh
		 NOTE: the . refers to the directory in which this README is placed.

(2) if the bash script from step (1) reported that software is missing, try to add/install:
	(a) Python version 2.7.x
		-This code was created using Python 2.7.4
		Python modules:
			-Pycluster 1.52 (one of the dependencies for this module is numpy, version 1.7.1 was used for this experiment)
				-One way to install:
					-In terminal: go to ./Installation_verification/Pycluster-1.52/
					-typ: sudo python setup.py install
			 	-Other way:
			 		-a link to download this is http://bonsai.hgc.jp/~mdehoon/software/cluster/software.htm
				for more information about installing python modules go to:
					-http://stackoverflow.com/questions/11893311/installing-3rd-party-python-modules-on-an-ubuntu-linux-machine
	(b) Unix-based command line interface
		-This was created using Ubuntu 13.10
	(c) Wordnet-tools. These can be downloaded from http://wordpress.let.vupr.nl/software/wordnettools//
        please download the zip folder and unzip it in the same folder as the README and call it 'wn_tools'.
	(d) Cornetto: a free research license can be obtained from the Dutch centre for language technology (http://tst-centrale.org/)
		After obtaining the file, please rename the file to 'cornetto2.1.lmf.xml' and place it in ./wn_tools/wordnettools.v1.0/resources/
		
#################################################
#        Section 3: Documentation               #
#################################################

In this section, we use the term "the paper" for the paper called Postma_Vossen_GWC_2014.pdf 
which is placed in the same folder as this README.

,/Configuation
	This folder contains two files: (1) CONFIF__DU.txt ,and (2) CONFIG__EN.txt.
	File (1) contains the configuartion used to run the wn_tools for the Dutch experimenets,
	whereas file (2) shows the configuration for the English experiments. For more information, we refer to sections 4 and 5 in the paper, respectively.
all
./Gold_standards
	This folder contains the gold standards used in the experiments. For more information, we refer to section 3 of the paper.

./Installation_verification
	This folder contains scripts that check if you have installed all the software and have obtained the resources.

./Results
	This folder contains the pair-wise scores from the experiments.
	In each line of a file, a word pair is shown with the scores from both the gold standard and the scores from the similarity measures used in this experiment.

./Script
	This folder contains scripts to run this experiment. 
	It was not designed as flexible software. Adapting the code might be challenging.

./Tables_paper
	This folder contains thee subfolders:
		./txt
			This folder contains the tables created in the replication attempt.
		./original_tables_paper
			This folder contains the original tables as shown in the paper.
		./comparison
			The file in the folder shows a comparison between the content of the two previous subfolders.

./Translation
	The file "translation_en_to_du.txt" shows the translation from English to Dutch as explained in section 3 of the paper.

./wn_tools
	This folder contains the wn_tools

./WT_input
	During the replication attempt. the input which will be used by the wn_tools will be put into this folder
	In addition, the wn_tools will save the pair-wise output into this folder. 
	Output can be recognised, because new files are added in this folder with .path and .path.log added to the input file name.
	

./WT_scripts
	During the replication attempt, the bash scripts used to run the wn_tools will be put into this folder.
	





	
  