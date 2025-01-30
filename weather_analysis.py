# Instructions:
# this file contains all the functions that are required to analyze the weather data.
# 1. **Remove the TODO comment and pass statement** once you’ve completed the function implementation.
#    - The TODO and pass are placeholders indicating that the function is not yet complete.
#    - Once the function is implemented, these should be removed to keep the code clean.
# 
# 2. **Best Coding Practices**:
#    - In professional programming, finalizing the code means removing unnecessary placeholders.
#    - This ensures your code is ready for review, testing, and does not contain clutter.
# 
# 3. **Adding Docstrings**:
#    - After removing TODO and pass, add a **docstring** for each function.
#    - The docstring should explain the function’s purpose, parameters, and expected output.
#    - Proper documentation improves code readability and helps with debugging and maintenance.

def read_weather_data(file_path: str):
    """
    Reads weather data from a file and returns it as a list of tuples
    First, we open the file in read mode and read the file line by line. Then we split the values by comma and remove 
    whitespace within the loop to access the file contents line by line.(Date, time and rain). Then we are creating a tuple 
    out of the list's values and adding it to the empty list we created at the start to make a list of tuples. 
    """
    return_list = [] #creates an empty list to store the tuples 
    file = open(file_path,"r"); #open file in read mode for reading line by line
    filelist = file.readlines(); #splits vals by commas and reads the file 
    for i in filelist: #iterating through file list 
        dtr = i.strip().split(","); #date, time rainfall, accessing line by line
        #tuplelist = tuple(dtr) casting to convert it 
        tuplelist = (dtr[0],dtr[1],dtr[2]); #creates a tuple out of the list
        return_list.append(tuplelist) #adds the tuple to our empty list to create a list of tuples

    return return_list


                

def calculate_average_temperature(weather_data):
    """
    First, we create an empty variable to store the sum of the temperatures. 
    Then we iterate through the weather data line by line and the second value of each list(date,time,rainfall) represents the 
    temperature, so we add all of the temperatures together.To calculate the average, we divide the total sum by the length of the weather_data list which should be 3.
    """
    
    sumtemp = 0 #creates an empty variable to store the sum of the temperatures
    for i in weather_data: #iterates through the weather data, line by line
        sumtemp += i[1] #the second value of each list represents the temperature, so we are going to add up all the temperatures in weather data
    
    avgtemp = sumtemp/len(weather_data) 
    return avgtemp 

def calculate_total_rainfall(weather_data):
    """
    TODO: Calculates the total rainfall from the weather data.
    """
    pass
    sumrain = 0 #creates an empty variable to store the sum of the rainfall
    for i in weather_data: #iterates through the weather data, line by line
        sumrain += i[2] #the third value of each list represents the rainfall, so we are going to add up all the rainfall in weather data
    return sumrain; #returns the sum of the rainfall

def find_highest_temperature(weather_data):
    """
    TODO: Finds the highest temperature and the corresponding date from the weather data.
    """
    max = weather_data[0]
    for i in weather_data: # i is the whole list
        if i[1] > max[1]:
            max = i
    return max[0],max[1]



def find_lowest_temperature(weather_data):
    """
    TODO: Finds the lowest temperature and the corresponding date from the weather data.
    """
    min = weather_data[0] #setting it equal to the first element of the list 
    for i in weather_data: # i is the whole list
        if i[1] < min[1]:
            min = i
    return min[0],min[1]

def find_day_with_most_rainfall(weather_data):
    """
    TODO: Finds the day with the most rainfall from the weather data.
    """
    max = weather_data[0] #gives us the first element of the list, which is a tuple
    for i in weather_data:
        if i[2] > max[2]:
            max = i
    return max[0],max[2]

