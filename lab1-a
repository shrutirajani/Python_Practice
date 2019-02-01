{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "data = pd.read_csv(\"adult.csv\",delimiter=',')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [],
   "source": [
    "df=data.replace(' ?', np.NaN)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "age               False\n",
       "workclass          True\n",
       "fnlwgt            False\n",
       "education         False\n",
       "education-num     False\n",
       "marital-status    False\n",
       "occupation         True\n",
       "relationship      False\n",
       "race              False\n",
       "sex               False\n",
       "capital-gain      False\n",
       "capital-loss      False\n",
       "hours-per-week    False\n",
       "native-country     True\n",
       "Salary            False\n",
       "dtype: bool"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().any()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "age               21999\n",
       "workclass         21999\n",
       "fnlwgt            21999\n",
       "education         21999\n",
       "education-num     21999\n",
       "marital-status    21999\n",
       "occupation        21999\n",
       "relationship      21999\n",
       "race              21999\n",
       "sex               21999\n",
       "capital-gain      21999\n",
       "capital-loss      21999\n",
       "hours-per-week    21999\n",
       "native-country    21999\n",
       "Salary            21999\n",
       "dtype: int64"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[(data['native-country']==' United-States') & (data['Salary']==' <=50K')].count()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "age               7171\n",
       "workclass         7171\n",
       "fnlwgt            7171\n",
       "education         7171\n",
       "education-num     7171\n",
       "marital-status    7171\n",
       "occupation        7171\n",
       "relationship      7171\n",
       "race              7171\n",
       "sex               7171\n",
       "capital-gain      7171\n",
       "capital-loss      7171\n",
       "hours-per-week    7171\n",
       "native-country    7171\n",
       "Salary            7171\n",
       "dtype: int64"
      ]
     },
     "execution_count": 78,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data[(data['native-country']==' United-States') & (data['Salary']==' >50K')].count()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "age               21999\n",
       "workclass         21999\n",
       "fnlwgt            21999\n",
       "education         21999\n",
       "education-num     21999\n",
       "marital-status    21999\n",
       "occupation        21999\n",
       "relationship      21999\n",
       "race              21999\n",
       "sex               21999\n",
       "capital-gain      21999\n",
       "capital-loss      21999\n",
       "hours-per-week    21999\n",
       "native-country    21999\n",
       "Salary            21999\n",
       "dtype: int64"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "data[(data['native-country']==' United-States') & (data['Salary']==' <=50K')].count(age)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
