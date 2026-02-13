import os
import shutil
import glob

# ================= 路径配置 =================
SRC_ROOT = "./audio/condition_10_filter/"
DST_ROOT = "./audio"

conditions = [
    "slow_flat_soft", "slow_flat_loud",
    "slow_dynamic_soft", "slow_dynamic_loud",
    "fast_flat_soft", "fast_flat_loud",
    "fast_dynamic_soft", "fast_dynamic_loud"
]

print("开始复制并重命名...")

for cond in conditions:
    src_dir = os.path.join(SRC_ROOT, cond)
    dst_dir = os.path.join(DST_ROOT, cond)

    if not os.path.exists(src_dir):
        print(f"Warning: {src_dir} 不存在")
        continue

    os.makedirs(dst_dir, exist_ok=True)

    wav_files = glob.glob(os.path.join(src_dir, "*.wav"))

    for wav_path in wav_files:
        filename = os.path.basename(wav_path)

        # S01_3.wav → S01.wav
        speaker_id = filename.split("_")[0]
        new_filename = f"{speaker_id}.wav"

        dst_path = os.path.join(dst_dir, new_filename)

        # 如果担心覆盖，可以加判断
        if os.path.exists(dst_path):
            print(f"Warning: {dst_path} 已存在，将被覆盖")

        shutil.copy2(wav_path, dst_path)

print("完成 ✅")
