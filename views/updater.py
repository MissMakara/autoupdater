import os
import requests
import json
import os
from flask_restful import Resource
#import wget
import zipfile
import io
from io import BytesIO
import filecmp
from difflib import Differ

class Configs():
    def __init__(self):
        self.config_file = []
        self.tunea =[]
        self.tuneb=[]
        self.link=""

class Updater(Resource):
    def get(self):
        status = self.run()
        return status

    def compare(self, new, old,items):

        for index, elem in enumerate(new):
            for index2, elem2 in enumerate(old):
                for item in items:
                    if item in elem and item in elem2:
                        print(item)
                        print(elem)
                        print(elem2)
                        
                        new[index] = elem2
        
                        #new[index]= elem2[index2]

        print(new)
        return new

    def create(self, data, name):
        with open(name, 'w+',encoding="utf8") as file:
            file.writelines(place for place in data)
        return 
        

    def attach(self, path, file):
        innerpath = os.path.join(path,file)
        with open(innerpath, 'r', encoding="utf8") as file1:
            data = file1.readlines()
        
        return data

    def run(self):
        try:
            old_configs = Configs()
            new_configs = Configs()
            new_configs.link ="link/to/new/file"
            old_configs.link = "link/to/old/file"
            items =["setting","time","device_id"]
            
            old_configs.config_file=self.attach(old_configs.link,'conf/config.cfg')
            new_configs.config_file = self.attach(new_configs.link,'conf/config.cfg')


            config_output = self.compare(new_configs.config_file, old_configs.config_file,items)
            self.create(config_output, 'new_files/new_config.cfg')


            return "Success"

        except Exception as e:
            print("Error {}".format(e))
            return "Error {}".format(e)
   
