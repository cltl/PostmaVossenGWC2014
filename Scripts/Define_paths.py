import os
from Pycluster.cluster import *

class Define_paths():
    
    def __init__(self,main_folder):
        self.configuration_folder = "%s/Configuration" % main_folder
        self.gold_standards = "%s/Gold_standards" % main_folder
        self.scripts = "%s/Scripts" % main_folder
        self.wt_input = "%s/WT_input" % main_folder
        self.wt_scripts = "%s/WT_scripts/" % main_folder
        self.wn_tools = "%s/wn_tools" % main_folder
        self.wn_tools_input = "%s/wordnettools.v1.0/input" % self.wn_tools
        self.wn_tools_scripts = "%s/wordnettools.v1.0/scripts" % self.wn_tools
        self.overall_results = "%s/Results" % main_folder
        self.tables = "%s/Tables_paper" % main_folder
        self.tables_txt = "%s/Tables_paper/txt" % main_folder
        self.translation = "%s/Translation" % main_folder
    
    def files(self,folder):
        bestanden = [("%s/%s") % (folder,basename) for basename in os.listdir(folder)]
        return bestanden
    
    def filename_extension(self,path):
        basename = os.path.basename(path)
        fileName, fileExtension = os.path.splitext(basename)
        return fileName,fileExtension
    
    def spearman(self,gold,smes):
        spearman_value =1-distancematrix((gold,smes), dist="s")[1][0]
        return spearman_value
    
    def rounding(self,getal,afronding):
        afgerond = round(getal,afronding)
        lengte = len(str(afgerond))
        if lengte == afronding+2:
            return afgerond
        else:
            return "%s0" % afgerond