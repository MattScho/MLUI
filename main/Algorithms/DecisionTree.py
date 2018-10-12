from sklearn import tree
import pickle
import pandas as pd

def decisionTreeF(inFile, max_depth):
    if max_depth == "None":
        max_depth = None
    else:
        max_depth = int(max_depth)

    inp = pd.read_csv(inFile)
    inpVal = inp.values
    X = inpVal
    inpVal = inpVal.transpose()
    Y = inpVal[2]
    clf = tree.DecisionTreeClassifier(max_depth=max_depth)
    clf = clf.fit(X, Y)
    res = {
        "Type": "Classification",
        "Algorithm": "Decision Tree",
        "Model": clf,
        "Statistics":
            {

            }
    }

    return res