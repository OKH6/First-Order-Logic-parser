# First-Order-Logic-parser

## Requirements:

Please download the executable Stable 2.38 Windows install 
packages to install Graphviz2.38 from this link:
https://graphviz.gitlab.io/download/ 
and follow the instructions on this page:
https://bobswift.atlassian.net/wiki/spaces/GVIZ/pages/20971549/How+to+install+Graphviz+software

After that you would need to install pydot package by typing “pip install pydot” 
on the command line and that’s it for the Requirements.



## Usage:

1. Please place program file and the input file you want to use in same folder.  
2. Open terminal in the program directory.
3. Then you can use the program by entering the following command :
```
python Parser.py inputFileName.txt
```
   of course you will have to change the inputFileName to your input file name. Also if you 
   want to see the steps that are happening in the stack you can add the argument show to see what’s happening at each step like this:
```
python Parser.py inputFileName.txt show
```
### Input File format

The input file should include:

- The Language of the First order logic, including:
  - A set of variables
  - A set of constants
  - A set of predicates
  - The equality symbol
  - The set of logical connectives
- The description of a (possibly non-valid) FO formula

refer to example input file
 
 
 
 
## Output Files:

When you run the program, it will output the following files in the same folder:

1. Production rules.txt: this file will contain the relevant grammar to the 
   input file you have given. There is an example of what this file could look 
   like called Production_rules_Example.txt in the folder example, this 
   example is generated from the input file example.txt in the same folder

2. LogFile.txt: this file will contain results of the execution of the program, 
   like it will indicate if everything executed correctly or if there are any 
   errors. There is an example of this file in the folder example that is 
   generated from the input file example.txt in the same folder, these will 
   also be printed on the command line
3. parse_tree.png: this file contains an image of the final parse tree. There 
   is an example of this file in the folder example it is generated from the 
   input file example.txt in the same folder following the grammar in 
   Parse_tree_Example.txt
   
   
   
   
## Types of errors handled:
In input file:
1. ensures the sets of equality, connectives, and quantifiers always have 1, 5, and 2 elements respectively. 
2. ensures no two symbols have the same name except in the formula e.g no variable called X and a predicate called X[2]
3. ensures that connectives and quantifiers contain Any nonempty string of letters, numbers, underscore and backslash.
4. ensures that user have entered a file name
5. ensures that equality symbol contain Any nonempty string of letters, numbers, underscore, backslash and =.
6. ensures that the input file doesn’t contain any non-terminals
7. any invalid formula that does not follow the rules will result in an errormessage. The parser will tell you at which position the error occurred and the cause of the error. 
