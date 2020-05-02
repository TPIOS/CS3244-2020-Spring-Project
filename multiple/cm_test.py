import sklearn.metrics as sm
y_true = ["cat", "ant", "cat", "cat", "ant", "bird"]
y_pred = ["ant", "ant", "cat", "cat", "ant", "cat"]
print(sm.confusion_matrix(y_true, y_pred, labels=["ant",  "cat", "bird"]))