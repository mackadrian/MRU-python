# USERNAME1 Mack Bautista - 201729981 
import math

# Knowns
# First location - Homage statue
H_LAT = 51.013760
H_LONG = 114.133691
DEC_DEG = (H_LAT , H_LONG)                    # Prints into (latitude, longtitude) form

# Unknowns
# Second location - Ask user for input
USER_LOCATION = (input("Please enter any location in Alberta:    ==>   "))
USER_LAT = float((input("Next, please provide the latitude of your location :    ==> ")))
USER_LONG = abs(float((input("Lastly, please provide the longtitude of your location :    ==>  "))))
DEC_DEGUSER = (USER_LAT , USER_LONG )     # Prints into (latitude , longtitude ) form

# Calculations (and sub calculations)
    # Conversions #
rad_lat1 = math.radians(H_LAT)
rad_long1 = math.radians(H_LONG)
rad_lat2 = math.radians(USER_LAT)
rad_long2 = math.radians(USER_LONG)
changein_lat = rad_lat1 - rad_lat2 
changein_long = rad_long1 - rad_long2

    # Haversine formulae #
A = math.sin(changein_lat / 2) ** 2 + math.cos(rad_lat1) * math.cos(rad_lat2) * math.sin(changein_long / 2) ** 2        # Formula used to calculate the change in latitude and longtitude
C = 2 * math.atan2(math.sqrt(A), math.sqrt(1 - A))                                                                      # Formula Used to find the arc of the Earth
EQUI_RAD = 6_378_137
POL_RAD = 6_356_752
R = (1 / 3) * (2 * EQUI_RAD + POL_RAD)       # R should be 6,371,008.667
DIST = (R * C) / 1000                        #Converts metres into kilometres

    # D/M/S #
# Homage statue conversion
    # Latitude 
LAT_DEG = int(H_LAT)
LAT_MIN = (H_LAT % 1) * 60                     # Use modulo to find remainder which is decimals
LAT_SEC = ((LAT_MIN % 1) * 60)               # Use modulo to find remainder which is decimals          

    #Longtitude
LONG_DEG = int(H_LONG)
LONG_MIN = (H_LONG % 1) * 60                  # Use modulo to find remainder which is decimals            
LONG_SEC = ((LONG_MIN % 1) * 60)            # Use modulo to find remainder which is decimals   

# User input conversion
    # User input latitude
USER_LAT_DEG = int(USER_LAT)
USER_LAT_MIN = (USER_LAT % 1) * 60           # Use modulo to find remainder which is decimals    
USER_LAT_SEC = ((USER_LAT_MIN % 1) * 60)      # Use modulo to find remainder which is decimals   

    #User input longtitude
USER_LONG_DEG = int(USER_LONG)
USER_LONG_MIN = (USER_LONG % 1) * 60         # Use modulo to find remainder which is decimals   
USER_LONG_SEC = ((USER_LONG_MIN % 1) * 60)    # Use modulo to find remainder which is decimals  

    #Conversion into integers to add into f-strings
LAT_MIN = int(LAT_MIN)
LONG_MIN = int(LONG_MIN)
USER_LAT_MIN = int(USER_LAT_MIN)
USER_LONG_MIN = int(USER_LONG_MIN)

# Solution Statement(s)
print(f"\nThe Homage Statue is located at {DEC_DEG} or {LAT_DEG}\u00B0 {LAT_MIN}\u0027 {LAT_SEC:.2f}\u0022 N , {LONG_DEG}\u00B0 {LONG_MIN}\u0027 {LONG_SEC:.2f}\u0022 W. ")
print(f"{USER_LOCATION} is located at {DEC_DEGUSER} or {USER_LAT_DEG}\u00B0 {USER_LAT_MIN}\u0027 {USER_LAT_SEC:.2f}\u0022 N , {USER_LONG_DEG}\u00B0 {USER_LONG_MIN}\u0027 {USER_LONG_SEC:.2f}\u0022 W. ")
print(f"The distance between the Homage Statue and {USER_LOCATION} is {DIST:.1f} km. ")

# Citations
    #[1] "Decimal Degrees to Degrees Minutes Seconds", Calculator Soup. Accessed Oct 5, 2022. Available: https://www.calculatorsoup.com/calculators/conversions/convert-decimal-degrees-to-degrees-minutes-seconds.php
    #[2] Google Maps. [Screen Capture]. Oct 5, 2022.
    #[3] "Unicode", Wikipedia: The Free Encyclopedia, [Edited  3 October 2022] Available https://en.wikipedia.org/wiki/Unicode
    #[4] "Calculate distance, bearing and more between Latitude/Longitude points", Movable Type Scripts. Accessed Oct 5, 2022. Available: https://www.movable-type.co.uk/scripts/latlong.html