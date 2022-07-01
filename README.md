## Github popularity Check

#### this service check the popularity of the repository
#### a repository is popular when the `score >= 500` where `score = num_stars * 1 + num_forks * 2`

### the libraries we have used 
1. FastAPI
2. unicorn
3. httpx
4. pydantic[dotenv]
***
#### NOTE: you you should install the env support version of `pydantic` to have the environment variable file `.env` be supported
$ `pip install pydantic[dotenv]`
#### with this you can make your own `.env` file, take a look at the `.env.sample` to see what variable we support.
***
### in order to build the Docker image enter the below comnad 
$ `docker build -t my_github_popularity_check .`

### then you can run the image with docker compoer
$ `docker-compose up`

#### NOTE: if you are not familiar with Docker please take a look at the [documentation](https://docs.docker.com/)
***
#### to run the tests enter the command below
$ ` pytest  tests/`
#### to run tests with coverage
$ `pytest --cov-report html --cov=. tests/`
***
#### to run the server locally simple enter the command in the root folder 
`python main.py` 
***

### improvements in future:
1. handle rate limits from the [Github API](https://docs.github.com/en/rest/rate-limit#about-the-rate-limit-api)
2. implement load test with [siege](https://github.com/JoeDog/siege)

### NOTE: 
before committing new changes please run the command `tox` to make sure some PEP8 rules are fixed 

you can modify tox configs in `tox.ini` file