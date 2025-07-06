clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find src/CTFuser/ -type f ! -name "info.txt" -delete
	find src/CTFuser/ -mindepth 1 -type d -exec rm -rf {} +