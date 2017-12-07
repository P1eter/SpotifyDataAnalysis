import pickle
import pandas as pd
h = pd.read_pickle("datasets/house_features")
f = pd.read_pickle("datasets/hiphop_features")
from sklearn.manifold import TSNE

mds = TSNE(n_components=2, perplexity = 40)
result = mds.fit_transform(h.append(f))

filename = 'finalized_model.sav'
pickle.dump(mds, open(filename, 'wb'))

filename = 'result_matrix'
pickle.dump(result, open(filename, 'wb'))

