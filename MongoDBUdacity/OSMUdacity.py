def import_osm_node_to_mongo():

    # This function will use lxml iterparse to go through each element to find the "tag" element. If this is the first "tag" of each "node",
    # it will get all the information of that "node", get all the tags, put them under "tag" key of dictionary "d". Then the entire dictionary
    # is push to mongodb data base. It's necessary because MongoDB provides efficient way to query data. 
    
    osm = "C:/Users/Long Nguyen/My-1st-Project/LAData/los-angeles_california.osm"
    from lxml import etree
    from pymongo import MongoClient
    client = MongoClient()
    db = client.examples
    temp1 = {}
    d = {}
    with open(osm, "r") as f:
        context = etree.iterparse(f, recover = True)
        for event,elem in context:
            temp1 = {}
            if elem.tag == "tag":
                par = elem.getparent()
                if elem.getprevious() is None:
                    if par.tag == "node":
                        att = par.attrib
                        for key in att:
                            d[key] = att[key]
                        for tag in par.iter("tag"):
                            key = tag.get("k")
                            value = tag.get("v")
                            if (key is not None) & (value is not None):
                                temp1[key] = value
                        d["tag"] = temp1
                        d["type"] = par.tag
                        del temp1
            if d:
                db.osm.node.insert(d)
                d = {}
            elem.clear()
            while elem.getprevious() is not None:
                del elem.getparent()[0]
        del context


def import_osm_way_to_mongo():

    # This function will use lxml iterparse to go through each element to find the "nd" element. If this is the first "nd" of each "way",
    # it will get all the information of that "way". All "nd" will be put into a list and then put under a key name "nd".
    # All the tags are put under "tag" key of dictionary "d". Then the entire dictionary
    # is push to mongodb data base. It's necessary because MongoDB provides efficient way to query data. 
    
    osm = "C:/Users/Long Nguyen/My-1st-Project/LAData/los-angeles_california.osm"
    from lxml import etree
    from pymongo import MongoClient
    client = MongoClient()
    db = client.examples
    temp1 = {}
    d = {}
    with open(osm, "r") as f:
        context = etree.iterparse(f, recover = True)
        for event,elem in context:
            temp2 = []
            temp1 = {}
            if elem.tag == "nd":
                par = elem.getparent()
                if elem.getprevious() is None:
                    if par.tag == "way":
                        att = par.attrib
                        for key in att:
                            d[key] = att[key]
                        for nd in par.iter("nd"):
                           if nd.get("ref"):
                                temp2.append(nd.get("ref"))
                        for tag in par.iter("tag"):
                            key = tag.get("k").strip(".")
                            value = tag.get("v")
                            if key.find(".") is not -1:
                                key = key.replace("."," ")
                            if (key is not None) & (value is not None):
                                temp1[key] = value
                        d["tag"] = temp1
                        d["nd"] = temp2
                        d["type"] = par.tag
                        del temp1
                        del temp2
            if d:
                db.osm.way.insert(d)
                d = {}
            elem.clear()
            while elem.getprevious() is not None:
                del elem.getparent()[0]
        del context


def import_osm_relation_to_mongo():

    # This function will use lxml iterparse to go through each element to find the "member" element. If this is the first "member" of each "relation",
    # it will get all the information of that "relation". All key-value pairs of each "member" will pe put into a dictionary, and all the dictionaries
    # will be put into a list under the key name "member". 
    # All the tags are put under "tag" key of dictionary "d". Then the entire dictionary
    # is push to mongodb data base. It's necessary because MongoDB provides efficient way to query data. 
    
    osm = "C:/Users/Long Nguyen/My-1st-Project/LAData/los-angeles_california.osm"
    from lxml import etree
    from pymongo import MongoClient
    client = MongoClient()
    db = client.examples
    temp1 = {}
    d = {}
    with open(osm, "r") as f:
        context = etree.iterparse(f, recover = True)
        for event,elem in context:
            temp2 = []
            temp1 = {}
            if elem.tag == "member":
                par = elem.getparent()
                if elem.getprevious() is None:
                    if par.tag == "relation":
                        att = par.attrib
                        for key in att:
                            d[key] = att[key]
                        for member in par.iter("member"):
                            temp2.append([member.get("type"),member.get("ref"),member.get("role")])
                        for tag in par.iter("tag"):
                            key = tag.get("k").strip(".")
                            value = tag.get("v")
                            if key.find(".") is not -1:
                                key = key.replace("."," ")
                            if (key is not None) & (value is not None):
                                temp1[key] = value
                        d["tag"] = temp1
                        d["member"] = temp2
                        d["type"] = par.tag
                        del temp1
                        del temp2
            if d:
                db.osm.relation.insert(d)
                d = {}
            elem.clear()
            while elem.getprevious() is not None:
                del elem.getparent()[0]
        del context



def update_way():

    # Data structure for each "way" document will be updated so that "version", "changeset", "timestamp", "user", and "uid"
    # will be keys in a single dictionary called "created"
    
    import pymongo
    from pymongo import MongoClient
    from bson.objectid import ObjectId
    client = MongoClient()
    db = client.examples
    result = db.osm.way.find()
    for doc in result:
        i = doc["_id"]
        if "version" in doc.keys():
            version = doc["version"]
        else:
            version = ""
        if "changeset" in doc.keys():
            changeset = doc["changeset"]
        else:
            changeset = ""
        if "timestamp" in doc.keys():
            timestamp = doc["timestamp"]
        else:
            timestamp = ""
        if "user" in doc.keys():
            user = doc["user"]
        else:
            user = ""
        if "uid" in doc.keys():
            uid = doc["uid"]
        else:
            uid = ""
        if ("lat" in doc.keys()) & ("lon" in doc.keys()):
            pos = [doc["lat"],doc["lon"]]
        else:
            pos = []
        db.osm.way.update({"_id":i},{"$set":{"created.version":version,
                                              "created.changeset":changeset,
                                              "created.timestamp":timestamp,
                                              "created.user":user,
                                              "created.uid":uid}})
        db.osm.way.update({"_id":i},{"$unset":{"version":"",
                                                "changeset":"",
                                                "timestamp":"",
                                                "user":"",
                                                "uid":""}})



def update_relation():

    # Data structure for each "relation" document will be updated so that "version", "changeset", "timestamp", "user", and "uid"
    # will be keys in a single dictionary called "created"
    
    import pymongo
    from pymongo import MongoClient
    from bson.objectid import ObjectId
    client = MongoClient()
    db = client.examples
    result = db.osm.relation.find()
    for doc in result:
        i = doc["_id"]
        if "version" in doc.keys():
            version = doc["version"]
        else:
            version = ""
        if "changeset" in doc.keys():
            changeset = doc["changeset"]
        else:
            changeset = ""
        if "timestamp" in doc.keys():
            timestamp = doc["timestamp"]
        else:
            timestamp = ""
        if "user" in doc.keys():
            user = doc["user"]
        else:
            user = ""
        if "uid" in doc.keys():
            uid = doc["uid"]
        else:
            uid = ""
        if ("lat" in doc.keys()) & ("lon" in doc.keys()):
            pos = [doc["lat"],doc["lon"]]
        else:
            pos = []
        db.osm.relation.update({"_id":i},{"$set":{"created.version":version,
                                              "created.changeset":changeset,
                                              "created.timestamp":timestamp,
                                              "created.user":user,
                                              "created.uid":uid}})
        db.osm.relation.update({"_id":i},{"$unset":{"version":"",
                                                "changeset":"",
                                                "timestamp":"",
                                                "user":"",
                                                "uid":""}})


def update_node_street():

    # Some nodes that have house number don't have street address. Since we want all nodes which have house number to have "street address",
    # "city", "state", "country", and "post code", we have to fill in "street address". By using "geopy" library to optain address from "geocode" API
    # knowing latitude and longitude, we can extract street address from there.
    
    import re
    import pymongo
    import unicodedata
    from pymongo import MongoClient
    from bson.objectid import ObjectId
    from geopy.geocoders import Nominatim
    client = MongoClient()
    db = client.examples
    geolocator = Nominatim()
    address_pattern = re.compile(r"[0-9]+\s*\w+")
    result = db.osm.test.find({"lat":{"$exists":True},"lon":{"$exists":True},
                               "tag.addr:housenumber":{"$exists":True},
                               "tag.addr:street":{"$exists":False},"$or":[
                               {"tag.addr:city":{"$exists":True}},
                               {"tag.addr:postcode":{"$exists":True}}]})
    for doc in result:
        i = doc["_id"]
        pos = doc["lat"] + "," +doc["lon"]
        location = geolocator.reverse(pos, timeout = 10)
        address = location.address.split(",")[0].strip(" ")
        if not(address_pattern.match(address)):
            street = location.address.split(",")[2].strip(" ")
        else:
            street = location.address.split(",")[1].strip(" ")
        db.osm.test.update({"_id":i},{"$set":{"tag.addr:street":street}})



def update_node_postcode():

    # Some nodes that have house number don't have post code. Since we want all nodes which have house number to have "street address",
    # "city", "state", "country", and "post code", we have to fill in "post code". By using "geopy" library to optain address from "geocode" API
    # knowing latitude and longitude, we can extract post code from there.
    
    import pymongo
    import unicodedata
    from pymongo import MongoClient
    from bson.objectid import ObjectId
    from geopy.geocoders import Nominatim
    client = MongoClient()
    db = client.examples
    geolocator = Nominatim()
    result = db.osm.test.find({"lat":{"$exists":True},"lon":{"$exists":True},
                               "tag.addr:housenumber":{"$exists":True},
                               "tag.addr:postcode":{"$exists":False},"$or":[
                               {"tag.addr:street":{"$exists":True}},
                               {"tag.addr:city":{"$exists":True}}]})
    for doc in result:
        i = doc["_id"]
        pos = doc["lat"] + "," + doc["lon"]
        location = geolocator.reverse(pos, timeout = 10)
        postcode = location.address.split(",")[-2].strip(" ")
        db.osm.test.update({"_id":i},{"$set":{"tag.addr:postcode":postcode}})    



def city_zip_mapping():

    # By using a downloaded list of cities in CA and its associated post code, a map is created to match zip code with its city
    # Link: http://www.zipcodestogo.com/California/
    
    import csv
    zip_city = "C:/Users/Long Nguyen/My-1st-Project/LAData/ziplistCA.csv"
    city_mapping = {}
    with open(zip_city, "r") as f:
        data = csv.reader(f)
        for line in data:
            key = line[0]
            value = line[1]
            city_mapping[key] = value
    return city_mapping


        
def update_node_city():

    # Some nodes that have house number don't have city. Since we want all nodes which have house number to have "street address",
    # "city", "state", "country", and "post code", we have to fill in "city". By using "geopy" library to optain address from "geocode" API
    # knowing latitude and longitude, we can extract post code from there. Then we can look up city from our mapping. By using a downlaoded
    # list, uodating process is easier because geopy tends to return full address and the position of "city" is not always the same.
    
    import pymongo
    import unicodedata
    from pymongo import MongoClient
    from bson.objectid import ObjectId
    from geopy.geocoders import Nominatim
    client = MongoClient()
    db = client.examples
    geolocator = Nominatim()
    city_mapping = city_zip_mapping()
    result = db.osm.test.find({"lat":{"$exists":True},"lon":{"$exists":True},
                               "tag.addr:housenumber":{"$exists":True},
                               "tag.addr:city":{"$exists":False}, "$or":[
                               {"tag.addr:street":{"$exists":True}},
                               {"tag.addr:postcode":{"$exists":True}}]})
    for doc in result:
        i = doc["_id"]
        pos = doc["lat"] + "," +doc["lon"]
        location = geolocator.reverse(pos, timeout = 10)
        postcode = location.address.split(",")[-2].strip(" ")
        new_postcode = unicodedata.normalize('NFKD', postcode).encode('ascii','ignore')
        if new_postcode in city_mapping.keys():
            city = city_mapping[new_postcode]
        else:
            city = ""
        db.osm.test.update({"_id":i},{"$set":{"tag.addr:city":street}})    



def update_node_full_address():

    # Once all nodes that have house number have "street address", "city", "state", "country", and "post code", we can create the field
    # "full address" by combining the components separated by comma. The fundction also group all components into a single dictionary callsed "address"

    import re
    import pymongo
    import pprint
    from pymongo import MongoClient
    from bson.objectid import ObjectId
    client = MongoClient()
    db = client.examples
    d = {}
    z = {}
    housenumber_re = re.compile(r"^[0-9]+\s[A-Za-z][A-Za-z]+")
    result = db.osm.test.find({"tag.addr:housenumber":{"$exists":True},"$or":[
                               {"tag.addr:street":{"$exists":True}},
                               {"tag.addr:city":{"$exists":True}},
                               {"tag.addr:postcode":{"$exists":True}}]})
    for doc in result:
        i = doc["_id"]
        if "addr:street" in doc["tag"].keys():
            street = doc["tag"]["addr:street"]
        else:
            street = ""
        if "addr:city" in doc["tag"].keys():
            city = doc["tag"]["addr:city"]
        else:
            city = ""
        if "timestamp" in doc.keys():
            timestamp = doc["timestamp"]
        else:
            timestamp = ""
        if "addr:postcode" in doc["tag"].keys():
            try:
                zipcode = int(doc["tag"]["addr:postcode"].strip("CA ").strip("Ca ").strip(",").split("-")[0])
            except ValueError:
                doczip = doc["tag"]["addr:postcode"]
                if housenumber_re.match(doczip):
                    zipcode = int(doczip.strip(",").split(",")[-2].strip(" CA "))
                else:
                    zipcode = ""
        else:
            zipcode = ""
        housenumber = doc["tag"]["addr:housenumber"]
        address = doc["tag"]["addr:housenumber"] + ", " + doc["tag"]["addr:street"] + ", " + doc["tag"]["addr:city"] + ", California, " + str(zipcode) + ", United States of America"
        db.osm.test.update({"_id":i},{"$set":{"address.full":address,
                                              "address.street":street,
                                              "address.housenumber":housenumber,
                                              "address.city":city,
                                              "address.state":"California",
                                              "address.country":"United States of America",
                                              "address.postcode":zipcode}})
        db.osm.test.update({"_id":i},{"$unset":{"tag.addr:full":"",
                                                "tag.addr:housenumber":"",
                                                "tag.addr:street":"",
                                                "tag.addr:city":"",
                                                "tag.addr:state":"",
                                                "tag.addr:country":"",
                                                "tag.addr:postcode":""}})




def clear_number_in_street_address():

    # Some street address include house numbers. We want to exclude the house number
    
    import pymongo
    from pymongo import MongoClient
    from bson.objectid import ObjectId
    client = MongoClient()
    db = client.examples
    d = {}
    result = db.osm.test.find({"address.housenumber":{"$exists":True},
                               "address.street":{"$exists":True}})
    for doc in result:
        i = doc["_id"]
        street = doc["address"]["street"].split(" ",1)
        try:
            int(street[0])
            if len(street) > 1:
                d[i] = street[1]
        except ValueError:
            continue
    for i in d:
        db.osm.test.update({"_id":i},{"$set":{"address.street":d[i]}})
    if d:
        del d



def create_mapping():

    # This function create a map of street types and their associated abbreviations using a downloaded file
    # Link: http://www.zip-codes.com/zip-code-database-faq-abbreviations.asp
    
    import csv
    file = "C:/Users/Long Nguyen/My-1st-Project/LAData/mapping.csv"
    mapping = {}
    with open(file, "r") as f:
        data = csv.reader(f)
        for line in data:
            key = line[0]
            value = [line[1],line[2]]
            mapping[key] = value
    return mapping


def update_node_street_type():

    # Using a street type abbreviation map, this function will look up all the explicitly spelled out street types and convert them to
    # abbreviated form. This is more effective since not enough information is provided to convert abbreviations to full street types
    
    import pprint
    import unicodedata
    from collections import defaultdict
    import pymongo
    from pymongo import MongoClient
    from bson.objectid import ObjectId
    client = MongoClient()
    db = client.examples
    street_type_list = {}
    d = {}
    update_street_type_list = {}
    mapping = {}
    result = db.osm.test.find({"address.housenumber":{"$exists":True},
                               "address.street":{"$exists":True}})
    for doc in result:
        i = doc["_id"]
        street_name = doc["address"]["street"]
        street_type = street_name.split(" ").pop()
        if len(street_type) > 2:
            try:
                int(street_type)
            except ValueError:
                street_type_list[i] = [street_type, street_name]
    streetmap = create_mapping()

    # COnvert street types to lower case for comparision
    
    for key in streetmap:
        name = key.lower()
        mapping[name] = streetmap[key]
    for objid in street_type_list:
        update_street_type_list[objid] = [street_type_list[objid][0].lower(), street_type_list[objid][1]]
    for objid in update_street_type_list:
        if update_street_type_list[objid][0] in mapping.keys():
            street_name = unicodedata.normalize('NFKD', update_street_type_list[objid][1]).encode('ascii','ignore')
            update_name = street_name.split(" ")
            update_name.pop()
            s = ""
            for word in update_name:
               s += word.strip(" ") + " "
            s = s + mapping[update_street_type_list[objid][0]][1].title()
            d[objid] = s
    for i in d:
        db.osm.test.update({"_id":i},{"$set":{"address.street":d[i]}})
    if d:
        del d


def update_node_house_number():

    # Some house numbers include street name or using different abbreviations for "Suite".
    # This function extract only house numbers. If "Ste" or "Sut" is found, they will be converted to "Suite"
    
    import re
    import pymongo
    from pymongo import MongoClient
    from bson.objectid import ObjectId
    db = client.examples
    d = {}
    result = db.osm.test.find({"address.housenumber":{"$exists":True}})
    suite_re = re.compile(r"ste|sut", re.IGNORECASE)
    housenumber_re = re.compile(r"^[0-9]+\s[A-Za-z][A-Za-z]+")
    for doc in result:
        i = doc["_id"]
        housenumber = doc["address"]["housenumber"]
        if housenumber_re.match(housenumber):
            if housenumber.find("Suite") == -1:
                number = housenumber.split(" ")[0]
                d[i] = number
                
        if suite_re.search(doc["address"]["housenumber"]):
                suite_number = housenumber.split(" ").pop()
                suite_name = housenumber.split(" ")[0] + " Suite " + suite_number
                d[i] = suite_name

    for i in d:
        db.osm.test.update({"_id":i},{"$set":{"address.housenumber":d[i]}})
    if d:
        del d



def update_node_structure():

    # This function will shape each document to follow a new data structure where "version", "changeset", "timestamp",
    # "user", and "uid" will be grouped into a single dictionary called "created". Also "lat" and "lon" are put together as a list
    # under the key name "pos"
    
    import pymongo
    from pymongo import MongoClient
    from bson.objectid import ObjectId
    client = MongoClient()
    db = client.examples
    result = db.osm.test.find()
    for doc in result:
        i = doc["_id"]
        if "version" in doc.keys():
            version = doc["version"]
        else:
            version = ""
        if "changeset" in doc.keys():
            changeset = doc["changeset"]
        else:
            changeset = ""
        if "timestamp" in doc.keys():
            timestamp = doc["timestamp"]
        else:
            timestamp = ""
        if "user" in doc.keys():
            user = doc["user"]
        else:
            user = ""
        if "uid" in doc.keys():
            uid = doc["uid"]
        else:
            uid = ""
        if ("lat" in doc.keys()) & ("lon" in doc.keys()):
            pos = [doc["lat"],doc["lon"]]
        else:
            pos = []
        db.osm.test.update({"_id":i},{"$set":{"created.version":version,
                                              "created.changeset":changeset,
                                              "created.timestamp":timestamp,
                                              "created.user":user,
                                              "created.uid":uid,
                                              "pos":pos}})
        db.osm.test.update({"_id":i},{"$unset":{"version":"",
                                                "changeset":"",
                                                "timestamp":"",
                                                "user":"",
                                                "uid":"",
                                                "lat":"",
                                                "lon":""}})


def combine():
    update_node_street()
    update_node_postcode()
    update_node_city()
    update_node_full_address()
    clear_number_in_street_address()
    update_node_street_type()
    update_node_house_number()
    update_node_structure()

    

