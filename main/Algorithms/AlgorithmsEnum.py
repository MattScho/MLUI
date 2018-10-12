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
                        "Advanced Description": ""
                    },
                    {
                        "ParamName": "Fit_Intercept",
                        "Type": "bool",
                        "Default": "True",
                        "Simple Description": "Whether the intercept should be estimated or not.\n If False, the data is assumed to be already centered.",
                        "Advanced Description": ""
                    }
                ],
                "Advanced Parameters":[

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
                "Advanced Parameters":[

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
                        "Default": "10",
                        "Simple Description": "",
                        "Advanced Description": ""
                    },
                ],
                "Advanced Parameters": [

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

    #CLUSTERING
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
    MEAN_SHIFT ={
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
    DBSCAN ={
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
    BIRCH ={
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
