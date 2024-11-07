Here’s a basic structure for a **README.md** file that includes the Google Drive folder link for the `.pkl` files and provides an overview of the project.

### **README.md** Template:

```markdown
# Youtube Sentimental Analysis

## Overview

This project implements a sentiment analysis tool for YouTube comments using machine learning techniques. The core part of the project involves analyzing YouTube video comments to categorize them into different sentiment classes using a pre-trained model. This model uses a **Random Forest classifier** and is stored in a `.pkl` file.

### Features:
- Sentiment analysis of YouTube comments.
- Interactive visualization of sentiment distribution.
- Easy-to-use interface for users to input YouTube video links and get sentiment analysis results.

## Project Structure

```bash
.
├── final_output/           # Folder for output charts
├── templates/              # Folder for HTML templates
├── uploads/                # Folder for uploaded files
└── random_forest_model.pkl # Pre-trained Random Forest model for sentiment analysis
```

## Pre-trained Model

The project relies on a **Random Forest model** (`random_forest_model.pkl`) to classify the sentiments of the comments. You can download the pre-trained model files from the Google Drive link below.

**Download the model:**

[Google Drive - Pretrained Models](https://drive.google.com/drive/folders/1Pw7C_syJAycM8p6y2-BwF8L_rERtmlmQ?usp=sharing)

> Make sure to place the `random_forest_model.pkl` file in the root directory of the project.

## Installation

### Prerequisites

- Python 3.x
- Required Python libraries:
  - `flask`
  - `sklearn`
  - `pandas`
  - `numpy`
  - `matplotlib`

You can install the necessary libraries using the following command:

```bash
pip install -r requirements.txt
```

### Running the Project

1. Clone the repository to your local machine:

```bash
git clone https://github.com/sujal-9999/Youtube-Sentimental-Analysis.git
```

2. Navigate to the project directory:

```bash
cd Youtube-Sentimental-Analysis
```

3. Start the Flask web application:

```bash
python app.py
```

4. Open a browser and go to `http://127.0.0.1:5000/` to start using the tool.

## Contributing

Feel free to fork this project and submit pull requests for improvements, bug fixes, or additional features. Contributions are always welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

### Steps to include:
1. **Google Drive Link**: The Google Drive link is placed under the **Pre-trained Model** section so that users can download the necessary `.pkl` files.
2. **Project Structure**: I’ve provided an example directory structure so users can understand how the project is organized.
3. **Instructions to Install and Run**: Clear steps for setting up and running the project, including the necessary dependencies.

#### Additional Notes:
- Ensure that your **`random_forest_model.pkl`** is placed in the **root directory** of the project or specify the path where it's located.
- You may also include a `requirements.txt` file in the root directory listing the dependencies, which can be generated using:

```bash
pip freeze > requirements.txt
```

This structure will provide clear guidance to users or collaborators who want to set up your project. Let me know if you need any changes!
