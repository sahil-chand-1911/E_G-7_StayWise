import os
import subprocess
import sys
import time

def run_notebook(notebook_path):
    print(f"--- Executing {notebook_path} ---")
    start_time = time.time()
    
    # Try different ways to call nbconvert
    commands = [
        ["jupyter", "nbconvert", "--to", "notebook", "--execute", "--inplace", notebook_path],
        [sys.executable, "-m", "jupyter", "nbconvert", "--to", "notebook", "--execute", "--inplace", notebook_path],
        [sys.executable, "-m", "nbconvert", "--to", "notebook", "--execute", "--inplace", notebook_path]
    ]
    
    success = False
    last_error = ""
    
    for cmd in commands:
        try:
            result = subprocess.run(cmd, check=True, capture_output=True, text=True)
            success = True
            break
        except Exception as e:
            last_error = str(e)
            continue
            
    if success:
        elapsed = time.time() - start_time
        print(f"Successfully finished {notebook_path} in {elapsed:.2f}s\n")
        return True
    else:
        print(f"Error executing {notebook_path}: {last_error}")
        return False

def main():
    # Identify project root
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(script_dir, '..'))
    os.chdir(project_root)
    
    notebooks = [
        'notebooks/01_loading.ipynb',
        'notebooks/02_cleaning.ipynb',
        'notebooks/03_eda.ipynb',
        'notebooks/04_statistical_analysis.ipynb',
        'notebooks/05_final_load_prep.ipynb'
    ]
    
    print(f"Starting ETL Pipeline in {project_root}...")
    
    overall_success = True
    for nb in notebooks:
        if not os.path.exists(nb):
            print(f"File not found: {nb}")
            overall_success = False
            break
            
        if not run_notebook(nb):
            overall_success = False
            break
            
    if overall_success:
        print("Pipeline execution complete. Final datasets are available in /data/processed and root directory.")
    else:
        print("Pipeline execution failed. Please check if jupyter and nbconvert are installed.")

if __name__ == "__main__":
    main()
