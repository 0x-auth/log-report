An Apache-style access log is available at `/app/access.log`.

Parse the log and write a JSON summary to `/app/report.json`.

**Success criteria:**

1. `/app/report.json` exists and contains valid JSON.
2. `total_requests` — integer count of all log lines.
3. `unique_ips` — integer count of distinct client IP addresses.
4. `top_path` — string, the URL path with the most GET/POST/etc. requests.

**Example output shape:**
```json
{"total_requests": 42, "unique_ips": 7, "top_path": "/index.html"}
```
