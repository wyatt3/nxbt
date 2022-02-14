import time
import nxbt

macro = """
HOME 0.1s
0.7s
X 0.1s
0.3s
A 0.1s
1s
A 0.1s
25s
A 0.1s
3s
A 0.1s
13s
A 0.1s
0.3s
A 0.1s
1.0s
A 0.1s
0.3s
A 0.1s
0.1s
"""
# Start the NXBT service
nx = nxbt.Nxbt()

# Create a Pro Controller and wait for it to connect
controller_index = nx.create_controller(nxbt.PRO_CONTROLLER, reconnect_address=nx.get_switch_addresses())
print("Connecting to the Pokemans...")
nx.wait_for_connection(controller_index)

print("Connected")
time.sleep(2)
nx.press_buttons(controller_index, [nxbt.Buttons.HOME])
time.sleep(1.5)
nx.press_buttons(controller_index, [nxbt.Buttons.HOME])

loop_count = 0
while True:
    print("You've reset " + str(loop_count) + " times.")
    loop = input('Reset? ')
    if loop == "no":
        break
    nx.macro(controller_index, macro)
    loop_count += 1
print("Times reset: " + str(loop_count))


alias macro="sudo python3 macro.py"
alias tui="sudo nxbt tui -r"