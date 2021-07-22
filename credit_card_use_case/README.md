# Overview

This document illustrate how to train a homogeneous logistic regression model with dataset of real world.

The following content assumes the guest party is 9999 and the host party is 10000.

## Steps

### Download dataset from Kaggle

https://www.kaggle.com/mlg-ulb/creditcardfraud

### Run Script to split data

```bash
$ bash splitting_data.sh
```

### Upload dataset and notebook to host party

1. log in to notebook service of the host party
2. upload dataset **"creditcard_host.csv"** to "Pipeline/notebooks/"
3. upload notebook **"homo_lr_host.ipynb"** to "Pipeline/notebooks/"
4. run every cells of the notebook

### Upload dataset and notebook to guest party

1. log in to notebook service of the guest party
2. upload dataset **"creditcard_guest.csv"** to "Pipeline/notebooks/"
3. upload notebook **"homo_lr_guest.ipynb"** to "Pipeline/notebooks/"
4. run every cells of the notebook