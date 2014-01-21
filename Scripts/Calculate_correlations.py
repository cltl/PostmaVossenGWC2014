from Define_paths import Define_paths
import os
import sys


class Calculate_correlations(Define_paths):
    
    def __init__(self,main_folder):
        Define_paths.__init__(self, main_folder)
        
    def get_lines(self,bestand):
        with open(bestand) as infile:
            return infile.readlines()

    def translate_keys(self,keys):
        export = []
        for key in keys:
            if key == 'Similar by path':
                key = "path"
            if key == 'Similar by L&C':
                key = "lch"
            if key == 'Similar by W&P':
                key = 'wup'
            if key == 'Similar by R':
                key = 'res'
            if key == 'Similar by L':
                key = 'lin'
            if key == 'Similar by J&C':
                key = 'jcn'
            export.append(key)
        return export

    def translate_path(self,path):
        basename = os.path.basename(path)
        if basename == "MC_NO_DU.csv":
            basename = "McNo"
        if basename == "MC_REL_DU.csv":
            basename = "McRel"
        if basename == "MC_SIM_DU.csv":
            basename = "McSim"
        if basename == "RG_NO_DU.csv":
            basename = "RgNo"
        if basename == "RG_REL_DU.csv":
            basename = "RgRel"
        if basename == "RG_SIM_DU.csv":
            basename = "RgSim"
        
        if basename == "GS_RG_EN.csv":
            basename = "RgWT"
        if basename == "GS_MC_EN.csv":
            basename = "McWT"
                                                                        
        return basename
    
    def create_dict(self,path,d={}):
        lines = self.get_lines(path)
        path = self.translate_path(path)
        d[path]={}
        old_keys = lines[0].split("\t")
        new_keys = self.translate_keys(old_keys)
        for line in lines[1:]:
            line = line.split("\t")
            for counter,key in enumerate(old_keys):
                new_key = new_keys[counter]
                if True in ["Similar" in key,key == 'GS_value']:
                    try:
                        value = float(line[counter])
                    except:
                        value = line[counter]
                    
                    if new_key in d[path]:
                        d[path][new_key].append(value)
                    else:
                        d[path][new_key] = [value]
        return d
    
      
    def create_table_5_2(self,d):
        outfile_path = "%s/b_Table_5_2_from_section_5_2_from_original_paper.txt" % self.tables_txt
        with open(outfile_path,"w") as outfile:
            headers = ['SM','McNo','McRel','McSim', 'RgNo', 'RgRel', 'RgSim']
            outfile.write(" ".join(headers)+'\n')
            local = []
            for sm in ['path','lch','wup','res','jcn','lin']:
                local.append(sm)
                for exp in ['McNo','McRel','McSim', 'RgNo', 'RgRel', 'RgSim']:
                    correlation = self.spearman(d[exp]["GS_value"],d[exp][sm])
                    correlation = self.rounding(correlation,3)
                    local.append(str(correlation))
                    if len(local) == 7:
                        outfile.write(" ".join(local)+'\n')
                        local = []
    
    def create_table_5_3(self,d):
        outfile_path = "%s/c_Table_5_3_from_section_5_3_from_original_paper.txt" % self.tables_txt
        McPed = [0.68,0.71,0.74,0.74,0.72,0.73]
        RgPed = [0.69,0.70,0.69,0.69,0.51,0.58]
        with open(outfile_path,"w") as outfile:
            headers = ['SM','McPed','McWT','diff', 'RgPed', 'RgWT', 'diff']
            outfile.write(" ".join(headers)+'\n')
            local=[]
            for counter,sm in enumerate(['path','lch','wup','res','jcn','lin']):
                local.append(sm)
                for second_counter,exp in enumerate(['McWT','RgWT']):
                    if second_counter == 0:
                        ped_value = McPed[counter]
                    if second_counter == 1:
                        ped_value = RgPed[counter]
                        
                    correlation = self.spearman(d[exp]["GS_value"],d[exp][sm])
                    diff = round((ped_value-correlation),2)
                    
                    if ped_value == "0.7":
                        ped_value = "0.70"
                    local.append(str(ped_value))
                    correlation = self.rounding(correlation,2)

                    local.append(str(correlation))
                    local.append(str(diff))
                    if len(local) == 7:
                        outfile.write(" ".join(local)+'\n')
                        local = []


        return None
    
    def loop(self):
        bestanden = self.files(self.overall_results)
        for bestand in bestanden:
            if os.path.isfile(bestand): d = self.create_dict(bestand)
        self.create_table_5_2(d)
        self.create_table_5_3(d)
        

if __name__ == "__main__":
    Calculate_correlations(sys.argv[1]).loop()