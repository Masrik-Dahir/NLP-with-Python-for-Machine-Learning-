import pandas as pd
fullCorpus = pd.read_csv('SMSSpamCollection.tsv',sep='\t',header=None)
fullCorpus.columns = ['label','body_text']
fullCorpus.head()