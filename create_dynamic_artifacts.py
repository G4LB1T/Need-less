import subprocess
import tempfile
import shutil
import time
import ctypes
from ctypes import wintypes
import artifacts

__author__ = 'G4l_B1t'

"""
Creating artifacts searched by malware using this script may repel potential attackers.
Feel free to use it **at your own risk**.

This script creates dynamic artifacts, thus less practical.
Check out its static sibling for better results and usability.
"""

temp_folder = tempfile.gettempdir()
actual_proc = "C:\\Windows\\System32\\ftp.exe"


def create_exe(fake_name):
    """
    This function recieves a process name and will copy and rename instance of Windows' ftp.exe under this name
    :param fake_name: name for the running process
    """
    fake_proc = temp_folder + "\\" + fake_name
    shutil.copyfile(actual_proc, fake_proc)


def run_exe(command):
    """
    Wrapper for executing the copied files.
    """
    try:
        subprocess.Popen(command)
    except Exception as e:
        print "Got exception {0} while creating {1}".format(e, command)
    return


def create_mutex():
    """
    Creates a mutexes
    1) just like the notorious Spora ransomware
    This prevents the execution of known Spora variants

    Based on Minerva's blog post:
    https://www.minerva-labs.com/post/vaccinating-against-spora-ransomware-a-proof-of-concept-tool-by-minerva

    2) WannaCry mutex, see reference at:
    https://www.minerva-labs.com/post/immune-yourself-from-wannacry-ransomware-with-minervas-free-vaccinator
    Note it won't work in some real life scenarios
    """
    try:
        # Spora mutex
        vol_serial = int(subprocess.check_output(['cmd', '/c', 'vol'])[-11:-2].replace("-", ""), 16)
        spora_mutex = 'm' + str(vol_serial)
        _CreateMutex = ctypes.windll.kernel32.CreateMutexA
        _CreateMutex.argtypes = [wintypes.LPCVOID, wintypes.BOOL, wintypes.LPCSTR]
        _CreateMutex.restype = wintypes.HANDLE

        _CreateMutex(None, False, spora_mutex)

        for m in artifacts.mutex:
            _CreateMutex(None, False, m)

    except Exception as e:
        print "Got exception {0} while creating {1}".format(e, "mutex: " + m)


def do_dynamic_vaccination():
    create_mutex()
    print "Mutexes created"

    for proc_name in artifacts.processes_to_mimic:
        create_exe(proc_name)
        run_exe(temp_folder + "\\" + proc_name)

    print "Processes create successfully\n\n" \
          ">>> Close this window to terminate the sub-processes and release the mutexes . . .\n"

    # This will make the script keep running - holding the mutex and child processes until it is closed
    time.sleep(-1)


if __name__ == '__main__':
    do_dynamic_vaccination()
