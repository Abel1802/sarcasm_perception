import os
import glob

base_dir = "audio/"

conditions = [
    "sarcsmtic", "genuine",
    "slow_flat_soft", "slow_flat_loud",
    "slow_dynamic_soft", "slow_dynamic_loud",
    "fast_flat_soft", "fast_flat_loud",
    "fast_dynamic_soft", "fast_dynamic_loud"
]

html = []

html.append("""
<html>
<head>
<style>
body {
    font-family: Arial, sans-serif;
}

.condition-block {
    margin-bottom: 40px;
}

.audio-row {
    display: flex;
    flex-wrap: wrap;   /* 自动换行 */
    gap: 15px;         /* 音频之间间距 */
}

.audio-item {
    text-align: center;
    width: 160px;
}

audio {
    width: 150px;
}
</style>
</head>
<body>
<h1>Audio Samples</h1>
""")

for cond in conditions:
    html.append(f'<div class="condition-block">')
    html.append(f"<h2>{cond}</h2>")
    html.append('<div class="audio-row">')
    
    wav_files = sorted(glob.glob(os.path.join(base_dir, cond, "*.wav")))
    
    for wav in wav_files:
        filename = os.path.basename(wav)
        
        html.append(f"""
        <div class="audio-item">
            <p>{filename}</p>
            <audio controls>
                <source src="{wav}" type="audio/wav">
            </audio>
        </div>
        """)

    html.append('</div>')  # close audio-row
    html.append('</div>')  # close condition-block

html.append("</body></html>")

with open("audio_demo.html", "w") as f:
    f.write("\n".join(html))

print("HTML generated: audio_demo.html")
