# Skills2022

## Github Skills Test
### Manage GitHub scripts and documents
> Task description: Create a folder “Skills2022” in your DEVASC virtual machine and start a git repository.  

**Task preparation**: This task required creating a folder locally on a Linux VM, initializing that folder, and uploading its contents to a githab repository.  
  
**Task implementation**: A repository on githab was created and a file `README.md` was written in the main directory, where the report on the term paper is formed and also created a directory `/sources` with subdirectories as `/img` etc.  
  

**Task troubleshooting**: There were no problems in completing this task.  
  
**Task verification**:  
  
<p align="center">
  <img width="600"  src="/sources/img/Skills2022_task_001_000.png">
</p>  

## Ansible Skills Test
### Manage Web Servers through Ansible.
> Task description: Write the Ansible script to install and test the websever with ping command in a single playbook. Choose either Apache or Nginx server based on your own preference.  

**Task preparation**: I'm not using the DEVASC build, so I had to additionally install `sshpass` and `ansible` itself.  
  
**Task implementation**: The subfolder contained the [`hosts`](/sources/task_2/hosts) and [`ansible_tasks`](/sources/task_2/ansible_tasks.yml) files. The apache2 webserver is installed on the remote hosts specified in the [`hosts`](/sources/task_2/hosts). We can also specify a *.cfg file, but to accomplish this task, the default config will be sufficient.  
  
**Task troubleshooting**: There were no problems in completing this task.  
    
**Task verification**:  
  
Apache installation:  

`ansible-playbook -v ansible_tasks.yml -i hosts`  

<p align="center">
  <img width="600"  src="/sources/img/Skills2022_task_002_000.png">
</p>

<p align="center">
  <img width="600"  src="/sources/img/Skills2022_task_002_001.png">
</p>    
  
Ping:  

<p align="center">
  <img width="600"  src="/sources/img/Skills2022_task_002_002.png">
</p>  
  
  
## Docker
### Manage Docker microservices
> Task description: Create a docker microservice.  
  
**Task preparation**: This task required installing the `docker` on the server, raising the docker container (I used [`cturra/ntp`](https://hub.docker.com/r/cturra/ntp)) and running `ntpdate` on the client
  
**Task implementation**: A docker image was launched and then `ntpdate` was used to synchronize the time between the server and the client. 
  
**Task troubleshooting**: There were no problems in completing this task.  
    
**Task verification**:  

Pull docker container:  

<p align="center">
  <img width="600"  src="/sources/img/Skills2022_task_003_000.png">
</p>  

Run docker container:  

```
    sudo docker run --name=ntp       
              --restart=always      
              --detach              
              --publish=123:123/udp 
              cturra/ntp
```  
  
<p align="center">
  <img width="600"  src="/sources/img/Skills2022_task_003_001.png">
</p> 

`sudo docker ps`  
  
<p align="center">
  <img width="600"  src="/sources/img/Skills2022_task_003_002.png">
</p>   

`sudo docker logs ntp`  
  
<p align="center">
  <img width="600"  src="/sources/img/Skills2022_task_003_003.png">
</p>  
  
`sudo ntpdate -q 192.168.64.2`  
  
<p align="center">
  <img width="600"  src="/sources/img/Skills2022_task_003_004.png">
</p>  
   
   
## Jenkins
### CI/CD Pipelinr using Jenkins
> Task description: Create a Jenkins pipeline.  
  
**Task preparation**: ][Jenkins](https://hub.docker.com/_/jenkins) 
  
**Task implementation**: The subfolder contained the [`hosts`](/sources/task_2/hosts) and [`ansible_tasks`](/sources/task_2/ansible_tasks.yml) files. The apache2 webserver is installed on the remote hosts specified in the [`hosts`](/sources/task_2/hosts). We can also specify a *.cfg file, but to accomplish this task, the default config will be sufficient.  
  
**Task troubleshooting**: There were no problems in completing this task.  
    
**Task verification**:  
  
`sudo docker pull jenkins/jenkins` 

`sudo docker run -p 8080:8080 -p 50000:50000 jenkins/jenkins`


`Jenkins URL: http://localhost:8080/`
  
<p align="center">
  <img width="600"  src="/sources/img/Skills2022_task_002_000.png">
</p>

<p align="center">
  <img width="600"  src="/sources/img/Skills2022_task_002_001.png">
</p>    
  
Ping:  

<p align="center">
  <img width="600"  src="/sources/img/Skills2022_task_002_002.png">
</p>  


## Unit Testing
> Task description: Create a unittest script in Python that asserts the output of all the functions in the given Python module.  