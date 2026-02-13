import os
import glob

base_dir = "audio/condition_10_filter"

conditions = [
    "slow_flat_soft", "slow_flat_loud",
    "slow_dynamic_soft", "slow_dynamic_loud",
    "fast_flat_soft", "fast_flat_loud",
    "fast_dynamic_soft", "fast_dynamic_loud"
]

html = []
html.append("<html><body>")
html.append("<h1>Condition 10 Filter Audio Samples</h1>")

for cond in conditions:
    html.append(f"<h2>{cond}</h2>")
    
    wav_files = sorted(glob.glob(os.path.join(base_dir, cond, "*.wav")))
    
    for wav in wav_files:
        rel_path = wav
        filename = os.path.basename(wav)
        
        html.append(f"<p>{filename}</p>")
        html.append(f"""
        <audio controls>
            <source src="{rel_path}" type="audio/wav">
        </audio>
        <br><br>
        """)

html.append("</body></html>")

with open("audio_demo.html", "w") as f:
    f.write("\n".join(html))

print("HTML generated: audio_demo.html")
