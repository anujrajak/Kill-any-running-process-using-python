from subprocess import check_output
import psutil
def get_pid(name):
    return check_output(["pidof",name])

pid = int(get_pid("Chrome"))
p = psutil.Process(pid)
p.terminate()

print(pid)
