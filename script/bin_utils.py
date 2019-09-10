import subprocess
import os

def exec(cmd):
    cmd_list = cmd.split()
    proc = subprocess.Popen(cmd_list, stdout=subprocess.PIPE)
    proc.wait()
    output = proc.stdout.read()
    return output
    
def exec_os(cmd):
    output = os.popen('powershell '+cmd).read()
    return output

def parse_exif_output(ret):
    exif = {}
    for line in ret.splitlines():
        line = line.decode()
        if ':' in line:
            (tag, value) = line.split(": ")
            exif[tag.strip()] = value.strip()
    return exif
    
if __name__ == "__main__":
    #test functions
    cmd = "../bin/exiftool -FLIR:ALL ../csq/FLIR1787.csq"
    output = exec(cmd)
    output = parse_exif_output(output)
    for key,value in output.items():
        print(key,":",value)
    pass