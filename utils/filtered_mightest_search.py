from mightest_search import *
from ptype_filter import *

def filtered_mightest_search(df, metric="HP", ptype=None):
    if ptype is not None:
        df = ptype_filter(df, ptype)
    return mightest_search(df, metric)
