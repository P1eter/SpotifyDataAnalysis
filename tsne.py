import pickle
import pandas as pd
h = pd.read_pickle("datasets/house_features")
f = pd.read_pickle("datasets/hiphop_features")
from sklearn.manifold import TSNE

mds = TSNE(n_components=2)
mds.fit(h.append(f))

filename = 'finalized_model.sav'
pickle.dump(mds, open(filename, 'wb'))
