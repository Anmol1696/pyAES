# AES modification
Project in which AES is modified, basically cloned by changing the irreducible polynomial. We also use an extra key that is used to XOR with the plain text.<br>
We also benchmark my code of AES in python<br>
In benchmark we take the time taken to run for 1 block and for multiple blocks. We also run the `dieharder` test to compare the strengths of the above mentioned implementations

## NOTE
The python implementation of AES is 25 times slower then cython implementation of AES both my implementations<br>

# Installation
One will need to install the `numpy`. `json` is pre installed.<br>
Apart from this one also has to install dieharder test series version 3.31.1 and cython version 0.25.2<br>

For installing these just run the command:
```
    sudo pip instal numpy
    sudo apt-get install dieharder
```

# Testing AES code
Once the tables are formed one can run the testing script that will encrypt and decrypt single block and multiple blocks.<br>
For this we run the command:
```
    python -m testing.testing_algo
```
`modified_aes` points to my python implementation of AES which has an extra key in start that is used to mix the plain text<br>

A sample command and result as follows:
```
    python -m testing.testing_algo

    # On sucessful run one will get similar output
    Testing------
    Starting main_encrypt and main_decrypt......
    All Test passed
    Time taken for encrypting of size 32  is -> 0.00110292434692  seconds
    Time taken for encrypting of size 32768  is -> 0.444746017456  seconds
    Time taken for decrypting of size 32  is -> 0.000833034515381  seconds
    Time taken for decrypting of size 32768  is -> 0.646589994431  seconds
    End testing-----
    Time Taken 1 seconds
```
If this is not the output, it will say test failed which means there is something wrong

# Forming files for Dieharder tests
Once we have a working model of AES from any source we have to run Dieharder tests on it. For this we have to form txt files that have 32 bit random numbers with proper headers that are required for `dieharder`<br>
For this we need to convert the AES to ctr mode. This is done is `ctr_drbg/`. Also a text file is formed similar to `data/cython_aes_ctr.txt`<br>

The dieharder file that is formed is a binary file in txt form<br>

The file that runs this and forms the final file is `ctr_drgb/run_random_ctr.py`.<br>
We take the input from `ctr_drgb/ctr_input.json` which is of the form:-
```
    {
        "count" : 2500000,
        "number_of_files" : 1,
        "file_location" : "data/run_3/",
    }
```
Here the `count` is the number of block it has this is s.t. the file formed is around 378MB. This is good size for `dieharder` tests. `number_of_files` is the files for each txt for different IVs and Nonce. The Dieharder test should be run for different files for the same algo. Hence number of files is mentioned.<br>
`<file_location>` is the location of the directory where you want the data to be created. In the dir `data/`<br>

For this we run the command:
```
    python -m ctr_drbg.run_random_ctr <json file name>

    # For our case we run as our json file is as given bellow
    python -m ctr_drbg.run_random_ctr ctr_drbg/ctr_input.json
```

# Running the Dieharder tests
For this one has to run the scrit present in `src_for_result`. This will run the dieharder test on the files created by `ctr_drbg/`<br>
The command that is run for this is:-
```
    python -m src_for_result.combine_result <num of files> <base input file> <base output file> <final file name>
```
Here `<num of files>` is the no. of files for which the data is formed. This is the previous json entry `number_of_files` from `ctr_drbg/`.<br>
`<base input file>` and `<base output file>` are the base files for input and output for dieharder tests. To these base names `_%i.txt` if added and a list is name with `i` range from 0 to `<num of files>`<br>
`<final file name>` is the file where the dieharder tests for all the files will be conacatinated into one for easy visualization. Then `<num of files>` is 1, then there will be no final file formed as it would be identical to the output file<br>

The comand that I run was:
```
    python -m src_for_result.combine_result 1 data/ctr_data result/ctr_data result/final_ctr.txt
```

## NOTE
Time taken to run dieharder test for 1 file is aprox 90 mins. So for multiple files this might take some time<br>
