# RESTful-web-service using DOCKER container

Created a Python RESTful services using Flask and use docker to run this application.                              
First, docker need to be installed. Link: https://docs.docker.com/toolbox/toolbox_install_mac/                  

## Steps
1. Get inside the app folder in terminal                          
2. Build the docker image:                                           

      ```bash
      docker build -t firstdockerimage .
      ```
3. once the docker image is created, run the "firstdockerimage" in docker container using below command.
                                                            
      ```bash
      docker run -d -p 5000:5000 firstdockerimage
      ```
4.Now, Run the below requests using the address as either localhost or the docker ip address.
                   
  **Request1**: Go to http://localhost:5000/getcars/  to list all restaurants data.                               
  **Request2**: Go to http://localhost:5000/getcars/18/ to retrieve a specific car entry with id=18.         
  **Request3**: Go to http://localhost:5000/getcars/Car_Name/Jaguar to get list of 'Jaguar' cars. 
  
  **Request4**: Go to http://localhost:5000/getcars/Year/2020 to get the list of cars introduced in the year 2020.    
  **Request5**: Go to http://localhost:5000/getcars/Car_Name/BMW/Year/2020 to get the list of BMW cars which are introduced in the year 2020 

## Below are the list of useful Docker Commands. 
1. List all images: *docker images*
2. List all containers which are running inside the docker: *docker ps*
3. Stop all running containers: *docker stop $(docker ps -aq)*
4. Remove all containers: *docker rm $(docker ps -aq)*                    
5. Remove all docker images: *docker rmi $(docker images -q)*
