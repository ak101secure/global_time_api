# Flask Timezone Converter API

A simple Flask API to convert the current UTC time to any specified timezone.

---

## Features

- Converts current UTC time to requested timezone.
- Supports both GET and POST requests.
- Returns times with timezone awareness information.
- Handles invalid timezone input gracefully.

---

## API Endpoint


GET /api/convert-time?timezone=Asia/Dhaka
POST /api/convert-time?timezone=Asia/Dhaka


### Query Parameters

| Parameter | Description                                   | Default |
| --------- | --------------------------------------------- | ------- |
| timezone  | Target timezone (e.g., `Asia/Dhaka`, `UTC`, `America/New_York`) | `UTC`   |

---

## Response Example

```json
{
  "naive_local_time": "2025-07-08T07:50:00.123456",
  "local_time_awareness": "naive",
  "utc_time": "2025-07-08T01:50:00.123456",
  "utc_time_awareness": "aware",
  "converted_time": "2025-07-08T07:50:00.123456+06:00",
  "converted_timezone": "Asia/Dhaka",
  "converted_time_awareness": "aware"
}


