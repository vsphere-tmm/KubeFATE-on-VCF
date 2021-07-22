# Steps

Assumes the guest party is 9999 and the host party is 10000.

## Download the MNIST dataset in both parties

``` bash
# login to the python pod
$ kubectl exec -it python-xxx -n fate-xxx bash

$ python /data/projects/fate/examples/scripts/download_mnist_data_as_images.py
```

## Upload the MNIST dataset to FATE cluster

On guest

```bash
python /data/projects/fate/python/fate_flow/fate_flow_client.py -f upload -c ./upload_guest.json
```

On host

```bash
python /data/projects/fate/python/fate_flow/fate_flow_client.py -f upload -c ./upload_host.json
```

## Submit training job

```bash
python /data/projects/fate/python/fate_flow/fate_flow_client.py -f submit_job -c ./mnist_conf.json -d ./mnist_dsl.json 
```

After that, a user can check the job status in the FATE Board.