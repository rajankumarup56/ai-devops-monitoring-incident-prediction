import numpy as np

def detect_anomaly(data):
    mean = np.mean(data)
    std = np.std(data)
    threshold = mean + 2 * std

    anomalies = [x for x in data if x > threshold]
    return anomalies

sample_metrics = [20, 22, 21, 23, 50, 22, 21]
print("Detected anomalies:", detect_anomaly(sample_metrics))
