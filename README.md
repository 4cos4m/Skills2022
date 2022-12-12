# Skills2022

## Github Skills Test
### Manage GitHub scripts and documents
> Task description: Create a folder “Skills2022” in your DEVASC virtual machine and start a git repository.  

**Task preparation**: This task required creating a folder locally on a Linux VM, initializing that folder, and uploading its contents to a github repository.  
  
**Task implementation**: A repository on github was created and a file `README.md` was written in the main directory, where the report on the term paper is formed and also created a directory `/sources` with subdirectories as `/img` etc.  
  

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
  
**Task preparation**:  This task required the use of a docker and [`Jenkins`](https://hub.docker.com/r/jenkins/jenkins), as well as a [`docker container`](https://hub.docker.com/r/cturra/ntp) *(which we used in the previous task)*  
  
**Task implementation**: For this task, we need to run the docker container from the last task via Jenkins, using a [`script`](/sources/task_4/ntp.sh) placed in its repository.  
  
**Task troubleshooting**: There were no problems in completing this task.  
    
**Task verification**:  
  
First of all we had to get `Jenkins` itself up — install it according to the [`manual`](https://hub.docker.com/r/jenkins/jenkins) (for the latest version use `docker pull jenkins/jenkins`).  
  
`sudo docker run -p 8080:8080 -p 50000:50000 jenkins/jenkins`  

<p align="center">
  <img width="600"  src="/sources/img/Skills2022_task_004_000.png">
</p>
  
After installation is complete, we get a key, which later allows us to log in.  

<p align="center">
  <img width="600"  src="/sources/img/Skills2022_task_004_001.png">
</p>    
  
<p align="center">
  <img width="600"  src="/sources/img/Skills2022_task_004_002.png">
</p>  

Create first admin user:  

<p align="center">
  <img width="600"  src="/sources/img/Skills2022_task_004_003.png">
</p>  

The task requires us to take code from our repository — specify it in the settings.  

<p align="center">
  <img width="600"  src="/sources/img/Skills2022_task_004_004.png">
</p> 

Enter the [`script`](/sources/task_4/ntp.sh) to be executed.  

<p align="center">
  <img width="600"  src="/sources/img/Skills2022_task_004_005.png">
</p> 


## Unit Testing
> Task description: Create a unittest script in Python that asserts the output of all the functions in the given Python module.  

**Task preparation**: The [`unittest`](https://docs.python.org/3/library/unittest.html) module is used to run automated tests and is preventively put together with python.  
  
**Task implementation**: To run tests, the [`script`](/sources/task_5/Skills2022_task_005_unittest.py) posted in the repository will be used. During the study of the topic of automated tests through this module was used [`article`](https://habr.com/ru/company/otus/blog/481806/).   
  
**Task troubleshooting**: There were no problems in completing this task.  
    
**Task verification**:  

Prescribe tests according to the assignment. You can also check out the [`script`](/sources/task_5/Skills2022_task_005_unittest.py) in the repository.

<p align="center">
  <img width="600"  src="/sources/img/Skills2022_task_005_000.png">
</p>
  
Running the script:  

`python3 Skills2022_task_005_unittest.py -v`  
  
<p align="center">
  <img width="600"  src="/sources/img/Skills2022_task_005_001.png">
</p>
  
