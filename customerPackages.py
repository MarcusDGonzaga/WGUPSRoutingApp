# Customer Package Class for creating and outputting customer package objects
class CustomerPackages:
    """
    Customer package constructor for creating package objects
    Information will be read from the CSV file passed through the constructor
    It will then be sent to the Hash Table Data Structure for referencing
    Sequence is based on the CSV WGUPSPackageFile while omitting State data based on the rubric
    """
    def __init__(self, packageID, deliveryStreetAddress, deliveryCity, deliveryZip, deliveryBy, packageWeight, deliveryUpdate):
        # Object is initialized with values assigned read from the WGUPSPackageFile CSV file
        self.packID = packageID
        self.packStreetAddress = deliveryStreetAddress
        self.packCity = deliveryCity
        self.packZip = deliveryZip
        self.packDeliveryBy = deliveryBy
        self.packWeight = packageWeight
        self.packUpdate = deliveryUpdate
        # Assigned from the truck object in the sortToDeliver function
        self.leaveHubSchedule = 0
        # Assigned based on the Nearest Neighbor Algorithm in the sortToDeliver function
        self.packageDeliveredUpdate = 0

    # String Function created for outputting readable data in the Main Class User Interface
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (self.packID, self.packStreetAddress, self.packCity, self.packZip,
                                               self.packDeliveryBy, self.packWeight, self.packUpdate)
