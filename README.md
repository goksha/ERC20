# blockchain
To install the containerized application docker pull command can be used.
<br/><br/>
docker pull shagok/x21226661:ecr20
<br/><br/>
if you are planning to compile on your own please follow below steps
<br/><br/>
Step1: 
<br/><br/>
create a python virtual environment and install the requirements from requirements.txt
<br/><br/>
Note: please use python 3.9.2 version
<br/><br/>
Step2:
<br/><br/>
.env file should be created with the contents as mentioned in env-example.txt as we are making use of python decouple
<br/><br/>
Step3:
<br/><br/>
run webserver.py 
<br/><br/>
if the webserver is up if curl command is run you will get a response with something like this " This is an example web server. "
<br/><br/>
Step4:
<br/><br/>
To containerize the application install docker and run the below code
<br/><br/>
e.g where "shagok/x21226661" is repository name on docker hub and "ecr20" is tagname
<br/><br/>
docker build -t shagok/x21226661:ecr20 .
<br/><br/>
docker run -p 8090:8080 --name ecr20_block_harbor -d shagok/x21226661:ecr20
<br/><br/>
step5:
<br/><br/>
To push the image to docker hub
<br/><br/>
docker push repositoryname:tagname
<br/><br/>
Once the Docker Container is runing --->
<br/><br/>
To transfer the token the below mentioned command can be used --->
<br/><br/>
curl --header "Content-Type: application/json" --request POST --data '{"address":"recievers ETH Address "}' http://localhost:8090/token
<br/><br/>
To transfer the ETH the below mentioned command can be used --->
<br/><br/>
curl --header "Content-Type: application/json" --request POST --data '{"address":"recievers ETH Address ","amount":"0.05"}' http://localhost:8090/eth