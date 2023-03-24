# main.py
# Author: Marcus Syldon Antino Dirige Gonzaga
# Student ID: 001401104
# Class: C950 Data Structures and Algorithms II
# Project: WGUPS Routing Application

# import statements
import datetime
from loadObjects import createPackageObjects
from WGUPSTrucks import WGUPSTrucks
from WGUPSTrucks import sortToDeliver
import loadObjects

# Loads Package Objects from the CSV into the Hash Table Data Structure
createPackageObjects('WGUPSPackageFile.csv')

"""
Truck objects for delivery
Creates object with loaded packages and departure time
Packages based on deliver time and notes in the CSV WGUPSPackageFile
"""
truck1 = WGUPSTrucks([1, 4, 5, 11, 13, 14, 15, 16, 19, 20, 21, 24, 26, 29, 30, 37],
                     datetime.timedelta(hours = 8, minutes= 0))
truck2 = WGUPSTrucks([3, 6, 12, 17, 18, 22, 23, 25, 28, 31, 32, 34, 36, 38, 40],
                     datetime.timedelta(hours= 9, minutes= 5))
truck3 = WGUPSTrucks([2, 7, 8, 9, 10, 27, 33, 35, 39], datetime.timedelta(hours= 11, minutes= 0))

"""
Main Function
Starts by loading truck objects into the sortToDeliver function
Followed by the User Interface on acquiring tracking information for the packages
Asks the user for input on the number of packages and time
Accounts for the update on Package #9 at 10:20
"""
class Main:
    # Truck objects called to sort and deliver the packages
    sortToDeliver(truck1)
    sortToDeliver(truck2)
    sortToDeliver(truck3)

    print("\nWelcome to the Western Governers University Parcel Service Tracking Software")

    # Asks the user if they would like to track a single package or all the packages in the tracker software
    print("\nHow many packages would you like to track?")
    print("Option 1: Single package")
    print("Option 2: All packages\n")
    # input statement for selection between option 1 or 2
    selection = input("Please type 1 or 2:  ")

    # Selection 1 if statement
    # User wants to track a single package
    if selection == '1':
        # Requests user for the Package ID number they would like to track
        requestID = input("Please type in Package ID number: ")
        # Package is search for in the Hash Table Data Structure
        package = loadObjects.packHash.searchItem(int(requestID))

        # Requests the time user would like to track the packages for
        print("Please enter the desired time for package tracking: ")
        hr = input("Hour: ")
        min = input("Minute: ")
        # input is assigned for time comparisons
        timeTracking = datetime.timedelta(hours=int(hr), minutes=int(min))
        # Print statement to reiterate desired time for tracking
        print("You have entered the time: ", timeTracking, "\n")

        # if statement for package 9
        # compares time to see if address of package 9 has been updated
        if timeTracking >= datetime.timedelta(hours= 10, minutes= 20):
            # Assigns new address to package 9 if statement is true
            package9 = loadObjects.packHash.searchItem(9)
            package9.packStreetAddress = "410 S State St"
            package9.packZip = "84111"

        # if elif else statement checking updates on packages based on desired time
        # Package update includes the time per rubric requirements
        if timeTracking < package.leaveHubSchedule:
            package.packUpdate = "At Hub " + "as of: " + str(timeTracking)
        elif timeTracking >= package.packageDeliveredUpdate:
            package.packUpdate = "Delivered " + "at: " + str(package.packageDeliveredUpdate)
        else:
            package.packUpdate = "En Route " + "as of: " + str(timeTracking)
        # Displays updated package information
        print(loadObjects.packHash.searchItem(int(requestID)))

    # Selection 2 elif statement
    # User wants to track a all packages at the WGUPS hub
    elif selection == '2':
        # Requests the time user would like to track the packages for
        print("Please enter the desired time for package tracking: ")
        hr = input("Hour: ")
        min = input("Minute: ")
        # input is assigned for time comparisons
        timeTracking = datetime.timedelta(hours=int(hr), minutes=int(min))
        # Print statement to reiterate desired time for tracking
        print("You have entered the time: ", timeTracking, "\n")

        # if statement for package 9
        # compares time to see if address of package 9 has been updated
        if timeTracking >= datetime.timedelta(hours= 10, minutes= 20):
            package9 = loadObjects.packHash.searchItem(9)
            package9.packStreetAddress = "410 S State St"
            package9.packZip = "84111"

        # Updates the status of ALL the packages based on inputted time using a for loop
        # O(n) time complexity
        for p in range(41):
            if p > 0:
                # utilizes value in the for loop to search in Hash Table Data Structure and make changes to object
                package = loadObjects.packHash.searchItem(p)
                # if elif else statement checking updates on packages based on desired time
                # Package update includes the time per rubric requirements
                if timeTracking < package.leaveHubSchedule:
                    package.packUpdate = "At Hub " + "as of: " + str(timeTracking)
                elif timeTracking >= package.packageDeliveredUpdate:
                    package.packUpdate = "Delivered " + "at: " + str(package.packageDeliveredUpdate)
                else:
                    package.packUpdate = "En Route " + "as of: " + str(timeTracking)
                # Displays updated package info one by one
                print(loadObjects.packHash.searchItem(p))

        # Displays Total Mileage of all trucks after all 40 packages have been delivered
        print("\nTotal Miles Traveled For All Trucks: ", round(truck1.distance + truck2.distance + truck3.distance, 2),
              "miles")

# exits the program after displaying the information
exit()


























