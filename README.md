# PythonPy.org
New website for Python Paraguay

### Prerequisites
* Python >= 3.6
* PostgreSQL >= 10+

### Dependencies
* Django >=2.2
* Wagtail >=2.6

### Getting started

```bash
git clone git@github.com:PythonParaguay/PythonPy.org.git
cd PythonPy.org
python3 -m venv env
source env/bin/activate
pip install -r requirements

```
### Environment variables

You can edit and rename `dotenv.example` to `.env` and it would load at the start.
If you choose other method you're gonna need to define this this environment variables:
```bash
DB_NAME_DEV="pythonpy_dev"
DB_USER_DEV=""
DB_PASSW_DEV=""
DB_HOST_DEV="localhost"
DB_HOST_PORT="5432"
SECRET_KEY_DEV="CHANGE_THIS_PUT_A_50_CHAR_RANDOM_STRING"
```

### First run

```bash
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
```
To load sample data (Optional)

```
./manage.py loaddata test_data.json
```


## TODO

- ~~Proper~~ better frontend
- Unit tests
- Documentation

## Contributing
 
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## License

This project is licensed under the terms of the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details
