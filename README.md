# <span style="color:#f9b000">OpenAI Django Tutorial</span>

## Prerequisites
* [Docker & Docker Compose](https://docs.docker.com/desktop/) (<span style="color:orange">Local Development with Docker</span> only)


***

## Repository
Clone or pull from the dev branch before you begin coding.
```
#cloning
git clone git@github.com:sabih1996/django-openAI.git .

```

***
***



## Environment variable and secrets
1. Create a .env file from .env.template
    ```
    #Unix and MacOS
    cd backend && cp .env.template .env
    ```

2. Add your ChatGPT api key tha can be found [here](https://platform.openai.com/account/api-keys)

***
***

## Fire up Docker:

>Note: You will need to make sure Docker is running on your machine!

Use the following command to build the docker images:
```
docker-compose  up -d --build
```

Alternatively, If you have [make](https://platform.openai.com/account/api-keys) installed, you can run the following command:
```
make build
```

### Finished
You should now be up and running!

* The web app is running on  http://localhost:8000

***
***

### References
This project is based on the official ChatGPT quick-start tutorial that can be found [here](https://platform.openai.com/docs/quickstart/build-your-application)

The Flask app that this Django app is based on can be found [here](https://github.com/openai/openai-quickstart-python)