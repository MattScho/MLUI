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


import time

class Executioner:
    '''
    Purpose:
    '''
    def __init__(self, order, typeOfData, columnsDict, allData=None, trainingData=None, testingData=None,):
        self.models = []
        self.order = order
        featuresCols = []
        self.typeOfData = typeOfData
        print(columnsDict)
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
            perceptron_fit_intercept = bool(e.get("Params").get("Fit_Intercept"))
            model = Perceptron(max_iter=perceptron_max_iter, fit_intercept=perceptron_fit_intercept)
        elif e.get("Algorithm") == "Decision Tree":
            dtc_max_depth = e.get("Params").get("Max Depth")
            dtc_max_depth = int(dtc_max_depth) if dtc_max_depth != "None" else None
            model = DecisionTreeClassifier(max_depth=dtc_max_depth)
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

        start = time.time()
        model.fit(self.trainingDataX, self.trainingDataY)
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
            scores = cross_validate(model, self.trainingDataX, self.trainingDataY, scoring=scoring, cv=3, return_train_score=True)
            entry["Statistics"] = {
                        "Accuracy": str(scores['test_accuracy'].mean())[0:4],
                        "Precision": str(scores["test_precision_macro"].mean())[0:4],
                        "Recall": str(scores["test_recall_macro"].mean())[0:4],
                        "F1": str(scores["test_f1_macro"].mean())[0:4]
                    }

        elif self.typeOfData == "All-n-One" or self.typeOfData == "1 Training 1 Testing":
            entry ["Statistics"] ={
                    "Accuracy": str(metrics.accuracy_score(self.testingDataY, model.predict(self.testingDataX)))[0:4],
                    "Precision": str(metrics.precision_score(self.testingDataY, model.predict(self.testingDataX), average='macro'))[0:4],
                    "Recall": str(metrics.recall_score(self.testingDataY, model.predict(self.testingDataX), average='macro'))[0:4],
                    "F1": str(metrics.f1_score(self.testingDataY, model.predict(self.testingDataX), average='macro'))[0:4]
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

        start = time.time()
        model.fit(self.trainingDataX, self.trainingDataY)
        end = time.time()
        entry = {
            "Type": "Regression",
            "Algorithm": e.get("Algorithm"),
            "Model": model,
            "Params": e.get("Params"),
        }
        if self.typeOfData == "K-Fold 1 CSV":
            scoring = ['neg_mean_squared_error']
            scores = cross_validate(model, self.trainingDataX, self.trainingDataY, scoring=scoring, cv=3,
                                    return_train_score=True)
            entry["Statistics"] = {
                "Mean Squared Error": str(-1*scores['test_neg_mean_squared_error'].mean())[0:4],
            }

        elif self.typeOfData == "All-n-One" or self.typeOfData == "1 Training 1 Testing":
            entry["Statistics"] = {
                "Mean Squared Error":str(-1*metrics.neg_mean_squared_error(self.testingDataY, model.predict(self.testingDataX)))[0:4]
            }
        entry["Statistics"]["Fit Time"] = int(end-start)
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


