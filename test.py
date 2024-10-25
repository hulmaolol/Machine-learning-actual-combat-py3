import importlib
import bayes
import numpy as np

importlib.reload(bayes)
listOPosts,listClasses = bayes.loadDataSet()
myVocabList = bayes.createVocabList(listOPosts)

print(bayes.spamTest())