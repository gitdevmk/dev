import os
import webbrowser
import datetime
import subprocess
import random
import time

def execute_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}")
        print(e)

def update_system():
    print("Updating system...")
    try:
        execute_command("sudo apt update && sudo apt upgrade -y")
        print("System update completed successfully.")
    except Exception as e:
        print(f"Failed to update system: {e}")

def play_music(music_folder):
    try:
        subprocess.run(["vlc", "--one-instance", "--playlist-autostart", music_folder])
    except Exception as e:
        print(f"Error playing music: {e}")

def clear_screen():
    os.system("clear")  # Clear the terminal screen

def start_tool(tool_name):
    tool_commands = {
        "nmap": ["gnome-terminal", "--", "nmap"],
        "burp suite": ["gnome-terminal", "--", "burpsuite"],
        "wireshark": ["gnome-terminal", "--", "wireshark"],
        "metasploit": ["gnome-terminal", "--", "msfconsole"],
        "maltego": ["gnome-terminal", "--", "maltego"],
        "dirb": ["gnome-terminal", "--", "dirb"],
        "sqlmap": ["gnome-terminal", "--", "sqlmap"],
        "ettercap": ["gnome-terminal", "--", "ettercap"],
        "john": ["gnome-terminal", "--", "john"],
        "msfvenom": ["gnome-terminal", "--", "msfvenom"],
        "mimikatz": ["gnome-terminal", "--", "mimikatz"],
        "reaver": ["gnome-terminal", "--", "reaver"],
        "arp spoof": ["gnome-terminal", "--", "arpspoof"],
        "hydra": ["gnome-terminal", "--", "hydra"],
        "msfconsole": ["gnome-terminal", "--", "msfconsole"],
        "xampp": ["sudo", "/opt/lampp/manager-linux-x64.run"],
        "ppsspp": ["ppsspp"],
        "calculator": ["gnome-calculator"],
        "vscode": ["code"],
        "android studio": ["studio.sh"],
        "apt list upgradable": ["apt", "list", "--upgradable"],
        "auto remove": ["sudo", "apt", "auto-remove", "-y"],
        "apt upgrade": ["sudo", "apt", "upgrade", "-y"],
        "speedtest": ["speedtest-cli"],
        "search files": ["search-files-script.sh"],  # Replace with actual script or command
        "clean disk": ["clean-disk-script.sh"],  # Replace with actual script or command
        "system logs": ["system-logs-script.sh"],  # Replace with actual script or command
        "network diagnostics": ["network-diagnostics-script.sh"],  # Replace with actual script or command
        "firewall config": ["firewall-config-script.sh"],  # Replace with actual script or command
        "scheduled tasks": ["scheduled-tasks-script.sh"],  # Replace with actual script or command
        "user permissions": ["user-permissions-script.sh"],  # Replace with actual script or command
        "check updates": ["check-updates-script.sh"],  # Replace with actual script or command
        "backup system": ["backup-system-script.sh"],  # Replace with actual script or command
        "remote shell": ["remote-shell-script.sh"],  # Replace with actual script or command
        "partition disks": ["partition-disks-script.sh"],  # Replace with actual script or command
        "system performance": ["system-performance-script.sh"],  # Replace with actual script or command
        "system recovery": ["system-recovery-script.sh"],  # Replace with actual script or command
        "ssh keys": ["ssh-keys-script.sh"],  # Replace with actual script or command
        "containers": ["containers-script.sh"],  # Replace with actual script or command
        "service control": ["service-control-script.sh"],  # Replace with actual script or command
        "encrypt files": ["encrypt-files-script.sh"],  # Replace with actual script or command
        "resolve dependencies": ["resolve-dependencies-script.sh"],  # Replace with actual script or command
        "system benchmark": ["system-benchmark-script.sh"],  # Replace with actual script or command
        "usb devices": ["usb-devices-script.sh"],  # Replace with actual script or command
    }
    if tool_name.lower() in tool_commands:
        print(f"Starting {tool_name}...")
        try:
            subprocess.Popen(tool_commands[tool_name.lower()])
