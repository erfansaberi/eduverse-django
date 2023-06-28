# EduVerse (Backend)
An E-learning website backend, written in Django

## How to run?
### Development
1. Rename *.env.dev-sample* to *.env.dev*
2. Update the environment variables in the *docker-compose.yml* and *.env.dev* files
3. Build and run using:
    ```sh
    $ docker-compose up -d --build
    ```
4. Test the apis at [http://localhost:8000](http://localhost:8000)

### Production
1. Renamce *.env.prod-sample* to *.env.prod* and *.env.prod.db-sample* to *.env.prod.db* and update the environment variables.
2. Build and run using:
    ```sh
    $ docker-compose -f docker-compose.prod.yml up -d --build
    ```
3. Test the system at [http://localhost](http://localhost)