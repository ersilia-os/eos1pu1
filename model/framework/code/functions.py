'''
Function script for clean importing and calling to
'''
import pandas as pd
import numpy as np
from mordred import Calculator, descriptors
from standardise_smiles import standardize_jumpcp
from rdkit import Chem
import pickle
import csv


def load_model(model_path):
   with open(model_path, 'rb') as file:
       classifier = pickle.load(file)
   return classifier


def load_data_columns(columns_path):
   with open(columns_path, 'rb') as file:
       data_columns = pickle.load(file)
   return data_columns


def preprocess_smiles(smiles_list):
   df = pd.DataFrame({'SMILES': smiles_list})
   df['Standardized_SMILES'] = df['SMILES'].apply(standardize_jumpcp)
   return df


def generate_mordred_descriptors(df, data_columns):
   calc = Calculator(descriptors, ignore_3D=True)
   mols = df['Standardized_SMILES'].apply(Chem.MolFromSmiles)
   valid = mols.notna()
   table = pd.DataFrame(float('nan'), index=mols.index, columns=data_columns)
   if valid.any():
       table.loc[valid, data_columns] = calc.pandas(mols[valid]).astype('float')[data_columns].values
   return table, valid


def run_predictions(classifier, df, data_columns):
   threshold = 0.641338  # Fixed threshold
   table, valid = generate_mordred_descriptors(df, data_columns)
   X = np.array(table)
   probs = np.full(len(X), float('nan'))
   if valid.any():
       X_valid = X[valid.values].copy()
       X_valid[np.isnan(X_valid)] = 0
       X_valid[np.isinf(X_valid)] = 0
       probs[valid.values] = classifier.predict_proba(X_valid)[:, 1]
   preds = np.where(~np.isnan(probs), (probs >= threshold).astype(int), float('nan'))
   return probs, preds



