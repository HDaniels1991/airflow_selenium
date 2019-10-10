
## Selenium on Airflow

The main goal of this post is to develop a plugin which utilises Selenium, to automate a mundane task, on Airflow.

The post will be structured as follows:
1. Setting up the custom Airflow environment.
2. Defining the Selenium Airflow plugin.
3. An example DAG. Donwloading a podcast and uploading the file to S3.

## Setting up the Airflow environment:

### The base Airflow environment:

XXX

1. Custom plugins.
2. Host
3. Rename compose file.

Pic.

### Modifying the environment to work with the plugin. 

Before completing the environment, it is neccessary to briefly explain how the Selenium plugin will work as some of its functionality will directly impact setup. The plugin will be covered in greater detail later in the post. 
The plugin will need to execute the following steps:
1. Start Selenium docker container.
2. Configure Selenium remote driver.
3. Run the Selenium script: The script will result in a specific file downloaded from the internet.
4. Remove the running Selenium container.

The steps above can be distilled into two categories:
* Using Docker
* Interacting with the new Selenium Docker container.

#### Using Docker:

What does this mean ...

1. DIND, WHAT IS REQUIRED, dockerfile and compose.
2. container bridge network.

#### Interacting with the remote container: 

What does this mean ...

1. Python Path, mounted volume. 
2. named downloads volume, downloads permissions and compose file.

#### Final scripts:

* airflow_dockerfile
GIST

```
docker build -t docker_airflow -f airflow_dockerfile .
```

* selenium_dockerfile
GIST

```
docker build -t docker_selenium -f selenium_dockerfile .
```

*. docker-compose
```
docker-compose up
```

## The Selenium Plugin


