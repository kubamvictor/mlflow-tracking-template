import mlflow
import os

os.environ['MLFLOW_TRACKING_TOKEN'] = 'YHON36336hhngEYEY'

# Configure mlflow: Location to save all mlflow related data
remote_server_uri = "http://localhost:8000"

if 'http' in remote_server_uri:
    remote_server_uri = remote_server_uri
else:
    remote_server_uri = 'file:'+remote_server_uri

try:
    # Pointing mlflow to the where it has to save its data
    mlflow.set_tracking_uri(remote_server_uri)
    # Experiment name
    mlflow.set_experiment("/experiment-name")
    mlflow_tracking = True
except Exception:
    mlflow_tracking = False


# Start run
if mlflow_tracking:
    mlflow.start_run()


# Start tracking
if mlflow_tracking:
    mlflow.log_param("hello", "World")
    mlflow.log_metric("acc", 0.99)

# End run
if mlflow_tracking:
    mlflow.end_run()


# MLflow UI
# mlflow server - -backend-store-uri < remote_server_uri > - -default-artifact-root < remote_server_uri > - -host 0.0.0.0: 5000
