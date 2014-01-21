export cwd=$(pwd)
cd Scripts
echo " "
echo "Started run at `date`"
echo " "
echo "STARTING  STEP 1: Creating bash scripts to run wordnet tools"

scripts=$(python Create_bash_scripts_wn_tools.py $cwd 2>&1)

echo "COMPLETED STEP 1: at `date`"
echo " "
echo "STARTING  STEP 2: Run bash scripts in wordnet tools." 
echo "COMMENT 1: Note that this might take some time."
echo "COMMENT 2: It took a minute on the laptop it was created with."
echo "COMMENT 3: after the script has been completed, press enter to open the following file(s):"
echo "FILE 1: overview_tables.txt, which contains the replicated tables as well as the original tables in the paper"
echo "the original paper itself is placed in the same folder as the README and is called Postma_Vossen_GWC_2014.pdf"

cd ../wn_tools/wordnettools.v1.0/scripts
IFS=', ' read -a array <<< "$scripts"
for element in "${array[@]}"
do
	local=$(bash "$element" 2>&1)
done

echo " "
echo "COMPLETED STEP 2: at `date`"

cd $cwd
cd Scripts
python create_overall_results.py $cwd
python Calculate_correlations.py $cwd
python create_table_5_1.py $cwd
cd $cwd
echo "Press ENTER to open overview_tables.txt"
read year
gnome-open ./Tables_paper/comparison/overview_tables.txt
