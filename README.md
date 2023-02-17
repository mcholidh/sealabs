#Intoduction
This script uses the Flask web framework to create a simple web application. When a user visits the root URL (/), the index() function is called. The function first gets the user's IP address using the request.remote_addr attribute, and then increments the hit count for this IP address in the users dictionary. Finally, the function returns a string that includes the user's IP address and hit count.

#Instalation Instruction
We can then build the Docker image using the command:
```
docker build -t mcholidh/sealabs-check-ip:0.0.1 .
```

Then we can run it wish this command
```
docker run -d -it -p 80:80 --name sealabs-check-ip mcholidh/sealabs-check-ip:0.0.1
```