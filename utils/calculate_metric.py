import logging
import os
from shutil import make_archive, unpack_archive
import subprocess


def calculate_tiou(model_results: str, dataset_gt: str) -> None:
    """Function allows to calculate TIoU and IoU metrics.
    
    Params:
        model_results (str): path to model results with structure
            - model/dataset/ and contains predictions
        dataset_gt (str): path to dataset gt annotations

    """
    logging.info(f"Create metrics structure!")
    metrics_path = os.path.join(model_results, 'metrics')
    os.makedirs(metrics_path, exist_ok=True)
    predictions = os.path.join(model_results, 'predictions')

    gt_archive = make_archive(os.path.join(metrics_path, 'gt') ,'zip', dataset_gt)
    predictions_archive = make_archive(predictions,'zip', predictions)
    logging.info(f"Start subprocess!!")
    status = subprocess.run(["python", "./protocols/TIoU/ic15/script.py", f"-g={gt_archive}", f"-s={predictions_archive}", f"-o={metrics_path}"],capture_output=True)
    for path_to_remove in [gt_archive, predictions_archive]:
        os.remove(path_to_remove)
    unpack_archive(os.path.join(metrics_path, 'results.zip'), metrics_path)
    logging.info(f"Metrics has been calculated for {model_results}!. Status: {status.returncode}.") #0 means ok