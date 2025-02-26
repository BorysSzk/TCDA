# TCDA

## Titanic Casualty Data Analyzer (TCDA) - what is it?
TCDA is an app written in Python designed to analyze available data regarding casualties of the Titanic tragedy. In this app you can explore the Titanic casualty data, analyze it with the help of a few visualizations 
and analytical interpretations - all of this throughout a user-friendly command line interface.

## Build Prerequisites
TCDA's build environment requires only Python and a couple of libraries (libs in `Installation` tab):
- Python 3.11.9 or newer from [here](https://www.python.org/downloads/);

## Installation
Clone the repository to your computer with:
```sh
git clone https://github.com/BorysSzk/TCDA.git
```
If you don't have Git installed, you can download the repository as a ZIP file from the repository page.

After cloning/downloading the repository, navigate to the project directory (`TCDA-main` folder) in your terminal and run the following command to install the libraries:
```sh
pip install -r requirements.txt
```

## Running TCDA
1. Make sure you are in the project directory.
2. To start the app, run:
```sh
python main.py
```
The app will launch in your terminal and you will see aforementioned interactive command line interface, which will let you "move" around the app.<br>
> [!NOTE]
> For better visual experience launch the app in your terminal on fullscreen.

## Dataset
The dataset used in this app comes from [this Kaggle's Machine Learning competition](https://www.kaggle.com/c/titanic/data).

## Tech Stack
* Python
* Pandas
* Matplotlib (Pyplot)
* Seaborn
* Python's built-in `os` and `time` libraries
