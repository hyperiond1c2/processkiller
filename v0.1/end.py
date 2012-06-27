#!/usr/bin/python
# Version 0.1 - Codename "Zeus"
# -----------------------------
# Changelog
# ====================================================================================================================
# v0.1:
#    - initial release.
# ====================================================================================================================
# If you find any issues send them to me at roeglobal@insicuri.net and use my public PGP key (else no reply):
#     http://sprunge.us/UNOC
# ====================================================================================================================

try:
    from os import system as cmd
    from sys import argv
    from sys import platform
    from time import sleep
except ImportError as ie:
    print "[-] Import error\n\t[*] Debugging info:\n"
    raise ie

if platform.startswith("linux") != True:
    print "[-] Sorry buddy, you need Linux for this one ;-)\n"
    exit(0)
else:
    pass

def help():
    print "[-] Usage:\n\t%s [service(s) list]\n\n\t[service(s) -space separated- list] = skype(shortcut: s) pidgin(shorcut: p) servicename" % str(argv[0])
    exit(0)

if len(argv) < 2:
    help()
    exit(0)
else:
    print "[i] Number of options detected: %s" % str(len(argv)-1)


shortcut = {'s': 'skype', 'p': 'pidgin'}

def process():
    t1 = 1
    t2 = len(argv)-1

    try:
        while t1 <= t2:
            if str(argv[t1]) in shortcut:
                print "[s] %s shortcut detected. Killing \"%s\" with -9" % (str(shortcut[argv[t1]][:1].upper())+str(shortcut[argv[t1]][1:].lower()), str(shortcut[argv[t1]]))
                cmd("killall -9 "+str(shortcut[argv[t1]]))
                print "="*60+"\n"
                t1 += 1
            else:
                print "[i] Killing with -9: %s" % str(argv[t1])
                cmd("killall -9 "+str(argv[t1]))
                print "="*60+"\n"
                t1 += 1
    except Exception as auch:
        print "[-] Something went wrong.\n\t[*] Debugging info:\n"
        raise auch

def main():
    print "[+] Engines online.\n"+"="*60
    process()
    print "[+] We are done.\n" 
    cmd("echo -n '[+] Shutting down ... ' && sleep 1 && echo ' [ OK ]'")
    exit(0)

if __name__ == "__main__":
    main()
