######################################################
#Name: Manisha
#student id : 21207194
#Objective : To acquire input json file from web using api and uploading it in mongodb nosql database using python
#######################################################

#installing required libraries
import pymongo
import json
import requests
import sys

#creating function to connect with mongodb
def connecting_to_mongodb():
    try:   
        print("**************************************")
        #creating connection parameters for mongodb
        dbPortNumber = '27017'  
        # Create a client to connect to host/server DB
        mongoClient = pymongo.MongoClient(f'mongodb://localhost:{dbPortNumber}')
        print("Connection created successfully")
        # Connect to database if exist, create db if it doesn't exist.
        mongoDB = mongoClient['dapDatabase']
        print("Database created successfully")
        # Create collection in the mongodb database for quarterly green house gas emission file
        qtrlyAirEmission = mongoDB['qtrlyAirEmission']
        print("qtrlyAirEmission collection created successfully")        
        # Create collection in the mongodb database for Co2 emission file
        co2Emission = mongoDB['co2Emission']
        print("co2Emission collection created successfully") 
        
    except Exception as e:
        print('Exception raised '+ str(e))
        print("Error in connection with mongo db!!!Please check!!")
        sys.exit(1)
    
def importing_json_to_mongodb():

    #trigerring json api to fetch inpout quarterly co2 emission file from web and saving it as a document in mongodb collection
    try:
        print("******************Starting api trigger to fetch the input file**********************")
        
        #response.request.get() method requests a web page and returns the status code
        response = requests.get('https://services9.arcgis.com/weJ1QsnbMYJlCHdG/arcgis/rest/services/Indicator_1_1_quarterly/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json')
        #reading the repsone of api in a list 
        listToWrite = response.json()
        count = 0
        offset = 0
        i=1;
        lisOfRecords = listToWrite['features']
        print("Iteration:"+str(i))
        for item in lisOfRecords:
            attr = item['attributes']
            attr['Country'] = str(attr['Country'])
            attr['ISO2'] = str(attr['ISO2'])
            attr['ISO3'] = str(attr['ISO3'])
            attr['Indicator'] = str(attr['Indicator'])
            attr['Unit'] = str(attr['Unit'])
            attr['Source'] = str(attr['Source'])
            attr['CTS_Code'] = str(attr['CTS_Code'])
            attr['CTS_Name'] = str(attr['CTS_Name'])
            attr['CTS_Full_Descriptor'] = str(attr['CTS_Full_Descriptor'])
            attr['Industry'] = str(attr['Industry'])
            attr['Gas_Type'] = str(attr['Gas_Type'])
            attr['Scale'] = str(attr['Scale'])
            attr['F2010Q1'] = str(attr['F2010Q1'])
            attr['F2010Q2'] = str(attr['F2010Q2'])
            attr['F2010Q3'] = str(attr['F2010Q3'])
            attr['F2010Q4'] = str(attr['F2010Q4'])
            attr['F2011Q1'] = str(attr['F2011Q1'])
            attr['F2011Q2'] = str(attr['F2011Q2'])
            attr['F2011Q3'] = str(attr['F2011Q3'])
            attr['F2011Q4'] = str(attr['F2011Q4'])
            attr['F2012Q1'] = str(attr['F2012Q1'])
            attr['F2012Q2'] = str(attr['F2012Q2'])
            attr['F2012Q3'] = str(attr['F2012Q3'])
            attr['F2012Q4'] = str(attr['F2012Q4'])
            attr['F2013Q1'] = str(attr['F2013Q1'])
            attr['F2013Q2'] = str(attr['F2013Q2'])
            attr['F2013Q3'] = str(attr['F2013Q3'])
            attr['F2013Q4'] = str(attr['F2013Q4'])
            attr['F2014Q1'] = str(attr['F2014Q1'])
            attr['F2014Q2'] = str(attr['F2014Q2'])
            attr['F2014Q3'] = str(attr['F2014Q3'])
            attr['F2014Q4'] = str(attr['F2014Q4'])
            attr['F2015Q1'] = str(attr['F2015Q1'])
            attr['F2015Q2'] = str(attr['F2015Q2'])
            attr['F2015Q3'] = str(attr['F2015Q3'])
            attr['F2015Q4'] = str(attr['F2015Q4'])
            attr['F2016Q1'] = str(attr['F2016Q1'])
            attr['F2016Q2'] = str(attr['F2016Q2'])
            attr['F2016Q3'] = str(attr['F2016Q3'])
            attr['F2016Q4'] = str(attr['F2016Q4'])
            attr['F2017Q1'] = str(attr['F2017Q1'])
            attr['F2017Q2'] = str(attr['F2017Q2'])
            attr['F2017Q3'] = str(attr['F2017Q3'])
            attr['F2017Q4'] = str(attr['F2017Q4'])
            attr['F2018Q1'] = str(attr['F2018Q1'])
            attr['F2018Q2'] = str(attr['F2018Q2'])
            attr['F2018Q3'] = str(attr['F2018Q3'])
            attr['F2018Q4'] = str(attr['F2018Q4'])
            attr['F2019Q1'] = str(attr['F2019Q1'])
            attr['F2019Q2'] = str(attr['F2019Q2'])
            attr['F2019Q3'] = str(attr['F2019Q3'])
            attr['F2019Q4'] = str(attr['F2019Q4'])
            attr['F2020Q1'] = str(attr['F2020Q1'])
            attr['F2020Q2'] = str(attr['F2020Q2'])
            attr['F2020Q3'] = str(attr['F2020Q3'])
            attr['F2020Q4'] = str(attr['F2020Q4'])
            attr['F2021Q1'] = str(attr['F2021Q1'])
            attr['F2021Q2'] = str(attr['F2021Q2'])
            attr['F2021Q3'] = str(attr['F2021Q3'])
            attr['F2021Q4'] = str(attr['F2021Q4'])
            attr['F2022Q1'] = str(attr['F2022Q1'])
            attr['F2022Q2'] = str(attr['F2022Q2'])
            #writing the records in file line by line in qtrlyAirEmission collection
            insertProcess = qtrlyAirEmission.insert_one(attr)
        count = count+1
    except Exception as e:
        print('Exception raised '+ str(e))
        print("Error in writing querterly air emission file in mongodb qtrlyAirEmission collection")
        sys.exit(1)
    
    try :
        print("******************Starting api trigger to fetch the input file**********************")
        
        #response.request.get() method requests a web page and returns the status code
        response = requests.get('https://services9.arcgis.com/weJ1QsnbMYJlCHdG/arcgis/rest/services/Indicator_2_Carbon_Emission_per_unit_of_Output/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json')
        #reading the repsone of api in a list
        listToWrite = response.json()
        count = 0
        offset = 0
        i=1;
        #
        while (listToWrite['exceededTransferLimit']):
            lisOfRecords = listToWrite['features']
            print("Iteration:"+str(i))
            for item in lisOfRecords:
                attr = item['attributes']
                attr['Country'] = str(attr['Country'])
                attr['ISO2'] = str(attr['ISO2'])
                attr['ISO3'] = str(attr['ISO3'])
                attr['Indicator'] = str(attr['Indicator'])
                attr['Unit'] = str(attr['Unit'])
                attr['Source'] = str(attr['Source'])
                attr['CTS_Code'] = str(attr['CTS_Code'])
                attr['CTS_Name'] = str(attr['CTS_Name'])
                attr['CTS_Full_Descriptor'] = str(attr['CTS_Full_Descriptor'])
                attr['Industry'] = str(attr['Industry'])
                attr['Scale'] = str(attr['Scale'])
                attr['F1995'] = str(attr['F1995'])
                attr['F1996'] = str(attr['F1996'])
                attr['F1997'] = str(attr['F1997'])
                attr['F1998'] = str(attr['F1998'])
                attr['F1999'] = str(attr['F1999'])
                attr['F2000'] = str(attr['F2000'])
                attr['F2001'] = str(attr['F2001'])
                attr['F2002'] = str(attr['F2002'])
                attr['F2003'] = str(attr['F2003'])
                attr['F2004'] = str(attr['F2004'])
                attr['F2005'] = str(attr['F2005'])
                attr['F2006'] = str(attr['F2006'])
                attr['F2007'] = str(attr['F2007'])
                attr['F2008'] = str(attr['F2008'])
                attr['F2009'] = str(attr['F2009'])
                attr['F2010'] = str(attr['F2010'])
                attr['F2011'] = str(attr['F2011'])
                attr['F2012'] = str(attr['F2012'])
                attr['F2013'] = str(attr['F2013'])
                attr['F2014'] = str(attr['F2014'])
                attr['F2015'] = str(attr['F2015'])
                attr['F2016'] = str(attr['F2016'])
                attr['F2017'] = str(attr['F2017'])
                attr['F2018'] = str(attr['F2018'])
                #writing the records in file line by line in co2Emission collection
                insertProcess = co2Emission.insert_one(attr)
                count = count+1
                print(count)
            offset = offset + 2000
            #response.request.get() method requests a web page and returns the status code
            response = requests.get('https://services9.arcgis.com/weJ1QsnbMYJlCHdG/arcgis/rest/services/Indicator_2_Carbon_Emission_per_unit_of_Output/FeatureServer/0/query?where=1%3D1&resultOffset='+str(offset)+'&outFields=*&outSR=4326&f=json')
            listToWrite = response.json()
            i = i+1
    except Exception as e:
        print(str(e))
        if ("'exceededTransferLimit'" in str(e)):
            lisOfRecords = listToWrite['features']
            print("Iteration:"+str(i))
            for item in lisOfRecords:
                attr = item['attributes']
                attr['Country'] = str(attr['Country'])
                attr['ISO2'] = str(attr['ISO2'])
                attr['ISO3'] = str(attr['ISO3'])
                attr['Indicator'] = str(attr['Indicator'])
                attr['Unit'] = str(attr['Unit'])
                attr['Source'] = str(attr['Source'])
                attr['CTS_Code'] = str(attr['CTS_Code'])
                attr['CTS_Name'] = str(attr['CTS_Name'])
                attr['CTS_Full_Descriptor'] = str(attr['CTS_Full_Descriptor'])
                attr['Industry'] = str(attr['Industry'])
                attr['Scale'] = str(attr['Scale'])
                attr['F1995'] = str(attr['F1995'])
                attr['F1996'] = str(attr['F1996'])
                attr['F1997'] = str(attr['F1997'])
                attr['F1998'] = str(attr['F1998'])
                attr['F1999'] = str(attr['F1999'])
                attr['F2000'] = str(attr['F2000'])
                attr['F2001'] = str(attr['F2001'])
                attr['F2002'] = str(attr['F2002'])
                attr['F2003'] = str(attr['F2003'])
                attr['F2004'] = str(attr['F2004'])
                attr['F2005'] = str(attr['F2005'])
                attr['F2006'] = str(attr['F2006'])
                attr['F2007'] = str(attr['F2007'])
                attr['F2008'] = str(attr['F2008'])
                attr['F2009'] = str(attr['F2009'])
                attr['F2010'] = str(attr['F2010'])
                attr['F2011'] = str(attr['F2011'])
                attr['F2012'] = str(attr['F2012'])
                attr['F2013'] = str(attr['F2013'])
                attr['F2014'] = str(attr['F2014'])
                attr['F2015'] = str(attr['F2015'])
                attr['F2016'] = str(attr['F2016'])
                attr['F2017'] = str(attr['F2017'])
                attr['F2018'] = str(attr['F2018'])
                #writing the records in file line by line in co2Emission collection
                insertProcess = co2Emission.insert_one(attr)
                count = count+1                

if __name__ == "__main__":
    
    try:
        print("*************Starting main function***************")
        print("*************Calling function for mongodb connection*******************")
        connecting_to_mongodb()
        print("*************Starting importing json file to mongodb database*******************")
        importing_json_to_mongodb()
    except Exception as e:
        print('Exception raised '+ str(e))
        print("Error in main function")
        sys.exit(1)
        