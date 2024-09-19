import os
import subprocess
import getpass
import shutil
import platform

# Tools and their respective installation commands
tools = {
    "amass": {
        "check_cmd": "amass --help",
        "install_cmd": "sudo apt install amass -y"
    },
    "sublist3r": {
        "check_cmd": "sublist3r --help",
        "install_cmd": "sudo apt install pipx && pipx install git+https://github.com/aboul3la/Sublist3r.git && export PATH=$HOME/.local/bin:$PATH && source ~/.bashrc"
    },
    "theHarvester": {
        "check_cmd": "theHarvester --help",
        "install_cmd": "sudo apt install theharvester -y"
    },
    "assetfinder": {
        "check_cmd": "assetfinder --help",
        "install_cmd": "go install github.com/tomnomnom/assetfinder@latest && sudo mv ~/go/bin/assetfinder /usr/bin"
    },
    "findomain": {
        "check_cmd": "findomain --help",
        "install_cmd": "curl -LO https://github.com/findomain/findomain/releases/latest/download/findomain-linux.zip && unzip findomain-linux.zip && chmod +x findomain && sudo mv findomain /usr/bin/findomain && rm findomain-linux.zip"
    }, 
    "dnsrecon": {
        "check_cmd": "dnsrecon --help",
        "install_cmd": "sudo apt install dnsrecon -y"
    },
    "dnsenum": {
        "check_cmd": "which dnsenum",  # Use 'which' to check if dnsenum is installed
        "install_cmd": "sudo apt install dnsenum -y"  # Add '-y' for non-interactive install
    },
    "subfinder": {
        "check_cmd": "subfinder --help",
        "install_cmd": "GO111MODULE=on go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest && sudo mv ~/go/bin/subfinder /usr/bin"
    },
    "curl": {
        "check_cmd": "curl --help",
        "install_cmd": "sudo apt install curl -y"
    },
    "massdns": {
        "check_cmd": "massdns --help",
        "install_cmd": "sudo apt install massdns -y"
    }
}

# Check if a tool is installed
def is_tool_installed(tool_command):
    try:
        subprocess.run(tool_command.split(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        return True
    except subprocess.CalledProcessError:
        return False
    except FileNotFoundError:
        return False

# Install a tool
def install_tool(tool_name, install_command):
    print(f"[𐄂] {tool_name} not installed. Installing...")
    try:
        subprocess.run(install_command, shell=True, check=True)
        print(f"Downloading and installing {tool_name} is complete.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {tool_name}: {e}")

# Get the system architecture for findomain
def get_architecture():
    arch = platform.machine()
    if arch == 'x86_64':
        return 'findomain-linux'
    elif arch == 'aarch64':
        return 'findomain-aarch64'
    else:
        raise Exception("Unsupported architecture")

# Move binary to /usr/bin and make executable
def move_to_usr_bin(tool_name, binary_path):
    if not shutil.which(tool_name):  # If the tool is still not in PATH
        try:
            root_password = getpass.getpass(f"Enter root password to move {tool_name} to /usr/bin: ")
            move_cmd = f"echo {root_password} | sudo -S mv {binary_path} /usr/bin/{tool_name} && sudo chmod +x /usr/bin/{tool_name}"
            subprocess.run(move_cmd, shell=True, check=True)
            print(f"{tool_name} has been moved to /usr/bin and made executable.")
        except subprocess.CalledProcessError:
            print(f"Failed to move {tool_name} to /usr/bin.")
    else:
        print(f"{tool_name} is already in /usr/bin or PATH.")

# Main function to check and install tools
def check_tools():
    for tool_name, tool_info in tools.items():
        check_cmd = tool_info['check_cmd']
        install_cmd = tool_info['install_cmd']

        if is_tool_installed(check_cmd):
            print(f"[✔️] {tool_name} installed")
        else:
            print(f"[✘] {tool_name} not installed")
            
            # Special handling for findomain to ensure correct architecture
            if tool_name == "findomain":
                arch = get_architecture()
                install_cmd = f"curl -LO https://github.com/findomain/findomain/releases/latest/download/{arch}.zip && unzip {arch}.zip && chmod +x findomain && sudo mv findomain /usr/bin/findomain && rm {arch}.zip"

            # Install the tool
            install_tool(tool_name, install_cmd)

            # Move certain tools to /usr/bin if required
            if tool_name in ["findomain", "massdns"]:
                binary_name = "./findomain" if tool_name == "findomain" else "./massdns"
                move_to_usr_bin(tool_name, binary_name)

# Run the program
if __name__ == "__main__":
    check_tools()

