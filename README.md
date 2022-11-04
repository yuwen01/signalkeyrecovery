# Building
In the root directory `signalkeyrecovery`, create a python3.8 virtualenv
```
virtualenv --python=python3.8 env
```
Start the virtual env (use bash)
```
source env/bin/activate
```
Install python dependencies
```
pip install simplejson cryptography pyopenssl grpc yaml
```

# Usage
Start the decentralized nodes - clone `dtrust` repo in the parent directory of where this repo is cloned. Say, you can have a parent directory `dtrust-project` which has 2 subdirectories `dtrust` and `dtrust-applications`.

Run the decentralized nodes in two separate terminal windows (`cd ../dtrust/`). On intel mac:
```
./platform/init_server --node_id node1 --config ./core-apps/pki/server_conf.yml

./platform/init_server --node_id node2 --config ./core-apps/pki/server_conf.yml
```

On linux / m1:

```
python3 platform/server_grpc/init_server.py --node_id node1 --config ./core-modules/pki/server_conf.yml

python3 platform/server_grpc/init_server.py --node_id node2 --config ./core-modules/pki/server_conf.yml
```

Now that the nodes are running, we can run our application.

First run the chat server who facilitates messages exchange (like center of a star network topology). Execute the following inside python virtual env which can be created as mentioned above under "Building".
```
cd Server/
python3 server.py
```

Now as many chat clients as needed can be started using (inside python virtual env)
```
cd Client/
python3 client.py
```