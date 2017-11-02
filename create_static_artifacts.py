import os
import _winreg as wreg
import artifacts

__author__ = 'G4l_B1t'

"""
Creating artifacts searched by malware using this script may repel potential attackers.
Feel free to use it **at your own risk**.
"""


def create_file(f, t):
    """
    create file or folder if it doesn't exist
    """
    print "\t+ creating {0}".format(f)
    try:
        if os.path.exists(f):
            print "\t+ {0} already exists!\n".format(f)
        else:
            if t == "file":
                open(f, 'w')
            elif t == "folder":
                os.makedirs(f)
            print "\t+ {0} was created!\n".format(f)

    except Exception as e:
        error_on_create(f, e)


def create_reg_key(hive, k):
    """
    create registry key
    currently supports only 32bit machines
    """
    print "\t+ creating {0}{1}{2}".format("HKLM", "\\", k)
    try:
        wreg.CreateKey(hive, k)
        print "\t+ {0}{1}{2} was created!\n".format("HKLM", "\\", k)
    except Exception as e:
        error_on_create(k, e)


def create_reg_val(k, v_name, v_data):
    """
    create and set registry value
    currently supports only 32bit machines and HKLM registry keys and values
    """
    print "\t+ creating {0}{1}{2}".format(k, "\\", v_name)
    try:
        kh = wreg.OpenKey(wreg.HKEY_LOCAL_MACHINE, k, 0, wreg.KEY_ALL_ACCESS)
        wreg.SetValueEx(kh, v_name, 0, wreg.REG_SZ, v_data)
        print "\t+ {0}{1}{2} was created!\n".format(k, "\\", v_name)
    except Exception as e:
        error_on_create(k + "\\" + v_name, e)


def error_on_create(i, e):
    print "\t+ error creating {0}\n\t+ Error was: {1}\n".format(i, e)


def do_static_vaccination():
    print "\ninitiating static vaccination..."

    print "\n+ Phase A: creating folders\n"
    for dir_item in artifacts.dir_list:
        create_file(dir_item, "folder")

    print "\n+ Phase B: creating files\n"
    for file_item in artifacts.file_list:
        create_file(file_item, "file")

    print "\n+ Phase C: creating registry keys\n"

    for reg_key in artifacts.key_list:
        create_reg_key(reg_key[0], reg_key[1])

    print "\n+ Phase D: creating registry values\n"

    for reg_value in artifacts.key_value_list:
        create_reg_val(reg_value[0], reg_value[1], reg_value[2])

    print "\n||=====()))))))))))))----->\nyou are now vaccinated!"


if __name__ == '__main__':
    do_static_vaccination()
