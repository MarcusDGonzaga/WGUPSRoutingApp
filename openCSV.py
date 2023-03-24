# import statement for included CSV files per Rubric Requirements
import csv

# Keeps CSV file for finding the street data
with open("WGUPSAddressTable.csv") as csvAddress:
    cAdd = csv.reader(csvAddress)
    cAdd = list(cAdd)

# Keeps CSV file open for finding interval data between locations
with open("WGUPSDistanceTable.csv") as csvInterval:
    cInterval = csv.reader(csvInterval)
    cInterval = list(cInterval)


# Function to get package ID based on street for sortToDeliver function
def searchStreet(location):
    for row in cAdd:  # O(n)
        if location in row[1]:
            # return converts string to and int for comparisons
            return int(row[0])


# Function to find interval in miles for sortToDeliver function
def searchTravel(h, v):
    # find interval in miles
    travel = cInterval[h][v]
    # if statement preventing reading of blank data
    if travel == '':
        travel = cInterval[v][h]
    # converts string read from csv into float for comparison in Nearest Neighbor Algorithm
    return float(travel)

