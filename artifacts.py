dir_list = [
    "C:\\program files\\VMware",
    "C:\\program files\\oracle\\virtualbox guest additions",
    "C:\\Program Files\\Malware Bytes"
]

file_list = [
    "C:\\Program Files\\Malware Bytes\\mbam.exe",
    "C:\\Program Files\\Malware Bytes\\mbae.exe",
    "C:\\WINDOWS\\system32\\drivers\\vmmouse.sys",
    "C:\\WINDOWS\\system32\\drivers\\vmhgfs.sys",
    "C:\\WINDOWS\\system32\\drivers\\VBoxMouse.sys",
    "C:\\WINDOWS\\system32\\drivers\\VBoxGuest.sys",
    "C:\\WINDOWS\\system32\\drivers\\VBoxSF.sys",
    "C:\\WINDOWS\\system32\\drivers\\VBoxVideo.sys",
    "C:\\WINDOWS\\system32\\vboxdisp.dll",
    "C:\\WINDOWS\\system32\\vboxhook.dll",
    "C:\\WINDOWS\\system32\\vboxmrxnp.dll",
    "C:\\WINDOWS\\system32\\vboxogl.dll",
    "C:\\WINDOWS\\system32\\vboxoglarrayspu.dll",
    "C:\\WINDOWS\\system32\\vboxoglcrutil.dll",
    "C:\\WINDOWS\\system32\\vboxoglerrorspu.dll",
    "C:\\WINDOWS\\system32\\vboxoglfeedbackspu.dll",
    "C:\\WINDOWS\\system32\\vboxoglpackspu.dll",
    "C:\\WINDOWS\\system32\\vboxoglpassthroughspu.dll",
    "C:\\WINDOWS\\system32\\vboxservice.exe",
    "C:\\WINDOWS\\system32\\vboxtray.exe",
    "C:\\WINDOWS\\system32\\VBoxControl.exe",
    "C:\\Windows\\perfc.dll",
    "C:\\Windows\\perfc.dat",
    "C:\\email.doc",
    "C:\\email.htm",
    "C:\\123\\email.doc",
    "C:\\123\\email.docx"
]

key_list = [
    [wreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Wireshark"],
    [wreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\ESET"],
    [wreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\AVAST"],
    [wreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\VMware, Inc.\\VMware Tools"],
    [wreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Oracle\\VirtualBox Guest Additions"],
    [wreg.HKEY_LOCAL_MACHINE, "HARDWARE\\ACPI\\DSDT\\VBOX__"],
    [wreg.HKEY_LOCAL_MACHINE, "HARDWARE\\ACPI\\FADT\\VBOX__"],
    [wreg.HKEY_LOCAL_MACHINE, "HARDWARE\\ACPI\\RSDT\\VBOX__"],
    [wreg.HKEY_LOCAL_MACHINE, "SYSTEM\\ControlSet001\\Services\\VBoxGuest"],
    [wreg.HKEY_LOCAL_MACHINE, "SYSTEM\\ControlSet001\\Services\\VBoxMouse"],
    [wreg.HKEY_LOCAL_MACHINE, "SYSTEM\\ControlSet001\\Services\\VBoxService"],
    [wreg.HKEY_LOCAL_MACHINE, "SYSTEM\\ControlSet001\\Services\\VBoxSF"],
    [wreg.HKEY_LOCAL_MACHINE, "SYSTEM\\ControlSet001\\Services\\VBoxVideo"],
    [wreg.HKEY_CURRENT_USER, "SOFTWARE\\Wine"],
]

key_value_list = [
    ["HARDWARE\\DESCRIPTION\\System", "SystemBiosVersion", "QEMU"],
    ["HARDWARE\\DEVICEMAP\\Scsi\\Scsi Port 2\\Scsi Bus 0\\Target Id 0\\Logical Unit Id 0", "Identifier", "VMWARE"],
    ["HARDWARE\\Description\\System", "VideoBiosVersion", "VIRTUALBOX"],
    ["HARDWARE\\DESCRIPTION\\System", "SystemBiosDate", "06/23/99"]
]

processes_to_mimic = [
    "Wireshark.exe",
    "OLLYDBG.exe",
    "windbg.exe",
    "joeboxcontrol",
    "sandbox.exe",
    "vmtoolsd.exe",
    "vboxtray.exe",
    "procmon.exe",
    "avp.exe",
    "NS.exe",
    "mspaint.exe",
    "Taskmgr.exe",
    "dwwatcher.exe",
    "McTray.exe"
]

mutex = [
    "MsWinZonesCacheCounterMutexA",
    "NUCLEAR"
]
