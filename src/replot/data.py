import os
import pickle


def get_data():
    """
    Load the data dictionary that was stored in the current directory.

    All this does is to load the file ``data.pkl`` and unpickle it. You can
    also include this code directly in your plotting code if you don't want
    it to depend on replot.

    :return: dictionary containing data for plotting
    """
    with open(os.path.join(os.getcwd(), "data.pkl"), "rb") as f:
        return pickle.load(f)
