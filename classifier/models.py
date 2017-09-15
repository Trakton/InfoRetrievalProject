from sklearn.preprocessing import Normalizer
from sklearn.svm import SVC
from sklearn.model_selection import cross_validate
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.pipeline import make_pipeline
import math

def svm(attributes, target):
    #Macro ou micro?
    #Separar em teste treino e cross validation no treino?
    scoring = ['precision_macro', 'f1_macro', 'recall_macro', 'accuracy']
    clf = make_pipeline(Normalizer(), SVC(C=math.pow(10,5), gamma="auto",
                                            kernel='rbf', decision_function_shape="ovo"))
    scores = cross_validate(clf, attributes, target, scoring=scoring,
                            cv=5, return_train_score=False)
    print(scores.keys())
    print(scores.values())
