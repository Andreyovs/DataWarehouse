(base) dev@cd-dev-001:~/Documents/Otus/DataWarehouse/HW5/airflow$ docker compose up
    [+] Building 0.0s (0/0)                                    docker:desktop-linux
    [+] Running 7/7
    ✔ Container airflow_redis_1              R...                             0.3s 
    ✔ Container airflow_postgres_1           Recreated                        0.2s 
    ✔ Container airflow-airflow-scheduler-1  Created                          0.1s 
    ✔ Container airflow_airflow-init_1       Recreated                        0.2s 
    ✔ Container airflow-airflow-worker-1     Created                          0.1s 
    ✔ Container airflow-flower-1             Created                          0.1s 
    ✔ Container airflow-airflow-webserver-1  Created                          0.1s 
    Attaching to airflow-airflow-init-1, airflow-airflow-scheduler-1, airflow-airflow-webserver-1, airflow-airflow-worker-1, airflow-flower-1, airflow-postgres-1, airflow-redis-1
    airflow-redis-1              | 1:C 10 Nov 2023 14:22:24.839 # WARNING Memory overcommit must be enabled! Without it, a background save or replication may fail under low memory condition. Being disabled, it can also cause failures without low memory condition, see https://github.com/jemalloc/jemalloc/issues/1328. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.
    airflow-redis-1              | 1:C 10 Nov 2023 14:22:24.839 * oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
    airflow-redis-1              | 1:C 10 Nov 2023 14:22:24.839 * Redis version=7.2.3, bits=64, commit=00000000, modified=0, pid=1, just started
    airflow-redis-1              | 1:C 10 Nov 2023 14:22:24.839 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
    airflow-redis-1              | 1:M 10 Nov 2023 14:22:24.840 * monotonic clock: POSIX clock_gettime
    airflow-redis-1              | 1:M 10 Nov 2023 14:22:24.840 * Running mode=standalone, port=6379.
    airflow-redis-1              | 1:M 10 Nov 2023 14:22:24.841 * Server initialized
    airflow-redis-1              | 1:M 10 Nov 2023 14:22:24.841 * Loading RDB produced by version 7.2.3
    airflow-redis-1              | 1:M 10 Nov 2023 14:22:24.841 * RDB age 0 seconds
    airflow-redis-1              | 1:M 10 Nov 2023 14:22:24.841 * RDB memory usage when created 0.85 Mb
    airflow-redis-1              | 1:M 10 Nov 2023 14:22:24.841 * Done loading RDB, keys loaded: 0, keys expired: 0.
    airflow-redis-1              | 1:M 10 Nov 2023 14:22:24.841 * DB loaded from disk: 0.000 seconds
    airflow-redis-1              | 1:M 10 Nov 2023 14:22:24.841 * Ready to accept connections tcp