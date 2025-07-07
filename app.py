from flask import Flask, request, jsonify
from datetime import datetime
import pytz
app = Flask(__name__)

@app.route('/api/convert-time', methods=['GET','POST'])

def convert_time():
    tz_name = request.args.get('timezone', default='UTC').strip()
    try:
        target_timezone = pytz.timezone(tz_name)
    except pytz.UnknownTimeZoneError:
        return jsonify({"error": "Invalid timezone"})
    now_naive = datetime.now()
    now_naive_str = now_naive.isoformat()
    now_aware = target_timezone.localize(now_naive)
    now_aware_str = now_aware.isoformat()
    now_utc_naive = datetime.utcnow()
    now_utc_aware = pytz.UTC.localize(now_utc_naive)
    now_utc_aware_str = now_utc_aware.isoformat()
    converted = now_utc_aware.astimezone(target_timezone)
    converted_str = converted.isoformat()

    return jsonify({
        "naive_local_time": now_naive_str,
        "local_time_awareness": "naive",
        "utc_time": now_utc_naive.isoformat(),
        "utc_time_awareness": "aware",
        "converted_time": converted_str,
        "converted_timezone": tz_name,
        "converted_time_awareness": "aware"
    })

if __name__ == "__main__":
    app.run(debug=True)
