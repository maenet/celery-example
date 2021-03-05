broker_url = "redis://redis:6379"
result_backend = "db+mysql://root:password@db/celery"
task_serializer = "json"
result_serializer = "json"
accept_content = ["json"]
timezone = "Asia/Tokyo"
enable_utc = True
task_track_starteda = True
