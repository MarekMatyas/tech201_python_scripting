# tech201_python_scripting


# Python scripting

A Python script is best described as a ***Python file that contains commands in logical order.***

A Python script is a collection of commands in a file designed to be ***executed like a program.***

The idea is that it will be run or executed from the command line or from within a Python interactive shell to perform a specific task.

Often a script first contains a set of function definition and then has the ***main program*** that might call the functions.

---
## Difference between scripting and programming

Generally, all the scripting languages are considered programming languages.

The main difference between both is scripting languages don't require any compilation and are directly interpreted. 

---

## Why are scripts useful ? 

Scripts in Python are useful because they allow us to **automate repetitive tasks, perform data processing and analysis and create standalone programs.** 

They also provide a way to interact with the operating system and other software,enabling you to perform complex tasks more easily and quickly than if you were to do them manually.

---
## How are scripts used in Python ?

Scripts are executed by running the Python interpreter and passing the script file as an argument. 

The interpreter reads the script, executes the code, and returns the result.

This can be done from the command line, from within an integrated development environment (IDE), or from another Python script.

---
## Why Python ? 

1. Easy to learn: Python has a simple syntax, making it easy for beginners to pick up and start writing scripts.
2. Versatile: Python can be used for a wide range of tasks, from simple data processing to complex scientific simulations and everything between.
3. Large community: Python has a large and active user community that has created many libraries and tools that can be easily integrated into scripts.
4. Cross-platform: Python can be run on multiple OS's, including Windows, MacOS and Linux so scripts can be written once and run on multiple platforms.
5. Interoperability: Python can interact with other software and systems, such as databases, web services and API's, making it possible to automate complex workflows.


---

## Why is scripting important for DevOps Engineers ? 

Scripting is important for DevOps Engineers because it **enables automation of repetitive and complex tasks**, which helps to increase efficiency, reduce errors, and improve consistency in the development and operations processes. 


Scripting also allows DevOps Engineers to ***automate infrastructure management, deployment processes, and test and deploy applications faster and more reliably. 

### Additional bonuses:

It provides a way for DevOps Engineers to standardize their work and share their scripts with other and the team, improving collaboration and knowledge sharing.


# 10 ways to use scripts in DevOps

1. Automating server provisioning and configuration management using scripts like **Bash, Ansible and Puppet** 
2. Building and deploying applications using scripts like **Jenkins and TravisCI**.
3. Automated testing and continuous integration with scripts like **Python and shell scripts**.
4. Database management and backup with scripts like **SQL and Python**.
5. Monitoring and logging with scripts like **Nagios and Logstash**.
6. Deployment pipeline automation with scripts like **Jenkinsfile and TravisCI**.
7. Infrastructure as code (IaC) with scripts like **Terraform and CloudFormation**.
8. Health check and system maintenance with scripts like **Python and shell scripts**.
9. Automated data processing and analysis with scripts like **Python and R**.
10. And lastly automated network configuration with scripts like **Python and Ansible**.

--- 

# 10 most important Python modules for DevOps

1. **Paramiko**: Python module for ***SSH connections and SFTP.***
[Paramiko documentation](https://www.paramiko.org/)

2. **Fabric**: Python library for ***executing shell commands remotely over SSH.***.
[Fabric documentation](https://www.fabfile.org/)
3. **Boto3**: Python module for ***AWS SDK, allowing Python developers to interact with AWS services***.
[Boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
4. **Ansible**: Python module for ***configuration management and automation***.
[Ansible documentation](https://docs.ansible.com/ansible/latest/index.html)
5. **Flask**: Python micro-framework for ***building web applications***.
[Flask documentation](https://flask.palletsprojects.com/en/2.2.x/)
6. **PyYAML**: Python module for ***parsing and emitting YAML*** (yet another markup language).
[PyYAML documentation](https://wiki.python.org/moin/YAML)
7. **Django**: Python web framework for ***building complex, database-driven websites***.
[Django documentation](https://docs.djangoproject.com/en/4.1/)
8. **NumPy**: Python module for ***numerical computing with support for a wide range of mathematical functions***.
[NumPy documentation](https://numpy.org/doc/stable/)
9. **Pandas**: Python module for ***data analysis and manipulation, providing fast, flexible, and expressive data structures***.
[Pandas documentation](https://pandasguide.readthedocs.io/en/latest/)
10. **Matplotlib**: Python module for ***plotting and visualizing data***.
[Marplotlib documentation](https://matplotlib.org/stable/index.html)


## Example of a simple Python script
###  downloads a webpage and saves it to a file:

```python 
import requests

url = 'https://www.example.com'
response = requests.get(url)

with open('example.html', 'w') as f:
    f.write(response.text)

```

- This scripts uses the `requests` module to download the content of a webpage specified by the URL. 

- The `requests.get(URL)` function sends a **GET** request to the specified URL and returns the response. 

- The response content is the written to a file name `example.html` using `with` statement and the `write` method of the file object.

### Use case:

This script could be useful for ***automating regular backups of websites*** or ***for storing a local copy of webpages for offline use***.

The script can be run regularly using a task scheduler such as `cron` on Linux or `Task Scheduler` on Windows systems. 



