from datetime import datetime, timedelta

# Define fixed Shah Alam prayer times (simplified)
azan_times = [
    ("Subuh", "05:45"),
    ("Zohor", "13:00"),
    ("Asar", "16:30"),
    ("Maghrib", "19:15"),
    ("Isyak", "20:30")
]

now = datetime.utcnow() + timedelta(hours=8)  # Malaysia time
current_time = now.strftime('%H:%M:%S')

# Determine next Azan
next_name, next_time = None, None
for name, t in azan_times:
    azan_dt = datetime.strptime(now.strftime('%Y-%m-%d') + ' ' + t, '%Y-%m-%d %H:%M')
    if azan_dt > now:
        next_name, next_time = name, azan_dt
        break
if not next_name:
    next_name, next_time = azan_times[0][0], datetime.strptime((now + timedelta(days=1)).strftime('%Y-%m-%d') + ' ' + azan_times[0][1], '%Y-%m-%d %H:%M')

countdown = str(next_time - now).split('.')[0]
next_label = f"({next_name} at {next_time.strftime('%H:%M')})"

# Write HTML
html = f"""<!DOCTYPE html>
<html lang='en'>
<head>
  <meta charset='UTF-8' />
  <meta name='viewport' content='width=device-width, initial-scale=1.0'/>
  <title>Waktu Azan Shah Alam</title>
  <style>
    body {{
      margin: 0;
      font-family: 'Inter', sans-serif;
      background: #111;
      color: #fff;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 100vh;
      text-align: center;
    }}
    .time {{
      font-size: 4em;
      font-weight: bold;
    }}
    .weather {{
      font-size: 1.5em;
      margin-top: 10px;
    }}
    .countdown {{
      font-size: 2em;
      margin-top: 20px;
      color: #0ff;
    }}
  </style>
</head>
<body>
  <div class='time'>{current_time}</div>
  <div class='weather'>Weather: 30°C, Partly Cloudy</div>
  <div class='countdown'>Next Azan: {next_label} ({countdown})</div>

  <audio id='azanSound' src='audio/azan.mp3' preload='auto'></audio>
  <audio id='beepSound' src='audio/beep.mp3' preload='auto'></audio>
</body>
</html>"""

with open("index.html", "w") as f:
    f.write(html)