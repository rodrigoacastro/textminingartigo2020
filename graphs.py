# process tables and plot graphs, including a dendrogram

import pandas as pd
import numpy as np
# import seaborn as sns
import matplotlib.pyplot as plt
#%matplotlib inline

# if directory Results/Graphs does not exist, try to create it
path = 'Results/Graphs/'

import os
if not os.path.exists('Results/Graphs/'):
    try:
        os.makedirs('Results/Graphs/')
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)

# read tables and process them

df_per_year = pd.read_csv('Results/df_per_year.csv')
df_per_year.head()

df_year_rel_results = pd.read_csv('Results/df_per_year_rel_freq.csv')
df_year_rel_results.head()

df_counts = pd.read_csv('Results/dataframe_counts.csv')
df_counts.head()

# dataset for dendrogram
df_counts_dend = df_counts[['filename','INTER','SENT','INTRA']]
df_counts_dend.index = df_counts_dend.filename
df_counts_dend = df_counts_dend.drop(columns=['filename'])
df_counts_dend.head()

complete_df = pd.read_csv('Results/complete_df.csv',sep='|')
complete_df.head()

# magazine section counts
section_counts = df_counts.type.value_counts().reset_index() 
section_counts.columns=['type','count']
section_counts.to_csv('Results/section_counts.csv',sep=';',index=False)

# create graphs

# line
df_per_year.plot(x='year',y=['INTER','SENT','INTRA'])
plt.title('Categories per year')
plt.savefig('Results/Graphs/Graph0.tiff',dpi=300)
# plt.show()

# bar
df_per_year.plot(kind='bar', x='year',y=['INTER','SENT','INTRA'])
plt.title('Categories per year')
plt.savefig('Results/Graphs/Graph1.tiff',dpi=300)
# plt.show()

df_year_rel_results.plot(kind='bar', x='year',y=['INTER','SENT','INTRA'])
plt.title('Categories per year - percentual distribution')
plt.savefig('Results/Graphs/Graph1A.tiff')
# plt.show()

section_counts.plot(kind='barh',x='type',y='count',fontsize=8)
plt.title('Frequency of magazine sections as sources')
plt.tight_layout()
plt.savefig('Results/Graphs/Graph2.tiff',dpi=300)
#plt.show()

# exported images in folder 'Results

# DENDROGRAM
# SOURCE
# https://stackabuse.com/hierarchical-clustering-with-python-and-scikit-learn/

# Create Dendrogram - ward method

method = 'ward'

from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt

linked = linkage(df_counts_dend, method)

#labelList = range(len(df_counts_dend))
labelList= list(df_counts_dend.index)
plt.figure(figsize=(10, 5)) # 1000x700 pixels
dend = dendrogram(linked,
            orientation='top',
            labels=labelList,
            distance_sort='descending',
            show_leaf_counts=True)
plt.tight_layout()
plt.savefig('Results/Graphs/Dendrogram_ward_texts.tiff',dpi=300)

#plt.show()

# Create Dendrogram - single method

method = 'single'

# from scipy.cluster.hierarchy import dendrogram, linkage
# from matplotlib import pyplot as plt

linked = linkage(df_counts_dend, method)

#labelList = range(len(df_counts_dend))
labelList= list(df_counts_dend.index)
plt.figure(figsize=(10, 5)) # 1000x700 pixels
dend = dendrogram(linked,
            orientation='top',
            labels=labelList,
            distance_sort='descending',
            show_leaf_counts=True)
plt.tight_layout()
plt.savefig('Results/Graphs/Dendrogram_single_texts.tiff',dpi=300)


# Create Dendrogram - complete method

method = 'complete'

# from scipy.cluster.hierarchy import dendrogram, linkage
# from matplotlib import pyplot as plt

linked = linkage(df_counts_dend, method)

#labelList = range(len(df_counts_dend))
labelList= list(df_counts_dend.index)
plt.figure(figsize=(10, 5)) # 1000x700 pixels
dend = dendrogram(linked,
            orientation='top',
            labels=labelList,
            distance_sort='descending',
            show_leaf_counts=True)
plt.tight_layout()
plt.savefig('Results/Graphs/Dendrogram_complete_texts.tiff',dpi=300)


# Create Dendrogram - average method

method = 'average'

# from scipy.cluster.hierarchy import dendrogram, linkage
# from matplotlib import pyplot as plt

linked = linkage(df_counts_dend, method)

#labelList = range(len(df_counts_dend))
labelList= list(df_counts_dend.index)
plt.figure(figsize=(10, 5)) # 1000x700 pixels
dend = dendrogram(linked,
            orientation='top',
            labels=labelList,
            distance_sort='descending',
            show_leaf_counts=True)
plt.tight_layout()
plt.savefig('Results/Graphs/Dendrogram_average_texts.tiff',dpi=300)