This is a plotly/Dash app of the Fe and Zn edge spectra, clustered with DBSCAN from the hexafs notebooks on clustering. The colors/greek letters correspond to arbitrary cluster groups.

Run the following (with port 8080 forwarded) to host the web-app:

nohup gunicorn ml_mcff:server -b 0.0.0.0:8080 -w &
