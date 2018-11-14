from enum import Enum

'''
Each algorithm is stored as a dict
{
    AlgName: <String> Algorithm name
    Types: <String> (Clustering, Regression, Classification,...)
    Simple Description: <String> Describes the algorithm to someone with mild to no experience in ML
    Advanced Description:<String> Describes the algorithm to someone with a good amount of experience in ML
    Keywords: <String[]> For search functionality
    Simple Parameters: [
         {
            ParamName: <String> name of the parameter
            Type: <String> describes type of data (int, Boolean, String, Strings, etc.)
            Default: <type> default input
            Simple Description: <String> (see above, but as applied to the parameter)
            Advanced Description: <String> (see above, but as applied to the parameter)
        },
        …
    ]
    Advanced Parameters: [
        {
            ParamName: <String> name of the parameter
            Type: <String> describes type of data (int, Boolean, String, Strings, etc.)
            Default: <type> default input
            Simple Description: <String> (see above, but as applied to the parameter)
            Advanced Description: <String> (see above, but as applied to the parameter)
        }
    ]
}
'''
class Algorithm(Enum):

    # CLASSIFICTION
    PERCEPTRON = {
                "AlgName": "Perceptron",
                "Type": "Classification",
                "Simple Description": "",
                "Advanced Description": "",
                "Keywords": [

                ],
                "Simple Parameters": [
                    {
                        "ParamName": "Max_Iter",
                        "Type": "int",
                        "Default": "1000",
                        "Simple Description": "The maximum number of passes over the training data.\n "
                                              "This is incase the data is not linearly seperable as \n"
                                              "otherwise the algorithm would enter an infinite loop.\n"
                                              "Too high and it will take longer, but will not negatively effect the model.\n"
                                              "Too low and the model may be inaccurate",
                        "Advanced Description": "Maximum number of epochs\n"
                    },

                ],
                "Advanced Parameters":[
                    {
                        "ParamName": "penalty",
                        "Type": "options",
                        "Default": ["None","l2", "l1", "elasticnet"],
                        "Advanced Description": "The penalty (aka regularization term) to be used."
                    },
                    {
                        "ParamName": "alpha",
                        "Type": "float",
                        "Default": 0.0001,
                        "Advanced Description": "Constant that multiplies the regularization term if regularization is used. "
                    },
                    {
                        "ParamName": "tol",
                        "Type": "float",
                        "Default": 1e-3,
                        "Advanced Description": "The stopping criterion. If it is not None, the iterations will stop when (loss > previous_loss - tol). "
                    },
                    {
                        "ParamName": "shuffle",
                        "Type": "bool",
                        "Default": True,
                        "Advanced Description": "Whether or not the training data should be shuffled after each epoch."
                    },
                    {
                        "ParamName": "eta0",
                        "Type": "double",
                        "Default": 1,
                        "Advanced Description": "Constant by which the updates are multiplied."
                    },
                ]
            }
    DECISION_TREE = {
                "AlgName": "Decision Tree",
                "Type": "Classification",
                "Simple Description": "",
                "Advanced Description": "",
                "Keywords": [

                ],
                "Simple Parameters": [
                    {
                        "ParamName": "Max Depth",
                        "Type": "int",
                        "Default": "None",
                        "Simple Description": "",
                        "Advanced Description": ""
                    },

                ],
                "Advanced Parameters": [
                    {
                        "ParamName": "criterion",
                        "Type": "options",
                        "Default": ["gini", "entropy"],
                        "Advanced Description": "The function to measure the quality of a split. "
                                                "\nSupported criteria are “gini” for the Gini impurity and "
                                                "\n“entropy” for the information gain."
                    },
                    {
                        "ParamName": "splitter",
                        "Type": "options",
                        "Default": ["best", "random"],
                        "Advanced Description": "The strategy used to choose the split at each node. "
                                                "\nSupported strategies are “best” to choose the best split and "
                                                "\n“random” to choose the best random split."
                    },
                ]
            }
    SUPPORT_VECTOR_CLASSIFIER = {
        "AlgName": "Support Vector Classifier",
        "Type": "Classification",
        "Simple Description": "",
        "Advanced Description": "",
        "Keywords": [

        ],
        "Simple Parameters": [
            {
                "ParamName": "Kernel",
                "Type": "options",
                "Default": ["rbf", "poly", "sigmoid", "linear"],
                "Simple Description": "",
                "Advanced Description": ""
            },

        ],
        "Advanced Parameters": [
            {
                "ParamName": "C",
                "Type": "float",
                "Default": 1.0,
                "Advanced Description": "Penalty parameter C of the error term"
            },
            {
                "ParamName": "degree",
                "Type": "int",
                "Default": 3,
                "Advanced Description": "Degree of the polynomial kernel function (‘poly’)."
                                        "\nIgnored by all other kernels."
            },
            {
                "ParamName": "gamma",
                "Type": "float",
                "Default": "auto",
                "Advanced Description": "Kernel coefficient for ‘rbf’, ‘poly’ and ‘sigmoid’." +
                    "\nCurrent default is ‘auto’ which uses 1 / n_features," +
                    "\nif gamma='scale' is passed then it uses 1 / (n_features * X.std()) as value of gamma.a"
            },
            {
                "ParamName": "coef0",
                "Type": "float",
                "Default": 0.0,
                "Advanced Description": "Independent term in kernel function. It is only significant in ‘poly’ and ‘sigmoid’."
            },
            {
                "ParamName": "shrinking",
                "Type": "bool",
                "Default": 0,
                "Advanced Description": "Whether to use the shrinking heuristic."
            },
            {
                "ParamName": "probability",
                "Type": "bool",
                "Default": 1,
                "Advanced Description": "Whether to enable probability estimates. This must be enabled prior to calling fit, and will slow down that method."
            },
            {
                "ParamName": "tol",
                "Type": "float",
                "Default": 1e-3,
                "Advanced Description": "Tolerance for stopping criterion."
            },
            {
                "ParamName": "cache_size",
                "Type": "float",
                "Default": -1,
                "Advanced Description": "Specify the size of the kernel cache (in MB)." +
                    "\n-1 to not pass."
            },
            {
                "ParamName": "max_iter",
                "Type": "int",
                "Default": -1,
                "Advanced Description": "Hard limit on iterations within solver, or -1 for no limit." +
                    "\n-1 to not pass."
            },
        ]
    }
    K_NEIGHBORS_CLASSIFIER = {
        "AlgName": "K Neighbors Classifier",
        "Type": "Classification",
        "Simple Description": "",
        "Advanced Description": "",
        "Keywords": [

        ],
        "Simple Parameters": [
            {
                "ParamName": "n_neighbors",
                "Type": "int",
                "Default": 5,
                "Simple Description": "",
                "Advanced Description": ""
            },
        ],
        "Advanced Parameters": [
            {
                "ParamName": "weights",
                "Type": "options",
                "Default": ["uniform", "distance"],
                "Simple Description": "",
                "Advanced Description": "weight function used in prediction. Possible values:" +
                    "\n‘uniform’ : uniform weights. All points in each neighborhood are weighted equally." +
                    "\n‘distance’ : weight points by the inverse of their distance. in this case, closer" +
                    "\n\tneighbors of a query point will have a greater influence than neighbors which are further away"
            },
            {
                "ParamName": "algorithm",
                "Type": "options",
                "Default": ["brute", "auto", "ball_tree", "kd_tree"],
                "Simple Description": "",
                "Advanced Description": "Algorithm used to compute the nearest neighbors:" +
                    "\n‘ball_tree’ will use BallTree" +
                    "\n‘kd_tree’ will use KDTree" +
                    "\n'brute’ will use a brute-force search." +
                    "\n'auto’ will attempt to decide the most appropriate algorithm based on the values passed to fit method." +
                    "\nNote: fitting on sparse input will override the setting of this parameter, using brute force."
            },
            {
                "ParamName": "leaf_size",
                "Type": "int",
                "Default": 30,
                "Simple Description": "",
                "Advanced Description": "Leaf size passed to BallTree or KDTree."
                                        "\nThis can affect the speed of the construction and query,"
                                        "\nas well as the memory required to store the tree."
                                        "\nThe optimal value depends on the nature of the problem."
            },
        ]
    }
    GAUSSIAN_PROCESS_CLASSIFIER = {
        "AlgName": "Gaussian Process Classifier",
        "Type": "Classification",
        "Simple Description": "",
        "Advanced Description": "",
        "Keywords": [

        ],
        "Simple Parameters": [
            {
                "ParamName": "Kernel",
                "Type": "options",
                "Default": ["rbf", "poly", "sigmoid", "linear"],
                "Simple Description": "",
                "Advanced Description": ""
            },
        ],
        "Advanced Parameters": [
			{
                "ParamName": "n_restarts_optimizer",
                "Type": "int",
                "Default": 0,
                "Simple Description": "",
                "Advanced Description": "The number of restarts of the optimizer for finding the kernel’s parameters which maximize" 
					"\nthe log-marginal likelihood. The first run of the optimizer is performed from the kernel’s initial parameters,"
					"\nthe remaining ones (if any) from thetas sampled log-uniform randomly from the space of allowed theta-values."
					"\nIf greater than 0, all bounds must be finite. Note that n_restarts_optimizer=0 implies that one run is performed."
            },
			{
                "ParamName": "max_iter_predict",
                "Type": "int",
                "Default": 100,
                "Simple Description": "",
                "Advanced Description": "The maximum number of iterations in Newton’s method for approximating the posterior during predict." 
										"\nSmaller values will reduce computation time at the cost of worse results."
            },
        ]
    }
    RANDOM_FOREST_CLASSIFIER = {
        "AlgName": "Random Forest Classifier",
        "Type": "Classification",
        "Simple Description": "",
        "Advanced Description": "",
        "Keywords": [

        ],
        "Simple Parameters": [
            {
                "ParamName": "Max Depth",
                "Type": "int",
                "Default": "None",
                "Simple Description": "",
                "Advanced Description": ""
            },
            {
                "ParamName": "Number of Trees (n_estimators)",
                "Type": "int",
                "Default": 10,
                "Simple Description": "",
                "Advanced Description": ""
            },
        ],
        "Advanced Parameters": [
			{	
				"ParamName": "criterion",
				"Type": "options",
				"Default": ["gini", "entropy"],
				"Advanced Description": "The function to measure the quality of a split. "
										"\nSupported criteria are “gini” for the Gini impurity and "
										"\n“entropy” for the information gain."
			},
        ]
    }
    MULTI_LAYER_PERCEPTRON = {
        "AlgName": "Multi-layer Perceptron",
        "Type": "Classification",
        "Simple Description": "",
        "Advanced Description": "",
        "Keywords": [

        ],
        "Simple Parameters": [
            {
                "ParamName": "alpha",
                "Type": "float",
                "Default": ".0001",
                "Simple Description": "",
                "Advanced Description": ""
            },
        ],
        "Advanced Parameters": [

        ]
    }
    ADABOOST_CLASSIFIER = {
        "AlgName": "AdaBoost Classifier",
        "Type": "Classification",
        "Simple Description": "",
        "Advanced Description": "",
        "Keywords": [

        ],
        "Simple Parameters": [

        ],
        "Advanced Parameters": [

        ]
    }
    GUASSIAN_NAIVE_BAYES = {
        "AlgName": "Gaussian Naive Bayes",
        "Type": "Classification",
        "Simple Description": "",
        "Advanced Description": "",
        "Keywords": [

        ],
        "Simple Parameters": [

        ],
        "Advanced Parameters": [

        ]
    }
    QUADRATIC_DISCRIMINANT_AANALYSIS = {
        "AlgName": "Quadratic Discriminant Analysis",
        "Type": "Classification",
        "Simple Description": "",
        "Advanced Description": "",
        "Keywords": [

        ],
        "Simple Parameters": [

        ],
        "Advanced Parameters": [

        ]
    }

    # REGRESSION
    LINEAR_REGRESSION = {
        "AlgName": "Linear Regression",
        "Type": "Regression",
        "Simple Description": "",
        "Advanced Description": "",
        "Keywords": [

        ],
        "Simple Parameters": [
        ],
        "Advanced Parameters": [

        ]
    }
    RIDGE_REGRESSION = {
        "AlgName": "Ridge Regression",
        "Type": "Regression",
        "Simple Description": "",
        "Advanced Description": "",
        "Keywords": [

        ],
        "Simple Parameters": [
            {
                "ParamName": "alpha",
                "Type": "float",
                "Default": 1.0,
                "Simple Description": "",
                "Advanced Description": ""
            },
        ],
        "Advanced Parameters": [

        ]
    }
    LASSO = {
        "AlgName": "Lasso",
        "Type": "Regression",
        "Simple Description": "",
        "Advanced Description": "",
        "Keywords": [

        ],
        "Simple Parameters": [
            {
                "ParamName": "alpha",
                "Type": "float",
                "Default": 1.0,
                "Simple Description": "",
                "Advanced Description": ""
            },
        ],
        "Advanced Parameters": [

        ]
    }
    BAYESIAN_RIDGE_REGRESSION = {
        "AlgName": "Bayesian Ridge Regression",
        "Type": "Regression",
        "Simple Description": "",
        "Advanced Description": "",
        "Keywords": [

        ],
        "Simple Parameters": [
            {
                "ParamName": "n_iter",
                "Type": "int",
                "Default": 300,
                "Simple Description": "",
                "Advanced Description": ""
            },
        ],
        "Advanced Parameters": [

        ]}
    LOGISTIC_REGRESSION = {
        "AlgName": "Logistic Regression",
        "Type": "Regression",
        "Simple Description": "",
        "Advanced Description": "",
        "Keywords": [

        ],
        "Simple Parameters": [
            {
                "ParamName": "max_iter",
                "Type": "int",
                "Default": 100,
                "Simple Description": "",
                "Advanced Description": ""
            },
        ],
        "Advanced Parameters": [

        ]
    }
    SUPPORT_VECTOR_REGRESSION = {
        "AlgName": "Support Vector Regression",
        "Type": "Regression",
        "Simple Description": "",
        "Advanced Description": "",
        "Keywords": [

        ],
        "Simple Parameters": [
            {
                "ParamName": "Kernel",
                "Type": "options",
                "Default": ["rbf", "poly", "sigmoid", "linear"],
                "Simple Description": "",
                "Advanced Description": ""
            },
        ],
        "Advanced Parameters": [

        ]
    }
    GAUSSIAN_PROCESS_REGRESSION = {
        "AlgName": "Gaussian Process Regression",
        "Type": "Regression",
        "Simple Description": "",
        "Advanced Description": "",
        "Keywords": [

        ],
        "Simple Parameters": [
            {
                "ParamName": "Kernel",
                "Type": "options",
                "Default": ["rbf", "poly", "sigmoid", "linear"],
                "Simple Description": "",
                "Advanced Description": ""
            },
        ],
        "Advanced Parameters": [

        ]}

    # CLUSTERING
    KMEANS = {
        "AlgName": "KMeans",
        "Type": "Clustering",
        "Simple Description": "",
        "Advanced Description": "",
        "Keywords": [

        ],
        "Simple Parameters": [
            {
                "ParamName": "n_clusters",
                "Type": "int",
                "Default": 8,
                "Simple Description": "",
                "Advanced Description": ""
            },
        ],
        "Advanced Parameters": [

        ]
    }
    AFFINITY_PROPAGATION = {
        "AlgName": "Affinity Propagation",
        "Type": "Clustering",
        "Simple Description": "",
        "Advanced Description": "",
        "Keywords": [

        ],
        "Simple Parameters": [
            {
                "ParamName": "damping",
                "Type": "float",
                "Default": .5,
                "Simple Description": "",
                "Advanced Description": ""
            },
        ],
        "Advanced Parameters": [

        ]
    }
    MEAN_SHIFT = {
        "AlgName": "Mean Shift",
        "Type": "Clustering",
        "Simple Description": "",
        "Advanced Description": "",
        "Keywords": [

        ],
        "Simple Parameters": [

        ],
        "Advanced Parameters": [

        ]
    }
    SPECTRAL_CLUSTERING = {
        "AlgName": "Spectral Clustering",
        "Type": "Clustering",
        "Simple Description": "",
        "Advanced Description": "",
        "Keywords": [

        ],
        "Simple Parameters": [
            {
                "ParamName": "n_clusters",
                "Type": "int",
                "Default": 8,
                "Simple Description": "",
                "Advanced Description": ""
            },
        ],
        "Advanced Parameters": [

        ]
    }
    AGGLOMERATIVE_CLUSTERING = {
        "AlgName": "Agglomerative Clustering",
        "Type": "Clustering",
        "Simple Description": "",
        "Advanced Description": "",
        "Keywords": [

        ],
        "Simple Parameters": [
            {
                "ParamName": "n_clusters",
                "Type": "int",
                "Default": 2,
                "Simple Description": "",
                "Advanced Description": ""
            },
        ],
        "Advanced Parameters": [

        ]
    }
    DBSCAN = {
        "AlgName": "DBSCAN",
        "Type": "Clustering",
        "Simple Description": "",
        "Advanced Description": "",
        "Keywords": [

        ],
        "Simple Parameters": [

        ],
        "Advanced Parameters": [

        ]
    }
    BIRCH = {
        "AlgName": "Birch",
        "Type": "Clustering",
        "Simple Description": "",
        "Advanced Description": "",
        "Keywords": [

        ],
        "Simple Parameters": [
            {
                "ParamName": "n_clusters",
                "Type": "int",
                "Default": 3,
                "Simple Description": "",
                "Advanced Description": ""
            },
        ],
        "Advanced Parameters": [

        ]
    }