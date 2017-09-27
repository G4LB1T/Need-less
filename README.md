# Need-less

## About

Basic PoC script to vaccinate Windows endpoints against paranoid malware

This repository contains:
1. Scripts for vaccination, as discussed demonstrated in the talk
2. One of IRONGATE's components source code (warning, malware!) to demonstrate the inner mechanisms of paranoid malware
3. A list of the tested malware

The core of the repository will create artifacts simulating an environment trying to mimic indicators of:
1. Virtual machines and emulators
2. Sandbox
3. Security products
4. Forensic tools
5. The malware iteslf (AKA infection markers)

Feel free to contribute more artifacts.


## HOWTO
Execute vaccination_manager.py on the machine you wish to protect with the following flags:

```
-s create only static artifacts
-d create only dynamic artifacts, the script needs to keep running if you want it to protect the endpoint
-a create both static and dynamic indicators, the script needs to keep running if you want it to protect the endpoint
-w update the artifact list from an online repository, if you wish to use it install python's requests module
```
Note that if you wish to test the dynamic vaccination module you'll need to either re-run on each reboot.


## Samples used in the Demo
 
### NotPetya
Destructive ransomware which turned out to be a wiper, has an infection marker and searches Norton\Symantec and Kaspersky related processes
027cc450ef5f8c5f653329641ec1fed91f694e0d229928963b30f6b0d7d3a745

### WannaCry
A ransomware which used the ETERNALBLIE\DOUBLEPULSAR exploits to infect machines all over the world, has an infection marker
ed01ebfbc9eb5bbea545af4d01bf5f1071661840480439c6e5babe8e080e41aa
 
### Andromeda\Gamarue Bot
periodically checks if any of the running processes are in a hardcoded anlysis related blacklist, if none are found it will create malicious child process - otherwise it will keep running and test later again which processes are running.
31f81b5e6854dfee0739c1f8266668622b13f36a5499d98809fcc04603ee7152

### IRONGATE - SCADA\ICS Targeted
Uveiled by Fireeye's researchers, see attached source if you wish to have a closer look at its VM detection function.
386ed16fece9cc24c4d123cdf91a371829098ba7abd4c8fefb40b4e376e7ac6a

### Locky Ransomware
Searches if specific AV vendor is installed by indicatiors in the Windows' registry
17c3d74e3c0645edb4b5145335b342d2929c92dff856cca1a5e79fa5d935fec2

### Spora Ransomware
Searches for a mutex and terminates if it detects it already exists
5ab9b586eaf1bcaa76443b4f69d67e57a057d57cb30b6d863a7cfab3d0882c2a

### TeslaCrypt Ransomware
Searches if specific AV vendor is installed by indicatiors in the Windows' registry
ca7cb56b9a254748e983929953df32f219905f96486d91390e8d5d641dc9916d


## License
CC-BY-SA
https://creativecommons.org/licenses/by-sa/2.0/

**Use at your own risk!** 
