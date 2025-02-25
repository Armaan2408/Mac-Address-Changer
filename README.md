# MAC Address Changer

## Description

This Python script allows you to change the MAC address of a network interface on Linux-based systems. It provides both an interactive and command-line-based approach for modifying the MAC address securely.

## Prerequisites

- Linux OS
- Python 3

## Installation

1. Ensure Python 3 is installed:
   ```bash
   python3 --version
   ```

## Usage

Run the script with the following command:

```bash
python3 mac_changer.py -i <interface> -m <new_mac>
```

### Example:

```bash
python3 mac_changer.py -i eth0 -m 00:1A:2B:3C:4D:5E
```

## Options

| Option              | Description                                                   |
| ------------------- | ------------------------------------------------------------- |
| `-i`, `--interface` | Specifies the network interface to modify (e.g., eth0, wlan0) |
| `-m`, `--mac`       | Specifies the new MAC address to assign                       |

If you do not provide arguments, the script will prompt you for input:

```bash
python3 mac_changer.py
```

## Features

- Checks if the network interface exists before proceeding.
- Validates the MAC address format before applying changes.
- Uses `ifconfig` to bring the interface down, change the MAC address, and bring it back up.
- Provides an option to verify the new MAC address after modification.

## Notes

- Ensure you have the necessary permissions (root access) before modifying network settings.
- Compatibility: This script is designed for Linux-based systems and requires the `ifconfig` command.

## Libraries Used

- `subprocess`
- `optparse`
- `re`
- `sys`

