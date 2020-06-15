import mlflow

# Configure mlflow
remote_server_uri = "/Users/Kubam/projects/machine_learning/data/mlflow"

mlflow.set_tracking_uri("file:"+remote_server_uri)
mlflow.set_experiment("/experiment-name")

# Start run
mlflow.start_run()


# Start tracking
mlflow.log_param("hello", "World")
mlflow.log_metric("acc", 0.99)

# End run
mlflow.end_run()


# See ui
# mlflow server - -backend-store-uri < remote_server_uri > - -default-artifact-root < remote_server_uri > - -host 0.0.0.0: 5000
