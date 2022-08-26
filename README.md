# SwagLabs Automation Assignement
## _Automation Demo of Login feature using pytest framework_

## Installation

tested with Python 3.8+
- create a virtual environment
- clone repo `git clone https://github.com/atifmalik58/SwagLabs.git`
- move to project directory `cd SwagLabsProject`
- install dependencies by `pip install -r requirements.txt`




## How to Run Tests

For are quick Run, following command can be used to execute Login Test Suite:


```
pytest -v -s -n 6 --browser chrome --url https://www.saucedemo.com/ --html=report.html --self-contained-html
```


## Command Line Arguments Breakdown


- ```--browser```       (mandatory)\
    Browser choice at the time of execution. valid inputs are firefox, chrome, edge. Empty value would result in execution failure


- ```-v``` or ```-vv``` or ```-vvv```       (optional)\
    enables verbose output


- ```-s```     (optional)\
    disables capturing of stdout/stderr


- ```_-n <int>_```   (optional)

  No. of test cases to runs parallel   



- ```--url```  (optional)
 
  Application URL on which testing is to be performed.
  Default value is "https://www.saucedemo.com/"


- ```--html=report.html --self-contained-html```  (optional)
    
    To Generate Execution Report
