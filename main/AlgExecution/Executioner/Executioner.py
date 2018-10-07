from main.Algorithms.Perceptron import perceptronF
from main.Algorithms.DecisionTree import decisionTreeF
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

class Executioner:
    def __init__(self, listToExecute, dataFrame, typeOfData):
        self.models = []

        self.listToExecute = listToExecute
        if typeOfData == "CSV with Data and Labels":
            self.dataX = dataFrame[dataFrame.columns[:-1]]
            if len(self.dataX.columns) == 2:
                self.twoDData = True
            else:
                self.twoDData = False

            self.dataY = dataFrame[dataFrame.columns[-1]]
            labels = []
            self.binaryOut = True
            for label in self.dataY:
                if not(label in labels):
                    if len(labels) < 2:
                        labels.append(label)
                    else:
                        self.binaryOut = False
                        break


            print(self.dataX)
            print("\n Y:" + str(self.dataY))

    def execute(self):
        for e in self.listToExecute:
            entry = None
            if e.get("Type") == "Classification":
                entry = self.classificationHandler(e)
            elif e.get("Type") == "Regression":
                entry = self.regressionHandler(e)
            elif e.get("Type") == "Clustering":
                entry = self.clusteringHandler(e)
            print("Entry " + str(entry))
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
            gpc_kernel = None
            if e.get("Params").get("Kernel") == "rbf":
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
        model.fit(self.dataX, self.dataY)
        entry = {
            "Type": "Classification",
            "Algorithm": e.get("Algorithm"),
            "Model": model,
            "Statistics":
            {
                "Accuracy": str(metrics.accuracy_score(self.dataY, model.predict(self.dataX)))[0:4]
            }
        }
        if self.binaryOut:
            entry["Statistics"]["Precision"] = str(metrics.precision_score(self.dataY, model.predict(self.dataX)))[0:4]
            entry["Statistics"]["Recall"] = str(metrics.recall_score(self.dataY, model.predict(self.dataX)))[0:4]
            entry["Statistics"]["F1"] = str(metrics.f1_score(self.dataY, model.predict(self.dataX)))[0:4]

        return entry

    def regressionHandler(self, e):
        model = None
        if e.get("Algorithm") == "Linear Regression":
            model = LinearRegression()
        elif e.get("Algorithm") == "Ridge Regression":
            model = Ridge()
        elif e.get("Algorithm") == "Lasso":
            model = Lasso()
        elif e.get("Algorithm") == "Bayesian Ridge Regression":
            model = BayesianRidge()
        elif e.get("Algorithm") == "Logistic Regression":
            model = LogisticRegression()
        elif e.get("Algorithm") == "Support Vector Regression":
            model = SVR()
        elif e.get("Algorithm") == "Gaussian Process Regression":
            model = GaussianProcessRegressor()
        model.fit(self.dataX, self.dataY)
        entry = {
            "Type": "Regression",
            "Algorithm": e.get("Algorithm"),
            "Model": model,
            "Statistics":
            {
                "Mean Squared Error": str(metrics.mean_squared_error(self.dataY, model.predict(self.dataX)))[0:4],
                "R^2": str(metrics.r2_score(self.dataY, model.predict(self.dataX)))[0:4]
            }
        }
        return entry

    def clusteringHandler(self, e):
        model = None
        if e.get("Algorithm") == "KMeans":
            model = KMeans()
        elif e.get("Algorithm") == "Affinity Propagation":
            model = AffinityPropagation()
        elif e.get("Algorithm") == "Mean Shift":
            model = MeanShift()
        elif e.get("Algorithm") == "Spectral Clustering":
            model = SpectralClustering()
        elif e.get("Algorithm") == "Agglomerative Clustering":
            model = AgglomerativeClustering()
        elif e.get("Algorithm") == "DBSCAN":
            model = DBSCAN()
        elif e.get("Algorithm") == "Birch":
            model = Birch()
        model.fit(self.dataX)
        try:
            modelAccuracy =  str(metrics.accuracy_score(self.dataY, model.predict(self.dataX)))[0:4]
        except:
            modelAccuracy = str(metrics.accuracy_score(self.dataY, model.fit_predict(self.dataX)))[0:4]
        entry = {
            "Type": "Clustering",
            "Algorithm": e.get("Algorithm"),
            "Model": model,
            "Statistics":
            {

                    "Accuracy": modelAccuracy
            }
        }
        return entry

