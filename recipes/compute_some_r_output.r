library(dataiku)

# Recipe inputs
ncp <- dkuReadDataset("ncp", samplingMethod="head", nbRows=100000)

# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a R dataframe or data table
some_r_output <- ncp # For this sample code, simply copy input to output


# Recipe outputs
dkuWriteDataset(some_r_output,"some_r_output")
