# Building
```sh
python setup.py sdist
```
# Installing
```sh
pip install <package_path> --upgrade
```
# How to use
For one processor running
```
python -m chess_calculator.server
```
For multi processes running
```
pip install uwsgi
uwsgi -w chess_calculator.server:app <other uwsgi options>
```
For example:
```
uwsgi --http :8000  -w chess_calculator.server:app --master --processes 8
```
# API
endpoint: /
method: only POST (for JSON exchange)
body:
```
{
    "n": <int>
    "chessPiece": "queen"|"knight"|"rook"|"bishop"
}
```
response:
```
{
    "solutionsCount": <int>
}
```
# What can improve
Add parameters(port, ip address) for one process mode.
Current algorithm supports calculation in case when figure count is not equal linear size of a board. Add this feature to API.
