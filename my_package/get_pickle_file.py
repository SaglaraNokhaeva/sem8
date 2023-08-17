import json
import os
import pickle


def my_pickle():
    with (open('result.json', 'r') as file_inp,
          open('result.pickle', 'wb') as file_out):
        pickle.dump((json.load(file_inp)), file_out)
