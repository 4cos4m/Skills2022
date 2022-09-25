# Skills2022

## Github Skills Test
### Manage GitHub scripts and documents
> Task description: Create a folder “Skills2022” in your DEVASC virtual machine and start a git repository.  

**Task preparation**: This task required creating a folder locally on a Linux VM, initializing that folder, and uploading its contents to a githab repository.  
  
**Task implementation**: A repository on githab was created and a file `README.md` was written in the main directory, where the report on the term paper is formed and also created a directory `/sources` with subdirectories as `/img` etc.  
  

**Task troubleshooting**: There were no problems in completing this task.  
  
**Task verification**:  
  
![Task_001_000](/sources/img/Skills2022_task_001_000.png)

## Ansible Skills Test
### Manage Web Servers through Ansible.
> Task description: Write the Ansible script to install and test the websever with ping command in a single playbook. Choose either Apache or Nginx server based on your own preference.  

**Task preparation**: I'm not using the DEVASC build, so I had to additionally install `sshpass` and `ansible` itself.  
  
**Task implementation**: The subfolder contained the [`hosts`](/sources/task2/hosts) and [`ansible_tasks`](/sources/task2/ansible_tasks.yml) files. The apache2 webserver is installed on the remote hosts specified in the [`hosts`](/sources/task2/hosts). We can also specify a *.cfg file, but to accomplish this task, the default config will be sufficient.  
  
**Task troubleshooting**: There were no problems in completing this task.  
    
**Task verification**:  
  
Apache installation:  

`ansible-playbook -v ansible_tasks.yml -i hosts`  

![Task_002_000](/sources/img/Skills2022_task_002_000.png)
![Task_002_001](/sources/img/Skills2022_task_002_001.png)  
  
Ping:  
![Task_002_002](/sources/img/Skills2022_task_002_002.png)
  
## Docker
### Manage Docker microservices
> Task description: Create a docker microservice.  

## Jenkins
### CI/CD Pipelinr using Jenkins
> Task description: Create a Jenkins pipeline.  

## Unit Testing
> Task description: Create a unittest script in Python that asserts the output of all the functions in the given Python module.  