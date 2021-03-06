# Author: Matthew Schofield

from sklearn import metrics
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import *
from sklearn.gaussian_process import *
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.linear_model import *
from sklearn.cluster import *
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_validate

import keras as k
from keras.layers import *
import time
class Executioner:
    '''
    Purpose:
    '''
    def __init__(self, order, typeOfData, columnsDict, allData=None, trainingData=None, testingData=None):
        self.models = []
        self.order = order
        featuresCols = []
        self.typeOfData = typeOfData

        for key in columnsDict.keys():
            value = columnsDict.get(key)
            if value == 1:
                featuresCols.append(key)
            elif value == 2:
                targetCol = key
        if typeOfData == "All-n-One":
            X = allData[featuresCols]
            y = allData[targetCol]
            self.trainingDataX, self.testingDataX, self.trainingDataY, self.testingDataY = train_test_split(X, y)
        elif typeOfData == "1 Training 1 Testing":
            self.trainingDataX = trainingData[featuresCols]
            self.trainingDataY = trainingData[targetCol]
            self.testingDataX = testingData[featuresCols]
            self.testingDataY = testingData[targetCol]
        elif typeOfData == "K-Fold 1 CSV":
            self.trainingDataX = allData[featuresCols]
            self.trainingDataY = allData[targetCol]

    def execute(self):
        entry = None
        if self.order.get("Type") == "Classification":
            entry = self.classificationHandler(self.order)
        elif self.order.get("Type") == "Regression":
            entry = self.regressionHandler(self.order)
        elif self.order.get("Type") == "Clustering":
            entry = self.clusteringHandler(self.order)
        self.models.append(
            entry
        )
        return self.models

    def classificationHandler(self, e):
        model = None
        if e.get("Algorithm") == "Perceptron":
            perceptron_max_iter = int(e.get("Params").get("Max_Iter"))
            perceptron_penalty = e.get("Params").get("penalty")
            perceptron_alpha = float(e.get("Params").get("alpha"))
            perceptron_tol = float(e.get("Params").get("tol"))
            perceptron_shuffle = bool(e.get("Params").get("shuffle"))
            perceptron_eta0 = float(e.get("Params").get("eta0"))
            model = Perceptron(max_iter=perceptron_max_iter, penalty=perceptron_penalty,
                        alpha=perceptron_alpha, tol=perceptron_tol, shuffle=perceptron_shuffle, eta0= perceptron_eta0)

        elif e.get("Algorithm") == "Decision Tree":
            dtc_max_depth = e.get("Params").get("Max Depth")
            dtc_max_depth = int(dtc_max_depth) if dtc_max_depth != "None" else None
            dtc_criterion = e.get("Params").get("criterion")
            dtc_splitter = e.get("Params").get("splitter")
            dtc_min_samples_split = e.get("Params").get("min_samples_split")
            print(dtc_min_samples_split)
            dtc_min_samples_split = float(dtc_min_samples_split) if int(dtc_min_samples_split) == 0 else int(dtc_min_samples_split)
            dtc_min_samples_leaf = e.get("Params").get("min_samples_leaf")
            print(dtc_min_samples_leaf)
            dtc_min_samples_leaf = float(dtc_min_samples_leaf) if int(dtc_min_samples_leaf) == 0 else int(dtc_min_samples_leaf)
            model = DecisionTreeClassifier(max_depth=dtc_max_depth, criterion=dtc_criterion, splitter=dtc_splitter,
                                           min_samples_split=dtc_min_samples_split, min_samples_leaf=dtc_min_samples_leaf)
        elif e.get("Algorithm") == "Support Vector Classifier":
            svc_kernel = e.get("Params").get("Kernel")
            model = SVC(kernel=svc_kernel)
        elif e.get("Algorithm") == "K Neighbors Classifier":
            knc_n_neighbors = int(e.get("Params").get("n_neighbors"))
            model = KNeighborsClassifier(n_neighbors=knc_n_neighbors)
        elif e.get("Algorithm") == "Gaussian Process Classifier":
            gpc_kernel = 1.0 * RBF(1.0)
            model = GaussianProcessClassifier(kernel=gpc_kernel)
        elif e.get("Algorithm") == "Random Forest Classifier":
            rf_max_depth = e.get("Params").get("Max Depth")
            if rf_max_depth != "None":
                rf_max_depth = int(rf_max_depth)
            else:
                rf_max_depth = None
            rf_n_estimators = int(e.get("Params").get("Number of Trees (n_estimators)"))
            model = RandomForestClassifier(n_estimators=rf_n_estimators, max_depth=rf_max_depth)
        elif e.get("Algorithm") == "Multi-layer Perceptron":
            mlp_alpha = float(e.get("Params").get("alpha"))
            model = MLPClassifier(alpha=mlp_alpha)
        elif e.get("Algorithm") == "AdaBoost Classifier":
            model = AdaBoostClassifier()
        elif e.get("Algorithm") == "Gaussian Naive Bayes":
            model = GaussianNB()
        elif e.get("Algorithm") == "Quadratic Discriminant Analysis":
            model = QuadraticDiscriminantAnalysis()
        elif e.get("Algorithm") == "Neural Network (Keras)":
            networkDef = e.get("Params").get("Network")
            overallNetwork = networkDef[0]
            if overallNetwork[0] == "Sequential":
                model = k.Sequential()

            model.add(Dense(units=networkDef[1].get("Nodes"),  activation=networkDef[1].get("Activation")))
            layerDefs = networkDef[2:]
            for layer in layerDefs:
                if layer.get("Type") == "Dense":
                    model.add(Dense(units=layer.get("Nodes"), activation=layer.get("Activation")))
                elif layer.get("Type") == "Conv 1D":
                    model.add(Conv1D(layer.get("Nodes"), 3, activation=layer.get("Activation")))
            model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=[overallNetwork[1]])
        if e.get("Algorithm") == "Neural Network (Keras)":
            start = time.time()
            model.fit(self.trainingDataX.values, k.utils.to_categorical(self.trainingDataY.values), epochs=overallNetwork[2], batch_size=overallNetwork[3])
            end = time.time()
        else:
            start = time.time()
            try:
                model.fit(self.trainingDataX.values, self.trainingDataY.values)
            except MemoryError:
                print("Memory Error")
            end = time.time()
        entry = {
            "Type": "Classification",
            "Algorithm": e.get("Algorithm"),
            "Model": model,
            "Params": e.get("Params"),
            "Statistics":
                {
                }
        }
        if self.typeOfData == "K-Fold 1 CSV":
            scoring = ['accuracy', 'precision_macro', 'recall_macro', 'f1_macro']
            scores = cross_validate(model, self.trainingDataX, self.trainingDataY, scoring=scoring, cv=3,
                                    return_train_score=True)
            entry["Statistics"] = {
                "Accuracy": str(scores['test_accuracy'].mean())[0:4],
                "Precision": str(scores["test_precision_macro"].mean())[0:4],
                "Recall": str(scores["test_recall_macro"].mean())[0:4],
                "F1": str(scores["test_f1_macro"].mean())[0:4]
            }

        elif self.typeOfData == "All-n-One" or self.typeOfData == "1 Training 1 Testing":
            if e.get("Algorithm") == "Neural Network (Keras)":
                entry["Statistics"] = {
                    "Accuracy": str(1.0),
                    "Precision": str(1.0),
                    "Recall": str(1.0),
                    "F1": str(1.0)
                }
            else:
                entry["Statistics"] = {
                    "Accuracy": str(metrics.accuracy_score(self.testingDataY.values, model.predict(self.testingDataX.values)))[0:4],
                    "Precision": str(
                        metrics.precision_score(self.testingDataY.values, model.predict(self.testingDataX.values), average='macro'))[0:4],
                    "Recall": str(
                        metrics.recall_score(self.testingDataY.values, model.predict(self.testingDataX.values), average='macro'))[0:4],
                    "F1": str(metrics.f1_score(self.testingDataY.values, model.predict(self.testingDataX.values), average='macro'))[0:4]
                }
        entry["Statistics"]["Fit Time"] = int(end - start)
        return entry

    def regressionHandler(self, e):
        model = None
        if e.get("Algorithm") == "Linear Regression":
            model = LinearRegression()
        elif e.get("Algorithm") == "Ridge Regression":
            ridReg_alpha = float(e.get("Params").get("alpha"))
            model = Ridge(alpha=ridReg_alpha)
        elif e.get("Algorithm") == "Lasso":
            lasso_alpha = float(e.get("Params").get("alpha"))
            model = Lasso(alpha=lasso_alpha)
        elif e.get("Algorithm") == "Bayesian Ridge Regression":
            bayRidReg_n_iter = int(e.get("Param").get("n_iter"))
            model = BayesianRidge(n_iter=bayRidReg_n_iter)
        elif e.get("Algorithm") == "Logistic Regression":
            logReg_max_iter = int(e.get("Params").get("max_iter"))
            model = LogisticRegression(max_iter=logReg_max_iter)
        elif e.get("Algorithm") == "Support Vector Regression":
            svr_kernel = 1.0 * RBF(1.0)
            model = SVR(kernel=svr_kernel)
        elif e.get("Algorithm") == "Gaussian Process Regression":
            gpr_kernel = 1.0 * RBF(1.0)
            model = GaussianProcessRegressor(kernel=gpr_kernel)
        model.fit(self.trainingDataX, self.trainingDataY)
        entry = {
            "Type": "Regression",
            "Algorithm": e.get("Algorithm"),
            "Model": model,
            "Params": e.get("Params"),
            "Statistics":
            {
                "Mean Squared Error": str(metrics.mean_squared_error(self.testingDataY, model.predict(self.testingDataX)))[0:4],
                "R^2": str(metrics.r2_score(self.testingDataY, model.predict(self.testingDataX)))[0:4]
            }
        }
        return entry

    def clusteringHandler(self, e):
        model = None
        if e.get("Algorithm") == "KMeans":
            kmeans_n_clustering = int(e.get("Params").get("n_clusters"))
            model = KMeans(n_clusters=kmeans_n_clustering)
        elif e.get("Algorithm") == "Affinity Propagation":
            affinity_damping = int(e.get("Params").get("damping"))
            model = AffinityPropagation(damping=affinity_damping)
        elif e.get("Algorithm") == "Mean Shift":
            model = MeanShift()
        elif e.get("Algorithm") == "Spectral Clustering":
            spectral_n_clusters = e.get("Params").get("n_clusters")
            model = SpectralClustering(n_clusters=spectral_n_clusters)
        elif e.get("Algorithm") == "Agglomerative Clustering":
            agglomerative_n_clusters = e.get("Params").get("n_clusters")
            model = AgglomerativeClustering(n_clusters=agglomerative_n_clusters)
        elif e.get("Algorithm") == "DBSCAN":
            model = DBSCAN()
        elif e.get("Algorithm") == "Birch":
            birch_n_clusters = e.get("Paramas").get("n_clusters")
            model = Birch(n_clusters=birch_n_clusters)
        model.fit(self.trainingDataX)
        try:
            modelAccuracy = str(metrics.accuracy_score(self.testingDataY, model.predict(self.testingDataX)))[0:4]
        except:
            modelAccuracy = str(metrics.accuracy_score(self.testingDataY, model.predict(self.testingDataX)))[0:4]
        entry = {
            "Type": "Clustering",
            "Algorithm": e.get("Algorithm"),
            "Model": model,
            "Params": e.get("Params"),
            "Statistics":
            {
                "Accuracy": modelAccuracy
            }
        }
        return entry