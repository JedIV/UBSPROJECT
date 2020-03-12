# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
import addition

# Read recipe inputs
new_customers = dataiku.Dataset("new_customers")
new_customers_df = new_customers.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

addition_df = new_customers_df # For this sample code, simply copy input to output

addition_df["add_stuff"] = addition.add_one(1)


# Write recipe outputs
addition = dataiku.Dataset("addition")
addition.write_with_schema(addition_df)
