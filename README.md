# managed-app-metered-billing
An example application to submit usage events to all plans of a particular offer ID and 
plan ID. This application will look at every managed application the identity provided
can see. For any subscriptions that match the right offer + plan combination, this will 
submit one meter at a fixed count. 

This is only an example of how to emit meters. This code is missing two pieces you will 
to add:

* Dimensions that your application actually uses.
* Counts that are accurate for each instance. 

Those bits are dependent on what your application charges for and how you collect the data. 
Getting that right will be far more complex than what is demonstrated here.


To setup the project, do the following:

ON LINUX:
---------
1. Make sure you have python3 and virtualenv installed. 
yum install python3
yum install python-virtualenv

2. From the root of the project, setup the venv 
virtualenv -p /usr/bin/python venv

3. Activate the virtual environment

source  venv/bin/activate  

4. Pull in the required python projects

 pip install -r ./requirements.txt

5. Run-- please keep in mind that this code will attempt to set dim1 on all deployments.
If you have different dimension names, these calls will all fail.

cd ./managed-app-metered-billing
python main.py --tenant-id <your tenant id> \
    --client-id <your client id> \
    --client-secret <your client secret> \
    --offer-id <your offer-id> \
    --plan-id <your plan-id>

ON Windows:
------------

1. From the root of the project, setup the venv

```
python -m venv venv
```

2. Activate the virtual environment

```
./venv/Scripts/activate
```

3. Pull in the required projects:

```
pip install -r ./requirements.txt
```

4. Run-- please keep in mind that this code will attempt to set dim1 on all deployments. 
If you have different dimension names, these calls will all fail.

```
cd .\managed-app-metered-billing\
python main.py --tenant-id <your tenant id> \
    --client-id <your client id> \
    --client-secret <your client secret> \
    --offer-id <your offer-id> \
    --plan-id <your plan-id>
```

