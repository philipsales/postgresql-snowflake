

# SnowFlake Design - Data Modeling with Postgres #
Schema design for datawarehousing approach using 
- PostgreSQL as the database
- Python as the ETL scripting language
- Pandas as dataframe library
- Jupyter Notebook as IDE
- DBeaver as SQL Schema visualizer (optional)

## Tested Environment ##
- [x] MacOS based machine - Local.
- [x] Linux based machine - Local. 
- [ ] Windows based machine. 

## Folder and File description ##
- data - contains the subset or sample dataset
- create_tables.py - contains the PostgreSQL connection set-up 
- sql_queries.py - contains the Data Definition Languages of the schema
- etl.ipynb - jupyter notebook use for local development
- etl.py - python script use for production
- test.ipynb - SQL query testing scripts

## Application Dependencies ##

| Dependencies | Versions |
| ------------ | -------- |
| Python       | 3.6.3    |
| PostgreSQL   | 10.5     |

### Instructions ###

1. Activate python environment (if applicable)
    ```
    source ~/<python_env_directory>/bin/activate 
    ```
1. Start PostgreSQL database (for Mac only)
    ```
    brew services start postgresql
    ```
1. Establish connection to database 
    ```
    cd <project_directory>
    python -B create_tables.py
    ```
1. Run the ETL script
    ```
    python -B etl.py
    ```

1. Verify if data were inserted in the database by running the  [test.ipynb](test.ipynb) in the jupyter notebook

## Built With ##
[x] Python

## Contributor ##
* **Philip Sales** - author
* **Yung-Chun L** - mentor

## Versioning ##
1.0.0

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments ##

* Open Source Community 

