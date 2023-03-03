# Get Elbow value:
# Elbow Value represnts no of clusters to be formed during clusterization:
#############################################################################################################################################################################

import pandas as pd
from sklearn.cluster import KMeans 
import sys
from kneed import KneeLocator

#########################################################################################################################################################################
# WE DO THE ELBOW ETHOD HERE 

def getElbowMethodGraph(X):
    range_of_ssc = 12
    cost =[]
    
    for i in range(1, range_of_ssc):
        KM = KMeans(n_clusters = i, max_iter = 500)
        KM.fit(X)
        # calculates squared error
        # for the clustered points
        cost.append(KM.inertia_)     
    
    sys.path.append('..')
    kn = KneeLocator(list(range(1, range_of_ssc)), cost, S=1.0, curve='convex', direction='decreasing')
    return kn.knee
