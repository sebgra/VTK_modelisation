# VTK Modelisation

Little standalone Python program for visualizing .vtk files, using PyQT5. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

<img src="https://github.com/sebgra/VTK_modelisation/blob/master/demo.gif"/>

### Prerequisites

* vtk
* PyQt5

<br/>

## Install Python dependencies

```
conda install -c anaconda vtk

conda install -c anaconda pyqt
```


## Running the script

Change the file location at line 331-332 of the code like : 

```
reader=vtk.vtkStructuredPointsReader()
reader.SetFileName("<your_file.vtk>")

```

## Built With

* [Python3](https://www.python.org/) - Language chosen
* [vtk](https://pypi.org/project/vtk/) - Used to read specific .vtk files
* [PyQt5](https://pypi.org/project/PyQt5/) - Used to build the interface


## Authors

* **Sébastien Gradit** - *Initial work* - [sebgra's github](https://github.com/sebgra)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is not  under any license 

