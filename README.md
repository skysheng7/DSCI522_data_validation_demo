# Data Validation Demo

This repository contains instructions and code we use in UBC Master of Data Science DSCI 522 Lecture 4: Data Validation, and Lecture 5: Non-interactive Scripts.

Instructor: Sky Sheng

Author of original code & setup: Tiffany Timbers

## About

This repository demonstrates data validation techniques in a data science workflow using the breast cancer predictor example.

## Dependencies

- [Docker](https://www.docker.com/) 
- [VS Code](https://code.visualstudio.com/download)
- [VS Code Jupyter Extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)

## Usage

### Setup

> If you are using Windows or Mac, make sure Docker Desktop is running.

1. Clone this GitHub repository.

### Running the analysis

1. Navigate to the root of this project on your computer using the
   command line and enter the following command:

```bash
docker compose up
```

2. In the terminal, look for a URL that starts with 
`http://127.0.0.1:8888/lab?token=` 
Copy and paste that URL into your browser.

3. To run the analysis,
open `notebooks/breast_cancer_predictor_report.ipynb` in Jupyter Lab
and under the "Kernel" menu click "Restart Kernel and Run All Cells...".

### Clean up

1. To shut down the container and clean up the resources, 
type `Ctrl` + `C` in the terminal
where you launched the container, and then type `docker compose rm`

## Acknowledgement 

This demo is built upon materials from Tiffany Timbers' [breast-cancer-predictor](https://github.com/ttimbers/breast-cancer-predictor) repository. Some code examples are adapted from the [UBC DSCI Reproducible and Trustworthy Workflows for Data Science course materials on Python Data Validation with Pandera](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/lectures/135-data_validation-python-pandera.html). See the [LICENSE](LICENSE) file for detailed licensing information.