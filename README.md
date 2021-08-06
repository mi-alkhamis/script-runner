
[![GitHub issues](https://img.shields.io/badge/dws-dev--007--python-critical?style=plastic)](https://github.com/mi-alkhamis/script-runner)
[![GitHub issues](https://img.shields.io/github/issues/mi-alkhamis/script-runner?color=orange&style=plastic)](https://github.com/mi-alkhamis/script-runner/issues)
[![GitHub forks](https://img.shields.io/github/forks/mi-alkhamis/script-runner?style=plastic)](https://github.com/mi-alkhamis/script-runner/network)
[![GitHub license](https://img.shields.io/github/license/mi-alkhamis/script-runner?style=plastic)](https://github.com/mi-alkhamis/script-runner/blob/main/LICENSE)

# Script Runner
A simple script to run another script, if the script run without errors, return 0, if not return 1.
it's very useful to run specific code in a period of time as many as you want, like when checking DB service is up or not, it takes couple of minutes to go up, so its a good idea to check it automatically


## How to use
1. get a clone `git clone https://github.com/mi-alkhamis/script-runner.git ` 
2. set a environmnets variables 
3. run it

### Examples
`$ DWS_TESTER_COMMAND="./db_service_check.py"  DWS_TESTER_THRESHOLD=20 DWS_TESTER_INTERVAL=5  python main.py`

 it runs `db_service_check.py` 20 times every 5 seconds, if `db_service_check` return 0 (DB service is up), the script ended, if not, it runs 20 times


## To do
- [ ] run c++ script
- [ ] get script directly from environment variable

## Contribute

All contributions are welcome:
- Read the issues, fork the project and do a Pull Request.
- Request a new topic creating a New issue with the enhancement tag.
- Find any kind of errors in the cheat sheet and create a New issue with the details or fork the project and do a Pull Request.

## License

This project is licensed under the Apache-2.0 License  - see the [LICENSE](https://github.com/mi-alkhamis/script-runner/blob/main/LICENSE) file for details.

[@dwsclass](https://github.com/dwsclass) dws-dev-007-python

