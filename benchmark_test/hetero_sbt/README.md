# Steps

Assumes the server to generate dataset is vmware@192.168.0.1; the guest party is 9999 and the host party is 10000.

## Generate the dataset with following command

``` bash
$ cd benchmark_test
$ python generate_hetero_data.py
```

## Copy data to guest party and upload to FATE cluster

``` sh
# use kubectl to log in the python pod of fate-9999 namespace
$ kubectl exec -it python-xxx -n fate-9999 bash

# use scp to copy test_hetero_guest.csv to local
$ cd /data/projects/fate/examples/data
$ scp vmware@192.168.0.1:/kubefate-on-vcf/benchmark_test/hetero_sbt/test_hetero_guest.csv ./
$ scp vmware@192.168.0.1:/kubefate-on-vcf/benchmark_test/hetero_sbt/upload_data_guest.json ./

# upload data

$ python /data/projects/fate/python/fate_flow/fate_flow_client.py -f upload -c ./upload_data_guest.json
```

## Copy data to host party and upload to FATE cluster

``` sh
# use kubectl to log in the python pod of fate-10000 namespace
$ kubectl exec -it python-xxx -n fate-10000 bash

# use scp to copy test_hetero_guest.csv to local
$ cd /data/projects/fate/examples/data

$ scp vmware@192.168.0.1:/kubefate-on-vcf/benchmark_test/hetero_sbt/test_hetero_host.csv ./
$ scp vmware@192.168.0.1:/kubefate-on-vcf/benchmark_test/hetero_sbt/upload_data_host.json ./

# upload data
$ python /data/projects/fate/python/fate_flow/fate_flow_client.py -f upload -c ./upload_data_host.json
```

## Submit job in guest party

Assumes it has logged in to the python pod

``` sh
$ scp vmware@192.168.0.1:/kubefate-on-vcf/benchmark_test/hetero_sbt/test_secureboost_train_binary_conf.json ./
$ scp vmware@192.168.0.1:/kubefate-on-vcf/benchmark_test/hetero_sbt/test_secureboost_train_dsl.json ./

$ python /data/projects/fate/python/fate_flow/fate_flow_client.py -f submit_job -c ./test_secureboost_train_binary_conf.json  -d test_secureboost_train_dsl.json  
```

A user can adjust `job_parameters.spark_run.num-executors and computing_partitions` of "test_secureboost_train_binary_conf.json" to meet actual requirement.

After that a user can check the FATE Board for job's status.
