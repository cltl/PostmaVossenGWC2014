echo "##############"
echo "Java version check"
echo " "
javacheck=$(java -version 2>&1)
echo "Java report the following message, when asked to show the version of java this is installed on your computer"
echo " "
echo $javacheck
echo " "
echo "if the message printed above this statement states that the version of Java is higher than 1.6, you should be alright, because the wordnet tools were compiled on Mac OS X version 10.6.8 with Java 1.6."
echo " "
echo "##############"
echo "Checking installed python modules"
python installed_modules.py
