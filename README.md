# elevator_app
Moving elevators

## Environment

For this project Anaconda is used.

Create a new environment
```
conda env create -f environment.yml
```

Import changes to an existing environment
```
conda env update --file environment.yml
```

Exporting the current environment (top dependencies only)
```
conda env export --from-history | grep -v "^prefix: " > environment.yml
```

## Starting and running the application
The application is started with (in the terminal)
```
cd elevator_app/  # Make sure we are in the project root folder for this project
docker-compose up
```
and then available in the browser at ```http://0.0.0.0:5000```.
