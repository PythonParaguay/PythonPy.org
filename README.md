# PythonPy.org
New website for Python Paraguay

### Prerequisites
* Python >= 3.6
* Virtualenv

### Dependencies
* Django >=2.0
* Wagtail >=2.0

### Getting started

```
git clone git@github.com:PythonParaguay/PythonPy.org.git
cd PythonPy.org
pip install virtualenv
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
```
To load sample data (Optional)

`./manage.py loaddata test_data.json`

## TODO

- Frontend
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