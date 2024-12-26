from pyscript import display
import matplotlib.pyplot as plt
from datetime import datetime

# サンプルデータの作成
dates = [datetime(2023, i, 1) for i in range(1, 13)]
deploy_frequency = [5, 7, 6, 8, 7, 9, 10, 12, 11, 13, 14, 15]
lead_time = [2.5, 2.0, 1.8, 1.5, 1.7, 1.4, 1.3, 1.2, 1.1, 1.0, 0.9, 0.8]
change_failure_rate = [0.05, 0.04, 0.06, 0.05, 0.04, 0.03, 0.02, 0.03, 0.02, 0.01, 0.01, 0.01]
time_to_restore = [30, 28, 25, 20, 18, 15, 14, 12, 10, 8, 7, 5]

# グラフ描画関数
def plot_metric(dates, values, title, xlabel, ylabel, target_id, color='blue'):
    fig, ax = plt.subplots(figsize=(6, 4))  # グラフサイズを指定
    ax.plot(dates, values, marker='o', color=color)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    display(fig, target=target_id)

# Plot each metric
plot_metric(dates, deploy_frequency, 'Deployment Frequency', 'Date', 'Number of Deployments', 'deploy-frequency')
plot_metric(dates, lead_time, 'Lead Time for Changes', 'Date', 'Lead Time (Days)', 'lead-time', color='orange')
plot_metric(dates, change_failure_rate, 'Change Failure Rate', 'Date', 'Failure Rate', 'change-failure-rate', color='red')
plot_metric(dates, time_to_restore, 'Time to Restore Service', 'Date', 'Recovery Time (Minutes)', 'time-to-restore', color='green')