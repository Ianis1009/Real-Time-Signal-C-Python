import subprocess
import matplotlib.pyplot as plt
proc = subprocess.Popen(["./signal"],stdout=subprocess.PIPE,text=True)
dt = 0.05
data = []
time_data = []
for i in range(500):
    line = proc.stdout.readline()
    if not line:
        continue

    value = float(line.strip())
    data.append(value)
    time_data.append(i * dt)

plt.style.use("seaborn-v0_8-darkgrid")
fig, ax = plt.subplots(figsize=(10, 5))


ax.plot(time_data, data, linewidth=2, label="Damped Signal")
ax.set_title("Signal")
ax.set_xlabel("Time [s]")
ax.set_ylabel("Amplitude")

ax.grid(True, which="both", linestyle="--", linewidth=0.5)
ax.minorticks_on()
ax.legend()

plt.savefig("graph.png", dpi=300, bbox_inches="tight")
print("Saved: graph.png")