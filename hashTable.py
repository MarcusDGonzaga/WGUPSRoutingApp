
# Class that contains a Self Adjusting Data Structure: Chaining Hash Table
class ChainingHashTable:
    """
    Hash Table Data Structure
    Maps all package objects into an array
    Package IDs are unique so there is only one package per bucket
    Insert, Search, and Delete Functions
    Citation: From WGU C950 Webinar 2
    """
    # Constructor for the Hash Table creating an empty list
    def __init__(self, initial_capacity=39):
        # Initialized array with empty buckets
        self.table = []
        # O(n) time complexity
        for i in range(initial_capacity):
            self.table.append([])

    # Insert Function for adding the package objects into the array
    def insert(self, key, item):
        # Modulus operand to find the bucket to map the package object
        hashBucket = hash(key) % len(self.table)
        hashBucketList = self.table[hashBucket]

        # Update and returns true if package object is already mapped
        # O(n) Time Complexity
        for pID in hashBucketList:
            if pID[0] == key:
                pID[1] = item
                return True

        # Append item if package object is not already mapped
        packageKey = [key, item]
        hashBucketList.append(packageKey)
        return True

    # Search Function that searches buckets for package object using package ID as the key
    def searchItem(self, key):
        hashBucket = hash(key) % len(self.table)
        hashBucketList = self.table[hashBucket]

        # Returns object if found in a bucket in the Hash Table
        for pk in hashBucketList:  # O(n)
            if pk[0] == key:
                return pk[1]  # value
        # Returns None if object is not found in a bucket in the Hash Table
        return None

    # Delete Function that deletes item from hash table if object is found using the package ID as the key
    def deleteHash(self, key):
        # finds the package object in the hash table using the modulus operator
        hashBucket = hash(key) % len(self.table)
        hashBucketList = self.table[hashBucket]

        # Removes item from Hash Table
        # O(n) time complexity
        for pk in hashBucketList:
            if pk[0] == key:
                hashBucketList.remove(key)
