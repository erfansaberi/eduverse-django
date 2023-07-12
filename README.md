# EduVerse (Backend)
An E-learning website backend, written in Django

## How to run?
### Development (APIs only)
1. Rename *.env.dev-sample* to *.env.dev*
2. Update the environment variables in the *docker-compose.yml* and *.env.dev* files
3. Build and run using:
    ```sh
    $ docker-compose up -d --build
    ```
4. Test the apis at [http://localhost:8000](http://localhost:8000)

### Production (Full project)
1. Rename *.env.prod-sample* to *.env.prod* and *.env.prod.db-sample* to *.env.prod.db* and update the environment variables.
2. Give execution permission to deploy.sh script and then run it by:
    ```sh
    $ chmod +x ./deploy.sh
    $ ./deploy.sh
    ```
    This will build the nuxt client app and move it to nginx/client folder, and then calls docker-compose to build and run the system. You can manually build the nuxt client and move the dist/ folder to nginx/client/ and then call docker-compose with command:
    ```sh
    $ docker-compose -f docker-compose.prod.yml up -d --build
    ```
3. Test the system at [http://localhost](http://localhost)

### Note
If you faced permission problem with the entrypoint scripts, you should give execution access to this files. Use commands:
```sh
~ chmod +x entrypoint.sh
~ chmod +x entrypoint.prod.sh
```