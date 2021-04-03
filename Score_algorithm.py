import json
import math
# simulated annealing global optimization for a multimodal objective function
from scipy.optimize import dual_annealing

class JSON_EDITOR:

    def __init__(self):
        #set json path
        self.json_path = '/home/brian/ec-552-hw1/input/Eco1C1G1T1.input (copy).json'
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
        add_string = '_sensor_model'
        name = "".join((input_signal, add_string))
        for i in range(self.max_json_index):
            if name in data[i]['name']:
                return i
        
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
        
    def Algorithm(self, input_signal):
        #Load Json file
        data = self.load_json()
        #get index value assosiated with input signal given
        index = self.get_index_from_input_signal(data, input_signal)
        #extract input signal parameters
        for param in data[index]['parameters']:
            #search for k and change value
            if param["name"] == 'ymax':
                ymax_og = param["value"]
                print("ymax_og "+str(ymax_og))
            if param["name"] == 'ymin':
                ymin_og = param["value"]
                print("ymin_og "+str(ymin_og))
            if param["name"] == 'alpha':
                n_og = param["value"]
                print("n_og "+str(n_og))
            if param["name"] == 'beta':
                k_og = param["value"]
                print("k_og "+str(k_og))
    
        # create negative response function to find global maxima and optmize for global maxima
        def objective(v):
            x,ymax,ymin,n,k = v
            return -(ymin_og*ymin+((ymax_og*ymax-ymin_og*ymin)/(1+((x/k_og*k) ** (n_og*n)))))
         
        # define range for parameters
        r_min, r_max = 0.01 , 20.0
        # define the bounds on the search
        bounds = [[r_min, r_max],[r_min, r_max],[r_min, r_max],[r_min, r_max],[r_min, r_max]]
        # perform the simulated annealing search
        result = dual_annealing(objective, bounds)
        # evaluate solution
        solution = result['x'] 
        evaluation = objective(solution)
        
        #retreive new parameters from optimized response function

        ymax_op = solution[1]*ymax_og
        ymin_op = solution[2]*ymin_og
        n_op = solution[3]*n_og
        k_op = solution[4]*k_og

        
        
        #Now we will use the operations given
        #to get as close as possible to the ideal response function calculated
        while n_og/1.05 > n_op:
            self.decrease_slope(input_signal, 1.05)
            n_og = n_og/1.05
                
        while n_og*1.05 < n_op:
            self.increase_slope(input_signal, 1.05)
            n_og = n_og*1.05
        
        if k_og > k_op:
            x = k_og/k_op
            self.Stronger_RBS(input_signal, x)
                
        if k_og < k_op:
            x = k_op/k_og
            self.Weaker_RBS(input_signal, x)

        
        while ymax_og*1.5 < ymax_op or ymin_og/1.5 > ymax_op:
            self.stretch(input_signal, 1.5)
            ymax_og = ymax_og*1.5
            ymin_og = ymin_og/1.5
