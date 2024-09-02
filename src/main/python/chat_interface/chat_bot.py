import xml.etree.ElementTree as ET
from src.main.python.macros.macro_runner import MacroRunner, predefined_macros
from src.main.python.hardware_detection.hardwar_scanner import get_system_info, get_cpu_info, get_memory_info, get_disk_info, get_network_info
from src.main.python.auth.auth_manager import AuthManager

# Initialize the macro runner and authentication manager
macro_runner = MacroRunner()
auth_manager = AuthManager()

for name, actions in predefined_macros().items():
    macro_runner.add_macro(name, actions)

# Load responses from XML
def load_responses(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    responses = {}
    for response in root.findall('response'):
        key = response.find('key').text.lower()
        value = response.find('value').text
        responses[key] = value
    return responses

responses = load_responses('C:/Users/Anand/PycharmProjects/Project - DeskBot/src/main/python/chat_interface/responses.xml')


def format_info(info_dict, title):
    formatted_info = f"{title}:\n"
    for key, value in info_dict.items():
        formatted_info += f"  {key}: {value}\n"
    return formatted_info

def get_response(user_input):
    user_input = user_input.lower()

    if user_input.startswith("register"):
        _, username, password = user_input.split()
        return auth_manager.register(username, password)
    elif user_input.startswith("login"):
        _, username, password = user_input.split()
        return auth_manager.login(username, password)
    elif user_input.startswith("logout"):
        _, username = user_input.split()
        return auth_manager.logout(username)
    elif user_input in responses:
        return responses[user_input]
    elif "run macro" in user_input:
        macro_name = user_input.replace("run macro", "").strip()
        if not macro_name:
            return "Please provide a macro name to run."
        return macro_runner.run_macro(macro_name)
    elif "scan hardware" in user_input:
        system_info = format_info(get_system_info(), "System Info")
        cpu_info = format_info(get_cpu_info(), "CPU Info")
        memory_info = format_info(get_memory_info(), "Memory Info")
        disk_info = "\nDisk Info:\n"
        for disk in get_disk_info():
            disk_info += format_info(disk, "  Disk") + "\n"
        network_info = format_info(get_network_info(), "Network Info")
        return f"{system_info}\n{cpu_info}\n{memory_info}\n{disk_info}\n{network_info}"
    else:
        return "I'm sorry, I don't understand that command. Can you please rephrase?"
