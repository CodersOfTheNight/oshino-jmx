oshino-jmx
=====================
Collect JMX metrics from JVM services

For more info, refer to parent project [Oshino](https://github.com/CodersOfTheNight/oshino)

Setup
=====
It basically downloads [JMXTrans](https://github.com/jmxtrans/jmxtrans) agent and launches it. All regular configuration is done via `etc/jmxconfig.yml`.
In parralel, [oshino_statsd](https://github.com/CodersOfTheNight/oshino-statsd) is launched to collect StatsD Metrics pushed by JMXTrans.
