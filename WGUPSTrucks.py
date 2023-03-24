# import statements for sorting and delivering packages
import datetime
import loadObjects
from openCSV import searchTravel
from openCSV import searchStreet


# WGUPS Truck Class for creating truck objects
class WGUPSTrucks:
    """
    WGUPS Truck constructor for creating truck objects
    Information is manually loaded based on package information and rubric requirements
    Location for all trucks will start at the WGUPS Hub
    """
    def __init__(self, truckPackages, timeLeaving):
        # starting location are all from the WGUPS HUB
        self.truckLocation = '4001 South 700 East'
        self.loadedCargo = truckPackages
        # Assigned manually based on Rubric Requirements
        self.truckDeparture = timeLeaving

        # Assigned in the sortToDeliver function
        # Information is outputted in the Main Class for user review
        self.distance = 0

        # Initially assigned to starting time
        # And will be updated as packages get delivered
        self.currentPoint = timeLeaving


# Function for sorting packages for the trucks to deliver
# Passes through truck object
def sortToDeliver(trucks):

    # Create temporary empty array to where packages will be loaded for sorting
    tempList = []

    # Takes packages off of the truck and into temporary array
    # O(n) time complexity
    for p in trucks.loadedCargo:
        truckPack = loadObjects.packHash.searchItem(p)
        tempList.append(truckPack)
    # Empty truck package itinerary
    trucks.loadedCargo.clear()
    """
    # Nearest Neighbor Algorithm 
    # Start from an initial point, go through each package object on the list, select closest destination
    # While Loop to go through each package on the temp array until there are no more packages to load to the truck
    # O(n^2) Time Complexity
    """
    while len(tempList) > 0:
        # temporary holds the distance to the nearest location
        # variable has a high number for comparison purposes to find the nearest delivery location
        nearestLoc = 1000
        currentPackage = 0
        # For loop to find next nearest location from current location
        for sortPack in tempList:
            truckLoc = 0
            packageLoc = 0
            truckLoc = searchStreet(trucks.truckLocation)
            packageLoc = searchStreet(sortPack.packStreetAddress)
            milesTo = searchTravel(truckLoc, packageLoc)
            # If statement comparing distances from current to previous locations
            if milesTo < nearestLoc:
                # assigns if statement is true
                nearestLoc = milesTo
                currentPackage = sortPack

        # After nearest destination is found
        # Loads the nearest package to truck and deletes from temporary hub array
        trucks.loadedCargo.append(currentPackage)
        tempList.remove(currentPackage)

        # Assigns Package departure time from Hub based on Rubric Assumptions and package delivery requests
        currentPackage.leaveHubSchedule = trucks.truckDeparture
        # Current truck location assigned location of the package
        trucks.truckLocation = currentPackage.packStreetAddress

        # Calculates mileage to destination to the Total Distance traveled by the truck
        # utilized in User Interface in the Main Class
        trucks.distance = trucks.distance + nearestLoc

        # Calculate interval to package destination
        # Truck speed is at 18 mph per prompt assumptions
        truckSpeed = 18
        # Variable converts time between seconds, minutes, and hours
        convertSecMinHr = 60
        # Calculates interval from previous stop to current stop
        timeInterval = (nearestLoc/truckSpeed) * convertSecMinHr

        # Calculate current time based on truck location using calculated interval
        trucks.currentPoint = trucks.currentPoint + datetime.timedelta(minutes=timeInterval)

        # Current time at destination is assigned to the package delivery time
        # Utilized in the user interface showing time of delivery
        currentPackage.packageDeliveredUpdate = trucks.currentPoint
