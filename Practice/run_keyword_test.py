import csv
from selenium import webdriver
from keyword_library import KeywordLibrary

def run_test(csv_file):
    driver = webdriver.Chrome()
    keywords =KeywordLibrary(driver)
    
    #Open and/or read the csv file
    with open(csv_file, newline="") as file:
        reader = csv.DictReader(file)
        #Create a loop through each row in the csv
        for row in reader:
            keyword = row["Keyword"]
            locator_type = row["LocatorType"]
            locator_value = row["LocatorValue"]
            data = row["Data"]
            #Check the existence of the method in the KeywordLibrary
            if hasattr(keywords,keyword): #hasattr-checks if the classs contains a method like the keyword
                method = getattr(keywords,keyword) #getattr-gets the actual function so that we can call it later
                #Conditional method calling
                if locator_type and locator_value and data:
                    method(locator_type,locator_value,data)
                elif locator_type and locator_value:
                    method(locator_type,locator_value)
                elif data:
                    method(data)
                else:
                    method()
            else:
                print(f" Keyword is unknown: {keyword}")
    driver.quit()
if __name__ =="__main__":
    run_test("loginKeys.csv")