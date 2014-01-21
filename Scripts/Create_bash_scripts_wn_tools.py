import sys
import shutil
from Define_paths import Define_paths

class Create_bash_scripts_input_wn_tools(Define_paths):
    
    def __init__(self,main_folder):
        Define_paths.__init__(self, main_folder)
        self.configuration_files = self.files(self.configuration_folder)
        self.wt_input_files = self.files(self.wt_input)
        self.bash_scripts_to_run = []
        
    def get_configuration_file(self,wt_input_file):
        wt_filename,wt_fileExtension = self.filename_extension(wt_input_file)
        del wt_fileExtension
        for config_file in self.configuration_files:
            config_file_name,config_extension = self.filename_extension(config_file)
            del config_extension
            if config_file_name[-2:] == wt_filename[-2:]:
                return config_file
    
    def path_bash_script(self,wt_input_file,lijst=[]):
        fileName,fileExtension = self.filename_extension(wt_input_file)
        del fileExtension
        self.bash_scripts_to_run.append("%s.sh, " % fileName)
        return "%s/%s.sh" % (self.wn_tools_scripts,fileName)
    
    def create_bash_script(self,config_file,bash_script,wt_input_file):
        with open(bash_script,"w") as outfile:
            commands = []
            with open(config_file) as infile:
                for line in infile:
                    if line[0] != "#":
                        if "--input" in line:
                            line = line.replace("CHANGE",wt_input_file)
                        commands.append(line.strip())
            outfile.write(" ".join(commands))
                        
    
    def loop(self):
        for wt_input_file in self.wt_input_files:
            if wt_input_file.endswith(".txt"):
                config_file = self.get_configuration_file(wt_input_file)
                bash_script = self.path_bash_script(wt_input_file)
                self.create_bash_script(config_file, bash_script,wt_input_file)
                shutil.copy(bash_script, self.wt_scripts)


if __name__ == "__main__":
    self = Create_bash_scripts_input_wn_tools(sys.argv[1])
    self.loop()
    print ",".join(self.bash_scripts_to_run)
    sys.exit()