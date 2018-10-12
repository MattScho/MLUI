import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import perceptron
import pandas as pd
import pickle

def perceptronF(inFile, max_iter, fit_intercept):
    inp = pd.read_csv(inFile)
    inpVal = inp.values
    inpVal = inpVal.transpose()

    d = inpVal[0:2]

    t = inpVal[2]

    colormap = np.array(['r', 'k'])
    plt.scatter(d[0], d[1], c=colormap[t], s=40)

    d90 = np.rot90(d)
    d90 = np.rot90(d90)
    d90 = np.rot90(d90)
    
    net = perceptron.Perceptron(max_iter=max_iter, verbose=0, random_state=None, fit_intercept=fit_intercept, eta0=0.002)
    net.fit(d90, t)

    #pickle.dump(net, open(outFile, 'wb'))
    # Print the results
    print("Prediction " + str(net.predict(d90)))

    print("Actual     " + str(t))

    print("Accuracy   " + str(net.score(d90, t) * 100) + "%")

    res = {
        "Type": "Classification",
        "Algorithm": "Perceptron",
        "Model": net,
        "Statistics":
            {

            }
    }

    return res
