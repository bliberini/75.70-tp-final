import pandas as pd
import numpy as np

def get_prediction_class(y_prob):
    y_pred = []
    for i in range(len(y_prob)):
        if y_prob[i][0] >= y_prob[i][1]:
            y_pred.append(0)
        else:
            y_pred.append(1)
    return y_pred

def get_confussion_matrix(real, pred):
    headers = ['target_0', 'target_1']
    indexes = ['target_0', 'target_1']
    values_0 = [0,0]
    values_1 = [0,0]
    for i in range(len(pred)):
        if pred[i] == 0:
            if real[i] == 0:
                values_0[0] += 1
            else:
                values_0[1] += 1
        else:
            if real[i] == 0:
                values_1[0] += 1
            else:
                values_1[1] += 1
    return pd.DataFrame(data=np.array([values_0, values_1]), index=np.array(indexes), columns=np.array(headers))

def flip_negative_positive_class(classes):
	flipped_classes = []
	for i in range(len(classes)):
		if (classes[i] == 0):
			flipped_classes.append(1)
		else:
			flipped_classes.append(0)

	return flipped_classes

	