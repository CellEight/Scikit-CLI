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
                print(colored("[!] Looking to predict Structure? Tough Luck :( ", 'red'))
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
        print(colored("[*] Fitting Fitting Linear SVC...", "yellow"))
        # Display results
        if ask("[?] Are these results satisfactory?") == "yes":
            return model 
        else:
            if ask("[?] Are you working with text data?") == "yes":
                # fit Naive Bayes
                print(colored("[*] Fitting Naive Bayes Classifier...", "yellow"))
                # Display results
                return model 
            else:
                # fit KNN
                print(colored("[*] Fitting KNN Classifier...", "yellow"))
                # Display results
                if ask("[?] Are these results satisfactory?") == "yes":
                    return model
                else:
                    # fit SVC (ensamble) 
                    print(colored("[*] Fitting Fitting SVC Ensemble...", "yellow"))
                    return model
    else:
        print(colored("[*] Dataset contains ≥100k data points", "yellow"))
        print(colored("[*] Fitting SGD Classifier...", "yellow"))
        # fit SGD Classifer
        if ask("[?] Are these results satisfactory?") == "yes":
            return model
        else:
            #fit kernel approximation
            print(colored("[*] Fitting Kernel Approximation...", "yellow"))
            return model

def createCluster(df):
    """ Implements the logic in the clustering sub-graph of the cheat sheet """
    if ask("[?] Is the number of clusters known?") == "yes":
        k = int(ask("[?] How many clusters are present? ", list(range(1,101))))
        print(colored("[*] Checking size of dataset", "yellow"))
        if data.train.size < 1e4:
            print(colored("[*] Dataset contains <10k data points", "yellow"))
            # fit KMeans
            print(colored("[*] Performing KMeans Clustering...", "yellow")) 
            #display results
            if ask("[?] Are these results satisfactory?") == "yes":
                return model
            else: 
                # fit Spectral Clustering
                print(colored("[*] Performing Spectral Clustering...", "yellow")) 
                #display results
                if ask("[?] Are these results satisfactory?") == "yes":
                    return model
                else:
                    # fit GMM 
                    print(colored("[*] Performing Gaussian Mixture Model...", "yellow")) 
                    #display results
                    return model
        else:
            print(colored("[*] Dataset contains ≥10k data points", "yellow"))
            # fit Mini Batch KMeans
            print(colored("[*] Performing MiniBatch KMeans Clustering...", "yellow")) 
            # display results
            return model
    else:
        k = int(ask("[?] How many clusters are present? ", list(range(1,101))))
        print(colored("[*] Checking size of dataset", "yellow"))
        if data.train.size < 1e4:
            print(colored("[*] Dataset contains <10k data points", "yellow"))
            # fit Mean Shift
            print(colored("[*] Performing Mean Shift Clustering...", "yellow")) 
            #display results
            if ask("[?] Are these results satisfactory?") == "yes":
                return model
            else: 
                # fit VBGMM 
                print(colored("[*] Performing Variational Bayesian Gaussian Mixture Clustering...", "yellow")) 
                #display results
                return model
        else:
            print(colored("[*] Dataset contains ≥10k data points", "yellow"))
            print(colored("[!] Sorry too much data! Tough Luck :( ", 'red'))
            sys.exit(0)

        

def createRegressor(df):
    """ Implements the logic in the regression sub-graph of the cheat sheet """
    print(colored("[*] Checking size of dataset", "yellow"))
    if data.train.size < 1e5:
        print(colored("[*] Dataset contains <100k data points", "yellow"))
        # fit a linear SGD Regressor
        print(colored("[*] Fitting SGD Regressor...", "yellow")) 
        # display results
        return model
    else:
        print(colored("[*] Dataset contains ≥100k data points", "yellow"))
        if ask("[?] Should the model perform implicit feature selection?") == 'yes':
            # fit a Lasso 
            print(colored("[*] Fitting Lasso Regressor...", "yellow")) 
            # display results
            if ask("[?] Are these results satisfactory?") == "yes":
                return model
            else: 
                # fit Elastic Net
                print(colored("[*] Fitting ElasticNet...", "yellow")) 
                #display results
                return model
        else: 

def createDimReduce(df):
    pass

def fitAndValidate(model,data)
    X_train = data.train.drop(label, axis=1)
    y_train = data.train[label]
    X_test = data.test.drop(label,axis=1)
    y_test = data.test[label]

