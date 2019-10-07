
L : No of iterations to continue the pruning to a threshold value to avoid complexity
	(if the number of attributes is given for L then, reduced error pruning can be implemented fully)
k : a random value to determine the range of random values to be taken for reduced error pruning

how to run the code of decision tree:
-------------------------------------

python main.py train_set_path validation_set_path test_set_path yes/no heuristic pruning L K

yes/ no ---- yes for printing the tree and no for not printing the tree

heuristic = 'e' or 'v'  ----- 'e' for entropy and 'v' for variance 

pruning = 'n' or 'r' ------ 'n' for no pruning and 'r' for reduced error pruning

L - integer value

K - Integer value

example command to run the code
-------------------------------

python main.py train_c300_d100.csv valid_c300_d100.csv test_c300_d100.csv yes e r 7 2 


how to run the code of random forest
-------------------------------------

python Random_Forests.py training_set validation_set test_set


example command to run
----------------------

python Random_Forests.py train_c300_d100.csv valid_c300_d100.csv test_c300_d100.csv
