#!/bin/python3
from termcolor import colored
import sys
# To start with I'll just implement the logic of the chart without the processing aspect
# Parse CLI directives
# Print informative banner
# Load data from speicifed pkl file

def scikitCheat(data):
    """ Implements the logic of the scikit-learn algorithmic cheat sheet which can be found at
        https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html """ 
    # Check that the dataframe contains >50 entries
    print(colored("[*] Checking size of dataset", "yellow"))
    if data.train.size > 50:
        print(colored("[~] Dataset contains >50 data points", "green"))
    else:
        print(coloured("[!] Not enough data! <50 data points, please gather more data"))
        if ask("[?] Continue Anyway?") != "yes":
            print("[*] Exiting...")
            sys.exit(0)
    # Categorical?
    if ask("[?] Do you want to predict categorical label?") == "yes":
        # Categorical Path
        if ask("[?] Is data labelled?") == "yes":
            # Classification Path
            # >>> ask which is the label
            model = createClassifer(data,label)
        else:
            # Clustering Path
            model = createCluster(df)
    else:
        if ask("[?] Do you want to predict a quantity?") == "yes":
            # Regression Path
            model = createRegressor(df)
        else:
            if ask("[?] Just looking/want to do dimensionality reduction?") == "yes":
                # Dimensionality Reduction Path
                model = createDimReduce(df)
            else:
                print("[*] Looking to predict Structure? Tough Luck :( ")
                sys.exit(0)


def ask(msg, valid=['yes','no']):
    """ Automate the process of asking for user input from a limited set of options """
    response = ''
    while response not in valid:
        response = input(colored(msg+" ["+"/".join(valid)+"]: ", "orange")).strip().lower()
    return response

def createClassifer(data,label):
    """ Implements the logic in the classification sub-graph of the cheat sheet """
    print(colored("[*] Checking size of dataset", "yellow"))
    if data.train.size < 1e5:
        print(colored("[*] Dataset contains <100k data points", "yellow"))
        # fit a linear SVC
        # Display results
        if ask("[?] Are these results satisfactory?") == "yes":
            return model 
        else:
            if ask("[?] Are you working with text data?") == "yes":
                # fit Naive Bayes
                # Display results
                return model 
            else:
                # fit KNN
                # Display results
                if ask("[?] Are these results satisfactory?") == "yes":
                    return model
                else:
                    # fit ensemble
                    return model
    else:
        print(colored("[*] Dataset contains ≥100k data points", "yellow"))
        # fit SGD Classifer
        if ask("[?] Are these results satisfactory?") == "yes":
            return model
        else:
            #fit kernel approximation
            return model

def createCluster(df):
    pass

def createRegressor(df):
    pass

def createDimReduce(df):
    pass

def fitAndValidate(model,data)
    X_train = data.train.drop(label, axis=1)
    y_train = data.train[label]
    X_test = data.test.drop(label,axis=1)
    y_test = data.test[label]

