```
python3 -m venv venv
```

Activate the virtual environment:
```
source venv/bin/activate
```


Create a file called requirements.txt in the top level of your project directory with the following contents:
pygame==2.6.1
<br />
This tells Python that this project requires pygame version 2.6.1.

Install the requirements:
```
pip install -r requirements.txt
```
pip is Python's package manager. It will install the pygame module into the virtual environment you created.
<br />
Make sure pygame is installed:
```
python3 -m pygame
```
