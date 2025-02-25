import subprocess
import optparse
import re
import sys

def get_data():
    p = optparse.OptionParser()
    p.add_option("-i", "--interface", dest="interface", help="used to store name of the interface")
    p.add_option("-m", "--mac", dest="new_mac", help="used to store value of the new mac")
    (options, arguments) = p.parse_args()  # used to

    interface = options.interface
    new_mac = options.new_mac

    if not interface:
        interface = input("enter interface : ")

    if not check_interface_exists(interface):
        print("Error ",interface," doesnt exist")
        print("-------Exit-------")
        sys.exit(1)

    current = check_mac(interface)
    if current is None:
        print("MAC Not Found. Try a different interface.")
        print("-------Exit-------")
        sys.exit()

    print("Current Mac     :", current)

    if not new_mac:
        new_mac = input("enter new mac   : ")
        #"00:1A:2B:4D:3D:6F"
    if not is_valid_mac(new_mac):
        print("Invalid MAC address format!")
        print("-------Exit-------")
        sys.exit(1)
    changing_mac(interface,new_mac)

def changing_mac(interface,new_mac):
    subprocess.run(["ifconfig", interface, "down"])
    subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.run(["ifconfig", interface, "up"])

    print("-------Done-------")

    checker = input("Do u wanna check Ifconfig Y/N ")
    if checker == "y" or checker == "Y":
        print("New Mac         :",check_mac(interface))
    print("-------Exit-------")

def check_mac(interface):
    result = subprocess.check_output(["ifconfig", interface],text=True)
    mac_address_searched = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",result)

    if mac_address_searched:
        return mac_address_searched.group(0)
    else:
        return None

def is_valid_mac(mac):
    pattern = r"00:\w\w:\w\w:\w\w:\w\w:\w\w"  # Your pattern
    return re.fullmatch(pattern, mac) is not None

def check_interface_exists(interface):
    result = subprocess.run(["ifconfig", interface], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return result == 0

if __name__ == "__main__":
    get_data()
