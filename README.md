# PythonPy.org
New website for Python Paraguay

### Prerequisites
* Python >= 3.6

### Dependencies
* Django >=2.2
* Wagtail >=2.6

### Getting started

```
git clone git@github.com:PythonParaguay/PythonPy.org.git
cd PythonPy.org
python3 -m venv env
source env/bin/activate
pip install -r requirements
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
```
To load sample data (Optional)

```
./manage.py loaddata test_data.json
```

## TODO

- ~~Proper~~ frontend
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
