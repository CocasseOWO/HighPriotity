import winreg as wr

print(" _    _ _       _     _____      _            _ _")
print("| |  | (_)     | |   |  __ \    (_)          (_) |")
print("| |__| |_  __ _| |__ | |__) | __ _  ___  _ __ _| |_ _   _")
print("|  __  | |/ _` | '_ \|  ___/ '__| |/ _ \| '__| | __| | | |")
print("| |  | | | (_| | | | | |   | |  | | (_) | |  | | |_| |_| |")
print("|_|  |_|_|\__, |_| |_|_|   |_|  |_|\___/|_|  |_|\__|\__, |")
print("           __/ |                                     __/ |")
print("          |___/                                     |___/")
print("")

path = wr.HKEY_LOCAL_MACHINE

softname = input("Name of the program to change to high priority : ")

place1 = wr.OpenKeyEx(path, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\\")
newkey = wr.CreateKey(place1, f"{softname}")

place2 = wr.OpenKeyEx(path, fr"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\{softname}\\")
newkey2 = wr.CreateKey(place2, "PerfOptions")

wr.SetValueEx(newkey2, "CpuPriorityClass", 0, wr.REG_DWORD, 0x00000003)

print("")
print(f"[HighPriotiry] - The {softname} program was successfully changed to High Priority,")
print("[HighPriotiry] - Important : if the program is currently opened, please restart it for the changes to take effect.")
print("")
input("Press enter to exit...")
