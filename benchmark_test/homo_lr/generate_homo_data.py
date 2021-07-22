import random
import numpy as np

guest_homo_data_sample_num = 100000
host_homo_data_sample_num = 100000
homo_data_feature_shape = 250


def gen_homo_data():
    header = ["sid", "y"] + ["x" + str(i) for i in range(homo_data_feature_shape)]
    fout_guest = open("test_homo_guest.csv", "w")
    fout_host = open("test_homo_host.csv", "w")
    fout_guest.write(",".join(header) + "\n")
    fout_host.write(",".join(header) + "\n")

    for i in range(guest_homo_data_sample_num):
        ret = [i, random.randint(0, 1)] + np.random.random((homo_data_feature_shape, )).tolist()
        fout_guest.write(",".join(map(str, ret)) + "\n")

    for i in range(host_homo_data_sample_num):
        ret = [i, random.randint(0, 1)] + np.random.random((homo_data_feature_shape, )).tolist()
        fout_host.write(",".join(map(str, ret)) + "\n")


gen_homo_data()