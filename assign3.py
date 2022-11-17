# Name: Mack Bautista (201729981)   /   Soona Youssef (201708547)

USERNAME = "mbaut981"  # define your MRU username here

def get_beverage_type(a_enabled: bool, b_enabled: bool) -> str:
    """
    Returns the beverage type defined by the switches.
    """
    if a_enabled and b_enabled:
        drink = "JUICE, APPLE"
    elif (not a_enabled) and b_enabled:
         drink = "COKE, REGULAR"
    elif a_enabled and (not b_enabled):
         drink = "TEA, GREEN"
    elif (not a_enabled) and (not b_enabled):
        drink = "TEA, GREEN"
    return drink

def get_temperature_desc(slider_value: int) -> str:
    """
    Returns the temperature description defined by the slider value.
    Assume the value is always an integer between 0 and 100 (inclusive).
    """
    FREEZING_POINT = 0 
    COOLING_POINT = 15
    WARMING_POINT = 39
    HEATING_POINT = 99
    BOILING_POINT = 100
    
    if slider_value == FREEZING_POINT:       
        temp = "FROZEN"
    elif slider_value <= COOLING_POINT:
        temp = "COLD"
    elif slider_value <= WARMING_POINT:
        temp = "WARM"
    elif slider_value <= HEATING_POINT:
        temp = "HOT"
    elif slider_value == BOILING_POINT:
        temp =  "BOILING"
    return temp

def get_switch_value(switch_name: str) -> bool:
    """
    Prompts the user for the state of the specified switch.
    Returns true if the specified switch is enabled and false otherwise.
    """
    user_input = switch_name
    user_input = str(input(f"Is switch {switch_name} enabled? (y/n): ").lower())
    
    if user_input == 'y':
        return True
    else:
        return False

def displayer(beverage: str, beverage_temp: str) -> None:
    """
    Displays the user's results
    """
    print(f"The drink you have selected is: {beverage}, {beverage_temp}.")

def main() -> None:
    """
    Prompts the user for the state of switches A and B and
    the value of the numeric slider. Using the various provided
    function headers, duplicate the functionality of the
    abandoned replicator at https://mru-replicator.fly.dev.
    """
    switch_a = get_switch_value('A')
    switch_b = get_switch_value('B')
    temperature = get_temperature_desc(int(input("What is the value of the numeric slider? (0-100): ")))
    beverage_type = get_beverage_type(switch_a, switch_b)
    displayer(beverage_type, temperature)
main()

# Citations
# [1] Python style guide. F22 COMP 1501-001. Charlotte Curtis 2022. [Accessed at: November, 3, 2022]: https://mru-f22-cs1.github.io/content-curtis/extras/python-style.html