from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.svm import SVC

from sklearn.metrics import accuracy_score,precision_score,confusion_matrix
import pandas as pd

svc = SVC(kernel='sigmoid',gamma=1.0)
knc = KNeighborsClassifier()
mnb = MultinomialNB()
dtc = DecisionTreeClassifier(max_depth=5)
lrc = LogisticRegression(solver='liblinear', penalty='l1')
rfc = RandomForestClassifier(n_estimators=50, random_state=2)
abc = AdaBoostClassifier(n_estimators=50, random_state=2)
bc  = BaggingClassifier(n_estimators=50, random_state=2)
etc = ExtraTreesClassifier(n_estimators=50, random_state=2)
gbdt = GradientBoostingClassifier(n_estimators=50, random_state=2)


clfs = {
    'SVC' : svc,
    'KNeighborsClassifier' : knc,
    'MultinomialNB' : mnb,
    'DecisionTreeClassifier' : dtc,
    'LogisticRegression' : lrc,
    'RandomForestClassifier' : rfc,
    'AdaBoostClassifier' : abc,
    'BaggingClassifier' : bc,
    'ExtraTreesClassifier' : etc,
    'GradientBoostingClassifier' : gbdt,
    'XGBClassifier' : xgb
}

def train_classifier(clf,x_train,x_test,y_train,y_test):
    clf.fit(x_train,y_train)
    y_pred = clf.predict(x_test)
    accuracy = accuracy_score(y_test,y_pred)
    precision = precision_score(y_test,y_pred)
    confusion_mat = confusion_matrix(y_test,y_pred)

    return accuracy,precision,confusion_mat

def getscores(clfs,x_train,x_test,y_train,y_test):
    accuracy_scores= []
    precision_scores = []
    confusion_mats=[]
    algorithms = clfs.keys()

    for name,clf in clfs.items():
        current_accuracy,current_precision,current_confusion_mat = train_classifier(clf,x_train,x_test,y_train,y_test)

        # print('FOR: ',name)
        # print('AccuracyScore\n',current_accuracy)
        # print('PrecisionScore\n',current_precision)
        # print('ConfusionMatrix\n',current_confusion_mat)
        accuracy_scores.append(current_accuracy)
        precision_scores.append(current_precision)
        confusion_mats.append(current_confusion_mat)

    dataFrame = pd.DataFrame({'Algorithm':algorithms,
                                'Accuracy':accuracy_scores,
                                'Precision':precision_scores,
                                'Confusion_Matrix':confusion_mats})

    return dataFrame


def modelTraining(x_train,x_test,y_train,y_test):
    dataframe = getscores(clfs,x_train,x_test,y_train,y_test)

    return dataframe

if __name__ =='__main__':
    modelTraining()