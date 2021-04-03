#Written by Brian Mahabir and Landon Kushimi using the Cello template code
import math
import sys
from os import listdir
from os.path import isfile, join
from itertools import combinations
from celloapi2 import CelloQuery, CelloResult
import Score_algorithm as SA 
# Set our directory variables. If you have a Windows based
# operating system you need to input window based paths.
in_dir = '/home/brian/ec-552-hw1/input'
out_dir = '/home/brian/ec-552-hw1/output'

# get all filenames in the input directory and put them in a list
onlyfiles = [f for f in listdir("/home/brian/ec-552-hw1/input") if isfile(join("/home/brian/ec-552-hw1/input", f))]
#ask user to input file with error checking
while True:
    v_file_input = input("enter verilog file with .v you want to optimize\n")
    if v_file_input in onlyfiles:
        v_file = v_file_input
        signal_input_number = input("enter the number of inputs for the verilog file ")
        signal_input = int(signal_input_number)
        break
    elif v_file_input == 'q':
        print("you have quit")
        sys.exit(5)
    else :
        print(v_file_input + " not a valid input try again if you want to quit press q")

options = 'options.csv'

#Change this to check a different ucf file
chassis_name = ['Eco1C1G1T1']

best_score = 0
best_chassis = None
best_input_signals = None

# find best score without optimize for finding what input_signasl are best for
for chassis in chassis_name:
    in_ucf = f'{chassis}.UCF.json'
    input_sensor_file = f'{chassis}.input (copy).json'
    output_device_file = f'{chassis}.output.json'
    q = CelloQuery(
        input_directory=in_dir,
        output_directory=out_dir,
        verilog_file=v_file,
        compiler_options=options,
        input_ucf=in_ucf,
        input_sensors=input_sensor_file,
        output_device=output_device_file,
    )
    signals = q.get_input_signals()
    signal_pairing = list(combinations(signals, signal_input))
    for signal_set in signal_pairing:
        signal_set = list(signal_set)
        q.set_input_signals(signal_set)
        q.get_results()
        try:
            #this code gets the data from the output
            res = CelloResult(results_dir=out_dir)
            if res.circuit_score > best_score:
                #Algorithmn
                best_score = res.circuit_score
                best_chassis = chassis
                best_input_signals = signal_set
        except:
            pass
        q.reset_input_signals()
    print('-----')
print(f'Best Score unoptimized: {best_score}')
print(f'Best Chassis unoptimzed: {best_chassis}')
print(f'Best Input Signals unoptimized: {best_input_signals}')

# Second round optimize
#Set variables to be used
old_score = best_score
best_score_op = 0
#instantiate class that will edit json file and do the algo
json_master=SA.JSON_EDITOR()
    

#Algorithmn
#loop for as many inputs given
for i in range(signal_input):
    json_master.Algorithm(best_input_signals[i])
#get results after the algo has edited the json file we want to check this more than once
#and get the best score since cello has random scores
in_ucf = f'{chassis}.UCF.json'
input_sensor_file = f'{chassis}.input (copy).json'
output_device_file = f'{chassis}.output.json'
q = CelloQuery(
    input_directory=in_dir,
    output_directory=out_dir,
    verilog_file=v_file,
    compiler_options=options,
    input_ucf=in_ucf,
    input_sensors=input_sensor_file,
    output_device=output_device_file,
)
for i in range(20):
    q.set_input_signals(best_input_signals)
    q.get_results()
    try:
        #this code gets the data from the output
        res = CelloResult(results_dir=out_dir)
        if res.circuit_score > best_score_op:
            best_score_op = res.circuit_score
            #best_chassis = chassis
            #best_input_signals = signal_set
    except:
        pass
    q.reset_input_signals()

print('-----')
print(f'Best Score optimized: {best_score_op}')
delta = best_score_op-old_score
print('Delta '+str(delta))