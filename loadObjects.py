# import statements for reading the CSV files to create objects
import csv
from customerPackages import CustomerPackages
from hashTable import ChainingHashTable


# Assign Hash Table Data Structure to utilize Package information
packHash = ChainingHashTable()

"""
Reads from the CSV file and creates objects from each row
Created objects are then inserted into the Hash Table Data Structure
Package ID needs to be converted from being a String to an int
"""
def createPackageObjects(filename):
    with open(filename) as packageInput:
        packageSpecifics = csv.reader(packageInput)
        # O(n) Time Complexity
        for packageObject in packageSpecifics:
            # Pacakge ID convert from a String to an int
            # Used as a key value as an int
            packageID = int(packageObject[0])
            packageStreetAddress = packageObject[1]
            packageCity = packageObject[2]
            # Column 3 is omitted as not required by the rubric and is redundant
            packageZip = packageObject[4]
            packageDeliverBy = packageObject[5]
            packageLbs = packageObject[6]
            # Initial Location of All packages at the WGUPS hub per Rubric Requirements
            packageUpdate = "At The Hub"

            # Objects are created from each row in the CSV
            package = CustomerPackages(packageID, packageStreetAddress, packageCity, packageZip, packageDeliverBy,
                                       packageLbs, packageUpdate)

            # Adds the package object and information into the hash table data structure
            # The package ID will be passed through as the key
            packHash.insert(packageID, package)
