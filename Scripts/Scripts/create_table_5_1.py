from Define_paths import Define_paths
import os
import sys
class Table_5_1(Define_paths):
    
    def __init__(self,main_folder):
        Define_paths.__init__(self,main_folder)

    def create_mapping(self):
        input_file = "%s/translation_en_to_du.txt" % self.translation
        d_en_nl = {}
        d_nl_en = {}
        with open(input_file) as infile:
            for line in infile:
                en,nl = line.strip().split()
                d_en_nl[en] = nl
                d_nl_en[nl] = en
        return d_en_nl,d_nl_en
    
    def English_files(self):
        export = []
        bestanden = self.files(self.gold_standards)
        for bestand in bestanden:
            if "EN" in bestand:
                type_of_experiment = os.path.basename(bestand).split("_")[1]
                export.append((type_of_experiment,bestand))
        return export
    
    def get_lines(self,path):
        with open(path) as infile:
            return infile.readlines()
    
    def do_check(self,w1,w2,w1_nl,w2_nl,d_en_nl,d_nl_en):
        en = sorted([w1.lower(),w2.lower()])
        nl = sorted([d_nl_en[w1_nl],d_nl_en[w2_nl]])
        if en == nl:
            return True
        else:
            return False
    
    
    def find_value(self,line,du_gs,d_en_nl,d_nl_en):
        w1,w2,waarde = line.strip().split()
        with open(du_gs) as infile:
            for line in infile:
                w1_nl,w2_nl,waarde = line.strip().split()
                if self.do_check(w1, w2, w1_nl, w2_nl,d_en_nl,d_nl_en):
                    return waarde
    
    def translate_path(self,path):
        basename = os.path.basename(path)
        if basename == "GS__MC_NO_DU.txt":
            basename = "McNo"
        if basename == "GS__MC_REL_DU.txt":
            basename = "McRel"
        if basename == "GS__MC_SIM_DU.txt":
            basename = "McSim"
        if basename == "GS__RG_NO_DU.txt":
            basename = "RgNo"
        if basename == "GS__RG_REL_DU.txt":
            basename = "RgRel"
        if basename == "GS__RG_SIM_DU.txt":
            basename = "RgSim"
        return basename
    
    def create_file(self,type_of_experiment,bestand):
        d_en_nl,d_nl_en = self.create_mapping()
        with open("%s/%s.csv" % (self.translation,type_of_experiment),"w") as outfile:
            lines = self.get_lines(bestand)
            for regel,line in enumerate(lines):
                
                if regel == 0:
                    headers = ["w1","w2","value GS EN"]
                    
                export = line.strip().split()
                for du_gs in self.files(self.gold_standards):
                    if "__%s_" % type_of_experiment in du_gs:
                        if regel == 0:
                            headers.append(self.translate_path(du_gs))
                            if len(headers) == 6:
                                outfile.write("\t".join(headers)+"\n")
                        value = self.find_value(line,du_gs,d_en_nl,d_nl_en)
                        export.append(value)
                outfile.write("\t".join(export)+"\n")
        return "%s/%s.csv" % (self.translation,type_of_experiment)
    
    def loop(self):
        bestanden = []
        for type_of_experiment,bestand in reversed(self.English_files()):
            bestanden.append(self.create_file(type_of_experiment, bestand))
        return bestanden
    
    def create_dict(self,bestand):
        d={}
        forbidden = ["cock","rooster","cushion","pillow","noon","midday","crane","chord"]
        with open(bestand) as infile:
            for counter,line in enumerate(infile):
                    
                if any(word in line.lower() for word in forbidden) == False:
                    if counter == 0:
                        keys = line.strip().split("\t")
                    else:
                        split = line.strip().split("\t")
                        for counter,key in enumerate(keys):
                            try:
                                element = float(split[counter])
                            except:
                                element = split[counter]
                            if key in d:
                                d[key].append(element)
                            else:
                                d[key] = [element]
                
        return d
    
    def calculate(self,bestand,outfile):
        d = self.create_dict(bestand)
        if "RgSim" in d.keys():
            keys = ["RgNo","RgSim","RgRel"]
        else:
            keys = ["McNo","McSim","McRel"]
        for key in keys:
            correlation = self.spearman(d["value GS EN"],d[key])
            correlation = self.rounding(correlation,2)
            outfile.write("%s %s\n" % (key,correlation))
    
    def correlaties_5_1(self):
        bestanden = self.loop()
        outfile_path = "%s/a_Table_5_1_from_section_5_1_from_original_paper.txt" % self.tables_txt
        with open(outfile_path,"w") as outfile:
            outfile.write("Dataset Correlation with original dataset\n")
            for bestand in bestanden:
                self.calculate(bestand,outfile)
        
        with open("%s/comparison/overview_tables.txt" % self.tables,"w") as outfile:
            tabellen = sorted(self.files(self.tables_txt))
            originals = sorted(self.files("%s/original_tables_paper" % self.tables))
            for counter,path in enumerate(tabellen):
                basename_table = os.path.basename(path)
                with open(path) as infile:
                    outfile.write("\n\nBelow, you will find the replicated table of: \n" +os.path.basename(path)+"\n\n")
                    outfile.write(infile.read())
                    for path2 in originals:
                        basename_gs = os.path.basename(path2)
                        if basename_table[0] == basename_gs[0]:
                            with open(path2) as second_infile:
                                outfile.write("\n\nThe original from the paper can be found below:\n\n\n")
                                outfile.write(second_infile.read()+"\n")

                        
                    
                
        


if __name__ == "__main__":
    Table_5_1(sys.argv[1]).correlaties_5_1()