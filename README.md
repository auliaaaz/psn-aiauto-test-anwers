
## **Calculate Total Downtime Device**

### **Overview**

This guide explains how to calculate the total downtime for a device network using CSV data. Each row in the dataset contains a timestamp and a status value, where the status can be either 'down' (represented by 1) or 'up' (represented by 0).

Before performing the downtime calculation, the script first executes a data cleaning process. This includes handling missing values and converting data types to ensure that the dataset is properly prepared for accurate analysis.

The downtime calculation works as follows:

-   For each segment where the system status is 'down' (1), look for the next occurrence where the status changes to 'up' (0). Calculate the downtime as the difference between the timestamp when the system was 'down' and the timestamp when it transitions to 'up' (i.e., `datetime(value=0) - datetime(value=1)`).
-   If the system remains 'down' (1) until the end of the dataset without transitioning to 'up' (0), calculate the total downtime as the difference between the timestamp of the first 'down' entry and the last 'down' entry.

For detailed code and manual calculations on sample data, refer to the provided Jupyter notebook (`.ipynb` file). 

### **How to run the code?**
1. Clone the repository that contains the Python script to your local machine. Open your terminal and run:
   
  ```
  git clone https://github.com/yourusername/your-repository.git
  ```

2. Navigate to the Project Directory
Change to the directory where the repository was cloned:

  ```
  cd your-repository
  ``` 

3. Create a Virtual Environment (Optional)
  ```
  python -m venv venv
  ```

	Activate the virtual environment:

-   **On Windows:**
    ```
    venv\Scripts\activate
    ```
    
-   **On macOS/Linux:**
    ```
    source venv/bin/activate
    ``` 
4. Install Dependencies
Ensure you have `pandas` and `numpy` installed. Can be do with

```
 pip install pandas numpy
```

5. Ensure the CSV file named `device_network_data.csv` and adjust `path_to_file\` directory. If the file is in a different location, update the file path in the script accordingly.

6. Run the python file with:
  ```
  python calculate_downtime.py
  ```

If it run expectedly it will return 58310.0 (seconds) as the result of total downtime calculation. 

If it grouped by each day, it will be shown that on 2023-12-31 total downtime was 23104.0 seconds and on 2024-01-01 total downtime was 35183.0 seconds (refer Jupyter notebook file)
