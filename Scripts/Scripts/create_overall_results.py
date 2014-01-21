from Define_paths import Define_paths
import sys
import os
class Overall_results(Define_paths):
    
    def __init__(self,main_folder):
        Define_paths.__init__(self, main_folder)
        self.input_files = self.files(self.wt_input)
        self.gs_files = self.files(self.gold_standards)

    
    
    def find_gold_standard_file(self,bestand):
        basename_bestand = os.path.basename(bestand)
        key_bestand =  basename_bestand[basename_bestand.find("GS_"):-8]
        for gs_file in self.gs_files:
            basename_gs = os.path.basename(gs_file)
            key_gs = basename_gs[basename_gs.find("GS_"):-4]
            if key_bestand == key_gs:
                return gs_file
    
    def get_lines(self,bestand):
        with open(bestand) as infile:
            return infile.readlines()
        
        
    def write_file(self,gs_file,bestand):
        lines_gs = self.get_lines(gs_file)
        lines_bestand = self.get_lines(bestand)
        basename_outfile = os.path.basename(bestand).split("__")[-1][:-8]
        outfile_path = "%s/%s.csv" % (self.overall_results,basename_outfile)
        with open(outfile_path,"w") as outfile:
            for line_number in xrange(len(lines_gs)+1):
                
                if line_number == 0:
                    info = lines_bestand[line_number].split('\t')
                    info.insert(2,"GS_value")
                    outfile.write("\t".join(info))
                else:
                    gs_value = lines_gs[line_number-1].split()[-1]
                    info = lines_bestand[line_number].split('\t')
                    info.insert(2,gs_value)
                    outfile.write("\t".join(info))

    
    def loop(self):
        for bestand in self.input_files:
            if bestand.endswith(".txt.all"):
                gs_file = self.find_gold_standard_file(bestand)
                self.write_file(gs_file, bestand)




if __name__ == "__main__":
    Overall_results(sys.argv[1]).loop()
