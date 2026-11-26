import json
from datetime import datetime, timezone
from pathlib import Path

CHANNELS_FILE = Path("channels.json")


def fetch_latest_channels() -> dict[str, str]:
    # Đọc danh sách hiện tại để giữ lại link nào chưa cần đổi
    if CHANNELS_FILE.exists():
        data = json.loads(CHANNELS_FILE.read_text(encoding="utf-8"))
        channels = data.get("channels", {})
    else:
        channels = {}

    # TODO: Thêm logic lấy link mới tại đây nếu có nguồn tự động
    # Ví dụ: channels["FM956"] = "https://link-moi.m3u8"

    return channels


def main() -> None:
    channels = fetch_latest_channels()
    payload = {
        "updated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "channels": channels,
    }
    CHANNELS_FILE.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
