import mlflow

# Configure mlflow: Location to save all mlflow related data
remote_server_uri = "/Users/Kubam/projects/machine_learning/data/mlflow"

# Pointing mlflow to the where it has to save its data
mlflow.set_tracking_uri("file:"+remote_server_uri)

# Experiment name
mlflow.set_experiment("/experiment-name")

# Start run
mlflow.start_run()


# Start tracking
mlflow.log_param("hello", "World")
mlflow.log_metric("acc", 0.99)

# End run
mlflow.end_run()


# MLflow UI
# mlflow server - -backend-store-uri < remote_server_uri > - -default-artifact-root < remote_server_uri > - -host 0.0.0.0: 5000
