
import sys
import os

major = sys.version_info.major
if major == 2:
    print "You have installed a version of python 2, which is the correct version of this software"
    print

if major == 3:
    print "You have installed a version of python 3.x"
    print "In order to run this program, a version python 2.x is required"
    print

try:
    import os
    import sys
    import shutil
except:
    print "one of the following modules: os, sys or shutil is not installed"

try:
    import Pycluster.cluster
    version = Pycluster.cluster.version()
    if version == '1.52':
        print "you have installed version %s of Pycluster.cluster, which is the correct version" % version
    else:
        print "you have installed version %s of Pycluster.cluster, which is the version which was used to create this script. However, it should probably work" % version
except:
    print "Pycluster.cluster does not seem to be installed"
print
print
top_level = "/".join(os.getcwd().split("/")[:-1])

print
print 
print "###################################"
print "wordnet tools check"
print 

folder_wn_tools = "%s/wn_tools" % top_level
if os.path.exists(folder_wn_tools):
    print "you have succesfully placed the wordnet tools in the same folder as the README"
    cornetto_lmf = "%s/wn_tools/wordnettools.v1.0/resources/cornetto2.1.lmf.xml" % top_level
    if os.path.exists(cornetto_lmf):
        print "you have been succesful at putting cornetto lmf in the resources folder of the wn_tools"
    else:
        print "Cornetto does not seem to be in the resources folder (./wn_tools/wordnettools.v1.0/resources/) of the wn_tools OR it has not been named 'cornetto2.1.lmf.xml'"
        print "Option 1: please rename the file to 'cornetto2.1.lmf.xml'"   
        print "Option 2: Obtain Cornetto: a free research license can be obtained from the Dutch centre for language technology (http://tst-centrale.org/)"

else:
    print "the wordnet-tools do not seem to be placed in the same folder as the README or the name of this folder has not been set to wn_tools"
    print "please go to http://wordpress.let.vupr.nl/software/wordnettools/ to download the wordnet tools."
    print "please download the zip folder and unzip it in the same folder as the README and call it 'wn_tools'."
    print "p.s. the link to the zip folder is http://let.vupr.nl/releases/wordnettools/wordnettools.v1.0.zip"

print
print
print "#################"
print "Next step"
print
print "If the messages above show that you have not installed the correct software, please read section 2: required software"
print "of the README to read instructions about how to install the needed software"
print
print "if the messages above show that you installed the correct software, you can continue with step 2 of the README (which is to run: cd .. and then bash Main.sh"
print

