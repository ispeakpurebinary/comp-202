DENSITY = 1.225
AREA_COST = 5
FUEL_COST = 6.1
TAX = 1.15
GRAVITY = 9.81
MIN_WEIGHT = 20
MAX_WEIGHT = 500                    
MIN_BOX_VOLUME = 0.125
 
import math

def feet_to_meter(length):
    """
    Converts length from feet to meters
    Parameters:
        length (float): input in feet
    Returns:
        length(float): output in meters
    Examples:
        >>> print(feet_to_meter(5.0))
        1.52
        >>> print(feet_to_meter(10.75))
        3.28
        >>> print(feet_to_meter(115.9))
        35.34     
    """
    feet_to_meter = length/3.28
    feet_to_meter_rounded = round(feet_to_meter,2)
    return feet_to_meter_rounded

def rocket_volume(radius,height_cone,height_cyl):
    """
    Calculates volume of rocket
    Parameters:
        radius (float) input
        height_cone (float) input
        height_cyl(float) input
    Returns:
        rocket_volume(float) rounded to 2 decimal places
    Examples:
        >>>print(rocket_volume(2.0,7.0,3.0))
        67.02
        >>>print(rocket_volume(12.6,9.50,4.0))
        3574.44
        >>>print(rocket_volume(7.9,15.4,9.0))
        2771.08   
    """
    volume_of_cone = (math.pi * radius*radius) * height_cone/3
    volume_of_cyl = math.pi * radius*radius * height_cyl
    rocket_volume = volume_of_cone + volume_of_cyl
    return round(rocket_volume,2)

def rocket_area(radius,height_cone,height_cyl):
    """
    Calculates the surface area of a rocket
    Parameters:
        radius(float) input
        height_cone(float) input
        height_cyl(float) input
    Returns:
        rocket_sa (float) rounded to 2 decimal places
    Examples:
        >>>print (rocket_area(13.4,17.6,3.9))
        1823.68
        >>>print(rocket_area(4.7,12.9,6.78))
        472.34
        >>>print(rocket_area(14.6,9.24,5.5))
        1966.71
    """
    Area_cone = math.pi * radius \
                *(radius + math.sqrt(height_cone * height_cone + radius * radius))
    Area_cyl = 2 * math.pi * radius * (height_cyl + radius)
    Area_circle = math.pi * radius *radius
    rocket_sa = Area_cone + Area_cyl - 2* Area_circle
    return round(rocket_sa,2)


def rocket_mass(radius,height_cone,height_cyl):
    """
    Calculates the rocket's mass by multiplying its volume by its density
    Parametres:
        radius(float) input
        height_cone(float) input
        height_cyl(float) input
    Returns:
        rocket_mass(float) rounded to 2 decimal places
    Examples:
        >>> print(rocket_mass(2.0,7.0,3.0))
        82.1
        >>>print(rocket_mass(6.0,8.3,2.0))
        660.4
        >>>print(rocket_mass(10.5,7.43,5.89))
        3549.9
    """
    rocket_mass = (rocket_volume(radius,height_cone,height_cyl) * DENSITY)
    return round(rocket_mass,2)


def rocket_fuel(radius,height_cone,height_cyl,velocity_e,velocity_i,time):
    """
    Calculates the total amount of fuel required by rocket based on the input parameters
    Parameters:
        radius (float) input
        height_cone (float) input
        height_cyl (float) input
        velocity_e (float) input exhaust velocity
        velocity_i (float) input initial velocity
        time (float) input
    Returns:
        total_fuel_needed(float) rounded to 2 decimal places
    Examples:
        >>> print(rocket_fuel(50.0,100.0,800.0,700.0,300.0,120.0))
        4616444.53
        >>>print(rocket_fuel(80.5,120.0,600.0,400.0,100.0,140.0))
        4914244.61
        >>>print(rocket_fuel(40,70.0,60.0,500,70.0,90.0))
        321999.51
    """
    mass_of_fuel = rocket_mass(radius,height_cone,height_cyl) \
                   * ((math.exp(velocity_i/velocity_e) - 1))
    # if statement to determine the amount of fuel needed in different conditions
    if rocket_mass(radius,height_cone,height_cyl) < 100000:
        fuel_burnt = 1360
    elif rocket_mass(radius,height_cone,height_cyl) < 400000:
        fuel_burnt = 2000
    else:
        fuel_burnt = 2721
    total_fuel_needed = round((mass_of_fuel + (fuel_burnt * time)),2)
    return total_fuel_needed

def calculate_cost(radius, height_cone, height_cyl,velocity_e, velocity_i, time, tax):
    """
    Calculates approximate cost of building and launching the rocket
    Parameters:
        radius(float) input
        height_cone (float) input
        height_cyl (float) input
        velocity_e (float) input exhaust velocity
        velocity_i (float) input initial velocity
        time (float) input
        time (boolean) input
    Returns:
        total_cost (float) in dollars rounded to 2 decimal points
    Examples:
        >>>print(calculate_cost(11.2, 51.8, 105.7, 123.45, 99.65, 81.94, True))
        1354550.56
        >>>print(calculate_cost(17.4, 22.8, 135.7, 47.45, 72.95, 41.94, False))
        4318522.61
        >>>print(calculate_cost(186.4, 51.8, 125.7, 78.45, 95.36, 92.59,True))
        322006974.25
    """
    cost_of_fuel = rocket_fuel(radius,height_cone,height_cyl,velocity_e,velocity_i,time) * FUEL_COST
    cost_of_materials = rocket_area(radius,height_cone,height_cyl) * AREA_COST
    if tax == True:
        total_cost = (cost_of_materials + cost_of_fuel)
        total_cost = (TAX * total_cost) 
    else:
        total_cost = cost_of_materials + cost_of_fuel
    return round(total_cost,2)

def compute_storage_space(radius,height_cyl):
    """
    Calculates the dimensions of the rectangular storage box
    Parameters:
        radius (float) input
        height_cyl (float) input
    Returns:
        width_rocket (float)
        length_rocket (float)
        height_rocket (float)
    Examples:
        >>>print(compute_storage_space(5.0, 10.0))
        (7.07, 7.07, 5.0)
        >>>print(compute_storage_space(7.8, 12.5))
        (11.03, 11.03, 6.25)
        >>>print(compute_storage_space(56.3, 35.0))
        (79.62, 79.62, 17.5)
          
    """
    length_rocket = round(math.sqrt(2)* radius,2)  
    width_rocket = length_rocket
    height_rocket = height_cyl/2
    return (width_rocket,length_rocket, height_rocket)

def load_rocket(initial_weight, radius, height_cyl):
    """
    Computes the volume of storage space, determines the constrains, \
    adds items to the rockets if the constrains are satisfied, prints a message \
    if no more  items can be added
    Parameters:
        rocket_mass (float) input, initial weight of the rocket
        radius (float) input
        height_cyl (float) input
    Returns:
        updated_weight = positive float
    Examples:
        >>>(load_rocket(399.0,100.0,1000.0))
        No more items can be added
        399.0

        >>>(load_rocket(7000,40,100)
        Please enter the weight of the next item (type "Done" when you are done filling the rocket): 5
        Enter item width: 7
        Enter item length: 9
        Enter item height: 4
        Item could not be added... please try again...
        Please enter the weight of the next item (type "Done" when you are done filling the rocket):

        >>load_rocket(10000, 60, 300)
        Please enter the weight of the next item (type "Done" when you are done filling the rocket): Done
        10000.0 

    
    """
    length_rocket, width_rocket, height_rocket = compute_storage_space(radius,height_cyl)
    storage_volume = length_rocket * width_rocket * height_rocket
    if ((MIN_BOX_VOLUME > 0.4 * storage_volume) or \
           (MIN_WEIGHT > 0.05 * initial_weight)):
        print("No more items can be added")
        return initial_weight
    else:
        updated_weight = float(initial_weight)
        total_weight_added = 0
        total_volume_added = 0
    while True:
        #obtaining inputs from the user
        item_weight = input('Please enter the weight of the next item (type "Done" when you \
                            are done filling the rocket): ')
        if item_weight != 'Done':
            item_weight = float(item_weight)
            item_width = float(input('Enter item width: '))
            item_length = float(input('Enter item length: '))
            item_height = float(input('Enter item height: '))
            item_volume = item_width * item_length * item_height
            
            total_weight_added = total_weight_added + item_weight
            total_volume_added = total_volume_added + item_volume
            
            #determining the constraints
            first_weight_condition = total_weight_added <= 0.05 * initial_weight
            second_weight_condition = MIN_WEIGHT <= item_weight <= MAX_WEIGHT
            first_volume_condition = total_volume_added <= 0.4 * storage_volume
            second_volume_condition = MIN_BOX_VOLUME <= item_volume
            
            end_weight_condition = total_weight_added > 0.05 * initial_weight - 20
            end_volume_condition = total_volume_added > 0.40 * storage_volume - MIN_BOX_VOLUME
            
            if not(second_weight_condition) or not(second_volume_condition) or \
                   not (first_weight_condition) or not(first_volume_condition):
                total_weight_added = total_weight_added - item_weight
                total_volume_added = total_volume_added - item_volume
                print("Item could not be added... please try again...")
                
            #Will check if space is remaining to add more items
            elif (end_weight_condition or end_volume_condition):
                updated_weight = updated_weight + item_weight
                print("No more items can be added")
                return round(updated_weight,2)
            else:
                updated_weight = float(updated_weight + item_weight)
        else:
            return round(updated_weight,2)
             
def projectile_sim(simulation_time, interval, velocity_i, angle):
    '''
    Prints the height of rocket at each time interval
    Parameters:
        simulation_time (int) 
        interval(int)
        velocity_i (float)
        angle(float)
    Returns:
        None (Nonetype)
    Examples:
        >>> projectile_sim(10,2,100,0.79)
            0.0
            122.45
            205.66
            249.63
            254.36
            219.85

        >>> projectile_sim(10,3,70,0.5)
            0.0
            56.53
            24.78
        >>> projectile_sim(10,2,50,0.85)
            0.0
            55.51
            71.78
            48.8
    '''
    #Takes input as the number of seconds we want the 
    for interval_time in range (0,simulation_time +1, interval):
        height = (-1/2 * GRAVITY * (interval_time**2)) + (velocity_i *\
                                                         math.sin(angle)*interval_time)
        if height >= 0:
            print(round(height,2))
               
def rocket_main():
    """
    Makes use of all the functions and gets all inputs from users
    Parameters:
        None(NoneType)
    Returns:
        None(NoneType)
    Examples:
    >>> rocket_main()
    Welcome to the Rocket Simulation!
    Enter the rocket radius in feet: 50
    Enter the rocket cone height in feet: 120
    Enter the rocket cylinder height in feet: 180
    Enter the exhaust velocity for the upcoming trip: 800
    Enter the initial velocity for the upcoming trip: 400
    Enter the angle of launch for the upcoming trip: 0.75
    Enter the length of the upcoming trip: 1500
    Would you like to factor in tax? 1 for yes, 0 for no: 1
    This trip will cost $14628767.44
    Now loading the rocket:
    Please enter the weight of the next item (type "Done" when you are done filling the rocket): 120
    Enter item width: 6
    Enter item length: 4
    Enter item height: 5
    Please enter the weight of the next item (type "Done" when you are done filling the rocket): Done
    The rocket and its equipment will weigh 60075.27 kg
    Enter the simulation total time: 7
    Enter the simulation interval: 1
    Now simulating the rocket trajectory:
    0.0
    267.75
    525.69
    773.82
    1012.14
    1240.65
    1459.35
    1668.24
    """
    print("Welcome to the Rocket Simulation!")
    radius = feet_to_meter(float(input("Enter the rocket radius in feet: ")))
    height_cone = feet_to_meter(float(input("Enter the rocket cone height in feet: ")))
    height_cyl = feet_to_meter(float(input("Enter the rocket cylinder height in feet: ")))
    initial_weight = rocket_mass(radius,height_cone,height_cyl)
    velocity_e = float(input("Enter the exhaust velocity for the upcoming trip: "))
    velocity_i = float(input("Enter the initial velocity for the upcoming trip: "))
    angle = float(input("Enter the angle of launch for the upcoming trip: "))
    time = int(input("Enter the length of the upcoming trip: "))
    tax = input("Would you like to factor in tax? 1 for yes, 0 for no: ")
    if tax == '1':
        tax = True
    else:
        tax = False
    rocket_cost = calculate_cost(radius, height_cone, height_cyl,velocity_e, velocity_i, time, tax)
    print("This trip will cost $" + str(rocket_cost))
    print("Now loading the rocket:")
    print("The rocket and its equipment will weigh", load_rocket(initial_weight, radius, height_cyl), "kg")
    simulation_time = int(input("Enter the simulation total time: "))
    interval = int(input("Enter the simulation interval: "))
    print("Now simulating the rocket trajectory:")
    projectile_sim(simulation_time, interval, velocity_i, angle)
