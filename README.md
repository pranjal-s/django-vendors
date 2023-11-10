# django-vendors

**Purpose**: Development of a multi-featured marketplace website.

**About**: A tutorial of Python-based Django website for vendors marketplace.

**Dependency**: Anaconda3 for Windows

**Usage**:

*Step 1a*. virtual environment via Anaconda
```
C:\ProgramData\Anaconda3\Scripts\activate
```

*Step 1b*. create via environment.yml
```
conda env create -f environment.yml
```

*Step 1c*. activate virtual environment
```
conda activate vendors
```

*Step 2a*. run server and open in browser
```
python manage.py runserver
# Ctrl+click on local development server link (http://localhost:8000)
# Ctrl+C to quit the server
```

*Step 2b*. remove virtual environment
```
conda env remove --name vendors
```

**Q&A**: If you have any questions, feel free to add an issue in this repository.