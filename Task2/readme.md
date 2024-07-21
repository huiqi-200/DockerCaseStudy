Using : https://github.com/docker-library/postgres/blob/d08757ccb56ee047efd76c41dbc148e2e2c4f68f/16/bookworm/Dockerfile for the Postgres Image

## Set up:
In Test2 (current directory),
1. Create a .env file with the following environment variables:  
    <code> POSTGRES_USER  =
            POSTGRES_PASSWORD  =  
            POSTGRES_DB = 
    </code>
    This will be called with the docker-compose.yml 

Commands to run in CMD:
1. cd to Task2 folder
2. <code> docker compose up </code>
 (will create postgres image and run the ddl sql scripts)
To access postgres server -   
    Requires opening the terminal of the running postgres container:   
3. Enter the following command in the shell:
    <code>psql -h localhost -p 5432 -U <POSTGRES_USER> -d <POSTGRES_DB> </code>   
    This should return the following:  
    <code> psql <version number>
    Type "help" for help.

    <POSTGRES_DB>=# 
    </code>
4. Check tables are in:  
    <code>\dt</code>




## Issues encountered: 
1. Authentication error when using own username and password defined in .env:
    Causes: 
    1. A local installation of Postgres exists, with its own set of users.  
        Removing it and building the docker image again resolved the issue.