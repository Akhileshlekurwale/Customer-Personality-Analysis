import os
import sys
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from customer_personality.logger.log import logging
from customer_personality.exception.exception_handler import AppException
from customer_personality.config.configuration import AppConfiguration
from sklearn.cluster import KMeans
from sklearn import metrics

class ModelTrainer:
    def __init__(self,app_config=AppConfiguration()):
        try:
            self.model_trainer_config = app_config.get_model_trainer_config()
        except Exception as e:
            raise AppException(e,sys) from e

    def train(self):
        try:
            final_df = pd.read_csv(self.model_trainer_config.transformed_data_file_dir)

            #Get number of cluster
            clusterRange = range(2,21)
            inertiaRange=[]
            silhouteRange=[]

            for m in clusterRange:
                model_m = KMeans(n_clusters=m)
                model_m.fit(final_df)
                inertiaRange.append(model_m.inertia_)
                silhouteRange.append(metrics.silhouette_score(final_df,model_m.labels_))

            os.makedirs(self.model_trainer_config.trained_model_dir,exist_ok=True)
            plt.plot(clusterRange,inertiaRange)
            image_name = os.path.join(self.model_trainer_config.trained_model_dir,self.model_trainer_config.trained_model_name)
            #plt.savefig(image_name.png)

            model = KMeans(n_clusters=4)
            model.fit(final_df)

            #saving model object for recommendation
            os.makedirs(self.model_trainer_config.trained_model_dir, exist_ok=True)
            file_name = os.path.join(self.model_trainer_config.trained_model_dir,self.model_trainer_config.trained_model_name)
            pickle.dump(model, open(file_name,'wb'))
            logging.info(f"Saving final model to {file_name}")

            
            
        except Exception as e:
            raise AppException(e, sys) from e

    def initiate_model_trainer(self):
        try:
            logging.info(f"{'='*20}Model Trainer log started.{'='*20} ")
            self.train()
            logging.info(f"{'='*20}Model Trainer log completed.{'='*20} \n\n")
        except Exception as e:
            raise AppException(e, sys) from e



