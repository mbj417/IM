#
# Regular cron jobs for the osm-imdocs package
#
0 4	* * *	root	[ -x /usr/bin/osm-imdocs_maintenance ] && /usr/bin/osm-imdocs_maintenance
