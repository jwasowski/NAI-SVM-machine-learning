# NAI - AI tools classes - SVM algorithm
The script is learning AI using SVM algorithm. The purpose is to allow AI to predict 100km car ride cost. <br />


### Requirements
```
Anaconda (Python 3.7) or Python 3.7
Python IDE (for development)
Data files uploaded along with the script ('learning_data_set.txt' and 'data_classification.txt')

```

### Short data description

AI during learning is fed with 5 parameters. These parameters are: <br />
```
engine capacity - float value (example 1.6)
horsepower - int value (example 125)
fuel consumption - float value (example 8.8)
fuel type - int value (example 1), there are available only two values (1 and 2). 1 is for gas and 2 is for diesel.
data classificator - int value (example 2), see Data classification description section.
```
Data is extracted from https://www.autocentrum.pl/spalanie/

#### Data classification description

Data classificator value is described by following table:

| Value | cost range in 'PLN' |
| ------------- | ------------- |
| 1  | 20-25  |
| 2  | 25-27  |
| 3  | 27-30  |
| 4  | 30-33  |
| 5  | 33-36  |
| 6  | 36-39  |
| 7  | 39-42  |
| 8  | 42-45  |
| 9  | 45-48  |
| 10  | 48-52  |
| 11  | 52-56  |
| 12  | 56-60  |
| 13  | 60-65  |
| 14  | 65-70  |
| 15  | 70-75  |
| 16  | 75-80  |
| 17  | 80-90  |


### Running Application

To run script use following syntax in Python console <br />
Script requires 4 arguments, below table contains argument descriptions: <br />

| Argument name | Argument description | Example value |
| ------------- | ------------- | ------------- |
| `$value1`  | Engine capacity  | 2.0  |
| `$value2`  | Horsepower  | 180  |
| `$value3`  | Desired fuel consumption  | 8.5  |
| `$value4`  | Fuel type  | 1  |
```
In Spyder IDE (Anaconda):
runfile('disk:\path\to\script\JW_SVM.py', args='-l $value,$value2,$value3,$value4', wdir='disk:\path\to\script\')

Example usage:
runfile('D:/Informatyka/NAI/lab5/JW_SVM.py', args='-l 2.0,180,8.8,d', wdir='D:/Informatyka/NAI/lab5')

In Anaconda terminal (use it inside folder containing script):
python JW_SVM.py -l 1.6,125,8.8,1

In PyCharm IDE (Python):
JW_SVM.py -l 1.6,125,8.8,1

In Python terminal (not tested, but it should work):
python JW_SVM.py -l 1.6,125,8.8,1

```


## Authors

* **Jakub Wąsowski** - [JWasowski](https://github.com/jwasowski) 