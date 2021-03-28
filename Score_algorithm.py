import json
import math

class JSON_EDITOR:

    def __init__(self):
        #set json path
        self.json_path = '/home/brian/ec-552-hw1/input/Eco1C1G1T1.input (copy)json'
        self.max_json_index = 17

    def load_json(self):
        #open json file and load data 
        f = open(self.json_path, "r")
        data=json.load(f)
        f.close()
        return data
    
    def write_json(self, data):
        #open json file and write to json file
        f = open(self.json_path, "w+")
        f.write(json.dumps(data))
        f.close()
        
    def get_index_from_input_signal(self, data, input_signal):
        if input_signal == 'LacI':
            name = 'LacI_sensor_model'
            for i in range(self.max_json_index):
                if name in data[i]['name']:
                    return i
        elif input_signal == 'TetR':
            name = 'TetR_sensor_model'
            for i in range(self.max_json_index):
                if name in data[i]['name']:
                    return i
        elif input_signal == 'AraC':
            name = 'AraC_sensor_model'
            for i in range(self.max_json_index):
                if name in data[i]['name']:
                    return i
        elif input_signal =='LuxR':
            name = 'LuxR_sensor_model'
            for i in range(self.max_json_index):
                if name in data[i]['name']:
                    return i
        else:
            print("The signal inputs do not match Ecol1.input.json")
            return None
        
    def stretch(self, input_signal, x):
        #load json and get index value for given input signal
        data = self.load_json()
        index = self.get_index_from_input_signal(data, input_signal)
        for param in data[index]['parameters']:
            #search for ymax and change value
            if param["name"] == 'ymax':
                ymax = param["value"]
                ymax_new = ymax*x
                param["value"] = ymax_new
            #search for ymin and change value   
            if param["name"] == 'ymin':
                ymin = param["value"]
                ymin_new = ymin/x
                param["value"] = ymin_new
                
        self.write_json(data)

    def increase_slope(self, input_signal, x):
        data = self.load_json()
        index = self.get_index_from_input_signal(data, input_signal)
        
        for param in data[index]['parameters']:
            #search for n and change value
            if param["name"] == 'alpha':
                n = param["value"]
                n_new = n*x
                param["value"] = n_new
                
        self.write_json(data)
        
    
    def decrease_slope(self, input_signal, x):
        data = self.load_json()
        index = self.get_index_from_input_signal(data, input_signal)
        
        for param in data[index]['parameters']:
            #search for n and change value
            if param["name"] == 'alpha':
                n = param["value"]
                n_new = n/x
                param["value"] = n_new
                
        self.write_json(data) 
    
    def Stronger_Promoter(self, input_signal, x):
        data = self.load_json()
        index = self.get_index_from_input_signal(data, input_signal)
        
        for param in data[index]['parameters']:
            #search for ymax and change value
            if param["name"] == 'ymax':
                ymax = param["value"]
                ymax_new = ymax*x
                param["value"] = ymax_new
            #search for ymin and change value   
            if param["name"] == 'ymin':
                ymin = param["value"]
                ymin_new = ymin*x
                param["value"] = ymin_new
                
        self.write_json(data)
    
    def Weaker_Promoter(self, input_signal, x):
        data = self.load_json()
        index = self.get_index_from_input_signal(data, input_signal)
        
        for param in data[index]['parameters']:
            #search for ymax and change value
            if param["name"] == 'ymax':
                ymax = param["value"]
                ymax_new = ymax/x
                param["value"] = ymax_new
            #search for ymin and change value   
            if param["name"] == 'ymin':
                ymin = param["value"]
                ymin_new = ymin/x
                param["value"] = ymin_new
                
        self.write_json(data)
    
    def Stronger_RBS(self, input_signal, x):
        data = self.load_json()
        index = self.get_index_from_input_signal(data, input_signal)
        
        for param in data[index]['parameters']:
            #search for k and change value
            if param["name"] == 'beta':
                k = param["value"]
                k_new = k/x
                param["value"] = k_new
                
        self.write_json(data) 
    
    def Weaker_RBS(self, input_signal, x):
        data = self.load_json()
        index = self.get_index_from_input_signal(data, input_signal)
        
        for param in data[index]['parameters']:
            #search for k and change value
            if param["name"] == 'beta':
                k = param["value"]
                k_new = k*x
                param["value"] = k_new
                
        self.write_json(data)
        
    #def Algorithm(self, input_signal, x, score, prev_score)
    
        