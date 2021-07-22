import random
import numpy as np

sample_num = 100000
guest_feature_shape = 250
host_feature_shape = 250


def gen_data(feature_shape, with_label=True):
    if with_label:
        header = ["sid", "y"] + ["x" + str(i) for i in range(feature_shape)]
        fout = open("test_hetero_guest.csv", "w")
    else:
        header = ["sid"] + ["x" + str(i) for i in range(feature_shape)]
        fout = open("test_hetero_host.csv", "w")

    fout.write(",".join(header) + "\n")
    for i in range(sample_num):
        ret = [i]
        if with_label:
            ret.append(random.randint(0, 1))

        ret += np.random.random((feature_shape, )).tolist()
        fout.write(",".join(map(str, ret)) + "\n")

    fout.close()


gen_data(guest_feature_shape, with_label=True)
gen_data(host_feature_shape, with_label=False)