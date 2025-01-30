# main.py
import weather_analysis #import the other files
def weather_analyze(file_path): #parameter is file path
    """
    TODO: Analyzes weather data from a file and prints the results.
    """
    weather_data = weather_analysis.read_weather_data(file_path) #called functions
    #where it returns a list of tuples
    avgtemp = weather_analysis.calculate_average_temperature(weather_data) #called functions
    totalrainfall = weather_analysis.calculate_total_rainfall(weather_data)
    highesttemp = weather_analysis.find_highest_temperature(weather_data)
    lowesttemp = weather_analysis.find_lowest_temperature(weather_data)

    return avgtemp, totalrainfall, highesttemp, lowesttemp

if __name__ == "__main__": # main function, where file goes 
    
    results = weather_analyze("weather_data.txt") #or the path to the file
    print(results)