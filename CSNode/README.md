## Implementing Remote Procedure Calls With gRPC and Protocol Buffers

Install npm packages

``` bash
$ npm install
```

##Usage

Start the node server

```bash
node server/
```

Make an RPC call from one of the respective clients

- #### Node client

```bash
node client/node
```

- #### Python client

Create and use a new virtual environment

```bash
mkvirtualenv new_grpc_env && workon new_grpc_env
```

Install the grpc python modules from `requirements.txt`
```bash
pip install -r requirements.txt
```

Run the Python client

```bash
python client/python/client.py
```



