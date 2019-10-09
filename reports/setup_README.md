# Setup on GCP console

Launch  a GCP image with the [Bitnami image](https://console.cloud.google.com/marketplace/details/bitnami-launchpad/kafka) as the base.

### Add firewall rules
Head to the network section of the GCP VM. And under Firewall Rules add 2 rules, one to allow traffic from all IP addresses `0.0.0.0/0` (Ingress) and one to send traffic to all IP addresses `0.0.0.0/0` (Egress)

SSH into the VM

Create a virtual environment on your GCP VM. For this use `virtualenv` to manage the various environments.


    sudo apt-get install python3.5, python3-pip
    sudo pip3 install virtualenv
    virtualenv big_data
    source big_data/bin/activate
    pip install -r requirements.txt
    nohup sudo ../../big_data/bin/python mysimbdp-daas.py &


### Set up Cloud Mongodb

The Database is always running on the cloud and the URI in the code.

But to setup an separate database. Create an account on Cloud MongoDB and setup a free tier account and then configure the database by creating a username and password. Then the database is ready to use   
