"""
    Script for combining the dieharder test result 
"""

import os
import sys
import time

def read_file(file_name, remove_space):
    """
        read file from the folder
    """

    file_open = open(file_name, 'r')
    all_lines = file_open.readlines()
    file_open.close()
    if remove_space:
        for i in range(len(all_lines)):
            all_lines[i].replace(" ", "")

    all_lines = all_lines[9:]

    return all_lines

def combine_results(list_file, output_filename):
    """
        from the list of lines from read_file, add to file
    """
    
    list_lines      = map(lambda x: read_file(x, True), list_file[1:])
    original_line   = read_file(list_file[0], False)
    final_line      = [0 for x in range(len(original_line))]

    for lines in list_lines:
        for i in range(len(original_line)):
            try:
                temp_value = lines[i].split('|')[-1].split('\n')[0]

                if list_lines.index(lines) == 0:
                    final_line[i] = original_line[i].split('\n')[0] + '|  ' + ' '*(6 - len(temp_value)) + temp_value
                else:
                    final_line[i] += '|  ' + ' '*(6-len(temp_value)) + temp_value

                if list_lines.index(lines) == len(list_lines) - 1:
                    final_line[i] += '\n'
            except:
                pass

    original_line = final_line

    original_file = open(output_filename, 'a')
    
    for line in original_line:
        original_file.write(line)

    original_file.close()

def run_dieharder_test(input_file_name, output_file_name):
    """
        Run the dieharder tests
    """
    start = time.time()
    os.system("dieharder -a -g 202 -f %s > %s" % (input_file_name, output_file_name))
    stop = time.time()
    print 'Time taken to run ->', stop - start

def main_dieharder(final_file_name, list_of_input_file, list_of_output_file):
    for i in range(len(list_of_input_file)):
        print 'Dieharder test for file ->', i
        run_dieharder_test(list_of_input_file[i], list_of_output_file[i])
    
    print 'Combining results'
    combine_results(list_of_output_file, final_file_name)

if __name__ == "__main__":
    #list_file = ['../sta/ctr_data_0455_%i.txt'%(i) for i in range(2)]
    #file_name = '../sta/finale_result_sta.txt'
    
    #combine_results(list_file, file_name)
    
    # This is something like ~/ctr_data_0433 and
    num_of_file = int(sys.argv[1])
    base_input_file = sys.argv[2]
    base_output_file = sys.argv[3]

    final_file_name = sys.argv[4]

    list_of_input_file = [base_input_file + '_%i.txt' % (i) for i in range(num_of_file)]
    list_of_output_file = [base_output_file + '_%i.txt' % (i) for i in range(num_of_file)]

    print list_of_input_file

    main_dieharder(final_file_name, list_of_input_file, list_of_output_file)

