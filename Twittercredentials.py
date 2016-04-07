Last login: Wed Apr  6 09:13:25 on ttys000
Alfreds-MBP:~ alfredarsenault$ cd downloads
Alfreds-MBP:downloads alfredarsenault$ ssh -i "Exercise_2_keys.pem" root@ec2-54-174-173-7.compute-1.amazonaws.com
Last login: Wed Apr  6 13:14:14 2016 from 192.80.55.242
     ___   _        __   __   ____            __    
    / _ \ (_)___ _ / /  / /_ / __/____ ___ _ / /___ 
   / , _// // _ `// _ \/ __/_\ \ / __// _ `// // -_)
  /_/|_|/_/ \_, //_//_/\__//___/ \__/ \_,_//_/ \__/ 
           /___/                                                 
                                              
Welcome to a virtual machine image brought to you by RightScale!


[root@ip-172-31-57-217 ~]# pwd
/root
[root@ip-172-31-57-217 ~]# ls
dans_bash_history.txt                    setuptools-20.3.1.zip
dead.letter                              start-hadoop.sh
EX2Tweetwordcount                        start-hadoop.sh~
ez_setup.py                              stop-hadoop.sh
ipython                                  stop-hadoop.sh~
pgxl-deployment-tools                    streamparse
rstudio-server-rhel-0.99.892-x86_64.rpm  w205-spring-16-labs-exercises
[root@ip-172-31-57-217 ~]# cd EX2T*
[root@ip-172-31-57-217 EX2Tweetwordcount]# ls
config.json              project.clj        src         Twittercredentials.py
fabfile.py               psycopg-sample.py  tasks.py    Twittercredentials.pyc
hello-stream-twitter.py  README.md          topologies  virtualenvs
[root@ip-172-31-57-217 EX2Tweetwordcount]# vi psycopg-sample.py
[root@ip-172-31-57-217 EX2Tweetwordcount]# cd ..
[root@ip-172-31-57-217 ~]# pwd
/root
[root@ip-172-31-57-217 ~]# /root/stop-hadoop.sh
stopping resourcemanager
Stopped Hadoop resourcemanager:                            [  OK  ]
stopping nodemanager
Stopped Hadoop nodemanager:                                [  OK  ]
stopping historyserver
historyserver did not stop gracefully after 5 seconds: killing with kill -9
Stopped Hadoop historyserver:                              [  OK  ]
no datanode to stop
Stopped Hadoop datanode:                                   [  OK  ]
no namenode to stop
Stopped Hadoop namenode:                                   [  OK  ]
no secondarynamenode to stop
Stopped Hadoop secondarynamenode:                          [  OK  ]
[root@ip-172-31-57-217 ~]# /data/stop_postgres.sh
-bash: /data/stop_postgres.sh: No such file or directory
[root@ip-172-31-57-217 ~]# /root/start-hadoop.sh
no datanode to stop
Stopped Hadoop datanode:                                   [  OK  ]
starting datanode, logging to /var/log/hadoop-hdfs/hadoop-hdfs-datanode-ip-172-31-57-217.out
Failed to start Hadoop datanode. Return value: 1           [FAILED]
no namenode to stop
Stopped Hadoop namenode:                                   [  OK  ]
starting namenode, logging to /var/log/hadoop-hdfs/hadoop-hdfs-namenode-ip-172-31-57-217.out
Failed to start Hadoop namenode. Return value: 1           [FAILED]
no secondarynamenode to stop
Stopped Hadoop secondarynamenode:                          [  OK  ]
starting secondarynamenode, logging to /var/log/hadoop-hdfs/hadoop-hdfs-secondarynamenode-ip-172-31-57-217.out
Failed to start Hadoop secondarynamenode. Return value: 1  [FAILED]
no resourcemanager to stop
Stopped Hadoop resourcemanager:                            [  OK  ]
starting resourcemanager, logging to /var/log/hadoop-yarn/yarn-yarn-resourcemanager-ip-172-31-57-217.out
Started Hadoop resourcemanager:                            [  OK  ]
no nodemanager to stop
Stopped Hadoop nodemanager:                                [  OK  ]
starting nodemanager, logging to /var/log/hadoop-yarn/yarn-yarn-nodemanager-ip-172-31-57-217.out
Started Hadoop nodemanager:                                [  OK  ]
no historyserver to stop
Stopped Hadoop historyserver:                              [  OK  ]
starting historyserver, logging to /var/log/hadoop-mapreduce/mapred-mapred-historyserver-ip-172-31-57-217.out
16/04/07 12:05:21 INFO hs.JobHistoryServer: STARTUP_MSG: 
/************************************************************
STARTUP_MSG: Starting JobHistoryServer
STARTUP_MSG:   host = ip-172-31-57-217.ec2.internal/172.31.57.217
STARTUP_MSG:   args = []
STARTUP_MSG:   version = 2.6.0-cdh5.4.5
STARTUP_MSG:   classpath = /etc/hadoop/conf:/usr/lib/hadoop/lib/apacheds-i18n-2.0.0-M15.jar:/usr/lib/hadoop/lib/asm-3.2.jar:/usr/lib/hadoop/lib/jersey-core-1.9.jar:/usr/lib/hadoop/lib/mockito-all-1.8.5.jar:/usr/lib/hadoop/lib/api-asn1-api-1.0.0-M20.jar:/usr/lib/hadoop/lib/curator-framework-2.7.1.jar:/usr/lib/hadoop/lib/slf4j-log4j12.jar:/usr/lib/hadoop/lib/jersey-json-1.9.jar:/usr/lib/hadoop/lib/aws-java-sdk-1.7.14.jar:/usr/lib/hadoop/lib/java-xmlbuilder-0.4.jar:/usr/lib/hadoop/lib/guava-11.0.2.jar:/usr/lib/hadoop/lib/xz-1.0.jar:/usr/lib/hadoop/lib/jaxb-impl-2.2.3-1.jar:/usr/lib/hadoop/lib/jackson-mapper-asl-1.8.8.jar:/usr/lib/hadoop/lib/commons-configuration-1.6.jar:/usr/lib/hadoop/lib/curator-client-2.7.1.jar:/usr/lib/hadoop/lib/xmlenc-0.52.jar:/usr/lib/hadoop/lib/commons-compress-1.4.1.jar:/usr/lib/hadoop/lib/hamcrest-core-1.3.jar:/usr/lib/hadoop/lib/htrace-core-3.0.4.jar:/usr/lib/hadoop/lib/jasper-compiler-5.5.23.jar:/usr/lib/hadoop/lib/avro.jar:/usr/lib/hadoop/lib/jsr305-3.0.0.jar:/usr/lib/hadoop/lib/commons-el-1.0.jar:/usr/lib/hadoop/lib/stax-api-1.0-2.jar:/usr/lib/hadoop/lib/jsch-0.1.42.jar:/usr/lib/hadoop/lib/commons-net-3.1.jar:/usr/lib/hadoop/lib/snappy-java-1.0.4.1.jar:/usr/lib/hadoop/lib/zookeeper.jar:/usr/lib/hadoop/lib/jackson-jaxrs-1.8.8.jar:/usr/lib/hadoop/lib/commons-io-2.4.jar:/usr/lib/hadoop/lib/paranamer-2.3.jar:/usr/lib/hadoop/lib/commons-digester-1.8.jar:/usr/lib/hadoop/lib/commons-codec-1.4.jar:/usr/lib/hadoop/lib/servlet-api-2.5.jar:/usr/lib/hadoop/lib/commons-lang-2.6.jar:/usr/lib/hadoop/lib/netty-3.6.2.Final.jar:/usr/lib/hadoop/lib/jettison-1.1.jar:/usr/lib/hadoop/lib/commons-cli-1.2.jar:/usr/lib/hadoop/lib/commons-collections-3.2.1.jar:/usr/lib/hadoop/lib/slf4j-api-1.7.5.jar:/usr/lib/hadoop/lib/apacheds-kerberos-codec-2.0.0-M15.jar:/usr/lib/hadoop/lib/jasper-runtime-5.5.23.jar:/usr/lib/hadoop/lib/jersey-server-1.9.jar:/usr/lib/hadoop/lib/api-util-1.0.0-M20.jar:/usr/lib/hadoop/lib/curator-recipes-2.7.1.jar:/usr/lib/hadoop/lib/activation-1.1.jar:/usr/lib/hadoop/lib/jackson-core-asl-1.8.8.jar:/usr/lib/hadoop/lib/jetty-6.1.26.cloudera.4.jar:/usr/lib/hadoop/lib/logredactor-1.0.3.jar:/usr/lib/hadoop/lib/commons-beanutils-core-1.8.0.jar:/usr/lib/hadoop/lib/jaxb-api-2.2.2.jar:/usr/lib/hadoop/lib/commons-math3-3.1.1.jar:/usr/lib/hadoop/lib/log4j-1.2.17.jar:/usr/lib/hadoop/lib/jets3t-0.9.0.jar:/usr/lib/hadoop/lib/protobuf-java-2.5.0.jar:/usr/lib/hadoop/lib/commons-beanutils-1.7.0.jar:/usr/lib/hadoop/lib/commons-httpclient-3.1.jar:/usr/lib/hadoop/lib/jackson-xc-1.8.8.jar:/usr/lib/hadoop/lib/commons-logging-1.1.3.jar:/usr/lib/hadoop/lib/jsp-api-2.1.jar:/usr/lib/hadoop/lib/httpclient-4.2.5.jar:/usr/lib/hadoop/lib/httpcore-4.2.5.jar:/usr/lib/hadoop/lib/gson-2.2.4.jar:/usr/lib/hadoop/lib/junit-4.11.jar:/usr/lib/hadoop/lib/jetty-util-6.1.26.cloudera.4.jar:/usr/lib/hadoop/.//hadoop-common-tests.jar:/usr/lib/hadoop/.//hadoop-aws.jar:/usr/lib/hadoop/.//parquet-generator.jar:/usr/lib/hadoop/.//parquet-encoding.jar:/usr/lib/hadoop/.//hadoop-common-2.6.0-cdh5.4.5-tests.jar:/usr/lib/hadoop/.//parquet-thrift.jar:/usr/lib/hadoop/.//parquet-pig-bundle.jar:/usr/lib/hadoop/.//parquet-format-javadoc.jar:/usr/lib/hadoop/.//parquet-format.jar:/usr/lib/hadoop/.//parquet-column.jar:/usr/lib/hadoop/.//parquet-format-sources.jar:/usr/lib/hadoop/.//parquet-pig.jar:/usr/lib/hadoop/.//parquet-avro.jar:/usr/lib/hadoop/.//parquet-hadoop-bundle.jar:/usr/lib/hadoop/.//parquet-common.jar:/usr/lib/hadoop/.//hadoop-annotations-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop/.//hadoop-auth-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop/.//hadoop-common.jar:/usr/lib/hadoop/.//hadoop-aws-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop/.//hadoop-nfs.jar:/usr/lib/hadoop/.//parquet-jackson.jar:/usr/lib/hadoop/.//parquet-hadoop.jar:/usr/lib/hadoop/.//parquet-cascading.jar:/usr/lib/hadoop/.//parquet-scrooge_2.10.jar:/usr/lib/hadoop/.//hadoop-auth.jar:/usr/lib/hadoop/.//hadoop-nfs-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop/.//hadoop-common-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop/.//parquet-test-hadoop2.jar:/usr/lib/hadoop/.//parquet-protobuf.jar:/usr/lib/hadoop/.//parquet-scala_2.10.jar:/usr/lib/hadoop/.//hadoop-annotations.jar:/usr/lib/hadoop/.//parquet-tools.jar:/usr/lib/hadoop-hdfs/./:/usr/lib/hadoop-hdfs/lib/asm-3.2.jar:/usr/lib/hadoop-hdfs/lib/jersey-core-1.9.jar:/usr/lib/hadoop-hdfs/lib/guava-11.0.2.jar:/usr/lib/hadoop-hdfs/lib/jackson-mapper-asl-1.8.8.jar:/usr/lib/hadoop-hdfs/lib/xmlenc-0.52.jar:/usr/lib/hadoop-hdfs/lib/htrace-core-3.0.4.jar:/usr/lib/hadoop-hdfs/lib/jsr305-3.0.0.jar:/usr/lib/hadoop-hdfs/lib/commons-el-1.0.jar:/usr/lib/hadoop-hdfs/lib/commons-io-2.4.jar:/usr/lib/hadoop-hdfs/lib/commons-codec-1.4.jar:/usr/lib/hadoop-hdfs/lib/servlet-api-2.5.jar:/usr/lib/hadoop-hdfs/lib/commons-lang-2.6.jar:/usr/lib/hadoop-hdfs/lib/netty-3.6.2.Final.jar:/usr/lib/hadoop-hdfs/lib/commons-cli-1.2.jar:/usr/lib/hadoop-hdfs/lib/jasper-runtime-5.5.23.jar:/usr/lib/hadoop-hdfs/lib/jersey-server-1.9.jar:/usr/lib/hadoop-hdfs/lib/jackson-core-asl-1.8.8.jar:/usr/lib/hadoop-hdfs/lib/jetty-6.1.26.cloudera.4.jar:/usr/lib/hadoop-hdfs/lib/log4j-1.2.17.jar:/usr/lib/hadoop-hdfs/lib/protobuf-java-2.5.0.jar:/usr/lib/hadoop-hdfs/lib/commons-daemon-1.0.13.jar:/usr/lib/hadoop-hdfs/lib/commons-logging-1.1.3.jar:/usr/lib/hadoop-hdfs/lib/jsp-api-2.1.jar:/usr/lib/hadoop-hdfs/lib/leveldbjni-all-1.8.jar:/usr/lib/hadoop-hdfs/lib/jetty-util-6.1.26.cloudera.4.jar:/usr/lib/hadoop-hdfs/.//hadoop-hdfs.jar:/usr/lib/hadoop-hdfs/.//hadoop-hdfs-nfs-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-hdfs/.//hadoop-hdfs-tests.jar:/usr/lib/hadoop-hdfs/.//hadoop-hdfs-2.6.0-cdh5.4.5-tests.jar:/usr/lib/hadoop-hdfs/.//hadoop-hdfs-nfs.jar:/usr/lib/hadoop-hdfs/.//hadoop-hdfs-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-yarn/lib/asm-3.2.jar:/usr/lib/hadoop-yarn/lib/jersey-core-1.9.jar:/usr/lib/hadoop-yarn/lib/jersey-json-1.9.jar:/usr/lib/hadoop-yarn/lib/guava-11.0.2.jar:/usr/lib/hadoop-yarn/lib/xz-1.0.jar:/usr/lib/hadoop-yarn/lib/jaxb-impl-2.2.3-1.jar:/usr/lib/hadoop-yarn/lib/jackson-mapper-asl-1.8.8.jar:/usr/lib/hadoop-yarn/lib/jersey-guice-1.9.jar:/usr/lib/hadoop-yarn/lib/commons-compress-1.4.1.jar:/usr/lib/hadoop-yarn/lib/aopalliance-1.0.jar:/usr/lib/hadoop-yarn/lib/jsr305-3.0.0.jar:/usr/lib/hadoop-yarn/lib/javax.inject-1.jar:/usr/lib/hadoop-yarn/lib/jersey-client-1.9.jar:/usr/lib/hadoop-yarn/lib/stax-api-1.0-2.jar:/usr/lib/hadoop-yarn/lib/zookeeper.jar:/usr/lib/hadoop-yarn/lib/guice-servlet-3.0.jar:/usr/lib/hadoop-yarn/lib/jackson-jaxrs-1.8.8.jar:/usr/lib/hadoop-yarn/lib/commons-io-2.4.jar:/usr/lib/hadoop-yarn/lib/commons-codec-1.4.jar:/usr/lib/hadoop-yarn/lib/jline-2.11.jar:/usr/lib/hadoop-yarn/lib/servlet-api-2.5.jar:/usr/lib/hadoop-yarn/lib/commons-lang-2.6.jar:/usr/lib/hadoop-yarn/lib/jettison-1.1.jar:/usr/lib/hadoop-yarn/lib/guice-3.0.jar:/usr/lib/hadoop-yarn/lib/commons-cli-1.2.jar:/usr/lib/hadoop-yarn/lib/commons-collections-3.2.1.jar:/usr/lib/hadoop-yarn/lib/jersey-server-1.9.jar:/usr/lib/hadoop-yarn/lib/activation-1.1.jar:/usr/lib/hadoop-yarn/lib/jackson-core-asl-1.8.8.jar:/usr/lib/hadoop-yarn/lib/jetty-6.1.26.cloudera.4.jar:/usr/lib/hadoop-yarn/lib/jaxb-api-2.2.2.jar:/usr/lib/hadoop-yarn/lib/log4j-1.2.17.jar:/usr/lib/hadoop-yarn/lib/protobuf-java-2.5.0.jar:/usr/lib/hadoop-yarn/lib/commons-httpclient-3.1.jar:/usr/lib/hadoop-yarn/lib/jackson-xc-1.8.8.jar:/usr/lib/hadoop-yarn/lib/commons-logging-1.1.3.jar:/usr/lib/hadoop-yarn/lib/leveldbjni-all-1.8.jar:/usr/lib/hadoop-yarn/lib/jetty-util-6.1.26.cloudera.4.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-common-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-server-common.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-applications-distributedshell.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-server-tests-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-server-tests.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-applications-distributedshell-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-api.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-common.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-server-nodemanager.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-server-applicationhistoryservice.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-applications-unmanaged-am-launcher.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-client-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-server-resourcemanager.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-server-nodemanager-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-server-resourcemanager-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-server-web-proxy-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-registry.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-server-web-proxy.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-server-common-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-client.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-server-applicationhistoryservice-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-registry-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-api-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-applications-unmanaged-am-launcher-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/lib/asm-3.2.jar:/usr/lib/hadoop-mapreduce/lib/jersey-core-1.9.jar:/usr/lib/hadoop-mapreduce/lib/xz-1.0.jar:/usr/lib/hadoop-mapreduce/lib/jackson-mapper-asl-1.8.8.jar:/usr/lib/hadoop-mapreduce/lib/jersey-guice-1.9.jar:/usr/lib/hadoop-mapreduce/lib/commons-compress-1.4.1.jar:/usr/lib/hadoop-mapreduce/lib/aopalliance-1.0.jar:/usr/lib/hadoop-mapreduce/lib/hamcrest-core-1.3.jar:/usr/lib/hadoop-mapreduce/lib/avro.jar:/usr/lib/hadoop-mapreduce/lib/javax.inject-1.jar:/usr/lib/hadoop-mapreduce/lib/snappy-java-1.0.4.1.jar:/usr/lib/hadoop-mapreduce/lib/guice-servlet-3.0.jar:/usr/lib/hadoop-mapreduce/lib/commons-io-2.4.jar:/usr/lib/hadoop-mapreduce/lib/paranamer-2.3.jar:/usr/lib/hadoop-mapreduce/lib/netty-3.6.2.Final.jar:/usr/lib/hadoop-mapreduce/lib/guice-3.0.jar:/usr/lib/hadoop-mapreduce/lib/jersey-server-1.9.jar:/usr/lib/hadoop-mapreduce/lib/jackson-core-asl-1.8.8.jar:/usr/lib/hadoop-mapreduce/lib/log4j-1.2.17.jar:/usr/lib/hadoop-mapreduce/lib/protobuf-java-2.5.0.jar:/usr/lib/hadoop-mapreduce/lib/junit-4.11.jar:/usr/lib/hadoop-mapreduce/lib/leveldbjni-all-1.8.jar:/usr/lib/hadoop-mapreduce/.//apacheds-i18n-2.0.0-M15.jar:/usr/lib/hadoop-mapreduce/.//asm-3.2.jar:/usr/lib/hadoop-mapreduce/.//jersey-core-1.9.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-examples.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-common.jar:/usr/lib/hadoop-mapreduce/.//hadoop-ant.jar:/usr/lib/hadoop-mapreduce/.//mockito-all-1.8.5.jar:/usr/lib/hadoop-mapreduce/.//api-asn1-api-1.0.0-M20.jar:/usr/lib/hadoop-mapreduce/.//hadoop-rumen.jar:/usr/lib/hadoop-mapreduce/.//hadoop-azure-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-sls-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//curator-framework-2.7.1.jar:/usr/lib/hadoop-mapreduce/.//jersey-json-1.9.jar:/usr/lib/hadoop-mapreduce/.//microsoft-windowsazure-storage-sdk-0.6.0.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-nativetask.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-shuffle-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//jackson-databind-2.2.3.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-shuffle.jar:/usr/lib/hadoop-mapreduce/.//java-xmlbuilder-0.4.jar:/usr/lib/hadoop-mapreduce/.//guava-11.0.2.jar:/usr/lib/hadoop-mapreduce/.//xz-1.0.jar:/usr/lib/hadoop-mapreduce/.//jaxb-impl-2.2.3-1.jar:/usr/lib/hadoop-mapreduce/.//jackson-mapper-asl-1.8.8.jar:/usr/lib/hadoop-mapreduce/.//commons-configuration-1.6.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-core-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-hs.jar:/usr/lib/hadoop-mapreduce/.//hadoop-sls.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-hs-plugins.jar:/usr/lib/hadoop-mapreduce/.//curator-client-2.7.1.jar:/usr/lib/hadoop-mapreduce/.//hadoop-extras-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-examples-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//xmlenc-0.52.jar:/usr/lib/hadoop-mapreduce/.//commons-compress-1.4.1.jar:/usr/lib/hadoop-mapreduce/.//hadoop-gridmix.jar:/usr/lib/hadoop-mapreduce/.//hadoop-gridmix-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hamcrest-core-1.3.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-common-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//htrace-core-3.0.4.jar:/usr/lib/hadoop-mapreduce/.//jasper-compiler-5.5.23.jar:/usr/lib/hadoop-mapreduce/.//avro.jar:/usr/lib/hadoop-mapreduce/.//jsr305-3.0.0.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-nativetask-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-jobclient-2.6.0-cdh5.4.5-tests.jar:/usr/lib/hadoop-mapreduce/.//hadoop-distcp.jar:/usr/lib/hadoop-mapreduce/.//commons-el-1.0.jar:/usr/lib/hadoop-mapreduce/.//stax-api-1.0-2.jar:/usr/lib/hadoop-mapreduce/.//jsch-0.1.42.jar:/usr/lib/hadoop-mapreduce/.//commons-net-3.1.jar:/usr/lib/hadoop-mapreduce/.//snappy-java-1.0.4.1.jar:/usr/lib/hadoop-mapreduce/.//hadoop-azure.jar:/usr/lib/hadoop-mapreduce/.//zookeeper.jar:/usr/lib/hadoop-mapreduce/.//hadoop-auth-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-jobclient-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-app.jar:/usr/lib/hadoop-mapreduce/.//jackson-jaxrs-1.8.8.jar:/usr/lib/hadoop-mapreduce/.//commons-io-2.4.jar:/usr/lib/hadoop-mapreduce/.//paranamer-2.3.jar:/usr/lib/hadoop-mapreduce/.//hadoop-extras.jar:/usr/lib/hadoop-mapreduce/.//commons-digester-1.8.jar:/usr/lib/hadoop-mapreduce/.//hadoop-streaming.jar:/usr/lib/hadoop-mapreduce/.//commons-codec-1.4.jar:/usr/lib/hadoop-mapreduce/.//hadoop-archives.jar:/usr/lib/hadoop-mapreduce/.//servlet-api-2.5.jar:/usr/lib/hadoop-mapreduce/.//commons-lang-2.6.jar:/usr/lib/hadoop-mapreduce/.//jackson-annotations-2.2.3.jar:/usr/lib/hadoop-mapreduce/.//jettison-1.1.jar:/usr/lib/hadoop-mapreduce/.//commons-cli-1.2.jar:/usr/lib/hadoop-mapreduce/.//commons-collections-3.2.1.jar:/usr/lib/hadoop-mapreduce/.//apacheds-kerberos-codec-2.0.0-M15.jar:/usr/lib/hadoop-mapreduce/.//hadoop-datajoin.jar:/usr/lib/hadoop-mapreduce/.//hadoop-datajoin-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//jasper-runtime-5.5.23.jar:/usr/lib/hadoop-mapreduce/.//jersey-server-1.9.jar:/usr/lib/hadoop-mapreduce/.//api-util-1.0.0-M20.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-app-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-streaming-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//curator-recipes-2.7.1.jar:/usr/lib/hadoop-mapreduce/.//metrics-core-3.0.1.jar:/usr/lib/hadoop-mapreduce/.//activation-1.1.jar:/usr/lib/hadoop-mapreduce/.//jackson-core-asl-1.8.8.jar:/usr/lib/hadoop-mapreduce/.//jetty-6.1.26.cloudera.4.jar:/usr/lib/hadoop-mapreduce/.//commons-beanutils-core-1.8.0.jar:/usr/lib/hadoop-mapreduce/.//jaxb-api-2.2.2.jar:/usr/lib/hadoop-mapreduce/.//commons-math3-3.1.1.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-jobclient.jar:/usr/lib/hadoop-mapreduce/.//hadoop-ant-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//log4j-1.2.17.jar:/usr/lib/hadoop-mapreduce/.//jets3t-0.9.0.jar:/usr/lib/hadoop-mapreduce/.//hadoop-archives-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//protobuf-java-2.5.0.jar:/usr/lib/hadoop-mapreduce/.//commons-beanutils-1.7.0.jar:/usr/lib/hadoop-mapreduce/.//commons-httpclient-3.1.jar:/usr/lib/hadoop-mapreduce/.//hadoop-auth.jar:/usr/lib/hadoop-mapreduce/.//jackson-xc-1.8.8.jar:/usr/lib/hadoop-mapreduce/.//hadoop-distcp-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//commons-logging-1.1.3.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-jobclient-tests.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-core.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-hs-plugins-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//jsp-api-2.1.jar:/usr/lib/hadoop-mapreduce/.//httpclient-4.2.5.jar:/usr/lib/hadoop-mapreduce/.//jackson-core-2.2.3.jar:/usr/lib/hadoop-mapreduce/.//httpcore-4.2.5.jar:/usr/lib/hadoop-mapreduce/.//gson-2.2.4.jar:/usr/lib/hadoop-mapreduce/.//hadoop-rumen-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-hs-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//junit-4.11.jar:/usr/lib/hadoop-mapreduce/.//jetty-util-6.1.26.cloudera.4.jar:/usr/lib/hadoop-mapreduce/.//activation-1.1.jar:/usr/lib/hadoop-mapreduce/.//apacheds-i18n-2.0.0-M15.jar:/usr/lib/hadoop-mapreduce/.//apacheds-kerberos-codec-2.0.0-M15.jar:/usr/lib/hadoop-mapreduce/.//api-asn1-api-1.0.0-M20.jar:/usr/lib/hadoop-mapreduce/.//api-util-1.0.0-M20.jar:/usr/lib/hadoop-mapreduce/.//asm-3.2.jar:/usr/lib/hadoop-mapreduce/.//avro.jar:/usr/lib/hadoop-mapreduce/.//commons-beanutils-1.7.0.jar:/usr/lib/hadoop-mapreduce/.//commons-beanutils-core-1.8.0.jar:/usr/lib/hadoop-mapreduce/.//commons-cli-1.2.jar:/usr/lib/hadoop-mapreduce/.//commons-codec-1.4.jar:/usr/lib/hadoop-mapreduce/.//commons-collections-3.2.1.jar:/usr/lib/hadoop-mapreduce/.//commons-compress-1.4.1.jar:/usr/lib/hadoop-mapreduce/.//commons-configuration-1.6.jar:/usr/lib/hadoop-mapreduce/.//commons-digester-1.8.jar:/usr/lib/hadoop-mapreduce/.//commons-el-1.0.jar:/usr/lib/hadoop-mapreduce/.//commons-httpclient-3.1.jar:/usr/lib/hadoop-mapreduce/.//commons-io-2.4.jar:/usr/lib/hadoop-mapreduce/.//commons-lang-2.6.jar:/usr/lib/hadoop-mapreduce/.//commons-logging-1.1.3.jar:/usr/lib/hadoop-mapreduce/.//commons-math3-3.1.1.jar:/usr/lib/hadoop-mapreduce/.//commons-net-3.1.jar:/usr/lib/hadoop-mapreduce/.//curator-client-2.7.1.jar:/usr/lib/hadoop-mapreduce/.//curator-framework-2.7.1.jar:/usr/lib/hadoop-mapreduce/.//curator-recipes-2.7.1.jar:/usr/lib/hadoop-mapreduce/.//gson-2.2.4.jar:/usr/lib/hadoop-mapreduce/.//guava-11.0.2.jar:/usr/lib/hadoop-mapreduce/.//hadoop-ant-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-ant.jar:/usr/lib/hadoop-mapreduce/.//hadoop-archives-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-archives.jar:/usr/lib/hadoop-mapreduce/.//hadoop-auth-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-auth.jar:/usr/lib/hadoop-mapreduce/.//hadoop-azure-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-azure.jar:/usr/lib/hadoop-mapreduce/.//hadoop-datajoin-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-datajoin.jar:/usr/lib/hadoop-mapreduce/.//hadoop-distcp-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-distcp.jar:/usr/lib/hadoop-mapreduce/.//hadoop-extras-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-extras.jar:/usr/lib/hadoop-mapreduce/.//hadoop-gridmix-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-gridmix.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-app-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-app.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-common-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-common.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-core-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-core.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-hs-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-hs-plugins-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-hs-plugins.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-hs.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-jobclient-2.6.0-cdh5.4.5-tests.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-jobclient-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-jobclient-tests.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-jobclient.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-nativetask-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-nativetask.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-shuffle-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-shuffle.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-examples-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-examples.jar:/usr/lib/hadoop-mapreduce/.//hadoop-rumen-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-rumen.jar:/usr/lib/hadoop-mapreduce/.//hadoop-sls-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-sls.jar:/usr/lib/hadoop-mapreduce/.//hadoop-streaming-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-streaming.jar:/usr/lib/hadoop-mapreduce/.//hamcrest-core-1.3.jar:/usr/lib/hadoop-mapreduce/.//htrace-core-3.0.4.jar:/usr/lib/hadoop-mapreduce/.//httpclient-4.2.5.jar:/usr/lib/hadoop-mapreduce/.//httpcore-4.2.5.jar:/usr/lib/hadoop-mapreduce/.//jackson-annotations-2.2.3.jar:/usr/lib/hadoop-mapreduce/.//jackson-core-2.2.3.jar:/usr/lib/hadoop-mapreduce/.//jackson-core-asl-1.8.8.jar:/usr/lib/hadoop-mapreduce/.//jackson-databind-2.2.3.jar:/usr/lib/hadoop-mapreduce/.//jackson-jaxrs-1.8.8.jar:/usr/lib/hadoop-mapreduce/.//jackson-mapper-asl-1.8.8.jar:/usr/lib/hadoop-mapreduce/.//jackson-xc-1.8.8.jar:/usr/lib/hadoop-mapreduce/.//jasper-compiler-5.5.23.jar:/usr/lib/hadoop-mapreduce/.//jasper-runtime-5.5.23.jar:/usr/lib/hadoop-mapreduce/.//java-xmlbuilder-0.4.jar:/usr/lib/hadoop-mapreduce/.//jaxb-api-2.2.2.jar:/usr/lib/hadoop-mapreduce/.//jaxb-impl-2.2.3-1.jar:/usr/lib/hadoop-mapreduce/.//jersey-core-1.9.jar:/usr/lib/hadoop-mapreduce/.//jersey-json-1.9.jar:/usr/lib/hadoop-mapreduce/.//jersey-server-1.9.jar:/usr/lib/hadoop-mapreduce/.//jets3t-0.9.0.jar:/usr/lib/hadoop-mapreduce/.//jettison-1.1.jar:/usr/lib/hadoop-mapreduce/.//jetty-6.1.26.cloudera.4.jar:/usr/lib/hadoop-mapreduce/.//jetty-util-6.1.26.cloudera.4.jar:/usr/lib/hadoop-mapreduce/.//jsch-0.1.42.jar:/usr/lib/hadoop-mapreduce/.//jsp-api-2.1.jar:/usr/lib/hadoop-mapreduce/.//jsr305-3.0.0.jar:/usr/lib/hadoop-mapreduce/.//junit-4.11.jar:/usr/lib/hadoop-mapreduce/.//log4j-1.2.17.jar:/usr/lib/hadoop-mapreduce/.//metrics-core-3.0.1.jar:/usr/lib/hadoop-mapreduce/.//microsoft-windowsazure-storage-sdk-0.6.0.jar:/usr/lib/hadoop-mapreduce/.//mockito-all-1.8.5.jar:/usr/lib/hadoop-mapreduce/.//paranamer-2.3.jar:/usr/lib/hadoop-mapreduce/.//protobuf-java-2.5.0.jar:/usr/lib/hadoop-mapreduce/.//servlet-api-2.5.jar:/usr/lib/hadoop-mapreduce/.//snappy-java-1.0.4.1.jar:/usr/lib/hadoop-mapreduce/.//stax-api-1.0-2.jar:/usr/lib/hadoop-mapreduce/.//xmlenc-0.52.jar:/usr/lib/hadoop-mapreduce/.//xz-1.0.jar:/usr/lib/hadoop-mapreduce/.//zookeeper.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-api-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-api.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-applications-distributedshell-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-applications-distributedshell.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-applications-unmanaged-am-launcher-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-applications-unmanaged-am-launcher.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-client-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-client.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-common-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-common.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-registry-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-registry.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-server-applicationhistoryservice-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-server-applicationhistoryservice.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-server-common-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-server-common.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-server-nodemanager-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-server-nodemanager.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-server-resourcemanager-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-server-resourcemanager.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-server-tests-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-server-tests.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-server-web-proxy-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-server-web-proxy.jar:/usr/lib/hadoop-mapreduce/lib/aopalliance-1.0.jar:/usr/lib/hadoop-mapreduce/lib/asm-3.2.jar:/usr/lib/hadoop-mapreduce/lib/avro.jar:/usr/lib/hadoop-mapreduce/lib/commons-compress-1.4.1.jar:/usr/lib/hadoop-mapreduce/lib/commons-io-2.4.jar:/usr/lib/hadoop-mapreduce/lib/guice-3.0.jar:/usr/lib/hadoop-mapreduce/lib/guice-servlet-3.0.jar:/usr/lib/hadoop-mapreduce/lib/hamcrest-core-1.3.jar:/usr/lib/hadoop-mapreduce/lib/jackson-core-asl-1.8.8.jar:/usr/lib/hadoop-mapreduce/lib/jackson-mapper-asl-1.8.8.jar:/usr/lib/hadoop-mapreduce/lib/javax.inject-1.jar:/usr/lib/hadoop-mapreduce/lib/jersey-core-1.9.jar:/usr/lib/hadoop-mapreduce/lib/jersey-guice-1.9.jar:/usr/lib/hadoop-mapreduce/lib/jersey-server-1.9.jar:/usr/lib/hadoop-mapreduce/lib/junit-4.11.jar:/usr/lib/hadoop-mapreduce/lib/leveldbjni-all-1.8.jar:/usr/lib/hadoop-mapreduce/lib/log4j-1.2.17.jar:/usr/lib/hadoop-mapreduce/lib/netty-3.6.2.Final.jar:/usr/lib/hadoop-mapreduce/lib/paranamer-2.3.jar:/usr/lib/hadoop-mapreduce/lib/protobuf-java-2.5.0.jar:/usr/lib/hadoop-mapreduce/lib/snappy-java-1.0.4.1.jar:/usr/lib/hadoop-mapreduce/lib/xz-1.0.jar:/usr/lib/hadoop-mapreduce/modules/*.jar
STARTUP_MSG:   build = http://github.com/cloudera/hadoop -r ab14c89fe25e9fb3f9de4fb852c21365b7c5608b; compiled by 'jenkins' on 2015-08-12T21:12Z
STARTUP_MSG:   java = 1.7.0_79
************************************************************/
Started Hadoop historyserver:                              [  OK  ]
[root@ip-172-31-57-217 ~]# ls
dans_bash_history.txt                    setuptools-20.3.1.zip
dead.letter                              start-hadoop.sh
EX2Tweetwordcount                        start-hadoop.sh~
ez_setup.py                              stop-hadoop.sh
ipython                                  stop-hadoop.sh~
pgxl-deployment-tools                    streamparse
rstudio-server-rhel-0.99.892-x86_64.rpm  w205-spring-16-labs-exercises
[root@ip-172-31-57-217 ~]# cd /data
[root@ip-172-31-57-217 data]# ls
[root@ip-172-31-57-217 data]# cd ..
[root@ip-172-31-57-217 /]# /data/start_postgres.sh
-bash: /data/start_postgres.sh: No such file or directory
[root@ip-172-31-57-217 /]# su - w205
[w205@ip-172-31-57-217 ~]$ python hello-stream-twitter.py
python: can't open file 'hello-stream-twitter.py': [Errno 2] No such file or directory
[w205@ip-172-31-57-217 ~]$ cd EX2T*
-bash: cd: EX2T*: No such file or directory
[w205@ip-172-31-57-217 ~]$ ls
derby.log  metastore_db  spark-1.5.0-bin-hadoop2.6.tgz  spark15
[w205@ip-172-31-57-217 ~]$ cd /root
-bash: cd: /root: Permission denied
[w205@ip-172-31-57-217 ~]$ exit   
logout
[root@ip-172-31-57-217 /]# su - w205
[w205@ip-172-31-57-217 ~]$ pip install psycopg2
Traceback (most recent call last):
  File "/usr/bin/pip", line 7, in <module>
    from pip import main
ImportError: No module named pip
[w205@ip-172-31-57-217 ~]$ exit
logout
[root@ip-172-31-57-217 /]# python --V
Unknown option: --
Unknown option: --
usage: python [option] ... [-c cmd | -m mod | file | -] [arg] ...
Try `python -h' for more information.
[root@ip-172-31-57-217 /]# ls
bin   data  etc   lib    lost+found  mnt  proc  sbin     srv  tmp  var
boot  dev   home  lib64  media       opt  root  selinux  sys  usr
[root@ip-172-31-57-217 /]# cd /data
[root@ip-172-31-57-217 data]# ls
[root@ip-172-31-57-217 data]# git clone
You must specify a repository to clone.

usage: git clone [options] [--] <repo> [<dir>]

    -v, --verbose         be more verbose
    -q, --quiet           be more quiet
    --progress            force progress reporting
    -n, --no-checkout     don't create a checkout
    --bare                create a bare repository
    --mirror              create a mirror repository (implies bare)
    -l, --local           to clone from a local repository
    --no-hardlinks        don't use local hardlinks, always copy
    -s, --shared          setup as shared repository
    --recursive           initialize submodules in the clone
    --template <path>     path the template repository
    --reference <repo>    reference repository
    -o, --origin <branch>
                          use <branch> instead of 'origin' to track upstream
    -b, --branch <branch>
                          checkout <branch> instead of the remote's HEAD
    -u, --upload-pack <path>
                          path to git-upload-pack on the remote
    --depth <depth>       create a shallow clone of that depth

[root@ip-172-31-57-217 data]# su - w205
[w205@ip-172-31-57-217 ~]$ git clone https://github.com/UC-Berkeley-I-School/w205-spring-16-labs-exercises
Initialized empty Git repository in /home/w205/w205-spring-16-labs-exercises/.git/
remote: Counting objects: 166, done.
remote: Compressing objects: 100% (13/13), done.
remote: Total 166 (delta 4), reused 0 (delta 0), pack-reused 153
Receiving objects: 100% (166/166), 344.84 MiB | 21.91 MiB/s, done.
Resolving deltas: 100% (41/41), done.
[w205@ip-172-31-57-217 ~]$ ls
derby.log     spark-1.5.0-bin-hadoop2.6.tgz  w205-spring-16-labs-exercises
metastore_db  spark15
[w205@ip-172-31-57-217 ~]$ cd w205*
[w205@ip-172-31-57-217 w205-spring-16-labs-exercises]$ ls
README.md  docs        exercise_2  lab_2  lab_4  lab_6  lab_8
data       exercise_1  lab_1       lab_3  lab_5  lab_7  lab_9
[w205@ip-172-31-57-217 w205-spring-16-labs-exercises]$ cd exercise_2
[w205@ip-172-31-57-217 exercise_2]$ ls
Exercise-2-Subject-205-Real Time Data Processing Using Apache Storm.pdf
Twittercredentials.py
hello-stream-twitter.py
psycopg-sample.py
tweetwordcount
[w205@ip-172-31-57-217 exercise_2]$ sparse quickstart EX2Tweetwordcount
Traceback (most recent call last):
  File "/usr/bin/sparse", line 5, in <module>
    from pkg_resources import load_entry_point
ImportError: No module named pkg_resources
[w205@ip-172-31-57-217 exercise_2]$ pythong --version
-bash: pythong: command not found
[w205@ip-172-31-57-217 exercise_2]$ python --version
Python 2.7.3
[w205@ip-172-31-57-217 exercise_2]$ sudo curl -o ez_setup.py https://bootstrap.pypa.io/ez_setup.py
[sudo] password for w205: 
Sorry, try again.
[sudo] password for w205: 
Sorry, try again.
[sudo] password for w205: 
Sorry, try again.
sudo: 3 incorrect password attempts
[w205@ip-172-31-57-217 exercise_2]$ pip
Traceback (most recent call last):
  File "/usr/bin/pip", line 7, in <module>
    from pip import main
ImportError: No module named pip
[w205@ip-172-31-57-217 exercise_2]$  exit
logout
[root@ip-172-31-57-217 data]# su - w205
[w205@ip-172-31-57-217 ~]$ sudo /usr/bin/easy_install-2.7 pip
[sudo] password for w205: 


Sorry, try again.
[sudo] password for w205: 



Sorry, try again.
[sudo] password for w205: 



Sorry, try again.
sudo: 3 incorrect password attempts
[w205@ip-172-31-57-217 ~]$ 
[w205@ip-172-31-57-217 ~]$ 
[w205@ip-172-31-57-217 ~]$ 
[w205@ip-172-31-57-217 ~]$ exit
logout
[root@ip-172-31-57-217 data]# python --version
Python 2.7.3
[root@ip-172-31-57-217 data]# sudo curl -o ez_setup.py https://bootstrap.pypa.io/ez_setup.py
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 12059  100 12059    0     0   112k      0 --:--:-- --:--:-- --:--:-- 1682k
[root@ip-172-31-57-217 data]# sudo python ez_setup.py
Downloading https://pypi.python.org/packages/source/s/setuptools/setuptools-20.6.7.zip
Extracting in /tmp/tmpps7Kwf
Now working in /tmp/tmpps7Kwf/setuptools-20.6.7
Installing Setuptools
running install
running bdist_egg
running egg_info
writing requirements to setuptools.egg-info/requires.txt
writing setuptools.egg-info/PKG-INFO
writing top-level names to setuptools.egg-info/top_level.txt
writing dependency_links to setuptools.egg-info/dependency_links.txt
writing entry points to setuptools.egg-info/entry_points.txt
reading manifest file 'setuptools.egg-info/SOURCES.txt'
reading manifest template 'MANIFEST.in'
warning: no files found matching '*.py' under directory '_markerlib'
warning: no files found matching '*' under directory 'setuptools/_vendor'
writing manifest file 'setuptools.egg-info/SOURCES.txt'
installing library code to build/bdist.linux-x86_64/egg
running install_lib
running build_py
creating build
creating build/lib
copying easy_install.py -> build/lib
creating build/lib/setuptools
copying setuptools/archive_util.py -> build/lib/setuptools
copying setuptools/launch.py -> build/lib/setuptools
copying setuptools/py27compat.py -> build/lib/setuptools
copying setuptools/version.py -> build/lib/setuptools
copying setuptools/depends.py -> build/lib/setuptools
copying setuptools/dist.py -> build/lib/setuptools
copying setuptools/py31compat.py -> build/lib/setuptools
copying setuptools/utils.py -> build/lib/setuptools
copying setuptools/py26compat.py -> build/lib/setuptools
copying setuptools/sandbox.py -> build/lib/setuptools
copying setuptools/windows_support.py -> build/lib/setuptools
copying setuptools/site-patch.py -> build/lib/setuptools
copying setuptools/msvc9_support.py -> build/lib/setuptools
copying setuptools/ssl_support.py -> build/lib/setuptools
copying setuptools/unicode_utils.py -> build/lib/setuptools
copying setuptools/extension.py -> build/lib/setuptools
copying setuptools/package_index.py -> build/lib/setuptools
copying setuptools/__init__.py -> build/lib/setuptools
copying setuptools/lib2to3_ex.py -> build/lib/setuptools
creating build/lib/pkg_resources
copying pkg_resources/__init__.py -> build/lib/pkg_resources
creating build/lib/setuptools/command
copying setuptools/command/upload_docs.py -> build/lib/setuptools/command
copying setuptools/command/rotate.py -> build/lib/setuptools/command
copying setuptools/command/register.py -> build/lib/setuptools/command
copying setuptools/command/test.py -> build/lib/setuptools/command
copying setuptools/command/alias.py -> build/lib/setuptools/command
copying setuptools/command/develop.py -> build/lib/setuptools/command
copying setuptools/command/saveopts.py -> build/lib/setuptools/command
copying setuptools/command/install.py -> build/lib/setuptools/command
copying setuptools/command/sdist.py -> build/lib/setuptools/command
copying setuptools/command/bdist_wininst.py -> build/lib/setuptools/command
copying setuptools/command/install_scripts.py -> build/lib/setuptools/command
copying setuptools/command/bdist_rpm.py -> build/lib/setuptools/command
copying setuptools/command/egg_info.py -> build/lib/setuptools/command
copying setuptools/command/easy_install.py -> build/lib/setuptools/command
copying setuptools/command/build_ext.py -> build/lib/setuptools/command
copying setuptools/command/bdist_egg.py -> build/lib/setuptools/command
copying setuptools/command/install_egg_info.py -> build/lib/setuptools/command
copying setuptools/command/setopt.py -> build/lib/setuptools/command
copying setuptools/command/upload.py -> build/lib/setuptools/command
copying setuptools/command/build_py.py -> build/lib/setuptools/command
copying setuptools/command/install_lib.py -> build/lib/setuptools/command
copying setuptools/command/__init__.py -> build/lib/setuptools/command
creating build/lib/setuptools/extern
copying setuptools/extern/__init__.py -> build/lib/setuptools/extern
creating build/lib/pkg_resources/_vendor
copying pkg_resources/_vendor/six.py -> build/lib/pkg_resources/_vendor
copying pkg_resources/_vendor/pyparsing.py -> build/lib/pkg_resources/_vendor
copying pkg_resources/_vendor/__init__.py -> build/lib/pkg_resources/_vendor
creating build/lib/pkg_resources/extern
copying pkg_resources/extern/__init__.py -> build/lib/pkg_resources/extern
creating build/lib/pkg_resources/_vendor/packaging
copying pkg_resources/_vendor/packaging/version.py -> build/lib/pkg_resources/_vendor/packaging
copying pkg_resources/_vendor/packaging/markers.py -> build/lib/pkg_resources/_vendor/packaging
copying pkg_resources/_vendor/packaging/utils.py -> build/lib/pkg_resources/_vendor/packaging
copying pkg_resources/_vendor/packaging/specifiers.py -> build/lib/pkg_resources/_vendor/packaging
copying pkg_resources/_vendor/packaging/__about__.py -> build/lib/pkg_resources/_vendor/packaging
copying pkg_resources/_vendor/packaging/_structures.py -> build/lib/pkg_resources/_vendor/packaging
copying pkg_resources/_vendor/packaging/requirements.py -> build/lib/pkg_resources/_vendor/packaging
copying pkg_resources/_vendor/packaging/__init__.py -> build/lib/pkg_resources/_vendor/packaging
copying pkg_resources/_vendor/packaging/_compat.py -> build/lib/pkg_resources/_vendor/packaging
copying setuptools/script (dev).tmpl -> build/lib/setuptools
copying setuptools/script.tmpl -> build/lib/setuptools
creating build/bdist.linux-x86_64
creating build/bdist.linux-x86_64/egg
creating build/bdist.linux-x86_64/egg/setuptools
copying build/lib/setuptools/archive_util.py -> build/bdist.linux-x86_64/egg/setuptools
copying build/lib/setuptools/launch.py -> build/bdist.linux-x86_64/egg/setuptools
copying build/lib/setuptools/py27compat.py -> build/bdist.linux-x86_64/egg/setuptools
copying build/lib/setuptools/version.py -> build/bdist.linux-x86_64/egg/setuptools
copying build/lib/setuptools/depends.py -> build/bdist.linux-x86_64/egg/setuptools
copying build/lib/setuptools/script.tmpl -> build/bdist.linux-x86_64/egg/setuptools
copying build/lib/setuptools/dist.py -> build/bdist.linux-x86_64/egg/setuptools
copying build/lib/setuptools/py31compat.py -> build/bdist.linux-x86_64/egg/setuptools
copying build/lib/setuptools/utils.py -> build/bdist.linux-x86_64/egg/setuptools
copying build/lib/setuptools/py26compat.py -> build/bdist.linux-x86_64/egg/setuptools
creating build/bdist.linux-x86_64/egg/setuptools/command
copying build/lib/setuptools/command/upload_docs.py -> build/bdist.linux-x86_64/egg/setuptools/command
copying build/lib/setuptools/command/rotate.py -> build/bdist.linux-x86_64/egg/setuptools/command
copying build/lib/setuptools/command/register.py -> build/bdist.linux-x86_64/egg/setuptools/command
copying build/lib/setuptools/command/test.py -> build/bdist.linux-x86_64/egg/setuptools/command
copying build/lib/setuptools/command/alias.py -> build/bdist.linux-x86_64/egg/setuptools/command
copying build/lib/setuptools/command/develop.py -> build/bdist.linux-x86_64/egg/setuptools/command
copying build/lib/setuptools/command/saveopts.py -> build/bdist.linux-x86_64/egg/setuptools/command
copying build/lib/setuptools/command/install.py -> build/bdist.linux-x86_64/egg/setuptools/command
copying build/lib/setuptools/command/sdist.py -> build/bdist.linux-x86_64/egg/setuptools/command
copying build/lib/setuptools/command/bdist_wininst.py -> build/bdist.linux-x86_64/egg/setuptools/command
copying build/lib/setuptools/command/install_scripts.py -> build/bdist.linux-x86_64/egg/setuptools/command
copying build/lib/setuptools/command/bdist_rpm.py -> build/bdist.linux-x86_64/egg/setuptools/command
copying build/lib/setuptools/command/egg_info.py -> build/bdist.linux-x86_64/egg/setuptools/command
copying build/lib/setuptools/command/easy_install.py -> build/bdist.linux-x86_64/egg/setuptools/command
copying build/lib/setuptools/command/build_ext.py -> build/bdist.linux-x86_64/egg/setuptools/command
copying build/lib/setuptools/command/bdist_egg.py -> build/bdist.linux-x86_64/egg/setuptools/command
copying build/lib/setuptools/command/install_egg_info.py -> build/bdist.linux-x86_64/egg/setuptools/command
copying build/lib/setuptools/command/setopt.py -> build/bdist.linux-x86_64/egg/setuptools/command
copying build/lib/setuptools/command/upload.py -> build/bdist.linux-x86_64/egg/setuptools/command
copying build/lib/setuptools/command/build_py.py -> build/bdist.linux-x86_64/egg/setuptools/command
copying build/lib/setuptools/command/install_lib.py -> build/bdist.linux-x86_64/egg/setuptools/command
copying build/lib/setuptools/command/__init__.py -> build/bdist.linux-x86_64/egg/setuptools/command
copying build/lib/setuptools/sandbox.py -> build/bdist.linux-x86_64/egg/setuptools
copying build/lib/setuptools/windows_support.py -> build/bdist.linux-x86_64/egg/setuptools
copying build/lib/setuptools/site-patch.py -> build/bdist.linux-x86_64/egg/setuptools
copying build/lib/setuptools/msvc9_support.py -> build/bdist.linux-x86_64/egg/setuptools
copying build/lib/setuptools/ssl_support.py -> build/bdist.linux-x86_64/egg/setuptools
copying build/lib/setuptools/unicode_utils.py -> build/bdist.linux-x86_64/egg/setuptools
copying build/lib/setuptools/extension.py -> build/bdist.linux-x86_64/egg/setuptools
copying build/lib/setuptools/script (dev).tmpl -> build/bdist.linux-x86_64/egg/setuptools
copying build/lib/setuptools/package_index.py -> build/bdist.linux-x86_64/egg/setuptools
copying build/lib/setuptools/__init__.py -> build/bdist.linux-x86_64/egg/setuptools
creating build/bdist.linux-x86_64/egg/setuptools/extern
copying build/lib/setuptools/extern/__init__.py -> build/bdist.linux-x86_64/egg/setuptools/extern
copying build/lib/setuptools/lib2to3_ex.py -> build/bdist.linux-x86_64/egg/setuptools
creating build/bdist.linux-x86_64/egg/pkg_resources
creating build/bdist.linux-x86_64/egg/pkg_resources/_vendor
creating build/bdist.linux-x86_64/egg/pkg_resources/_vendor/packaging
copying build/lib/pkg_resources/_vendor/packaging/version.py -> build/bdist.linux-x86_64/egg/pkg_resources/_vendor/packaging
copying build/lib/pkg_resources/_vendor/packaging/markers.py -> build/bdist.linux-x86_64/egg/pkg_resources/_vendor/packaging
copying build/lib/pkg_resources/_vendor/packaging/utils.py -> build/bdist.linux-x86_64/egg/pkg_resources/_vendor/packaging
copying build/lib/pkg_resources/_vendor/packaging/specifiers.py -> build/bdist.linux-x86_64/egg/pkg_resources/_vendor/packaging
copying build/lib/pkg_resources/_vendor/packaging/__about__.py -> build/bdist.linux-x86_64/egg/pkg_resources/_vendor/packaging
copying build/lib/pkg_resources/_vendor/packaging/_structures.py -> build/bdist.linux-x86_64/egg/pkg_resources/_vendor/packaging
copying build/lib/pkg_resources/_vendor/packaging/requirements.py -> build/bdist.linux-x86_64/egg/pkg_resources/_vendor/packaging
copying build/lib/pkg_resources/_vendor/packaging/__init__.py -> build/bdist.linux-x86_64/egg/pkg_resources/_vendor/packaging
copying build/lib/pkg_resources/_vendor/packaging/_compat.py -> build/bdist.linux-x86_64/egg/pkg_resources/_vendor/packaging
copying build/lib/pkg_resources/_vendor/six.py -> build/bdist.linux-x86_64/egg/pkg_resources/_vendor
copying build/lib/pkg_resources/_vendor/pyparsing.py -> build/bdist.linux-x86_64/egg/pkg_resources/_vendor
copying build/lib/pkg_resources/_vendor/__init__.py -> build/bdist.linux-x86_64/egg/pkg_resources/_vendor
copying build/lib/pkg_resources/__init__.py -> build/bdist.linux-x86_64/egg/pkg_resources
creating build/bdist.linux-x86_64/egg/pkg_resources/extern
copying build/lib/pkg_resources/extern/__init__.py -> build/bdist.linux-x86_64/egg/pkg_resources/extern
copying build/lib/easy_install.py -> build/bdist.linux-x86_64/egg
byte-compiling build/bdist.linux-x86_64/egg/setuptools/archive_util.py to archive_util.pyc
byte-compiling build/bdist.linux-x86_64/egg/setuptools/launch.py to launch.pyc
byte-compiling build/bdist.linux-x86_64/egg/setuptools/py27compat.py to py27compat.pyc
byte-compiling build/bdist.linux-x86_64/egg/setuptools/version.py to version.pyc
byte-compiling build/bdist.linux-x86_64/egg/setuptools/depends.py to depends.pyc
byte-compiling build/bdist.linux-x86_64/egg/setuptools/dist.py to dist.pyc
byte-compiling build/bdist.linux-x86_64/egg/setuptools/py31compat.py to py31compat.pyc
byte-compiling build/bdist.linux-x86_64/egg/setuptools/utils.py to utils.pyc
byte-compiling build/bdist.linux-x86_64/egg/setuptools/py26compat.py to py26compat.pyc
byte-compiling build/bdist.linux-x86_64/egg/setuptools/command/upload_docs.py to upload_docs.pyc
byte-compiling build/bdist.linux-x86_64/egg/setuptools/command/rotate.py to rotate.pyc
byte-compiling build/bdist.linux-x86_64/egg/setuptools/command/register.py to register.pyc
byte-compiling build/bdist.linux-x86_64/egg/setuptools/command/test.py to test.pyc
byte-compiling build/bdist.linux-x86_64/egg/setuptools/command/alias.py to alias.pyc
byte-compiling build/bdist.linux-x86_64/egg/setuptools/command/develop.py to develop.pyc
byte-compiling build/bdist.linux-x86_64/egg/setuptools/command/saveopts.py to saveopts.pyc
byte-compiling build/bdist.linux-x86_64/egg/setuptools/command/install.py to install.pyc
byte-compiling build/bdist.linux-x86_64/egg/setuptools/command/sdist.py to sdist.pyc
byte-compiling build/bdist.linux-x86_64/egg/setuptools/command/bdist_wininst.py to bdist_wininst.pyc
byte-compiling build/bdist.linux-x86_64/egg/setuptools/command/install_scripts.py to install_scripts.pyc
byte-compiling build/bdist.linux-x86_64/egg/setuptools/command/bdist_rpm.py to bdist_rpm.pyc
byte-compiling build/bdist.linux-x86_64/egg/setuptools/command/egg_info.py to egg_info.pyc
byte-compiling build/bdist.linux-x86_64/egg/setuptools/command/easy_install.py to easy_install.pyc
byte-compiling build/bdist.linux-x86_64/egg/setuptools/command/build_ext.py to build_ext.pyc
byte-compiling build/bdist.linux-x86_64/egg/setuptools/command/bdist_egg.py to bdist_egg.pyc
byte-compiling build/bdist.linux-x86_64/egg/setuptools/command/install_egg_info.py to install_egg_info.pyc
byte-compiling build/bdist.linux-x86_64/egg/setuptools/command/setopt.py to setopt.pyc
byte-compiling build/bdist.linux-x86_64/egg/setuptools/command/upload.py to upload.pyc
byte-compiling build/bdist.linux-x86_64/egg/setuptools/command/build_py.py to build_py.pyc
byte-compiling build/bdist.linux-x86_64/egg/setuptools/command/install_lib.py to install_lib.pyc
byte-compiling build/bdist.linux-x86_64/egg/setuptools/command/__init__.py to __init__.pyc
byte-compiling build/bdist.linux-x86_64/egg/setuptools/sandbox.py to sandbox.pyc
byte-compiling build/bdist.linux-x86_64/egg/setuptools/windows_support.py to windows_support.pyc
byte-compiling build/bdist.linux-x86_64/egg/setuptools/site-patch.py to site-patch.pyc
byte-compiling build/bdist.linux-x86_64/egg/setuptools/msvc9_support.py to msvc9_support.pyc
byte-compiling build/bdist.linux-x86_64/egg/setuptools/ssl_support.py to ssl_support.pyc
byte-compiling build/bdist.linux-x86_64/egg/setuptools/unicode_utils.py to unicode_utils.pyc
byte-compiling build/bdist.linux-x86_64/egg/setuptools/extension.py to extension.pyc
byte-compiling build/bdist.linux-x86_64/egg/setuptools/package_index.py to package_index.pyc
byte-compiling build/bdist.linux-x86_64/egg/setuptools/__init__.py to __init__.pyc
byte-compiling build/bdist.linux-x86_64/egg/setuptools/extern/__init__.py to __init__.pyc
byte-compiling build/bdist.linux-x86_64/egg/setuptools/lib2to3_ex.py to lib2to3_ex.pyc
byte-compiling build/bdist.linux-x86_64/egg/pkg_resources/_vendor/packaging/version.py to version.pyc
byte-compiling build/bdist.linux-x86_64/egg/pkg_resources/_vendor/packaging/markers.py to markers.pyc
byte-compiling build/bdist.linux-x86_64/egg/pkg_resources/_vendor/packaging/utils.py to utils.pyc
byte-compiling build/bdist.linux-x86_64/egg/pkg_resources/_vendor/packaging/specifiers.py to specifiers.pyc
byte-compiling build/bdist.linux-x86_64/egg/pkg_resources/_vendor/packaging/__about__.py to __about__.pyc
byte-compiling build/bdist.linux-x86_64/egg/pkg_resources/_vendor/packaging/_structures.py to _structures.pyc
byte-compiling build/bdist.linux-x86_64/egg/pkg_resources/_vendor/packaging/requirements.py to requirements.pyc
byte-compiling build/bdist.linux-x86_64/egg/pkg_resources/_vendor/packaging/__init__.py to __init__.pyc
byte-compiling build/bdist.linux-x86_64/egg/pkg_resources/_vendor/packaging/_compat.py to _compat.pyc
byte-compiling build/bdist.linux-x86_64/egg/pkg_resources/_vendor/six.py to six.pyc
byte-compiling build/bdist.linux-x86_64/egg/pkg_resources/_vendor/pyparsing.py to pyparsing.pyc
byte-compiling build/bdist.linux-x86_64/egg/pkg_resources/_vendor/__init__.py to __init__.pyc
byte-compiling build/bdist.linux-x86_64/egg/pkg_resources/__init__.py to __init__.pyc
byte-compiling build/bdist.linux-x86_64/egg/pkg_resources/extern/__init__.py to __init__.pyc
byte-compiling build/bdist.linux-x86_64/egg/easy_install.py to easy_install.pyc
creating build/bdist.linux-x86_64/egg/EGG-INFO
copying setuptools.egg-info/PKG-INFO -> build/bdist.linux-x86_64/egg/EGG-INFO
copying setuptools.egg-info/SOURCES.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
copying setuptools.egg-info/dependency_links.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
copying setuptools.egg-info/entry_points.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
copying setuptools.egg-info/requires.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
copying setuptools.egg-info/top_level.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
copying setuptools.egg-info/zip-safe -> build/bdist.linux-x86_64/egg/EGG-INFO
creating dist
creating 'dist/setuptools-20.6.7-py2.7.egg' and adding 'build/bdist.linux-x86_64/egg' to it
removing 'build/bdist.linux-x86_64/egg' (and everything under it)
Processing setuptools-20.6.7-py2.7.egg
Copying setuptools-20.6.7-py2.7.egg to /usr/lib/python2.7/site-packages
Adding setuptools 20.6.7 to easy-install.pth file
Installing easy_install script to /usr/bin
Installing easy_install-2.7 script to /usr/bin

Installed /usr/lib/python2.7/site-packages/setuptools-20.6.7-py2.7.egg
Processing dependencies for setuptools==20.6.7
Finished processing dependencies for setuptools==20.6.7
[root@ip-172-31-57-217 data]# sudo /usr/bin/easy_install-2.7 pip
Searching for pip
Reading https://pypi.python.org/simple/pip/
Best match: pip 8.1.1
Downloading https://pypi.python.org/packages/source/p/pip/pip-8.1.1.tar.gz#md5=6b86f11841e89c8241d689956ba99ed7
Processing pip-8.1.1.tar.gz
Writing /tmp/easy_install-ArN3HV/pip-8.1.1/setup.cfg
Running pip-8.1.1/setup.py -q bdist_egg --dist-dir /tmp/easy_install-ArN3HV/pip-8.1.1/egg-dist-tmp-bs4abO
warning: no previously-included files found matching '.coveragerc'
warning: no previously-included files found matching '.mailmap'
warning: no previously-included files found matching '.travis.yml'
warning: no previously-included files found matching '.landscape.yml'
warning: no previously-included files found matching 'pip/_vendor/Makefile'
warning: no previously-included files found matching 'tox.ini'
warning: no previously-included files found matching 'dev-requirements.txt'
warning: no previously-included files found matching 'appveyor.yml'
no previously-included directories found matching '.github'
no previously-included directories found matching '.travis'
no previously-included directories found matching 'docs/_build'
no previously-included directories found matching 'contrib'
no previously-included directories found matching 'tasks'
no previously-included directories found matching 'tests'
creating /usr/lib/python2.7/site-packages/pip-8.1.1-py2.7.egg
Extracting pip-8.1.1-py2.7.egg to /usr/lib/python2.7/site-packages
Adding pip 8.1.1 to easy-install.pth file
Installing pip script to /usr/bin
Installing pip2.7 script to /usr/bin
Installing pip2 script to /usr/bin

Installed /usr/lib/python2.7/site-packages/pip-8.1.1-py2.7.egg
Processing dependencies for pip
Finished processing dependencies for pip
[root@ip-172-31-57-217 data]# sudo pip install virtualenv
Collecting virtualenv
/usr/lib/python2.7/site-packages/pip-8.1.1-py2.7.egg/pip/_vendor/requests/packages/urllib3/util/ssl_.py:315: SNIMissingWarning: An HTTPS request has been made, but the SNI (Subject Name Indication) extension to TLS is not available on this platform. This may cause the server to present an incorrect TLS certificate, which can cause validation failures. For more information, see https://urllib3.readthedocs.org/en/latest/security.html#snimissingwarning.
  SNIMissingWarning
/usr/lib/python2.7/site-packages/pip-8.1.1-py2.7.egg/pip/_vendor/requests/packages/urllib3/util/ssl_.py:120: InsecurePlatformWarning: A true SSLContext object is not available. This prevents urllib3 from configuring SSL appropriately and may cause certain SSL connections to fail. For more information, see https://urllib3.readthedocs.org/en/latest/security.html#insecureplatformwarning.
  InsecurePlatformWarning
  Using cached virtualenv-15.0.1-py2.py3-none-any.whl
Installing collected packages: virtualenv
Successfully installed virtualenv-15.0.1
/usr/lib/python2.7/site-packages/pip-8.1.1-py2.7.egg/pip/_vendor/requests/packages/urllib3/util/ssl_.py:120: InsecurePlatformWarning: A true SSLContext object is not available. This prevents urllib3 from configuring SSL appropriately and may cause certain SSL connections to fail. For more information, see https://urllib3.readthedocs.org/en/latest/security.html#insecureplatformwarning.
  InsecurePlatformWarning
[root@ip-172-31-57-217 data]# wget --directory-prefix=/usr/bin https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein
--2016-04-07 12:26:11--  https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein
Resolving raw.githubusercontent.com... 199.27.76.133
Connecting to raw.githubusercontent.com|199.27.76.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 12871 (13K) [text/plain]
Saving to: “/usr/bin/lein.2”

100%[======================================>] 12,871      --.-K/s   in 0s      

2016-04-07 12:26:11 (553 MB/s) - “/usr/bin/lein.2” saved [12871/12871]

[root@ip-172-31-57-217 data]# ls -l /usr/bin/lein
-rwxr-xr-x 1 root root 12871 Mar 15 01:13 /usr/bin/lein
[root@ip-172-31-57-217 data]# chmod a+x /usr/bin/lein
[root@ip-172-31-57-217 data]# ls -l /usr/bin/lein
-rwxr-xr-x 1 root root 12871 Mar 15 01:13 /usr/bin/lein
[root@ip-172-31-57-217 data]# sudo /usr/bin/lein
WARNING: You're currently running as root; probably by accident.
Press control-C to abort or Enter to continue as root.
Set LEIN_ROOT to disable this warning.

Leiningen is a tool for working with Clojure projects.

Several tasks are available:
change              Rewrite project.clj by applying a function.
check               Check syntax and warn on reflection.
classpath           Print the classpath of the current project.
clean               Remove all files from project's target-path.
compile             Compile Clojure source into .class files.
deploy              Build and deploy jar to remote repository.
deps                Download all dependencies.
do                  Higher-order task to perform other tasks in succession.
help                Display a list of tasks or help for a given task.
install             Install the current project to the local repository.
jar                 Package up all the project's files into a jar file.
javac               Compile Java source files.
new                 Generate project scaffolding based on a template.
plugin              DEPRECATED. Please use the :user profile instead.
pom                 Write a pom.xml file to disk for Maven interoperability.
release             Perform :release-tasks.
repl                Start a repl session either with the current project or standalone.
retest              Run only the test namespaces which failed last time around.
run                 Run a -main function with optional command-line arguments.
search              Search remote maven repositories for matching jars.
show-profiles       List all available profiles or display one if given an argument.
test                Run the project's tests.
trampoline          Run a task without nesting the project's JVM inside Leiningen's.
uberjar             Package up the project files and dependencies into a jar file.
update-in           Perform arbitrary transformations on your project map.
upgrade             Upgrade Leiningen to specified version or latest stable.
vcs                 Interact with the version control system.
version             Print version for Leiningen and the current JVM.
with-profile        Apply the given task with the profile(s) specified.

Run `lein help $TASK` for details.

Global Options:
  -o             Run a task offline.
  -U             Run a task after forcing update of snapshots.
  -h, --help     Print this help or help for a specific task.
  -v, --version  Print Leiningen's version.

These aliases are available:
downgrade, expands to upgrade

See also: readme, faq, tutorial, news, sample, profiles, deploying, gpg,
mixed-source, templates, and copying.
[root@ip-172-31-57-217 data]# pip install streamparse
Collecting streamparse
/usr/lib/python2.7/site-packages/pip-8.1.1-py2.7.egg/pip/_vendor/requests/packages/urllib3/util/ssl_.py:315: SNIMissingWarning: An HTTPS request has been made, but the SNI (Subject Name Indication) extension to TLS is not available on this platform. This may cause the server to present an incorrect TLS certificate, which can cause validation failures. For more information, see https://urllib3.readthedocs.org/en/latest/security.html#snimissingwarning.
  SNIMissingWarning
/usr/lib/python2.7/site-packages/pip-8.1.1-py2.7.egg/pip/_vendor/requests/packages/urllib3/util/ssl_.py:120: InsecurePlatformWarning: A true SSLContext object is not available. This prevents urllib3 from configuring SSL appropriately and may cause certain SSL connections to fail. For more information, see https://urllib3.readthedocs.org/en/latest/security.html#insecureplatformwarning.
  InsecurePlatformWarning
Collecting requests (from streamparse)
  Using cached requests-2.9.1-py2.py3-none-any.whl
Collecting prettytable (from streamparse)
Collecting simplejson (from streamparse)
Collecting invoke>=0.8 (from streamparse)
  Using cached invoke-0.12.2-py2.py3-none-any.whl
Collecting jinja2 (from streamparse)
  Using cached Jinja2-2.8-py2.py3-none-any.whl
Collecting six>=1.5 (from streamparse)
  Using cached six-1.10.0-py2.py3-none-any.whl
Collecting contextlib2 (from streamparse)
Collecting fabric (from streamparse)
  Using cached Fabric-1.10.2-py2-none-any.whl
Collecting MarkupSafe (from jinja2->streamparse)
Collecting paramiko>=1.10 (from fabric->streamparse)
  Using cached paramiko-1.16.0-py2.py3-none-any.whl
Collecting ecdsa>=0.11 (from paramiko>=1.10->fabric->streamparse)
  Using cached ecdsa-0.13-py2.py3-none-any.whl
Collecting pycrypto!=2.4,>=2.1 (from paramiko>=1.10->fabric->streamparse)
Installing collected packages: requests, prettytable, simplejson, invoke, MarkupSafe, jinja2, six, contextlib2, ecdsa, pycrypto, paramiko, fabric, streamparse
Successfully installed MarkupSafe-0.23 contextlib2-0.5.1 ecdsa-0.13 fabric-1.10.2 invoke-0.12.2 jinja2-2.8 paramiko-1.16.0 prettytable-0.7.2 pycrypto-2.6.1 requests-2.9.1 simplejson-3.8.2 six-1.10.0 streamparse-2.1.4
[root@ip-172-31-57-217 data]# sparse quickstart EX2Tweetwordcount

Creating your EX2Tweetwordcount streamparse project...
    create    EX2Tweetwordcount
    create    EX2Tweetwordcount/.gitignore
    create    EX2Tweetwordcount/config.json
    create    EX2Tweetwordcount/fabfile.py
    create    EX2Tweetwordcount/project.clj
    create    EX2Tweetwordcount/README.md
    create    EX2Tweetwordcount/src
    create    EX2Tweetwordcount/src/bolts
    create    EX2Tweetwordcount/src/bolts/__init__.py
    create    EX2Tweetwordcount/src/bolts/wordcount.py
    create    EX2Tweetwordcount/src/spouts
    create    EX2Tweetwordcount/src/spouts/__init__.py
    create    EX2Tweetwordcount/src/spouts/words.py
    create    EX2Tweetwordcount/tasks.py
    create    EX2Tweetwordcount/topologies
    create    EX2Tweetwordcount/topologies/wordcount.clj
    create    EX2Tweetwordcount/virtualenvs
    create    EX2Tweetwordcount/virtualenvs/wordcount.txt
Done.

Try running your topology locally with:

	cd EX2Tweetwordcount
	sparse run
[root@ip-172-31-57-217 data]# pwd
/data
[root@ip-172-31-57-217 data]# ls
EX2Tweetwordcount  ez_setup.py  setuptools-20.6.7.zip
[root@ip-172-31-57-217 data]# cd EX2Tweetwordcount
[root@ip-172-31-57-217 EX2Tweetwordcount]# ls
config.json  project.clj  src       topologies
fabfile.py   README.md    tasks.py  virtualenvs
[root@ip-172-31-57-217 EX2Tweetwordcount]# cd src
[root@ip-172-31-57-217 src]# ls
bolts  spouts
[root@ip-172-31-57-217 src]# cd spouts
[root@ip-172-31-57-217 spouts]# ls
__init__.py  words.py
[root@ip-172-31-57-217 spouts]# cd /root
[root@ip-172-31-57-217 ~]# ls
dans_bash_history.txt                    setuptools-20.3.1.zip
dead.letter                              start-hadoop.sh
EX2Tweetwordcount                        start-hadoop.sh~
ez_setup.py                              stop-hadoop.sh
ipython                                  stop-hadoop.sh~
pgxl-deployment-tools                    streamparse
rstudio-server-rhel-0.99.892-x86_64.rpm  w205-spring-16-labs-exercises
[root@ip-172-31-57-217 ~]# cd w205*
[root@ip-172-31-57-217 w205-spring-16-labs-exercises]# ls
data  exercise_1  lab_1  lab_3  lab_5  README.md
docs  exercise_2  lab_2  lab_4  lab_6
[root@ip-172-31-57-217 w205-spring-16-labs-exercises]# cd exercise_2
[root@ip-172-31-57-217 exercise_2]# ls
Exercise-2-Subject-205-Real Time Data Processing Using Apache Storm.pdf
hello-stream-twitter.py
psycopg-sample.py
tweetwordcount
Twittercredentials.py
[root@ip-172-31-57-217 exercise_2]# cd tweetwordcount
[root@ip-172-31-57-217 tweetwordcount]# ls
config.json  project.clj  src       topologies
fabfile.py   README.md    tasks.py  virtualenvs
[root@ip-172-31-57-217 tweetwordcount]# cd src
[root@ip-172-31-57-217 src]# ls
bolts  spouts
[root@ip-172-31-57-217 src]# cs spouts
-bash: cs: command not found
[root@ip-172-31-57-217 src]# cd spouts
[root@ip-172-31-57-217 spouts]# ls
__init__.py  tweets.py
[root@ip-172-31-57-217 spouts]# pwd 
/root/w205-spring-16-labs-exercises/exercise_2/tweetwordcount/src/spouts
[root@ip-172-31-57-217 spouts]# cd tweets.py /root/EX2Tweetwordcount/src/spouts
-bash: cd: tweets.py: Not a directory
[root@ip-172-31-57-217 spouts]# cp tweets.py /root/EX2Tweetwordcount/src/spouts
[root@ip-172-31-57-217 spouts]# cd ..
[root@ip-172-31-57-217 src]# ls
bolts  spouts
[root@ip-172-31-57-217 src]# cd bolts
[root@ip-172-31-57-217 bolts]# ls
__init__.py  parse.py  wordcount.py
[root@ip-172-31-57-217 bolts]# cp .py /root/EX2Tweetwordcount/src/bolts
cp: cannot stat `.py': No such file or directory
[root@ip-172-31-57-217 bolts]# cp *.py /root/EX2Tweetwordcount/src/bolts
[root@ip-172-31-57-217 bolts]# cd ..
[root@ip-172-31-57-217 src]# ls
bolts  spouts
[root@ip-172-31-57-217 src]# cd ..
[root@ip-172-31-57-217 tweetwordcount]# ls
config.json  project.clj  src       topologies
fabfile.py   README.md    tasks.py  virtualenvs
[root@ip-172-31-57-217 tweetwordcount]# cd topologies
[root@ip-172-31-57-217 topologies]# ls
tweetwordcount.clj
[root@ip-172-31-57-217 topologies]# cp *.clj /root/EX2Tweetwordcount/topologies
[root@ip-172-31-57-217 topologies]# cd ..
[root@ip-172-31-57-217 tweetwordcount]# ls
config.json  project.clj  src       topologies
fabfile.py   README.md    tasks.py  virtualenvs
[root@ip-172-31-57-217 tweetwordcount]# cd ..
[root@ip-172-31-57-217 exercise_2]# ls
Exercise-2-Subject-205-Real Time Data Processing Using Apache Storm.pdf
hello-stream-twitter.py
psycopg-sample.py
tweetwordcount
Twittercredentials.py
[root@ip-172-31-57-217 exercise_2]# cp .py /root/EX2Tweetwordcount
cp: cannot stat `.py': No such file or directory
[root@ip-172-31-57-217 exercise_2]# cp *.py /root/EX2Tweetwordcount
[root@ip-172-31-57-217 exercise_2]# cd /root/EX2*
[root@ip-172-31-57-217 EX2Tweetwordcount]# ls
config.json              project.clj        src         Twittercredentials.py
fabfile.py               psycopg-sample.py  tasks.py    Twittercredentials.pyc
hello-stream-twitter.py  README.md          topologies  virtualenvs
[root@ip-172-31-57-217 EX2Tweetwordcount]# cd topologies
[root@ip-172-31-57-217 topologies]# ls
tweetwordcount.clj
[root@ip-172-31-57-217 topologies]# cd ..
[root@ip-172-31-57-217 EX2Tweetwordcount]# cd src/bolts
[root@ip-172-31-57-217 bolts]# ls
__init__.py  parse.py  wordcount.py
[root@ip-172-31-57-217 bolts]# cd ..
[root@ip-172-31-57-217 src]# ls
bolts  spouts
[root@ip-172-31-57-217 src]# cd spouts
[root@ip-172-31-57-217 spouts]# ls
__init__.py  tweets.py
[root@ip-172-31-57-217 spouts]# cd ..
[root@ip-172-31-57-217 src]# ls
bolts  spouts
[root@ip-172-31-57-217 src]# cd ..
[root@ip-172-31-57-217 EX2Tweetwordcount]# ls
config.json              project.clj        src         Twittercredentials.py
fabfile.py               psycopg-sample.py  tasks.py    Twittercredentials.pyc
hello-stream-twitter.py  README.md          topologies  virtualenvs
[root@ip-172-31-57-217 EX2Tweetwordcount]# pip install tweepy
Collecting tweepy
/usr/lib/python2.7/site-packages/pip-8.1.1-py2.7.egg/pip/_vendor/requests/packages/urllib3/util/ssl_.py:315: SNIMissingWarning: An HTTPS request has been made, but the SNI (Subject Name Indication) extension to TLS is not available on this platform. This may cause the server to present an incorrect TLS certificate, which can cause validation failures. For more information, see https://urllib3.readthedocs.org/en/latest/security.html#snimissingwarning.
  SNIMissingWarning
/usr/lib/python2.7/site-packages/pip-8.1.1-py2.7.egg/pip/_vendor/requests/packages/urllib3/util/ssl_.py:120: InsecurePlatformWarning: A true SSLContext object is not available. This prevents urllib3 from configuring SSL appropriately and may cause certain SSL connections to fail. For more information, see https://urllib3.readthedocs.org/en/latest/security.html#insecureplatformwarning.
  InsecurePlatformWarning
  Using cached tweepy-3.5.0-py2.py3-none-any.whl
Requirement already satisfied (use --upgrade to upgrade): requests>=2.4.3 in /usr/lib/python2.7/site-packages (from tweepy)
Requirement already satisfied (use --upgrade to upgrade): six>=1.7.3 in /usr/lib/python2.7/site-packages (from tweepy)
Collecting requests-oauthlib>=0.4.1 (from tweepy)
  Using cached requests_oauthlib-0.6.1-py2.py3-none-any.whl
Collecting oauthlib>=0.6.2 (from requests-oauthlib>=0.4.1->tweepy)
Installing collected packages: oauthlib, requests-oauthlib, tweepy
Successfully installed oauthlib-1.0.3 requests-oauthlib-0.6.1 tweepy-3.5.0
[root@ip-172-31-57-217 EX2Tweetwordcount]# pwd
/root/EX2Tweetwordcount
[root@ip-172-31-57-217 EX2Tweetwordcount]# ls
config.json              project.clj        src         Twittercredentials.py
fabfile.py               psycopg-sample.py  tasks.py    Twittercredentials.pyc
hello-stream-twitter.py  README.md          topologies  virtualenvs
[root@ip-172-31-57-217 EX2Tweetwordcount]# vi Twittercredentials.py
[root@ip-172-31-57-217 EX2Tweetwordcount]# vt Twittercredentials.pyc
-bash: vt: command not found
[root@ip-172-31-57-217 EX2Tweetwordcount]# vi Twittercredentials.pyc
[root@ip-172-31-57-217 EX2Tweetwordcount]# vi Twittercredentials.py
[root@ip-172-31-57-217 EX2Tweetwordcount]# python hello-stream-twitter.py
Gathering data at Thu Apr  7 12:41:12 2016
Start Time = Thu Apr  7 12:41:12 2016
/usr/lib/python2.7/site-packages/requests/packages/urllib3/util/ssl_.py:315: SNIMissingWarning: An HTTPS request has been made, but the SNI (Subject Name Indication) extension to TLS is not available on this platform. This may cause the server to present an incorrect TLS certificate, which can cause validation failures. For more information, see https://urllib3.readthedocs.org/en/latest/security.html#snimissingwarning.
  SNIMissingWarning
/usr/lib/python2.7/site-packages/requests/packages/urllib3/util/ssl_.py:120: InsecurePlatformWarning: A true SSLContext object is not available. This prevents urllib3 from configuring SSL appropriately and may cause certain SSL connections to fail. For more information, see https://urllib3.readthedocs.org/en/latest/security.html#insecureplatformwarning.
  InsecurePlatformWarning
Count==  2823
End Time = Thu Apr  7 12:42:12 2016
Elapsed Time = 60.0725858212
[root@ip-172-31-57-217 EX2Tweetwordcount]# vi create_dp.py
[root@ip-172-31-57-217 EX2Tweetwordcount]# ls
config.json              project.clj        tasks.py                virtualenvs
create_dp.py             psycopg-sample.py  topologies
fabfile.py               README.md          Twittercredentials.py
hello-stream-twitter.py  src                Twittercredentials.pyc
[root@ip-172-31-57-217 EX2Tweetwordcount]# vi psycopg-sample.py
[root@ip-172-31-57-217 EX2Tweetwordcount]# vi create_dp.py
[root@ip-172-31-57-217 EX2Tweetwordcount]# python create_dp
python: can't open file 'create_dp': [Errno 2] No such file or directory
[root@ip-172-31-57-217 EX2Tweetwordcount]# python create_dp.py
Traceback (most recent call last):
  File "create_dp.py", line 1, in <module>
    from psycopg2 import connect
ImportError: No module named psycopg2
[root@ip-172-31-57-217 EX2Tweetwordcount]# pip install psycopg2
Collecting psycopg2
/usr/lib/python2.7/site-packages/pip-8.1.1-py2.7.egg/pip/_vendor/requests/packages/urllib3/util/ssl_.py:315: SNIMissingWarning: An HTTPS request has been made, but the SNI (Subject Name Indication) extension to TLS is not available on this platform. This may cause the server to present an incorrect TLS certificate, which can cause validation failures. For more information, see https://urllib3.readthedocs.org/en/latest/security.html#snimissingwarning.
  SNIMissingWarning
/usr/lib/python2.7/site-packages/pip-8.1.1-py2.7.egg/pip/_vendor/requests/packages/urllib3/util/ssl_.py:120: InsecurePlatformWarning: A true SSLContext object is not available. This prevents urllib3 from configuring SSL appropriately and may cause certain SSL connections to fail. For more information, see https://urllib3.readthedocs.org/en/latest/security.html#insecureplatformwarning.
  InsecurePlatformWarning
Installing collected packages: psycopg2
Successfully installed psycopg2-2.6.1
[root@ip-172-31-57-217 EX2Tweetwordcount]# python create_dp.py
Traceback (most recent call last):
  File "create_dp.py", line 3, in <module>
    from pyscopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
ImportError: No module named pyscopg2.extensions
[root@ip-172-31-57-217 EX2Tweetwordcount]# ls
config.json              project.clj        tasks.py                virtualenvs
create_dp.py             psycopg-sample.py  topologies
fabfile.py               README.md          Twittercredentials.py
hello-stream-twitter.py  src                Twittercredentials.pyc
[root@ip-172-31-57-217 EX2Tweetwordcount]# vi psycopy-sample.py
[root@ip-172-31-57-217 EX2Tweetwordcount]# vi psycopg-sample.py
[root@ip-172-31-57-217 EX2Tweetwordcount]# mv create_dp.py create_db.py
[root@ip-172-31-57-217 EX2Tweetwordcount]# vi create_db.py
[root@ip-172-31-57-217 EX2Tweetwordcount]# python create_db.py
Traceback (most recent call last):
  File "create_db.py", line 4, in <module>
    con = connect(dbname='postgres', user='postgres', host='localhost', password='pass')
NameError: name 'connect' is not defined
[root@ip-172-31-57-217 EX2Tweetwordcount]# vi create_db.py
[root@ip-172-31-57-217 EX2Tweetwordcount]# python create_db.py
Traceback (most recent call last):
  File "create_db.py", line 2, in <module>
    from psychopg2 import connect
ImportError: No module named psychopg2
[root@ip-172-31-57-217 EX2Tweetwordcount]# vi create_db.py
[root@ip-172-31-57-217 EX2Tweetwordcount]# python create_db.py
Traceback (most recent call last):
  File "create_db.py", line 5, in <module>
    con = connect(dbname='postgres', user='postgres', host='localhost', password='pass')
  File "/usr/lib64/python2.7/site-packages/psycopg2/__init__.py", line 164, in connect
    conn = _connect(dsn, connection_factory=connection_factory, async=async)
psycopg2.OperationalError: could not connect to server: Connection refused
	Is the server running on host "localhost" and accepting
	TCP/IP connections on port 5432?

[root@ip-172-31-57-217 EX2Tweetwordcount]# python create_db.py
Traceback (most recent call last):
  File "create_db.py", line 5, in <module>
    con = connect(dbname='postgres', user='postgres', host='localhost', password='pass')
  File "/usr/lib64/python2.7/site-packages/psycopg2/__init__.py", line 164, in connect
    conn = _connect(dsn, connection_factory=connection_factory, async=async)
psycopg2.OperationalError: could not connect to server: Connection refused
	Is the server running on host "localhost" and accepting
	TCP/IP connections on port 5432?

[root@ip-172-31-57-217 EX2Tweetwordcount]# cd /root
[root@ip-172-31-57-217 ~]# cd /data
[root@ip-172-31-57-217 data]# ls
EX2Tweetwordcount  ez_setup.py  setuptools-20.6.7.zip
[root@ip-172-31-57-217 data]# cd /root
[root@ip-172-31-57-217 ~]# wget httsp://s3.amazonaws.com/ucbdatasciencew205/setup_ucb_complete_plus_postgres.sh
httsp://s3.amazonaws.com/ucbdatasciencew205/setup_ucb_complete_plus_postgres.sh: Unsupported scheme “httsp”.
[root@ip-172-31-57-217 ~]# wget https://s3.amazonaws.com/ucbdatasciencew205/setup_ucb_complete_plus_postgres.sh
--2016-04-07 13:18:59--  https://s3.amazonaws.com/ucbdatasciencew205/setup_ucb_complete_plus_postgres.sh
Resolving s3.amazonaws.com... 54.231.19.171
Connecting to s3.amazonaws.com|54.231.19.171|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 5716 (5.6K) [application/x-sh]
Saving to: “setup_ucb_complete_plus_postgres.sh”

100%[======================================>] 5,716       --.-K/s   in 0s      

2016-04-07 13:18:59 (132 MB/s) - “setup_ucb_complete_plus_postgres.sh” saved [5716/5716]

[root@ip-172-31-57-217 ~]# chmod +x ./setup_ucb_complete_plus_postgres.sh
[root@ip-172-31-57-217 ~]# ./setup_usc_complete_plus_postgres.sh
-bash: ./setup_usc_complete_plus_postgres.sh: No such file or directory
[root@ip-172-31-57-217 ~]# ls
dans_bash_history.txt                    setup_ucb_complete_plus_postgres.sh
dead.letter                              start-hadoop.sh
EX2Tweetwordcount                        start-hadoop.sh~
ez_setup.py                              stop-hadoop.sh
ipython                                  stop-hadoop.sh~
pgxl-deployment-tools                    streamparse
rstudio-server-rhel-0.99.892-x86_64.rpm  w205-spring-16-labs-exercises
setuptools-20.3.1.zip
[root@ip-172-31-57-217 ~]# ./setup_ucb_complete_plus_postgres.sh
umount: /data: not mounted
using drive 
WARNING!! This will format the drive at
Press any key to continue or control-C to quit...

[root@ip-172-31-57-217 ~]# ls
dans_bash_history.txt                    setup_ucb_complete_plus_postgres.sh
dead.letter                              start-hadoop.sh
EX2Tweetwordcount                        start-hadoop.sh~
ez_setup.py                              stop-hadoop.sh
ipython                                  stop-hadoop.sh~
pgxl-deployment-tools                    streamparse
rstudio-server-rhel-0.99.892-x86_64.rpm  w205-spring-16-labs-exercises
setuptools-20.3.1.zip
[root@ip-172-31-57-217 ~]# cd /data
[root@ip-172-31-57-217 data]# ls
EX2Tweetwordcount  ez_setup.py  setuptools-20.6.7.zip
[root@ip-172-31-57-217 data]# vi start_postgres.sh
[root@ip-172-31-57-217 data]# vi stop_postgres.sh
[root@ip-172-31-57-217 data]# cd /root
[root@ip-172-31-57-217 ~]# /data/start_postgres.sh
-bash: /data/start_postgres.sh: Permission denied
[root@ip-172-31-57-217 ~]# sudo -u postgres pg_ctl -D /data/pgsql/data -l /data/pgsql/logs/pgsql.log start
could not change directory to "/root"
server starting
sh: /data/pgsql/logs/pgsql.log: No such file or directory
[root@ip-172-31-57-217 ~]# pwd
/root
[root@ip-172-31-57-217 ~]# ls
dans_bash_history.txt                    setup_ucb_complete_plus_postgres.sh
dead.letter                              start-hadoop.sh
EX2Tweetwordcount                        start-hadoop.sh~
ez_setup.py                              stop-hadoop.sh
ipython                                  stop-hadoop.sh~
pgxl-deployment-tools                    streamparse
rstudio-server-rhel-0.99.892-x86_64.rpm  w205-spring-16-labs-exercises
setuptools-20.3.1.zip
[root@ip-172-31-57-217 ~]# cd EX2Tweetwordcount
[root@ip-172-31-57-217 EX2Tweetwordcount]# ls
config.json              project.clj        tasks.py                virtualenvs
create_db.py             psycopg-sample.py  topologies
fabfile.py               README.md          Twittercredentials.py
hello-stream-twitter.py  src                Twittercredentials.pyc
[root@ip-172-31-57-217 EX2Tweetwordcount]# python create_db.py
Traceback (most recent call last):
  File "create_db.py", line 5, in <module>
    con = connect(dbname='postgres', user='postgres', host='localhost', password='pass')
  File "/usr/lib64/python2.7/site-packages/psycopg2/__init__.py", line 164, in connect
    conn = _connect(dsn, connection_factory=connection_factory, async=async)
psycopg2.OperationalError: could not connect to server: Connection refused
	Is the server running on host "localhost" and accepting
	TCP/IP connections on port 5432?

[root@ip-172-31-57-217 EX2Tweetwordcount]# ls
config.json              project.clj        tasks.py                virtualenvs
create_db.py             psycopg-sample.py  topologies
fabfile.py               README.md          Twittercredentials.py
hello-stream-twitter.py  src                Twittercredentials.pyc
[root@ip-172-31-57-217 EX2Tweetwordcount]# cd ..
[root@ip-172-31-57-217 ~]# 
Broadcast message from root@ip-172-31-57-217
	(unknown) at 13:44 ...

The system is going down for power off NOW!
Connection to ec2-54-174-173-7.compute-1.amazonaws.com closed by remote host.
Connection to ec2-54-174-173-7.compute-1.amazonaws.com closed.
Alfreds-MBP:downloads alfredarsenault$ cd downloads
-bash: cd: downloads: No such file or directory
Alfreds-MBP:downloads alfredarsenault$ ssh -i "Exercise_2_keys.pem" root@ec2-54-88-237-162.compute-1.amazonaws.com
The authenticity of host 'ec2-54-88-237-162.compute-1.amazonaws.com (54.88.237.162)' can't be established.
RSA key fingerprint is SHA256:35xjINeYN9dLD1VSJFvj6G3fHiaEoiIp3uouzLUl+KQ.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'ec2-54-88-237-162.compute-1.amazonaws.com,54.88.237.162' (RSA) to the list of known hosts.
Last login: Thu Apr  7 11:56:42 2016 from 108.40.124.232
     ___   _        __   __   ____            __    
    / _ \ (_)___ _ / /  / /_ / __/____ ___ _ / /___ 
   / , _// // _ `// _ \/ __/_\ \ / __// _ `// // -_)
  /_/|_|/_/ \_, //_//_/\__//___/ \__/ \_,_//_/ \__/ 
           /___/                                                 
                                              
Welcome to a virtual machine image brought to you by RightScale!


[root@ip-172-31-57-217 ~]# cd data
-bash: cd: data: No such file or directory
[root@ip-172-31-57-217 ~]# cd /data
[root@ip-172-31-57-217 data]# ls
EX2Tweetwordcount  setuptools-20.6.7.zip  stop_postgres.sh
ez_setup.py        start_postgres.sh
[root@ip-172-31-57-217 data]# start_postgres.sh
-bash: start_postgres.sh: command not found
[root@ip-172-31-57-217 data]# ls
EX2Tweetwordcount  setuptools-20.6.7.zip  stop_postgres.sh
ez_setup.py        start_postgres.sh
[root@ip-172-31-57-217 data]# start_postgres.sh
-bash: start_postgres.sh: command not found
[root@ip-172-31-57-217 data]# cd ..
[root@ip-172-31-57-217 /]# /root/stop_hadoop.sh
-bash: /root/stop_hadoop.sh: No such file or directory
[root@ip-172-31-57-217 /]# ls
bin   data  etc   lib    lost+found  mnt  proc  sbin     srv  tmp  var
boot  dev   home  lib64  media       opt  root  selinux  sys  usr
[root@ip-172-31-57-217 /]# cd /data/EX2Tweetwordcount
[root@ip-172-31-57-217 EX2Tweetwordcount]# ls
config.json  project.clj  src       topologies
fabfile.py   README.md    tasks.py  virtualenvs
[root@ip-172-31-57-217 EX2Tweetwordcount]# cd src
[root@ip-172-31-57-217 src]# ls
bolts  spouts
[root@ip-172-31-57-217 src]# cd bolts
[root@ip-172-31-57-217 bolts]# ls
__init__.py  wordcount.py
[root@ip-172-31-57-217 bolts]# cd ..
[root@ip-172-31-57-217 src]# ls
bolts  spouts
[root@ip-172-31-57-217 src]# cd spouts
[root@ip-172-31-57-217 spouts]# ls
__init__.py  words.py
[root@ip-172-31-57-217 spouts]# su - w205
[w205@ip-172-31-57-217 ~]$ ls
derby.log     spark-1.5.0-bin-hadoop2.6.tgz  w205-spring-16-labs-exercises
metastore_db  spark15
[w205@ip-172-31-57-217 ~]$ exit
logout
[root@ip-172-31-57-217 spouts]# lsblk
NAME  MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
xvda1 202:1    0   30G  0 disk /
xvdf  202:80   0  100G  0 disk 
xvdb  202:16   0   30G  0 disk 
[root@ip-172-31-57-217 spouts]# sudo file -s /dev/xvdf
/dev/xvdf: Linux rev 1.0 ext4 filesystem data (extents) (large files) (huge files)
[root@ip-172-31-57-217 spouts]# sudo mount /dev/xvdf /data
[root@ip-172-31-57-217 spouts]# ls
__init__.py  words.py
[root@ip-172-31-57-217 spouts]# cd /root
[root@ip-172-31-57-217 ~]# ls
dans_bash_history.txt                    setup_ucb_complete_plus_postgres.sh
dead.letter                              start-hadoop.sh
EX2Tweetwordcount                        start-hadoop.sh~
ez_setup.py                              stop-hadoop.sh
ipython                                  stop-hadoop.sh~
pgxl-deployment-tools                    streamparse
rstudio-server-rhel-0.99.892-x86_64.rpm  w205-spring-16-labs-exercises
setuptools-20.3.1.zip
[root@ip-172-31-57-217 ~]# /data/stop-hadoop.sh
-bash: /data/stop-hadoop.sh: No such file or directory
[root@ip-172-31-57-217 ~]# /root/stop-hadoop.sh
stopping resourcemanager
Stopped Hadoop resourcemanager:                            [  OK  ]
stopping nodemanager
Stopped Hadoop nodemanager:                                [  OK  ]
stopping historyserver
historyserver did not stop gracefully after 5 seconds: killing with kill -9
Stopped Hadoop historyserver:                              [  OK  ]
no datanode to stop
Stopped Hadoop datanode:                                   [  OK  ]
no namenode to stop
Stopped Hadoop namenode:                                   [  OK  ]
no secondarynamenode to stop
Stopped Hadoop secondarynamenode:                          [  OK  ]
[root@ip-172-31-57-217 ~]# /data/stop_postgres.sh
could not change directory to "/root"
pg_ctl: PID file "/data/pgsql/data/postmaster.pid" does not exist
Is server running?
[root@ip-172-31-57-217 ~]# /root/start-hadoop.sh
no datanode to stop
Stopped Hadoop datanode:                                   [  OK  ]
starting datanode, logging to /var/log/hadoop-hdfs/hadoop-hdfs-datanode-ip-172-31-57-217.out
Started Hadoop datanode (hadoop-hdfs-datanode):            [  OK  ]
no namenode to stop
Stopped Hadoop namenode:                                   [  OK  ]
starting namenode, logging to /var/log/hadoop-hdfs/hadoop-hdfs-namenode-ip-172-31-57-217.out
Failed to start Hadoop namenode. Return value: 1           [FAILED]
no secondarynamenode to stop
Stopped Hadoop secondarynamenode:                          [  OK  ]
starting secondarynamenode, logging to /var/log/hadoop-hdfs/hadoop-hdfs-secondarynamenode-ip-172-31-57-217.out
Started Hadoop secondarynamenode:                          [  OK  ]
no resourcemanager to stop
Stopped Hadoop resourcemanager:                            [  OK  ]
starting resourcemanager, logging to /var/log/hadoop-yarn/yarn-yarn-resourcemanager-ip-172-31-57-217.out
Started Hadoop resourcemanager:                            [  OK  ]
no nodemanager to stop
Stopped Hadoop nodemanager:                                [  OK  ]
starting nodemanager, logging to /var/log/hadoop-yarn/yarn-yarn-nodemanager-ip-172-31-57-217.out
Started Hadoop nodemanager:                                [  OK  ]
no historyserver to stop
Stopped Hadoop historyserver:                              [  OK  ]
starting historyserver, logging to /var/log/hadoop-mapreduce/mapred-mapred-historyserver-ip-172-31-57-217.out
16/04/07 13:57:34 INFO hs.JobHistoryServer: STARTUP_MSG: 
/************************************************************
STARTUP_MSG: Starting JobHistoryServer
STARTUP_MSG:   host = ip-172-31-57-217.ec2.internal/172.31.57.217
STARTUP_MSG:   args = []
STARTUP_MSG:   version = 2.6.0-cdh5.4.5
STARTUP_MSG:   classpath = /etc/hadoop/conf:/usr/lib/hadoop/lib/apacheds-i18n-2.0.0-M15.jar:/usr/lib/hadoop/lib/asm-3.2.jar:/usr/lib/hadoop/lib/jersey-core-1.9.jar:/usr/lib/hadoop/lib/mockito-all-1.8.5.jar:/usr/lib/hadoop/lib/api-asn1-api-1.0.0-M20.jar:/usr/lib/hadoop/lib/curator-framework-2.7.1.jar:/usr/lib/hadoop/lib/slf4j-log4j12.jar:/usr/lib/hadoop/lib/jersey-json-1.9.jar:/usr/lib/hadoop/lib/aws-java-sdk-1.7.14.jar:/usr/lib/hadoop/lib/java-xmlbuilder-0.4.jar:/usr/lib/hadoop/lib/guava-11.0.2.jar:/usr/lib/hadoop/lib/xz-1.0.jar:/usr/lib/hadoop/lib/jaxb-impl-2.2.3-1.jar:/usr/lib/hadoop/lib/jackson-mapper-asl-1.8.8.jar:/usr/lib/hadoop/lib/commons-configuration-1.6.jar:/usr/lib/hadoop/lib/curator-client-2.7.1.jar:/usr/lib/hadoop/lib/xmlenc-0.52.jar:/usr/lib/hadoop/lib/commons-compress-1.4.1.jar:/usr/lib/hadoop/lib/hamcrest-core-1.3.jar:/usr/lib/hadoop/lib/htrace-core-3.0.4.jar:/usr/lib/hadoop/lib/jasper-compiler-5.5.23.jar:/usr/lib/hadoop/lib/avro.jar:/usr/lib/hadoop/lib/jsr305-3.0.0.jar:/usr/lib/hadoop/lib/commons-el-1.0.jar:/usr/lib/hadoop/lib/stax-api-1.0-2.jar:/usr/lib/hadoop/lib/jsch-0.1.42.jar:/usr/lib/hadoop/lib/commons-net-3.1.jar:/usr/lib/hadoop/lib/snappy-java-1.0.4.1.jar:/usr/lib/hadoop/lib/zookeeper.jar:/usr/lib/hadoop/lib/jackson-jaxrs-1.8.8.jar:/usr/lib/hadoop/lib/commons-io-2.4.jar:/usr/lib/hadoop/lib/paranamer-2.3.jar:/usr/lib/hadoop/lib/commons-digester-1.8.jar:/usr/lib/hadoop/lib/commons-codec-1.4.jar:/usr/lib/hadoop/lib/servlet-api-2.5.jar:/usr/lib/hadoop/lib/commons-lang-2.6.jar:/usr/lib/hadoop/lib/netty-3.6.2.Final.jar:/usr/lib/hadoop/lib/jettison-1.1.jar:/usr/lib/hadoop/lib/commons-cli-1.2.jar:/usr/lib/hadoop/lib/commons-collections-3.2.1.jar:/usr/lib/hadoop/lib/slf4j-api-1.7.5.jar:/usr/lib/hadoop/lib/apacheds-kerberos-codec-2.0.0-M15.jar:/usr/lib/hadoop/lib/jasper-runtime-5.5.23.jar:/usr/lib/hadoop/lib/jersey-server-1.9.jar:/usr/lib/hadoop/lib/api-util-1.0.0-M20.jar:/usr/lib/hadoop/lib/curator-recipes-2.7.1.jar:/usr/lib/hadoop/lib/activation-1.1.jar:/usr/lib/hadoop/lib/jackson-core-asl-1.8.8.jar:/usr/lib/hadoop/lib/jetty-6.1.26.cloudera.4.jar:/usr/lib/hadoop/lib/logredactor-1.0.3.jar:/usr/lib/hadoop/lib/commons-beanutils-core-1.8.0.jar:/usr/lib/hadoop/lib/jaxb-api-2.2.2.jar:/usr/lib/hadoop/lib/commons-math3-3.1.1.jar:/usr/lib/hadoop/lib/log4j-1.2.17.jar:/usr/lib/hadoop/lib/jets3t-0.9.0.jar:/usr/lib/hadoop/lib/protobuf-java-2.5.0.jar:/usr/lib/hadoop/lib/commons-beanutils-1.7.0.jar:/usr/lib/hadoop/lib/commons-httpclient-3.1.jar:/usr/lib/hadoop/lib/jackson-xc-1.8.8.jar:/usr/lib/hadoop/lib/commons-logging-1.1.3.jar:/usr/lib/hadoop/lib/jsp-api-2.1.jar:/usr/lib/hadoop/lib/httpclient-4.2.5.jar:/usr/lib/hadoop/lib/httpcore-4.2.5.jar:/usr/lib/hadoop/lib/gson-2.2.4.jar:/usr/lib/hadoop/lib/junit-4.11.jar:/usr/lib/hadoop/lib/jetty-util-6.1.26.cloudera.4.jar:/usr/lib/hadoop/.//hadoop-common-tests.jar:/usr/lib/hadoop/.//hadoop-aws.jar:/usr/lib/hadoop/.//parquet-generator.jar:/usr/lib/hadoop/.//parquet-encoding.jar:/usr/lib/hadoop/.//hadoop-common-2.6.0-cdh5.4.5-tests.jar:/usr/lib/hadoop/.//parquet-thrift.jar:/usr/lib/hadoop/.//parquet-pig-bundle.jar:/usr/lib/hadoop/.//parquet-format-javadoc.jar:/usr/lib/hadoop/.//parquet-format.jar:/usr/lib/hadoop/.//parquet-column.jar:/usr/lib/hadoop/.//parquet-format-sources.jar:/usr/lib/hadoop/.//parquet-pig.jar:/usr/lib/hadoop/.//parquet-avro.jar:/usr/lib/hadoop/.//parquet-hadoop-bundle.jar:/usr/lib/hadoop/.//parquet-common.jar:/usr/lib/hadoop/.//hadoop-annotations-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop/.//hadoop-auth-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop/.//hadoop-common.jar:/usr/lib/hadoop/.//hadoop-aws-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop/.//hadoop-nfs.jar:/usr/lib/hadoop/.//parquet-jackson.jar:/usr/lib/hadoop/.//parquet-hadoop.jar:/usr/lib/hadoop/.//parquet-cascading.jar:/usr/lib/hadoop/.//parquet-scrooge_2.10.jar:/usr/lib/hadoop/.//hadoop-auth.jar:/usr/lib/hadoop/.//hadoop-nfs-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop/.//hadoop-common-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop/.//parquet-test-hadoop2.jar:/usr/lib/hadoop/.//parquet-protobuf.jar:/usr/lib/hadoop/.//parquet-scala_2.10.jar:/usr/lib/hadoop/.//hadoop-annotations.jar:/usr/lib/hadoop/.//parquet-tools.jar:/usr/lib/hadoop-hdfs/./:/usr/lib/hadoop-hdfs/lib/asm-3.2.jar:/usr/lib/hadoop-hdfs/lib/jersey-core-1.9.jar:/usr/lib/hadoop-hdfs/lib/guava-11.0.2.jar:/usr/lib/hadoop-hdfs/lib/jackson-mapper-asl-1.8.8.jar:/usr/lib/hadoop-hdfs/lib/xmlenc-0.52.jar:/usr/lib/hadoop-hdfs/lib/htrace-core-3.0.4.jar:/usr/lib/hadoop-hdfs/lib/jsr305-3.0.0.jar:/usr/lib/hadoop-hdfs/lib/commons-el-1.0.jar:/usr/lib/hadoop-hdfs/lib/commons-io-2.4.jar:/usr/lib/hadoop-hdfs/lib/commons-codec-1.4.jar:/usr/lib/hadoop-hdfs/lib/servlet-api-2.5.jar:/usr/lib/hadoop-hdfs/lib/commons-lang-2.6.jar:/usr/lib/hadoop-hdfs/lib/netty-3.6.2.Final.jar:/usr/lib/hadoop-hdfs/lib/commons-cli-1.2.jar:/usr/lib/hadoop-hdfs/lib/jasper-runtime-5.5.23.jar:/usr/lib/hadoop-hdfs/lib/jersey-server-1.9.jar:/usr/lib/hadoop-hdfs/lib/jackson-core-asl-1.8.8.jar:/usr/lib/hadoop-hdfs/lib/jetty-6.1.26.cloudera.4.jar:/usr/lib/hadoop-hdfs/lib/log4j-1.2.17.jar:/usr/lib/hadoop-hdfs/lib/protobuf-java-2.5.0.jar:/usr/lib/hadoop-hdfs/lib/commons-daemon-1.0.13.jar:/usr/lib/hadoop-hdfs/lib/commons-logging-1.1.3.jar:/usr/lib/hadoop-hdfs/lib/jsp-api-2.1.jar:/usr/lib/hadoop-hdfs/lib/leveldbjni-all-1.8.jar:/usr/lib/hadoop-hdfs/lib/jetty-util-6.1.26.cloudera.4.jar:/usr/lib/hadoop-hdfs/.//hadoop-hdfs.jar:/usr/lib/hadoop-hdfs/.//hadoop-hdfs-nfs-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-hdfs/.//hadoop-hdfs-tests.jar:/usr/lib/hadoop-hdfs/.//hadoop-hdfs-2.6.0-cdh5.4.5-tests.jar:/usr/lib/hadoop-hdfs/.//hadoop-hdfs-nfs.jar:/usr/lib/hadoop-hdfs/.//hadoop-hdfs-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-yarn/lib/asm-3.2.jar:/usr/lib/hadoop-yarn/lib/jersey-core-1.9.jar:/usr/lib/hadoop-yarn/lib/jersey-json-1.9.jar:/usr/lib/hadoop-yarn/lib/guava-11.0.2.jar:/usr/lib/hadoop-yarn/lib/xz-1.0.jar:/usr/lib/hadoop-yarn/lib/jaxb-impl-2.2.3-1.jar:/usr/lib/hadoop-yarn/lib/jackson-mapper-asl-1.8.8.jar:/usr/lib/hadoop-yarn/lib/jersey-guice-1.9.jar:/usr/lib/hadoop-yarn/lib/commons-compress-1.4.1.jar:/usr/lib/hadoop-yarn/lib/aopalliance-1.0.jar:/usr/lib/hadoop-yarn/lib/jsr305-3.0.0.jar:/usr/lib/hadoop-yarn/lib/javax.inject-1.jar:/usr/lib/hadoop-yarn/lib/jersey-client-1.9.jar:/usr/lib/hadoop-yarn/lib/stax-api-1.0-2.jar:/usr/lib/hadoop-yarn/lib/zookeeper.jar:/usr/lib/hadoop-yarn/lib/guice-servlet-3.0.jar:/usr/lib/hadoop-yarn/lib/jackson-jaxrs-1.8.8.jar:/usr/lib/hadoop-yarn/lib/commons-io-2.4.jar:/usr/lib/hadoop-yarn/lib/commons-codec-1.4.jar:/usr/lib/hadoop-yarn/lib/jline-2.11.jar:/usr/lib/hadoop-yarn/lib/servlet-api-2.5.jar:/usr/lib/hadoop-yarn/lib/commons-lang-2.6.jar:/usr/lib/hadoop-yarn/lib/jettison-1.1.jar:/usr/lib/hadoop-yarn/lib/guice-3.0.jar:/usr/lib/hadoop-yarn/lib/commons-cli-1.2.jar:/usr/lib/hadoop-yarn/lib/commons-collections-3.2.1.jar:/usr/lib/hadoop-yarn/lib/jersey-server-1.9.jar:/usr/lib/hadoop-yarn/lib/activation-1.1.jar:/usr/lib/hadoop-yarn/lib/jackson-core-asl-1.8.8.jar:/usr/lib/hadoop-yarn/lib/jetty-6.1.26.cloudera.4.jar:/usr/lib/hadoop-yarn/lib/jaxb-api-2.2.2.jar:/usr/lib/hadoop-yarn/lib/log4j-1.2.17.jar:/usr/lib/hadoop-yarn/lib/protobuf-java-2.5.0.jar:/usr/lib/hadoop-yarn/lib/commons-httpclient-3.1.jar:/usr/lib/hadoop-yarn/lib/jackson-xc-1.8.8.jar:/usr/lib/hadoop-yarn/lib/commons-logging-1.1.3.jar:/usr/lib/hadoop-yarn/lib/leveldbjni-all-1.8.jar:/usr/lib/hadoop-yarn/lib/jetty-util-6.1.26.cloudera.4.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-common-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-server-common.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-applications-distributedshell.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-server-tests-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-server-tests.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-applications-distributedshell-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-api.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-common.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-server-nodemanager.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-server-applicationhistoryservice.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-applications-unmanaged-am-launcher.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-client-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-server-resourcemanager.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-server-nodemanager-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-server-resourcemanager-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-server-web-proxy-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-registry.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-server-web-proxy.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-server-common-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-client.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-server-applicationhistoryservice-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-registry-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-api-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-applications-unmanaged-am-launcher-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/lib/asm-3.2.jar:/usr/lib/hadoop-mapreduce/lib/jersey-core-1.9.jar:/usr/lib/hadoop-mapreduce/lib/xz-1.0.jar:/usr/lib/hadoop-mapreduce/lib/jackson-mapper-asl-1.8.8.jar:/usr/lib/hadoop-mapreduce/lib/jersey-guice-1.9.jar:/usr/lib/hadoop-mapreduce/lib/commons-compress-1.4.1.jar:/usr/lib/hadoop-mapreduce/lib/aopalliance-1.0.jar:/usr/lib/hadoop-mapreduce/lib/hamcrest-core-1.3.jar:/usr/lib/hadoop-mapreduce/lib/avro.jar:/usr/lib/hadoop-mapreduce/lib/javax.inject-1.jar:/usr/lib/hadoop-mapreduce/lib/snappy-java-1.0.4.1.jar:/usr/lib/hadoop-mapreduce/lib/guice-servlet-3.0.jar:/usr/lib/hadoop-mapreduce/lib/commons-io-2.4.jar:/usr/lib/hadoop-mapreduce/lib/paranamer-2.3.jar:/usr/lib/hadoop-mapreduce/lib/netty-3.6.2.Final.jar:/usr/lib/hadoop-mapreduce/lib/guice-3.0.jar:/usr/lib/hadoop-mapreduce/lib/jersey-server-1.9.jar:/usr/lib/hadoop-mapreduce/lib/jackson-core-asl-1.8.8.jar:/usr/lib/hadoop-mapreduce/lib/log4j-1.2.17.jar:/usr/lib/hadoop-mapreduce/lib/protobuf-java-2.5.0.jar:/usr/lib/hadoop-mapreduce/lib/junit-4.11.jar:/usr/lib/hadoop-mapreduce/lib/leveldbjni-all-1.8.jar:/usr/lib/hadoop-mapreduce/.//apacheds-i18n-2.0.0-M15.jar:/usr/lib/hadoop-mapreduce/.//asm-3.2.jar:/usr/lib/hadoop-mapreduce/.//jersey-core-1.9.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-examples.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-common.jar:/usr/lib/hadoop-mapreduce/.//hadoop-ant.jar:/usr/lib/hadoop-mapreduce/.//mockito-all-1.8.5.jar:/usr/lib/hadoop-mapreduce/.//api-asn1-api-1.0.0-M20.jar:/usr/lib/hadoop-mapreduce/.//hadoop-rumen.jar:/usr/lib/hadoop-mapreduce/.//hadoop-azure-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-sls-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//curator-framework-2.7.1.jar:/usr/lib/hadoop-mapreduce/.//jersey-json-1.9.jar:/usr/lib/hadoop-mapreduce/.//microsoft-windowsazure-storage-sdk-0.6.0.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-nativetask.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-shuffle-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//jackson-databind-2.2.3.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-shuffle.jar:/usr/lib/hadoop-mapreduce/.//java-xmlbuilder-0.4.jar:/usr/lib/hadoop-mapreduce/.//guava-11.0.2.jar:/usr/lib/hadoop-mapreduce/.//xz-1.0.jar:/usr/lib/hadoop-mapreduce/.//jaxb-impl-2.2.3-1.jar:/usr/lib/hadoop-mapreduce/.//jackson-mapper-asl-1.8.8.jar:/usr/lib/hadoop-mapreduce/.//commons-configuration-1.6.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-core-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-hs.jar:/usr/lib/hadoop-mapreduce/.//hadoop-sls.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-hs-plugins.jar:/usr/lib/hadoop-mapreduce/.//curator-client-2.7.1.jar:/usr/lib/hadoop-mapreduce/.//hadoop-extras-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-examples-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//xmlenc-0.52.jar:/usr/lib/hadoop-mapreduce/.//commons-compress-1.4.1.jar:/usr/lib/hadoop-mapreduce/.//hadoop-gridmix.jar:/usr/lib/hadoop-mapreduce/.//hadoop-gridmix-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hamcrest-core-1.3.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-common-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//htrace-core-3.0.4.jar:/usr/lib/hadoop-mapreduce/.//jasper-compiler-5.5.23.jar:/usr/lib/hadoop-mapreduce/.//avro.jar:/usr/lib/hadoop-mapreduce/.//jsr305-3.0.0.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-nativetask-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-jobclient-2.6.0-cdh5.4.5-tests.jar:/usr/lib/hadoop-mapreduce/.//hadoop-distcp.jar:/usr/lib/hadoop-mapreduce/.//commons-el-1.0.jar:/usr/lib/hadoop-mapreduce/.//stax-api-1.0-2.jar:/usr/lib/hadoop-mapreduce/.//jsch-0.1.42.jar:/usr/lib/hadoop-mapreduce/.//commons-net-3.1.jar:/usr/lib/hadoop-mapreduce/.//snappy-java-1.0.4.1.jar:/usr/lib/hadoop-mapreduce/.//hadoop-azure.jar:/usr/lib/hadoop-mapreduce/.//zookeeper.jar:/usr/lib/hadoop-mapreduce/.//hadoop-auth-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-jobclient-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-app.jar:/usr/lib/hadoop-mapreduce/.//jackson-jaxrs-1.8.8.jar:/usr/lib/hadoop-mapreduce/.//commons-io-2.4.jar:/usr/lib/hadoop-mapreduce/.//paranamer-2.3.jar:/usr/lib/hadoop-mapreduce/.//hadoop-extras.jar:/usr/lib/hadoop-mapreduce/.//commons-digester-1.8.jar:/usr/lib/hadoop-mapreduce/.//hadoop-streaming.jar:/usr/lib/hadoop-mapreduce/.//commons-codec-1.4.jar:/usr/lib/hadoop-mapreduce/.//hadoop-archives.jar:/usr/lib/hadoop-mapreduce/.//servlet-api-2.5.jar:/usr/lib/hadoop-mapreduce/.//commons-lang-2.6.jar:/usr/lib/hadoop-mapreduce/.//jackson-annotations-2.2.3.jar:/usr/lib/hadoop-mapreduce/.//jettison-1.1.jar:/usr/lib/hadoop-mapreduce/.//commons-cli-1.2.jar:/usr/lib/hadoop-mapreduce/.//commons-collections-3.2.1.jar:/usr/lib/hadoop-mapreduce/.//apacheds-kerberos-codec-2.0.0-M15.jar:/usr/lib/hadoop-mapreduce/.//hadoop-datajoin.jar:/usr/lib/hadoop-mapreduce/.//hadoop-datajoin-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//jasper-runtime-5.5.23.jar:/usr/lib/hadoop-mapreduce/.//jersey-server-1.9.jar:/usr/lib/hadoop-mapreduce/.//api-util-1.0.0-M20.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-app-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-streaming-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//curator-recipes-2.7.1.jar:/usr/lib/hadoop-mapreduce/.//metrics-core-3.0.1.jar:/usr/lib/hadoop-mapreduce/.//activation-1.1.jar:/usr/lib/hadoop-mapreduce/.//jackson-core-asl-1.8.8.jar:/usr/lib/hadoop-mapreduce/.//jetty-6.1.26.cloudera.4.jar:/usr/lib/hadoop-mapreduce/.//commons-beanutils-core-1.8.0.jar:/usr/lib/hadoop-mapreduce/.//jaxb-api-2.2.2.jar:/usr/lib/hadoop-mapreduce/.//commons-math3-3.1.1.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-jobclient.jar:/usr/lib/hadoop-mapreduce/.//hadoop-ant-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//log4j-1.2.17.jar:/usr/lib/hadoop-mapreduce/.//jets3t-0.9.0.jar:/usr/lib/hadoop-mapreduce/.//hadoop-archives-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//protobuf-java-2.5.0.jar:/usr/lib/hadoop-mapreduce/.//commons-beanutils-1.7.0.jar:/usr/lib/hadoop-mapreduce/.//commons-httpclient-3.1.jar:/usr/lib/hadoop-mapreduce/.//hadoop-auth.jar:/usr/lib/hadoop-mapreduce/.//jackson-xc-1.8.8.jar:/usr/lib/hadoop-mapreduce/.//hadoop-distcp-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//commons-logging-1.1.3.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-jobclient-tests.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-core.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-hs-plugins-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//jsp-api-2.1.jar:/usr/lib/hadoop-mapreduce/.//httpclient-4.2.5.jar:/usr/lib/hadoop-mapreduce/.//jackson-core-2.2.3.jar:/usr/lib/hadoop-mapreduce/.//httpcore-4.2.5.jar:/usr/lib/hadoop-mapreduce/.//gson-2.2.4.jar:/usr/lib/hadoop-mapreduce/.//hadoop-rumen-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-hs-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//junit-4.11.jar:/usr/lib/hadoop-mapreduce/.//jetty-util-6.1.26.cloudera.4.jar:/usr/lib/hadoop-mapreduce/.//activation-1.1.jar:/usr/lib/hadoop-mapreduce/.//apacheds-i18n-2.0.0-M15.jar:/usr/lib/hadoop-mapreduce/.//apacheds-kerberos-codec-2.0.0-M15.jar:/usr/lib/hadoop-mapreduce/.//api-asn1-api-1.0.0-M20.jar:/usr/lib/hadoop-mapreduce/.//api-util-1.0.0-M20.jar:/usr/lib/hadoop-mapreduce/.//asm-3.2.jar:/usr/lib/hadoop-mapreduce/.//avro.jar:/usr/lib/hadoop-mapreduce/.//commons-beanutils-1.7.0.jar:/usr/lib/hadoop-mapreduce/.//commons-beanutils-core-1.8.0.jar:/usr/lib/hadoop-mapreduce/.//commons-cli-1.2.jar:/usr/lib/hadoop-mapreduce/.//commons-codec-1.4.jar:/usr/lib/hadoop-mapreduce/.//commons-collections-3.2.1.jar:/usr/lib/hadoop-mapreduce/.//commons-compress-1.4.1.jar:/usr/lib/hadoop-mapreduce/.//commons-configuration-1.6.jar:/usr/lib/hadoop-mapreduce/.//commons-digester-1.8.jar:/usr/lib/hadoop-mapreduce/.//commons-el-1.0.jar:/usr/lib/hadoop-mapreduce/.//commons-httpclient-3.1.jar:/usr/lib/hadoop-mapreduce/.//commons-io-2.4.jar:/usr/lib/hadoop-mapreduce/.//commons-lang-2.6.jar:/usr/lib/hadoop-mapreduce/.//commons-logging-1.1.3.jar:/usr/lib/hadoop-mapreduce/.//commons-math3-3.1.1.jar:/usr/lib/hadoop-mapreduce/.//commons-net-3.1.jar:/usr/lib/hadoop-mapreduce/.//curator-client-2.7.1.jar:/usr/lib/hadoop-mapreduce/.//curator-framework-2.7.1.jar:/usr/lib/hadoop-mapreduce/.//curator-recipes-2.7.1.jar:/usr/lib/hadoop-mapreduce/.//gson-2.2.4.jar:/usr/lib/hadoop-mapreduce/.//guava-11.0.2.jar:/usr/lib/hadoop-mapreduce/.//hadoop-ant-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-ant.jar:/usr/lib/hadoop-mapreduce/.//hadoop-archives-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-archives.jar:/usr/lib/hadoop-mapreduce/.//hadoop-auth-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-auth.jar:/usr/lib/hadoop-mapreduce/.//hadoop-azure-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-azure.jar:/usr/lib/hadoop-mapreduce/.//hadoop-datajoin-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-datajoin.jar:/usr/lib/hadoop-mapreduce/.//hadoop-distcp-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-distcp.jar:/usr/lib/hadoop-mapreduce/.//hadoop-extras-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-extras.jar:/usr/lib/hadoop-mapreduce/.//hadoop-gridmix-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-gridmix.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-app-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-app.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-common-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-common.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-core-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-core.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-hs-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-hs-plugins-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-hs-plugins.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-hs.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-jobclient-2.6.0-cdh5.4.5-tests.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-jobclient-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-jobclient-tests.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-jobclient.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-nativetask-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-nativetask.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-shuffle-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-client-shuffle.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-examples-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-mapreduce-examples.jar:/usr/lib/hadoop-mapreduce/.//hadoop-rumen-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-rumen.jar:/usr/lib/hadoop-mapreduce/.//hadoop-sls-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-sls.jar:/usr/lib/hadoop-mapreduce/.//hadoop-streaming-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-mapreduce/.//hadoop-streaming.jar:/usr/lib/hadoop-mapreduce/.//hamcrest-core-1.3.jar:/usr/lib/hadoop-mapreduce/.//htrace-core-3.0.4.jar:/usr/lib/hadoop-mapreduce/.//httpclient-4.2.5.jar:/usr/lib/hadoop-mapreduce/.//httpcore-4.2.5.jar:/usr/lib/hadoop-mapreduce/.//jackson-annotations-2.2.3.jar:/usr/lib/hadoop-mapreduce/.//jackson-core-2.2.3.jar:/usr/lib/hadoop-mapreduce/.//jackson-core-asl-1.8.8.jar:/usr/lib/hadoop-mapreduce/.//jackson-databind-2.2.3.jar:/usr/lib/hadoop-mapreduce/.//jackson-jaxrs-1.8.8.jar:/usr/lib/hadoop-mapreduce/.//jackson-mapper-asl-1.8.8.jar:/usr/lib/hadoop-mapreduce/.//jackson-xc-1.8.8.jar:/usr/lib/hadoop-mapreduce/.//jasper-compiler-5.5.23.jar:/usr/lib/hadoop-mapreduce/.//jasper-runtime-5.5.23.jar:/usr/lib/hadoop-mapreduce/.//java-xmlbuilder-0.4.jar:/usr/lib/hadoop-mapreduce/.//jaxb-api-2.2.2.jar:/usr/lib/hadoop-mapreduce/.//jaxb-impl-2.2.3-1.jar:/usr/lib/hadoop-mapreduce/.//jersey-core-1.9.jar:/usr/lib/hadoop-mapreduce/.//jersey-json-1.9.jar:/usr/lib/hadoop-mapreduce/.//jersey-server-1.9.jar:/usr/lib/hadoop-mapreduce/.//jets3t-0.9.0.jar:/usr/lib/hadoop-mapreduce/.//jettison-1.1.jar:/usr/lib/hadoop-mapreduce/.//jetty-6.1.26.cloudera.4.jar:/usr/lib/hadoop-mapreduce/.//jetty-util-6.1.26.cloudera.4.jar:/usr/lib/hadoop-mapreduce/.//jsch-0.1.42.jar:/usr/lib/hadoop-mapreduce/.//jsp-api-2.1.jar:/usr/lib/hadoop-mapreduce/.//jsr305-3.0.0.jar:/usr/lib/hadoop-mapreduce/.//junit-4.11.jar:/usr/lib/hadoop-mapreduce/.//log4j-1.2.17.jar:/usr/lib/hadoop-mapreduce/.//metrics-core-3.0.1.jar:/usr/lib/hadoop-mapreduce/.//microsoft-windowsazure-storage-sdk-0.6.0.jar:/usr/lib/hadoop-mapreduce/.//mockito-all-1.8.5.jar:/usr/lib/hadoop-mapreduce/.//paranamer-2.3.jar:/usr/lib/hadoop-mapreduce/.//protobuf-java-2.5.0.jar:/usr/lib/hadoop-mapreduce/.//servlet-api-2.5.jar:/usr/lib/hadoop-mapreduce/.//snappy-java-1.0.4.1.jar:/usr/lib/hadoop-mapreduce/.//stax-api-1.0-2.jar:/usr/lib/hadoop-mapreduce/.//xmlenc-0.52.jar:/usr/lib/hadoop-mapreduce/.//xz-1.0.jar:/usr/lib/hadoop-mapreduce/.//zookeeper.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-api-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-api.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-applications-distributedshell-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-applications-distributedshell.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-applications-unmanaged-am-launcher-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-applications-unmanaged-am-launcher.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-client-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-client.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-common-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-common.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-registry-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-registry.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-server-applicationhistoryservice-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-server-applicationhistoryservice.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-server-common-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-server-common.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-server-nodemanager-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-server-nodemanager.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-server-resourcemanager-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-server-resourcemanager.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-server-tests-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-server-tests.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-server-web-proxy-2.6.0-cdh5.4.5.jar:/usr/lib/hadoop-yarn/.//hadoop-yarn-server-web-proxy.jar:/usr/lib/hadoop-mapreduce/lib/aopalliance-1.0.jar:/usr/lib/hadoop-mapreduce/lib/asm-3.2.jar:/usr/lib/hadoop-mapreduce/lib/avro.jar:/usr/lib/hadoop-mapreduce/lib/commons-compress-1.4.1.jar:/usr/lib/hadoop-mapreduce/lib/commons-io-2.4.jar:/usr/lib/hadoop-mapreduce/lib/guice-3.0.jar:/usr/lib/hadoop-mapreduce/lib/guice-servlet-3.0.jar:/usr/lib/hadoop-mapreduce/lib/hamcrest-core-1.3.jar:/usr/lib/hadoop-mapreduce/lib/jackson-core-asl-1.8.8.jar:/usr/lib/hadoop-mapreduce/lib/jackson-mapper-asl-1.8.8.jar:/usr/lib/hadoop-mapreduce/lib/javax.inject-1.jar:/usr/lib/hadoop-mapreduce/lib/jersey-core-1.9.jar:/usr/lib/hadoop-mapreduce/lib/jersey-guice-1.9.jar:/usr/lib/hadoop-mapreduce/lib/jersey-server-1.9.jar:/usr/lib/hadoop-mapreduce/lib/junit-4.11.jar:/usr/lib/hadoop-mapreduce/lib/leveldbjni-all-1.8.jar:/usr/lib/hadoop-mapreduce/lib/log4j-1.2.17.jar:/usr/lib/hadoop-mapreduce/lib/netty-3.6.2.Final.jar:/usr/lib/hadoop-mapreduce/lib/paranamer-2.3.jar:/usr/lib/hadoop-mapreduce/lib/protobuf-java-2.5.0.jar:/usr/lib/hadoop-mapreduce/lib/snappy-java-1.0.4.1.jar:/usr/lib/hadoop-mapreduce/lib/xz-1.0.jar:/usr/lib/hadoop-mapreduce/modules/*.jar
STARTUP_MSG:   build = http://github.com/cloudera/hadoop -r ab14c89fe25e9fb3f9de4fb852c21365b7c5608b; compiled by 'jenkins' on 2015-08-12T21:12Z
STARTUP_MSG:   java = 1.7.0_79
************************************************************/
Started Hadoop historyserver:                              [  OK  ]
[root@ip-172-31-57-217 ~]# /data/start_postgres.sh
could not change directory to "/root"
server starting
[root@ip-172-31-57-217 ~]# ls
dans_bash_history.txt                    setup_ucb_complete_plus_postgres.sh
dead.letter                              start-hadoop.sh
EX2Tweetwordcount                        start-hadoop.sh~
ez_setup.py                              stop-hadoop.sh
ipython                                  stop-hadoop.sh~
pgxl-deployment-tools                    streamparse
rstudio-server-rhel-0.99.892-x86_64.rpm  w205-spring-16-labs-exercises
setuptools-20.3.1.zip
[root@ip-172-31-57-217 ~]# cd EX2Tweetwordcount
[root@ip-172-31-57-217 EX2Tweetwordcount]# ls
config.json              project.clj        tasks.py                virtualenvs
create_db.py             psycopg-sample.py  topologies
fabfile.py               README.md          Twittercredentials.py
hello-stream-twitter.py  src                Twittercredentials.pyc
[root@ip-172-31-57-217 EX2Tweetwordcount]# vi Twittercredentials.py
[root@ip-172-31-57-217 EX2Tweetwordcount]# python create_db.py
Traceback (most recent call last):
  File "create_db.py", line 8, in <module>
    cur.execute('CREATE DATABASE ' + "TCount")
psycopg2.InternalError: CREATE DATABASE cannot run inside a transaction block

[root@ip-172-31-57-217 EX2Tweetwordcount]# vi create_db.py
[root@ip-172-31-57-217 EX2Tweetwordcount]# mv create_db.py create_table.py
[root@ip-172-31-57-217 EX2Tweetwordcount]# python create_table.py
[root@ip-172-31-57-217 EX2Tweetwordcount]# ls
config.json              project.clj        tasks.py                virtualenvs
create_table.py          psycopg-sample.py  topologies
fabfile.py               README.md          Twittercredentials.py
hello-stream-twitter.py  src                Twittercredentials.pyc
[root@ip-172-31-57-217 EX2Tweetwordcount]# vi create_table.py
[root@ip-172-31-57-217 EX2Tweetwordcount]# cd src/bolts
[root@ip-172-31-57-217 bolts]# ls
__init__.py  parse.py  wordcount.py
[root@ip-172-31-57-217 bolts]# vi parse.py
[root@ip-172-31-57-217 bolts]# vi wordcount.py
[root@ip-172-31-57-217 bolts]# vi parse.py
[root@ip-172-31-57-217 bolts]# vi wordcount.py
[root@ip-172-31-57-217 bolts]# cd ..
[root@ip-172-31-57-217 src]# cd ..
[root@ip-172-31-57-217 EX2Tweetwordcount]# cd src/bolts
[root@ip-172-31-57-217 bolts]# vi wordcount.py
[root@ip-172-31-57-217 bolts]# cd ..
[root@ip-172-31-57-217 src]# cd ..
[root@ip-172-31-57-217 EX2Tweetwordcount]# sparse run
Running tweetwordcount topology...
Routing Python logging to /root/EX2Tweetwordcount/logs.
Running lein command to run local cluster:
lein run -m streamparse.commands.run/-main topologies/tweetwordcount.clj -t 0 --option 'topology.workers=2' --option 'topology.acker.executors=2' --option 'streamparse.log.path="/root/EX2Tweetwordcount/logs"' --option 'streamparse.log.level="debug"'
WARNING: You're currently running as root; probably by accident.
Press control-C to abort or Enter to continue as root.
Set LEIN_ROOT to disable this warning.

Retrieving org/apache/storm/storm-core/0.9.5/storm-core-0.9.5.pom from central
Retrieving org/apache/storm/storm/0.9.5/storm-0.9.5.pom from central
Retrieving org/apache/apache/10/apache-10.pom from central
Retrieving org/clojure/clojure/1.5.1/clojure-1.5.1.pom from central
Retrieving org/sonatype/oss/oss-parent/5/oss-parent-5.pom from central
Retrieving clj-time/clj-time/0.4.1/clj-time-0.4.1.pom from clojars
Retrieving joda-time/joda-time/2.0/joda-time-2.0.pom from central
Retrieving org/clojure/clojure/1.3.0/clojure-1.3.0.pom from central
Retrieving compojure/compojure/1.1.3/compojure-1.1.3.pom from clojars
Retrieving org/clojure/clojure/1.2.1/clojure-1.2.1.pom from central
Retrieving org/clojure/core.incubator/0.1.0/core.incubator-0.1.0.pom from central
Retrieving org/clojure/pom.contrib/0.0.20/pom.contrib-0.0.20.pom from central
Retrieving org/clojure/clojure/1.3.0-alpha5/clojure-1.3.0-alpha5.pom from central
Retrieving org/clojure/tools.macro/0.1.0/tools.macro-0.1.0.pom from central
Retrieving clout/clout/1.0.1/clout-1.0.1.pom from clojars
Retrieving ring/ring-core/1.1.5/ring-core-1.1.5.pom from clojars
Retrieving commons-codec/commons-codec/1.6/commons-codec-1.6.pom from central
Retrieving org/apache/commons/commons-parent/22/commons-parent-22.pom from central
Retrieving org/apache/apache/9/apache-9.pom from central
Retrieving commons-io/commons-io/2.1/commons-io-2.1.pom from central
Retrieving commons-fileupload/commons-fileupload/1.2.1/commons-fileupload-1.2.1.pom from central
Retrieving org/apache/commons/commons-parent/7/commons-parent-7.pom from central
Retrieving org/apache/apache/4/apache-4.pom from central
Retrieving javax/servlet/servlet-api/2.5/servlet-api-2.5.pom from central
Retrieving clj-time/clj-time/0.3.7/clj-time-0.3.7.pom from clojars
Retrieving hiccup/hiccup/0.3.6/hiccup-0.3.6.pom from clojars
Retrieving org/clojure/clojure/1.2.0/clojure-1.2.0.pom from central
Retrieving ring/ring-devel/0.3.11/ring-devel-0.3.11.pom from clojars
Retrieving ring/ring-core/0.3.11/ring-core-0.3.11.pom from clojars
Retrieving commons-codec/commons-codec/1.4/commons-codec-1.4.pom from central
Retrieving org/apache/commons/commons-parent/11/commons-parent-11.pom from central
Retrieving commons-io/commons-io/1.4/commons-io-1.4.pom from central
Retrieving clj-stacktrace/clj-stacktrace/0.2.2/clj-stacktrace-0.2.2.pom from clojars
Retrieving ring/ring-jetty-adapter/0.3.11/ring-jetty-adapter-0.3.11.pom from clojars
Retrieving ring/ring-servlet/0.3.11/ring-servlet-0.3.11.pom from clojars
Retrieving org/mortbay/jetty/jetty/6.1.26/jetty-6.1.26.pom from central
Retrieving org/mortbay/jetty/project/6.1.26/project-6.1.26.pom from central
Retrieving org/mortbay/jetty/jetty-parent/10/jetty-parent-10.pom from central
Retrieving org/eclipse/jetty/jetty-parent/14/jetty-parent-14.pom from central
Retrieving org/mortbay/jetty/jetty-util/6.1.26/jetty-util-6.1.26.pom from central
Retrieving org/mortbay/jetty/servlet-api/2.5-20081211/servlet-api-2.5-20081211.pom from central
Retrieving org/mortbay/jetty/jetty-parent/7/jetty-parent-7.pom from central
Retrieving org/clojure/tools.logging/0.2.3/tools.logging-0.2.3.pom from central
Retrieving org/clojure/pom.contrib/0.0.23/pom.contrib-0.0.23.pom from central
Retrieving org/clojure/clojure/1.3.0-beta1/clojure-1.3.0-beta1.pom from central
Retrieving org/clojure/math.numeric-tower/0.0.1/math.numeric-tower-0.0.1.pom from central
Retrieving org/clojure/pom.contrib/0.0.25/pom.contrib-0.0.25.pom from central
Retrieving org/clojure/tools.cli/0.2.4/tools.cli-0.2.4.pom from central
Retrieving org/clojure/pom.contrib/0.1.2/pom.contrib-0.1.2.pom from central
Retrieving org/sonatype/oss/oss-parent/7/oss-parent-7.pom from central
Retrieving org/clojure/clojure/1.4.0/clojure-1.4.0.pom from central
Retrieving commons-io/commons-io/2.4/commons-io-2.4.pom from central
Retrieving org/apache/commons/commons-parent/25/commons-parent-25.pom from central
Retrieving org/apache/commons/commons-exec/1.1/commons-exec-1.1.pom from central
Retrieving org/apache/commons/commons-parent/17/commons-parent-17.pom from central
Retrieving org/apache/apache/7/apache-7.pom from central
Retrieving commons-lang/commons-lang/2.5/commons-lang-2.5.pom from central
Retrieving org/apache/commons/commons-parent/12/commons-parent-12.pom from central
Retrieving com/googlecode/json-simple/json-simple/1.1/json-simple-1.1.pom from central
Retrieving com/twitter/carbonite/1.4.0/carbonite-1.4.0.pom from clojars
Retrieving com/esotericsoftware/kryo/kryo/2.21/kryo-2.21.pom from central
Retrieving com/esotericsoftware/reflectasm/reflectasm/1.07/reflectasm-1.07.pom from central
Retrieving org/ow2/asm/asm/4.0/asm-4.0.pom from central
Retrieving org/ow2/asm/asm-parent/4.0/asm-parent-4.0.pom from central
Retrieving org/ow2/ow2/1.3/ow2-1.3.pom from central
Retrieving com/esotericsoftware/minlog/minlog/1.2/minlog-1.2.pom from central
Retrieving org/objenesis/objenesis/1.2/objenesis-1.2.pom from central
Retrieving org/objenesis/objenesis-parent/1.2/objenesis-parent-1.2.pom from central
Retrieving com/twitter/chill-java/0.3.5/chill-java-0.3.5.pom from central
Retrieving org/yaml/snakeyaml/1.11/snakeyaml-1.11.pom from central
Retrieving commons-logging/commons-logging/1.1.3/commons-logging-1.1.3.pom from central
Retrieving org/apache/commons/commons-parent/28/commons-parent-28.pom from central
Retrieving org/apache/apache/13/apache-13.pom from central
Retrieving com/googlecode/disruptor/disruptor/2.10.1/disruptor-2.10.1.pom from central
Retrieving org/jgrapht/jgrapht-core/0.9.0/jgrapht-core-0.9.0.pom from central
Retrieving org/jgrapht/jgrapht/0.9.0/jgrapht-0.9.0.pom from central
Retrieving ch/qos/logback/logback-classic/1.0.13/logback-classic-1.0.13.pom from central
Retrieving ch/qos/logback/logback-parent/1.0.13/logback-parent-1.0.13.pom from central
Retrieving ch/qos/logback/logback-core/1.0.13/logback-core-1.0.13.pom from central
Retrieving org/slf4j/slf4j-api/1.7.5/slf4j-api-1.7.5.pom from central
Retrieving org/slf4j/slf4j-parent/1.7.5/slf4j-parent-1.7.5.pom from central
Retrieving org/slf4j/log4j-over-slf4j/1.6.6/log4j-over-slf4j-1.6.6.pom from central
Retrieving org/slf4j/slf4j-parent/1.6.6/slf4j-parent-1.6.6.pom from central
Retrieving org/slf4j/slf4j-api/1.6.6/slf4j-api-1.6.6.pom from central
Retrieving jline/jline/2.11/jline-2.11.pom from central
Retrieving com/parsely/streamparse/0.0.4-SNAPSHOT/streamparse-0.0.4-20160314.185928-7.pom from clojars
Retrieving org/clojure/data.json/0.2.6/data.json-0.2.6.pom from central
Retrieving org/apache/storm/storm-core/0.9.4/storm-core-0.9.4.pom from central
Retrieving org/apache/storm/storm/0.9.4/storm-0.9.4.pom from central
Retrieving org/clojure/tools.nrepl/0.2.12/tools.nrepl-0.2.12.pom from central
Retrieving clojure-complete/clojure-complete/0.2.4/clojure-complete-0.2.4.pom from clojars
Retrieving org/apache/storm/storm-core/0.9.5/storm-core-0.9.5.jar from central
Retrieving org/clojure/clojure/1.5.1/clojure-1.5.1.jar from central
Retrieving joda-time/joda-time/2.0/joda-time-2.0.jar from central
Retrieving org/clojure/core.incubator/0.1.0/core.incubator-0.1.0.jar from central
Retrieving org/clojure/tools.macro/0.1.0/tools.macro-0.1.0.jar from central
Retrieving commons-fileupload/commons-fileupload/1.2.1/commons-fileupload-1.2.1.jar from central
Retrieving javax/servlet/servlet-api/2.5/servlet-api-2.5.jar from central
Retrieving org/mortbay/jetty/jetty/6.1.26/jetty-6.1.26.jar from central
Retrieving org/mortbay/jetty/jetty-util/6.1.26/jetty-util-6.1.26.jar from central
Retrieving org/clojure/tools.logging/0.2.3/tools.logging-0.2.3.jar from central
Retrieving org/clojure/math.numeric-tower/0.0.1/math.numeric-tower-0.0.1.jar from central
Retrieving org/clojure/tools.cli/0.2.4/tools.cli-0.2.4.jar from central
Retrieving commons-io/commons-io/2.4/commons-io-2.4.jar from central
Retrieving org/apache/commons/commons-exec/1.1/commons-exec-1.1.jar from central
Retrieving commons-lang/commons-lang/2.5/commons-lang-2.5.jar from central
Retrieving com/googlecode/json-simple/json-simple/1.1/json-simple-1.1.jar from central
Retrieving com/esotericsoftware/reflectasm/reflectasm/1.07/reflectasm-1.07-shaded.jar from central
Retrieving com/esotericsoftware/kryo/kryo/2.21/kryo-2.21.jar from central
Retrieving org/ow2/asm/asm/4.0/asm-4.0.jar from central
Retrieving com/esotericsoftware/minlog/minlog/1.2/minlog-1.2.jar from central
Retrieving org/objenesis/objenesis/1.2/objenesis-1.2.jar from central
Retrieving com/twitter/chill-java/0.3.5/chill-java-0.3.5.jar from central
Retrieving org/yaml/snakeyaml/1.11/snakeyaml-1.11.jar from central
Retrieving commons-logging/commons-logging/1.1.3/commons-logging-1.1.3.jar from central
Retrieving commons-codec/commons-codec/1.6/commons-codec-1.6.jar from central
Retrieving com/googlecode/disruptor/disruptor/2.10.1/disruptor-2.10.1.jar from central
Retrieving org/jgrapht/jgrapht-core/0.9.0/jgrapht-core-0.9.0.jar from central
Retrieving ch/qos/logback/logback-classic/1.0.13/logback-classic-1.0.13.jar from central
Retrieving ch/qos/logback/logback-core/1.0.13/logback-core-1.0.13.jar from central
Retrieving org/slf4j/slf4j-api/1.7.5/slf4j-api-1.7.5.jar from central
Retrieving org/slf4j/log4j-over-slf4j/1.6.6/log4j-over-slf4j-1.6.6.jar from central
Retrieving jline/jline/2.11/jline-2.11.jar from central
Retrieving org/clojure/data.json/0.2.6/data.json-0.2.6.jar from central
Retrieving org/clojure/tools.nrepl/0.2.12/tools.nrepl-0.2.12.jar from central
Retrieving clj-time/clj-time/0.4.1/clj-time-0.4.1.jar from clojars
Retrieving compojure/compojure/1.1.3/compojure-1.1.3.jar from clojars
Retrieving clout/clout/1.0.1/clout-1.0.1.jar from clojars
Retrieving ring/ring-devel/0.3.11/ring-devel-0.3.11.jar from clojars
Retrieving hiccup/hiccup/0.3.6/hiccup-0.3.6.jar from clojars
Retrieving ring/ring-core/1.1.5/ring-core-1.1.5.jar from clojars
Retrieving clj-stacktrace/clj-stacktrace/0.2.2/clj-stacktrace-0.2.2.jar from clojars
Retrieving ring/ring-jetty-adapter/0.3.11/ring-jetty-adapter-0.3.11.jar from clojars
Retrieving ring/ring-servlet/0.3.11/ring-servlet-0.3.11.jar from clojars
Retrieving com/twitter/carbonite/1.4.0/carbonite-1.4.0.jar from clojars
Retrieving com/parsely/streamparse/0.0.4-SNAPSHOT/streamparse-0.0.4-20160314.185928-7.jar from clojars
Retrieving clojure-complete/clojure-complete/0.2.4/clojure-complete-0.2.4.jar from clojars
1418 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:zookeeper.version=3.4.6-1569965, built on 02/20/2014 09:09 GMT
1424 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:host.name=ip-172-31-57-217.ec2.internal
1424 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.version=1.7.0_79
1424 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.vendor=Oracle Corporation
1424 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.home=/opt/jdk1.7.0_79/jre
1425 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.class.path=/root/EX2Tweetwordcount/test:/root/EX2Tweetwordcount/topologies:/root/EX2Tweetwordcount/dev-resources:/root/EX2Tweetwordcount/_resources:/root/EX2Tweetwordcount/_build/classes:/root/.m2/repository/ch/qos/logback/logback-classic/1.0.13/logback-classic-1.0.13.jar:/root/.m2/repository/org/clojure/tools.macro/0.1.0/tools.macro-0.1.0.jar:/root/.m2/repository/ring/ring-core/1.1.5/ring-core-1.1.5.jar:/root/.m2/repository/hiccup/hiccup/0.3.6/hiccup-0.3.6.jar:/root/.m2/repository/ring/ring-servlet/0.3.11/ring-servlet-0.3.11.jar:/root/.m2/repository/com/googlecode/json-simple/json-simple/1.1/json-simple-1.1.jar:/root/.m2/repository/org/clojure/math.numeric-tower/0.0.1/math.numeric-tower-0.0.1.jar:/root/.m2/repository/clj-time/clj-time/0.4.1/clj-time-0.4.1.jar:/root/.m2/repository/org/objenesis/objenesis/1.2/objenesis-1.2.jar:/root/.m2/repository/com/twitter/chill-java/0.3.5/chill-java-0.3.5.jar:/root/.m2/repository/com/parsely/streamparse/0.0.4-SNAPSHOT/streamparse-0.0.4-SNAPSHOT.jar:/root/.m2/repository/ring/ring-jetty-adapter/0.3.11/ring-jetty-adapter-0.3.11.jar:/root/.m2/repository/jline/jline/2.11/jline-2.11.jar:/root/.m2/repository/clj-stacktrace/clj-stacktrace/0.2.2/clj-stacktrace-0.2.2.jar:/root/.m2/repository/org/clojure/tools.nrepl/0.2.12/tools.nrepl-0.2.12.jar:/root/.m2/repository/org/slf4j/slf4j-api/1.7.5/slf4j-api-1.7.5.jar:/root/.m2/repository/ring/ring-devel/0.3.11/ring-devel-0.3.11.jar:/root/.m2/repository/org/mortbay/jetty/jetty-util/6.1.26/jetty-util-6.1.26.jar:/root/.m2/repository/javax/servlet/servlet-api/2.5/servlet-api-2.5.jar:/root/.m2/repository/clojure-complete/clojure-complete/0.2.4/clojure-complete-0.2.4.jar:/root/.m2/repository/org/yaml/snakeyaml/1.11/snakeyaml-1.11.jar:/root/.m2/repository/ch/qos/logback/logback-core/1.0.13/logback-core-1.0.13.jar:/root/.m2/repository/commons-lang/commons-lang/2.5/commons-lang-2.5.jar:/root/.m2/repository/org/mortbay/jetty/jetty/6.1.26/jetty-6.1.26.jar:/root/.m2/repository/joda-time/joda-time/2.0/joda-time-2.0.jar:/root/.m2/repository/commons-io/commons-io/2.4/commons-io-2.4.jar:/root/.m2/repository/commons-logging/commons-logging/1.1.3/commons-logging-1.1.3.jar:/root/.m2/repository/com/esotericsoftware/kryo/kryo/2.21/kryo-2.21.jar:/root/.m2/repository/com/esotericsoftware/minlog/minlog/1.2/minlog-1.2.jar:/root/.m2/repository/org/apache/storm/storm-core/0.9.5/storm-core-0.9.5.jar:/root/.m2/repository/compojure/compojure/1.1.3/compojure-1.1.3.jar:/root/.m2/repository/com/esotericsoftware/reflectasm/reflectasm/1.07/reflectasm-1.07-shaded.jar:/root/.m2/repository/com/twitter/carbonite/1.4.0/carbonite-1.4.0.jar:/root/.m2/repository/commons-codec/commons-codec/1.6/commons-codec-1.6.jar:/root/.m2/repository/commons-fileupload/commons-fileupload/1.2.1/commons-fileupload-1.2.1.jar:/root/.m2/repository/org/clojure/data.json/0.2.6/data.json-0.2.6.jar:/root/.m2/repository/org/slf4j/log4j-over-slf4j/1.6.6/log4j-over-slf4j-1.6.6.jar:/root/.m2/repository/org/jgrapht/jgrapht-core/0.9.0/jgrapht-core-0.9.0.jar:/root/.m2/repository/org/clojure/clojure/1.5.1/clojure-1.5.1.jar:/root/.m2/repository/org/clojure/tools.logging/0.2.3/tools.logging-0.2.3.jar:/root/.m2/repository/org/ow2/asm/asm/4.0/asm-4.0.jar:/root/.m2/repository/clout/clout/1.0.1/clout-1.0.1.jar:/root/.m2/repository/org/apache/commons/commons-exec/1.1/commons-exec-1.1.jar:/root/.m2/repository/com/googlecode/disruptor/disruptor/2.10.1/disruptor-2.10.1.jar:/root/.m2/repository/org/clojure/core.incubator/0.1.0/core.incubator-0.1.0.jar:/root/.m2/repository/org/clojure/tools.cli/0.2.4/tools.cli-0.2.4.jar
1425 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.library.path=/usr/java/packages/lib/amd64:/usr/lib64:/lib64:/lib:/usr/lib
1425 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.io.tmpdir=/tmp
1425 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:java.compiler=<NA>
1426 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:os.name=Linux
1426 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:os.arch=amd64
1426 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:os.version=2.6.32-504.12.2.el6.centos.plus.x86_64
1426 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:user.name=root
1426 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:user.home=/root
1426 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Client environment:user.dir=/root/EX2Tweetwordcount
1459 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:zookeeper.version=3.4.6-1569965, built on 02/20/2014 09:09 GMT
1459 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:host.name=ip-172-31-57-217.ec2.internal
1459 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.version=1.7.0_79
1459 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.vendor=Oracle Corporation
1459 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.home=/opt/jdk1.7.0_79/jre
1459 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.class.path=/root/EX2Tweetwordcount/test:/root/EX2Tweetwordcount/topologies:/root/EX2Tweetwordcount/dev-resources:/root/EX2Tweetwordcount/_resources:/root/EX2Tweetwordcount/_build/classes:/root/.m2/repository/ch/qos/logback/logback-classic/1.0.13/logback-classic-1.0.13.jar:/root/.m2/repository/org/clojure/tools.macro/0.1.0/tools.macro-0.1.0.jar:/root/.m2/repository/ring/ring-core/1.1.5/ring-core-1.1.5.jar:/root/.m2/repository/hiccup/hiccup/0.3.6/hiccup-0.3.6.jar:/root/.m2/repository/ring/ring-servlet/0.3.11/ring-servlet-0.3.11.jar:/root/.m2/repository/com/googlecode/json-simple/json-simple/1.1/json-simple-1.1.jar:/root/.m2/repository/org/clojure/math.numeric-tower/0.0.1/math.numeric-tower-0.0.1.jar:/root/.m2/repository/clj-time/clj-time/0.4.1/clj-time-0.4.1.jar:/root/.m2/repository/org/objenesis/objenesis/1.2/objenesis-1.2.jar:/root/.m2/repository/com/twitter/chill-java/0.3.5/chill-java-0.3.5.jar:/root/.m2/repository/com/parsely/streamparse/0.0.4-SNAPSHOT/streamparse-0.0.4-SNAPSHOT.jar:/root/.m2/repository/ring/ring-jetty-adapter/0.3.11/ring-jetty-adapter-0.3.11.jar:/root/.m2/repository/jline/jline/2.11/jline-2.11.jar:/root/.m2/repository/clj-stacktrace/clj-stacktrace/0.2.2/clj-stacktrace-0.2.2.jar:/root/.m2/repository/org/clojure/tools.nrepl/0.2.12/tools.nrepl-0.2.12.jar:/root/.m2/repository/org/slf4j/slf4j-api/1.7.5/slf4j-api-1.7.5.jar:/root/.m2/repository/ring/ring-devel/0.3.11/ring-devel-0.3.11.jar:/root/.m2/repository/org/mortbay/jetty/jetty-util/6.1.26/jetty-util-6.1.26.jar:/root/.m2/repository/javax/servlet/servlet-api/2.5/servlet-api-2.5.jar:/root/.m2/repository/clojure-complete/clojure-complete/0.2.4/clojure-complete-0.2.4.jar:/root/.m2/repository/org/yaml/snakeyaml/1.11/snakeyaml-1.11.jar:/root/.m2/repository/ch/qos/logback/logback-core/1.0.13/logback-core-1.0.13.jar:/root/.m2/repository/commons-lang/commons-lang/2.5/commons-lang-2.5.jar:/root/.m2/repository/org/mortbay/jetty/jetty/6.1.26/jetty-6.1.26.jar:/root/.m2/repository/joda-time/joda-time/2.0/joda-time-2.0.jar:/root/.m2/repository/commons-io/commons-io/2.4/commons-io-2.4.jar:/root/.m2/repository/commons-logging/commons-logging/1.1.3/commons-logging-1.1.3.jar:/root/.m2/repository/com/esotericsoftware/kryo/kryo/2.21/kryo-2.21.jar:/root/.m2/repository/com/esotericsoftware/minlog/minlog/1.2/minlog-1.2.jar:/root/.m2/repository/org/apache/storm/storm-core/0.9.5/storm-core-0.9.5.jar:/root/.m2/repository/compojure/compojure/1.1.3/compojure-1.1.3.jar:/root/.m2/repository/com/esotericsoftware/reflectasm/reflectasm/1.07/reflectasm-1.07-shaded.jar:/root/.m2/repository/com/twitter/carbonite/1.4.0/carbonite-1.4.0.jar:/root/.m2/repository/commons-codec/commons-codec/1.6/commons-codec-1.6.jar:/root/.m2/repository/commons-fileupload/commons-fileupload/1.2.1/commons-fileupload-1.2.1.jar:/root/.m2/repository/org/clojure/data.json/0.2.6/data.json-0.2.6.jar:/root/.m2/repository/org/slf4j/log4j-over-slf4j/1.6.6/log4j-over-slf4j-1.6.6.jar:/root/.m2/repository/org/jgrapht/jgrapht-core/0.9.0/jgrapht-core-0.9.0.jar:/root/.m2/repository/org/clojure/clojure/1.5.1/clojure-1.5.1.jar:/root/.m2/repository/org/clojure/tools.logging/0.2.3/tools.logging-0.2.3.jar:/root/.m2/repository/org/ow2/asm/asm/4.0/asm-4.0.jar:/root/.m2/repository/clout/clout/1.0.1/clout-1.0.1.jar:/root/.m2/repository/org/apache/commons/commons-exec/1.1/commons-exec-1.1.jar:/root/.m2/repository/com/googlecode/disruptor/disruptor/2.10.1/disruptor-2.10.1.jar:/root/.m2/repository/org/clojure/core.incubator/0.1.0/core.incubator-0.1.0.jar:/root/.m2/repository/org/clojure/tools.cli/0.2.4/tools.cli-0.2.4.jar
1459 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.library.path=/usr/java/packages/lib/amd64:/usr/lib64:/lib64:/lib:/usr/lib
1459 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.io.tmpdir=/tmp
1459 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:java.compiler=<NA>
1459 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:os.name=Linux
1459 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:os.arch=amd64
1459 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:os.version=2.6.32-504.12.2.el6.centos.plus.x86_64
1459 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:user.name=root
1459 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:user.home=/root
1459 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Server environment:user.dir=/root/EX2Tweetwordcount
2260 [main] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Created server with tickTime 2000 minSessionTimeout 4000 maxSessionTimeout 40000 datadir /tmp/2721bad8-e128-4b89-a82f-477e79a0c341/version-2 snapdir /tmp/2721bad8-e128-4b89-a82f-477e79a0c341/version-2
2268 [main] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - binding to port 0.0.0.0/0.0.0.0:2000
2271 [main] INFO  backtype.storm.zookeeper - Starting inprocess zookeeper at port 2000 and dir /tmp/2721bad8-e128-4b89-a82f-477e79a0c341
2463 [main] INFO  backtype.storm.daemon.nimbus - Starting Nimbus with conf {"dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/9dfe6000-48be-41d4-9ebc-f874aebbce2f", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" nil, "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" nil, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" [6700 6701 6702 6703], "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.message.timeout.secs" 30, "task.refresh.poll.secs" 10, "topology.workers" 1, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil}
2468 [main] INFO  backtype.storm.daemon.nimbus - Using default scheduler
2477 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
2548 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
2550 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@7cde8c87
2567 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
2572 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:59456
2576 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
2580 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:59456
2582 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.persistence.FileTxnLog - Creating new log file: log.1
2594 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x153f161ed900000, negotiated timeout = 20000
2595 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x153f161ed900000 with negotiated timeout 20000 for client /127.0.0.1:59456
2597 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
2599 [main-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
2625 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x153f161ed900000
2626 [main-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
2627 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x153f161ed900000 closed
2632 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
2632 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:59456 which had sessionid 0x153f161ed900000
2633 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
2633 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@24d9d889
2634 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
2635 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:59457
2635 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
2635 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:59457
2638 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x153f161ed900001 with negotiated timeout 20000 for client /127.0.0.1:59457
2638 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x153f161ed900001, negotiated timeout = 20000
2638 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
2673 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
2673 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
2674 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@761d5b3a
2675 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
2675 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:59458
2676 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
2676 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:59458
2678 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x153f161ed900002 with negotiated timeout 20000 for client /127.0.0.1:59458
2679 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x153f161ed900002, negotiated timeout = 20000
2679 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
2679 [main-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
2681 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x153f161ed900002
2683 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:59458 which had sessionid 0x153f161ed900002
2683 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x153f161ed900002 closed
2683 [main-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
2683 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
2687 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
2687 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@3e7403c9
2688 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
2688 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
2688 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:59459
2689 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:59459
2690 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
2690 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
2690 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@3071681
2691 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
2692 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:59460
2692 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
2692 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:59460
2693 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x153f161ed900003 with negotiated timeout 20000 for client /127.0.0.1:59459
2693 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x153f161ed900003, negotiated timeout = 20000
2693 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
2694 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x153f161ed900004 with negotiated timeout 20000 for client /127.0.0.1:59460
2695 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x153f161ed900004, negotiated timeout = 20000
2695 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
2695 [main-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
3697 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x153f161ed900004
3699 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:59460 which had sessionid 0x153f161ed900004
3699 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x153f161ed900004 closed
3700 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
3700 [main-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
3701 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
3701 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@518e322b
3702 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
3702 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
3706 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:59462
3706 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:59462
3707 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x153f161ed900005 with negotiated timeout 20000 for client /127.0.0.1:59462
3708 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x153f161ed900005, negotiated timeout = 20000
3708 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
3740 [main] INFO  backtype.storm.daemon.supervisor - Starting Supervisor with conf {"dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/aebc58b9-9c46-4f7d-a3e6-af5238fc9b90", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" nil, "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" nil, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" (1024 1025 1026), "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.message.timeout.secs" 30, "task.refresh.poll.secs" 10, "topology.workers" 1, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil}
3749 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
3750 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
3750 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@3d5e76ac
3752 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
3752 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
3752 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:59463
3753 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:59463
3755 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x153f161ed900006 with negotiated timeout 20000 for client /127.0.0.1:59463
3755 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x153f161ed900006, negotiated timeout = 20000
3755 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
3756 [main-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
3758 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x153f161ed900006
3759 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x153f161ed900006 closed
3759 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:59463 which had sessionid 0x153f161ed900006
3759 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
3760 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
3760 [main-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
3760 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@7c491585
3761 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
3762 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
3762 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:59464
3763 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:59464
3764 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x153f161ed900007 with negotiated timeout 20000 for client /127.0.0.1:59464
3765 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x153f161ed900007, negotiated timeout = 20000
3765 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
4787 [main] INFO  backtype.storm.daemon.supervisor - Starting supervisor with id 5851c060-38e5-4410-98c5-78f9640a15f1 at host ip-172-31-57-217.ec2.internal
4793 [main] INFO  backtype.storm.daemon.supervisor - Starting Supervisor with conf {"dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/b214eb4a-3d02-44e1-afc2-9ffbc7379640", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" nil, "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" nil, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" (1027 1028 1029), "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.message.timeout.secs" 30, "task.refresh.poll.secs" 10, "topology.workers" 1, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil}
4795 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
4796 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
4796 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@4e8e3a30
4797 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
4798 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:59465
4798 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
4798 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:59465
4800 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x153f161ed900008 with negotiated timeout 20000 for client /127.0.0.1:59465
4800 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x153f161ed900008, negotiated timeout = 20000
4800 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
4801 [main-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
5803 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x153f161ed900008
5804 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x153f161ed900008 closed
5805 [main] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
5806 [main] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
5811 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] WARN  org.apache.storm.zookeeper.server.NIOServerCnxn - caught end of stream exception
org.apache.storm.zookeeper.server.ServerCnxn$EndOfStreamException: Unable to read additional data from client sessionid 0x153f161ed900008, likely client has closed socket
	at org.apache.storm.zookeeper.server.NIOServerCnxn.doIO(NIOServerCnxn.java:228) ~[storm-core-0.9.5.jar:0.9.5]
	at org.apache.storm.zookeeper.server.NIOServerCnxnFactory.run(NIOServerCnxnFactory.java:208) [storm-core-0.9.5.jar:0.9.5]
	at java.lang.Thread.run(Thread.java:745) [na:1.7.0_79]
5812 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:59465 which had sessionid 0x153f161ed900008
5812 [main] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@3098fb0b
5813 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
5813 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:59466
5814 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
5815 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:59466
5815 [main-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
5818 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x153f161ed900009 with negotiated timeout 20000 for client /127.0.0.1:59466
5818 [main-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x153f161ed900009, negotiated timeout = 20000
5818 [main-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
5826 [main] INFO  backtype.storm.daemon.supervisor - Starting supervisor with id 2a83c3b9-d002-4d93-8822-6333a2a86c07 at host ip-172-31-57-217.ec2.internal
5889 [main] INFO  backtype.storm.daemon.nimbus - Received topology submission for tweetwordcount with conf {"storm.id" "tweetwordcount-1-1460043643", "topology.acker.executors" 2, "streamparse.log.path" "\"/root/EX2Tweetwordcount/logs\"", "topology.kryo.decorators" (), "topology.name" "tweetwordcount", "topology.max.spout.pending" 5000, "topology.debug" false, "topology.kryo.register" nil, "topology.message.timeout.secs" 60, "topology.workers" 2, "topology.max.task.parallelism" nil, "streamparse.log.level" "debug"}
5928 [main] INFO  backtype.storm.daemon.nimbus - Activating tweetwordcount: tweetwordcount-1-1460043643
6029 [main] INFO  backtype.storm.scheduler.EvenScheduler - Available slots: (["2a83c3b9-d002-4d93-8822-6333a2a86c07" 1027] ["2a83c3b9-d002-4d93-8822-6333a2a86c07" 1028] ["2a83c3b9-d002-4d93-8822-6333a2a86c07" 1029] ["5851c060-38e5-4410-98c5-78f9640a15f1" 1024] ["5851c060-38e5-4410-98c5-78f9640a15f1" 1025] ["5851c060-38e5-4410-98c5-78f9640a15f1" 1026])
6092 [main] INFO  backtype.storm.daemon.nimbus - Setting new assignment for topology id tweetwordcount-1-1460043643: #backtype.storm.daemon.common.Assignment{:master-code-dir "/tmp/9dfe6000-48be-41d4-9ebc-f874aebbce2f/nimbus/stormdist/tweetwordcount-1-1460043643", :node->host {"5851c060-38e5-4410-98c5-78f9640a15f1" "ip-172-31-57-217.ec2.internal", "2a83c3b9-d002-4d93-8822-6333a2a86c07" "ip-172-31-57-217.ec2.internal"}, :executor->node+port {[3 3] ["2a83c3b9-d002-4d93-8822-6333a2a86c07" 1027], [6 6] ["5851c060-38e5-4410-98c5-78f9640a15f1" 1024], [5 5] ["2a83c3b9-d002-4d93-8822-6333a2a86c07" 1027], [4 4] ["5851c060-38e5-4410-98c5-78f9640a15f1" 1024], [7 7] ["2a83c3b9-d002-4d93-8822-6333a2a86c07" 1027], [2 2] ["5851c060-38e5-4410-98c5-78f9640a15f1" 1024], [1 1] ["2a83c3b9-d002-4d93-8822-6333a2a86c07" 1027]}, :executor->start-time-secs {[7 7] 1460043643, [5 5] 1460043643, [3 3] 1460043643, [1 1] 1460043643, [6 6] 1460043643, [4 4] 1460043643, [2 2] 1460043643}}
6619 [Thread-3] INFO  backtype.storm.daemon.supervisor - Copying resources at file:/root/EX2Tweetwordcount/_resources/resources to /tmp/aebc58b9-9c46-4f7d-a3e6-af5238fc9b90/supervisor/stormdist/tweetwordcount-1-1460043643/resources
6649 [Thread-4] INFO  backtype.storm.daemon.supervisor - Launching worker with assignment #backtype.storm.daemon.supervisor.LocalAssignment{:storm-id "tweetwordcount-1-1460043643", :executors ([6 6] [4 4] [2 2])} for this supervisor 5851c060-38e5-4410-98c5-78f9640a15f1 on port 1024 with id 8c803721-eaf9-4b81-892a-80bfa47fe222
6651 [Thread-4] INFO  backtype.storm.daemon.worker - Launching worker for tweetwordcount-1-1460043643 on 5851c060-38e5-4410-98c5-78f9640a15f1:1024 with id 8c803721-eaf9-4b81-892a-80bfa47fe222 and conf {"dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/aebc58b9-9c46-4f7d-a3e6-af5238fc9b90", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" nil, "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" nil, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" (1024 1025 1026), "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.message.timeout.secs" 30, "task.refresh.poll.secs" 10, "topology.workers" 1, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil}
6652 [Thread-4] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
6652 [Thread-4] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
6653 [Thread-4] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@7b0aa31f
6655 [Thread-4-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
6655 [Thread-4-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
6655 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:59467
6655 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:59467
6657 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x153f161ed90000a with negotiated timeout 20000 for client /127.0.0.1:59467
6657 [Thread-4-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x153f161ed90000a, negotiated timeout = 20000
6657 [Thread-4-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
6657 [Thread-4-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
6659 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x153f161ed90000a
6660 [Thread-4] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x153f161ed90000a closed
6660 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:59467 which had sessionid 0x153f161ed90000a
6660 [Thread-4] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
6660 [Thread-4-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
6661 [Thread-4] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
6661 [Thread-4] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@542a7fe3
6663 [Thread-4-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
6663 [Thread-4-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
6663 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:59468
6663 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:59468
6665 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x153f161ed90000b with negotiated timeout 20000 for client /127.0.0.1:59468
6665 [Thread-4-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x153f161ed90000b, negotiated timeout = 20000
6665 [Thread-4-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
6672 [Thread-4] INFO  backtype.storm.daemon.worker - Reading Assignments.
6749 [Thread-4] INFO  backtype.storm.daemon.worker - Launching receive-thread for 5851c060-38e5-4410-98c5-78f9640a15f1:1024
6768 [Thread-7-worker-receiver-thread-0] INFO  backtype.storm.messaging.loader - Starting receive-thread: [stormId: tweetwordcount-1-1460043643, port: 1024, thread-id: 0 ]
7238 [Thread-4] INFO  backtype.storm.daemon.executor - Loading executor __acker:[2 2]
7241 [Thread-5] INFO  backtype.storm.daemon.supervisor - Copying resources at file:/root/EX2Tweetwordcount/_resources/resources to /tmp/b214eb4a-3d02-44e1-afc2-9ffbc7379640/supervisor/stormdist/tweetwordcount-1-1460043643/resources
7258 [Thread-4] INFO  backtype.storm.daemon.executor - Loaded executor tasks __acker:[2 2]
7263 [Thread-6] INFO  backtype.storm.daemon.supervisor - Launching worker with assignment #backtype.storm.daemon.supervisor.LocalAssignment{:storm-id "tweetwordcount-1-1460043643", :executors ([3 3] [5 5] [7 7] [1 1])} for this supervisor 2a83c3b9-d002-4d93-8822-6333a2a86c07 on port 1027 with id 90498bf6-41db-4adc-9ed4-55f248d748b4
7269 [Thread-6] INFO  backtype.storm.daemon.worker - Launching worker for tweetwordcount-1-1460043643 on 2a83c3b9-d002-4d93-8822-6333a2a86c07:1027 with id 90498bf6-41db-4adc-9ed4-55f248d748b4 and conf {"dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/b214eb4a-3d02-44e1-afc2-9ffbc7379640", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" nil, "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" nil, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" (1027 1028 1029), "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.message.timeout.secs" 30, "task.refresh.poll.secs" 10, "topology.workers" 1, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil}
7269 [Thread-6] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
7270 [Thread-6] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
7270 [Thread-6] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000 sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@609aef91
7273 [Thread-4] INFO  backtype.storm.daemon.executor - Timeouts disabled for executor __acker:[2 2]
7273 [Thread-4] INFO  backtype.storm.daemon.executor - Finished loading executor __acker:[2 2]
7276 [Thread-6-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
7277 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:59469
7277 [Thread-6-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
7277 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:59469
7279 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x153f161ed90000c with negotiated timeout 20000 for client /127.0.0.1:59469
7279 [Thread-6-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x153f161ed90000c, negotiated timeout = 20000
7281 [Thread-6-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
7281 [Thread-6-EventThread] INFO  backtype.storm.zookeeper - Zookeeper state update: :connected:none
7286 [ProcessThread(sid:0 cport:-1):] INFO  org.apache.storm.zookeeper.server.PrepRequestProcessor - Processed session termination for sessionid: 0x153f161ed90000c
7287 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxn - Closed socket connection for client /127.0.0.1:59469 which had sessionid 0x153f161ed90000c
7287 [Thread-6] INFO  org.apache.storm.zookeeper.ZooKeeper - Session: 0x153f161ed90000c closed
7288 [Thread-6] INFO  backtype.storm.utils.StormBoundedExponentialBackoffRetry - The baseSleepTimeMs [1000] the maxSleepTimeMs [30000] the maxRetries [5]
7288 [Thread-6] INFO  org.apache.storm.curator.framework.imps.CuratorFrameworkImpl - Starting
7288 [Thread-6-EventThread] INFO  org.apache.storm.zookeeper.ClientCnxn - EventThread shut down
7289 [Thread-6] INFO  org.apache.storm.zookeeper.ZooKeeper - Initiating client connection, connectString=localhost:2000/storm sessionTimeout=20000 watcher=org.apache.storm.curator.ConnectionState@4d62193b
7292 [Thread-4] INFO  backtype.storm.daemon.executor - Loading executor count-bolt:[4 4]
7293 [Thread-6-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Opening socket connection to server localhost/127.0.0.1:2000. Will not attempt to authenticate using SASL (unknown error)
7293 [Thread-6-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Socket connection established to localhost/127.0.0.1:2000, initiating session
7293 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.NIOServerCnxnFactory - Accepted socket connection from /127.0.0.1:59470
7293 [NIOServerCxn.Factory:0.0.0.0/0.0.0.0:2000] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Client attempting to establish new session at /127.0.0.1:59470
7298 [SyncThread:0] INFO  org.apache.storm.zookeeper.server.ZooKeeperServer - Established session 0x153f161ed90000d with negotiated timeout 20000 for client /127.0.0.1:59470
7298 [Thread-6-SendThread(localhost:2000)] INFO  org.apache.storm.zookeeper.ClientCnxn - Session establishment complete on server localhost/127.0.0.1:2000, sessionid = 0x153f161ed90000d, negotiated timeout = 20000
7298 [Thread-6-EventThread] INFO  org.apache.storm.curator.framework.state.ConnectionStateManager - State change: CONNECTED
7301 [Thread-4] INFO  backtype.storm.daemon.executor - Loaded executor tasks count-bolt:[4 4]
7303 [Thread-4] INFO  backtype.storm.daemon.executor - Finished loading executor count-bolt:[4 4]
7311 [Thread-4] INFO  backtype.storm.daemon.executor - Loading executor parse-tweet-bolt:[6 6]
7321 [Thread-4] INFO  backtype.storm.daemon.executor - Loaded executor tasks parse-tweet-bolt:[6 6]
7323 [Thread-4] INFO  backtype.storm.daemon.executor - Finished loading executor parse-tweet-bolt:[6 6]
7329 [Thread-4] INFO  backtype.storm.daemon.executor - Loading executor __system:[-1 -1]
7330 [Thread-4] INFO  backtype.storm.daemon.executor - Loaded executor tasks __system:[-1 -1]
7332 [Thread-4] INFO  backtype.storm.daemon.executor - Finished loading executor __system:[-1 -1]
7337 [Thread-4] INFO  backtype.storm.daemon.worker - Worker has topology config {"storm.id" "tweetwordcount-1-1460043643", "dev.zookeeper.path" "/tmp/dev-storm-zookeeper", "topology.tick.tuple.freq.secs" nil, "topology.builtin.metrics.bucket.size.secs" 60, "topology.fall.back.on.java.serialization" true, "topology.max.error.report.per.interval" 5, "zmq.linger.millis" 0, "topology.skip.missing.kryo.registrations" true, "storm.messaging.netty.client_worker_threads" 1, "ui.childopts" "-Xmx768m", "storm.zookeeper.session.timeout" 20000, "nimbus.reassign" true, "topology.trident.batch.emit.interval.millis" 50, "storm.messaging.netty.flush.check.interval.ms" 10, "nimbus.monitor.freq.secs" 10, "logviewer.childopts" "-Xmx128m", "java.library.path" "/usr/local/lib:/opt/local/lib:/usr/lib", "topology.executor.send.buffer.size" 1024, "storm.local.dir" "/tmp/aebc58b9-9c46-4f7d-a3e6-af5238fc9b90", "storm.messaging.netty.buffer_size" 5242880, "supervisor.worker.start.timeout.secs" 120, "topology.enable.message.timeouts" true, "nimbus.cleanup.inbox.freq.secs" 600, "nimbus.inbox.jar.expiration.secs" 3600, "drpc.worker.threads" 64, "storm.meta.serialization.delegate" "backtype.storm.serialization.DefaultSerializationDelegate", "topology.worker.shared.thread.pool.size" 4, "nimbus.host" "localhost", "storm.messaging.netty.min_wait_ms" 100, "storm.zookeeper.port" 2000, "transactional.zookeeper.port" nil, "topology.executor.receive.buffer.size" 1024, "transactional.zookeeper.servers" nil, "storm.zookeeper.root" "/storm", "storm.zookeeper.retry.intervalceiling.millis" 30000, "supervisor.enable" true, "storm.messaging.netty.server_worker_threads" 1, "storm.zookeeper.servers" ["localhost"], "transactional.zookeeper.root" "/transactional", "topology.acker.executors" 2, "streamparse.log.path" "\"/root/EX2Tweetwordcount/logs\"", "topology.kryo.decorators" (), "topology.name" "tweetwordcount", "topology.transfer.buffer.size" 1024, "topology.worker.childopts" nil, "drpc.queue.size" 128, "worker.childopts" "-Xmx768m", "supervisor.heartbeat.frequency.secs" 5, "topology.error.throttle.interval.secs" 10, "zmq.hwm" 0, "drpc.port" 3772, "supervisor.monitor.frequency.secs" 3, "drpc.childopts" "-Xmx768m", "topology.receiver.buffer.size" 8, "task.heartbeat.frequency.secs" 3, "topology.tasks" nil, "storm.messaging.netty.max_retries" 300, "topology.spout.wait.strategy" "backtype.storm.spout.SleepSpoutWaitStrategy", "nimbus.thrift.max_buffer_size" 1048576, "topology.max.spout.pending" 5000, "storm.zookeeper.retry.interval" 1000, "topology.sleep.spout.wait.strategy.time.ms" 1, "nimbus.topology.validator" "backtype.storm.nimbus.DefaultTopologyValidator", "supervisor.slots.ports" (1024 1025 1026), "topology.environment" nil, "topology.debug" false, "nimbus.task.launch.secs" 120, "nimbus.supervisor.timeout.secs" 60, "topology.kryo.register" nil, "topology.message.timeout.secs" 60, "task.refresh.poll.secs" 10, "topology.workers" 2, "supervisor.childopts" "-Xmx256m", "nimbus.thrift.port" 6627, "topology.stats.sample.rate" 0.05, "worker.heartbeat.frequency.secs" 1, "topology.tuple.serializer" "backtype.storm.serialization.types.ListDelegateSerializer", "topology.disruptor.wait.strategy" "com.lmax.disruptor.BlockingWaitStrategy", "topology.multilang.serializer" "backtype.storm.multilang.JsonSerializer", "nimbus.task.timeout.secs" 30, "storm.zookeeper.connection.timeout" 15000, "topology.kryo.factory" "backtype.storm.serialization.DefaultKryoFactory", "drpc.invocations.port" 3773, "logviewer.port" 8000, "zmq.threads" 1, "storm.zookeeper.retry.times" 5, "topology.worker.receiver.thread.count" 1, "storm.thrift.transport" "backtype.storm.security.auth.SimpleTransportPlugin", "topology.state.synchronization.timeout.secs" 60, "supervisor.worker.timeout.secs" 30, "nimbus.file.copy.expiration.secs" 600, "storm.messaging.transport" "backtype.storm.messaging.netty.Context", "logviewer.appender.name" "A1", "storm.messaging.netty.max_wait_ms" 1000, "drpc.request.timeout.secs" 600, "storm.local.mode.zmq" false, "ui.port" 8080, "nimbus.childopts" "-Xmx1024m", "storm.cluster.mode" "local", "topology.max.task.parallelism" nil, "storm.messaging.netty.transfer.batch.size" 262144, "topology.classpath" nil, "streamparse.log.level" "debug"}
7338 [Thread-4] INFO  backtype.storm.daemon.worker - Worker 8c803721-eaf9-4b81-892a-80bfa47fe222 for storm tweetwordcount-1-1460043643 on 5851c060-38e5-4410-98c5-78f9640a15f1:1024 has finished loading
7697 [refresh-active-timer] INFO  backtype.storm.daemon.worker - All connections are ready for worker 5851c060-38e5-4410-98c5-78f9640a15f1:1024 with id 8c803721-eaf9-4b81-892a-80bfa47fe222
7730 [Thread-13-parse-tweet-bolt] INFO  backtype.storm.daemon.executor - Preparing bolt parse-tweet-bolt:(6)
7733 [Thread-15-__system] INFO  backtype.storm.daemon.executor - Preparing bolt __system:(-1)
7738 [Thread-15-__system] INFO  backtype.storm.daemon.executor - Prepared bolt __system:(-1)
7742 [Thread-13-parse-tweet-bolt] INFO  backtype.storm.utils.ShellProcess - Storm multilang serializer: backtype.storm.multilang.JsonSerializer
7774 [Thread-9-__acker] INFO  backtype.storm.daemon.executor - Preparing bolt __acker:(2)
7776 [Thread-9-__acker] INFO  backtype.storm.daemon.executor - Prepared bolt __acker:(2)
7804 [Thread-11-count-bolt] INFO  backtype.storm.daemon.executor - Preparing bolt count-bolt:(4)
7804 [Thread-11-count-bolt] INFO  backtype.storm.utils.ShellProcess - Storm multilang serializer: backtype.storm.multilang.JsonSerializer
7829 [Thread-13-parse-tweet-bolt] INFO  backtype.storm.task.ShellBolt - Launched subprocess with pid 5581
7848 [Thread-13-parse-tweet-bolt] INFO  backtype.storm.task.ShellBolt - Start checking heartbeat...
7848 [Thread-13-parse-tweet-bolt] INFO  backtype.storm.daemon.executor - Prepared bolt parse-tweet-bolt:(6)
7851 [Thread-17] ERROR backtype.storm.task.ShellBolt - Halting process: ShellBolt died.
java.lang.RuntimeException: backtype.storm.multilang.NoOutputException: Pipe to subprocess seems to be broken! No output read.
Serializer Exception:
Traceback (most recent call last):
  File "/usr/lib64/python2.7/runpy.py", line 162, in _run_module_as_main
    "__main__", fname, loader, pkg_name)
  File "/usr/lib64/python2.7/runpy.py", line 72, in _run_code
    exec code in run_globals
  File "/usr/lib/python2.7/site-packages/streamparse/run.py", line 25, in <module>
    main()
  File "/usr/lib/python2.7/site-packages/streamparse/run.py", line 21, in main
    cls().run()
  File "/usr/lib/python2.7/site-packages/streamparse/storm/component.py", line 484, in run
    self._setup_component(storm_conf, context)
  File "/usr/lib/python2.7/site-packages/streamparse/storm/component.py", line 246, in _setup_component
    backupCount=backup_count)
  File "/usr/lib64/python2.7/logging/handlers.py", line 118, in __init__
    BaseRotatingHandler.__init__(self, filename, mode, encoding, delay)
  File "/usr/lib64/python2.7/logging/handlers.py", line 65, in __init__
    logging.FileHandler.__init__(self, filename, mode, encoding, delay)
  File "/usr/lib64/python2.7/logging/__init__.py", line 897, in __init__
    StreamHandler.__init__(self, self._open())
  File "/usr/lib64/python2.7/logging/__init__.py", line 916, in _open
    stream = open(self.baseFilename, self.mode)
IOError: [Errno 2] No such file or directory: u'/tmp/aebc58b9-9c46-4f7d-a3e6-af5238fc9b90/supervisor/stormdist/tweetwordcount-1-1460043643/resources/"/root/EX2Tweetwordcount/logs"/streamparse_tweetwordcount_parse-tweet-bolt_6_5581.log'


	at backtype.storm.utils.ShellProcess.readShellMsg(ShellProcess.java:101) ~[storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.task.ShellBolt$BoltReaderRunnable.run(ShellBolt.java:318) ~[storm-core-0.9.5.jar:0.9.5]
	at java.lang.Thread.run(Thread.java:745) [na:1.7.0_79]
7852 [Thread-17] ERROR backtype.storm.daemon.executor - 
java.lang.RuntimeException: backtype.storm.multilang.NoOutputException: Pipe to subprocess seems to be broken! No output read.
Serializer Exception:
Traceback (most recent call last):
  File "/usr/lib64/python2.7/runpy.py", line 162, in _run_module_as_main
    "__main__", fname, loader, pkg_name)
  File "/usr/lib64/python2.7/runpy.py", line 72, in _run_code
    exec code in run_globals
  File "/usr/lib/python2.7/site-packages/streamparse/run.py", line 25, in <module>
    main()
  File "/usr/lib/python2.7/site-packages/streamparse/run.py", line 21, in main
    cls().run()
  File "/usr/lib/python2.7/site-packages/streamparse/storm/component.py", line 484, in run
    self._setup_component(storm_conf, context)
  File "/usr/lib/python2.7/site-packages/streamparse/storm/component.py", line 246, in _setup_component
    backupCount=backup_count)
  File "/usr/lib64/python2.7/logging/handlers.py", line 118, in __init__
    BaseRotatingHandler.__init__(self, filename, mode, encoding, delay)
  File "/usr/lib64/python2.7/logging/handlers.py", line 65, in __init__
    logging.FileHandler.__init__(self, filename, mode, encoding, delay)
  File "/usr/lib64/python2.7/logging/__init__.py", line 897, in __init__
    StreamHandler.__init__(self, self._open())
  File "/usr/lib64/python2.7/logging/__init__.py", line 916, in _open
    stream = open(self.baseFilename, self.mode)
IOError: [Errno 2] No such file or directory: u'/tmp/aebc58b9-9c46-4f7d-a3e6-af5238fc9b90/supervisor/stormdist/tweetwordcount-1-1460043643/resources/"/root/EX2Tweetwordcount/logs"/streamparse_tweetwordcount_parse-tweet-bolt_6_5581.log'


	at backtype.storm.utils.ShellProcess.readShellMsg(ShellProcess.java:101) ~[storm-core-0.9.5.jar:0.9.5]
	at backtype.storm.task.ShellBolt$BoltReaderRunnable.run(ShellBolt.java:318) ~[storm-core-0.9.5.jar:0.9.5]
	at java.lang.Thread.run(Thread.java:745) [na:1.7.0_79]
Traceback (most recent call last):
  File "/usr/bin/sparse", line 11, in <module>
    sys.exit(main())
  File "/usr/lib/python2.7/site-packages/streamparse/cli/sparse.py", line 57, in main
    args.func(args)
  File "/usr/lib/python2.7/site-packages/streamparse/cli/run.py", line 81, in main
    debug=args.debug)
  File "/usr/lib/python2.7/site-packages/streamparse/cli/run.py", line 52, in run_local_topology
    run(full_cmd)
  File "/usr/lib/python2.7/site-packages/invoke/__init__.py", line 27, in run
    return Context().run(command, **kwargs)
  File "/usr/lib/python2.7/site-packages/invoke/context.py", line 53, in run
    return runner_class(context=self).run(command, **kwargs)
  File "/usr/lib/python2.7/site-packages/invoke/runners.py", line 302, in run
    raise Failure(result)
invoke.exceptions.Failure: Command execution failure!

Exit code: 11

Stderr:

Retrieving org/apache/storm/storm-core/0.9.5/storm-core-0.9.5.pom from central
Retrieving org/apache/storm/storm/0.9.5/storm-0.9.5.pom from central
Retrieving org/apache/apache/10/apache-10.pom from central
Retrieving org/clojure/clojure/1.5.1/clojure-1.5.1.pom from central
Retrieving org/sonatype/oss/oss-parent/5/oss-parent-5.pom from central
Retrieving clj-time/clj-time/0.4.1/clj-time-0.4.1.pom from clojars
Retrieving joda-time/joda-time/2.0/joda-time-2.0.pom from central
Retrieving org/clojure/clojure/1.3.0/clojure-1.3.0.pom from central
Retrieving compojure/compojure/1.1.3/compojure-1.1.3.pom from clojars
Retrieving org/clojure/clojure/1.2.1/clojure-1.2.1.pom from central
Retrieving org/clojure/core.incubator/0.1.0/core.incubator-0.1.0.pom from central
Retrieving org/clojure/pom.contrib/0.0.20/pom.contrib-0.0.20.pom from central
Retrieving org/clojure/clojure/1.3.0-alpha5/clojure-1.3.0-alpha5.pom from central
Retrieving org/clojure/tools.macro/0.1.0/tools.macro-0.1.0.pom from central
Retrieving clout/clout/1.0.1/clout-1.0.1.pom from clojars
Retrieving ring/ring-core/1.1.5/ring-core-1.1.5.pom from clojars
Retrieving commons-codec/commons-codec/1.6/commons-codec-1.6.pom from central
Retrieving org/apache/commons/commons-parent/22/commons-parent-22.pom from central
Retrieving org/apache/apache/9/apache-9.pom from central
Retrieving commons-io/commons-io/2.1/commons-io-2.1.pom from central
Retrieving commons-fileupload/commons-fileupload/1.2.1/commons-fileupload-1.2.1.pom from central
Retrieving org/apache/commons/commons-parent/7/commons-parent-7.pom from central
Retrieving org/apache/apache/4/apache-4.pom from central
Retrieving javax/servlet/servlet-api/2.5/servlet-api-2.5.pom from central
Retrieving clj-time/clj-time/0.3.7/clj-time-0.3.7.pom from clojars
Retrieving hiccup/hiccup/0.3.6/hiccup-0.3.6.pom from clojars
Retrieving org/clojure/clojure/1.2.0/clojure-1.2.0.pom from central
Retrieving ring/ring-devel/0.3.11/ring-devel-0.3.11.pom from clojars
Retrieving ring/ring-core/0.3.11/ring-core-0.3.11.pom from clojars
Retrieving commons-codec/commons-codec/1.4/commons-codec-1.4.pom from central
Retrieving org/apache/commons/commons-parent/11/commons-parent-11.pom from central
Retrieving commons-io/commons-io/1.4/commons-io-1.4.pom from central
Retrieving clj-stacktrace/clj-stacktrace/0.2.2/clj-stacktrace-0.2.2.pom from clojars
Retrieving ring/ring-jetty-adapter/0.3.11/ring-jetty-adapter-0.3.11.pom from clojars
Retrieving ring/ring-servlet/0.3.11/ring-servlet-0.3.11.pom from clojars
Retrieving org/mortbay/jetty/jetty/6.1.26/jetty-6.1.26.pom from central
Retrieving org/mortbay/jetty/project/6.1.26/project-6.1.26.pom from central
Retrieving org/mortbay/jetty/jetty-parent/10/jetty-parent-10.pom from central
Retrieving org/eclipse/jetty/jetty-parent/14/jetty-parent-14.pom from central
Retrieving org/mortbay/jetty/jetty-util/6.1.26/jetty-util-6.1.26.pom from central
Retrieving org/mortbay/jetty/servlet-api/2.5-20081211/servlet-api-2.5-20081211.pom from central
Retrieving org/mortbay/jetty/jetty-parent/7/jetty-parent-7.pom from central
Retrieving org/clojure/tools.logging/0.2.3/tools.logging-0.2.3.pom from central
Retrieving org/clojure/pom.contrib/0.0.23/pom.contrib-0.0.23.pom from central
Retrieving org/clojure/clojure/1.3.0-beta1/clojure-1.3.0-beta1.pom from central
Retrieving org/clojure/math.numeric-tower/0.0.1/math.numeric-tower-0.0.1.pom from central
Retrieving org/clojure/pom.contrib/0.0.25/pom.contrib-0.0.25.pom from central
Retrieving org/clojure/tools.cli/0.2.4/tools.cli-0.2.4.pom from central
Retrieving org/clojure/pom.contrib/0.1.2/pom.contrib-0.1.2.pom from central
Retrieving org/sonatype/oss/oss-parent/7/oss-parent-7.pom from central
Retrieving org/clojure/clojure/1.4.0/clojure-1.4.0.pom from central
Retrieving commons-io/commons-io/2.4/commons-io-2.4.pom from central
Retrieving org/apache/commons/commons-parent/25/commons-parent-25.pom from central
Retrieving org/apache/commons/commons-exec/1.1/commons-exec-1.1.pom from central
Retrieving org/apache/commons/commons-parent/17/commons-parent-17.pom from central
Retrieving org/apache/apache/7/apache-7.pom from central
Retrieving commons-lang/commons-lang/2.5/commons-lang-2.5.pom from central
Retrieving org/apache/commons/commons-parent/12/commons-parent-12.pom from central
Retrieving com/googlecode/json-simple/json-simple/1.1/json-simple-1.1.pom from central
Retrieving com/twitter/carbonite/1.4.0/carbonite-1.4.0.pom from clojars
Retrieving com/esotericsoftware/kryo/kryo/2.21/kryo-2.21.pom from central
Retrieving com/esotericsoftware/reflectasm/reflectasm/1.07/reflectasm-1.07.pom from central
Retrieving org/ow2/asm/asm/4.0/asm-4.0.pom from central
Retrieving org/ow2/asm/asm-parent/4.0/asm-parent-4.0.pom from central
Retrieving org/ow2/ow2/1.3/ow2-1.3.pom from central
Retrieving com/esotericsoftware/minlog/minlog/1.2/minlog-1.2.pom from central
Retrieving org/objenesis/objenesis/1.2/objenesis-1.2.pom from central
Retrieving org/objenesis/objenesis-parent/1.2/objenesis-parent-1.2.pom from central
Retrieving com/twitter/chill-java/0.3.5/chill-java-0.3.5.pom from central
Retrieving org/yaml/snakeyaml/1.11/snakeyaml-1.11.pom from central
Retrieving commons-logging/commons-logging/1.1.3/commons-logging-1.1.3.pom from central
Retrieving org/apache/commons/commons-parent/28/commons-parent-28.pom from central
Retrieving org/apache/apache/13/apache-13.pom from central
Retrieving com/googlecode/disruptor/disruptor/2.10.1/disruptor-2.10.1.pom from central
Retrieving org/jgrapht/jgrapht-core/0.9.0/jgrapht-core-0.9.0.pom from central
Retrieving org/jgrapht/jgrapht/0.9.0/jgrapht-0.9.0.pom from central
Retrieving ch/qos/logback/logback-classic/1.0.13/logback-classic-1.0.13.pom from central
Retrieving ch/qos/logback/logback-parent/1.0.13/logback-parent-1.0.13.pom from central
Retrieving ch/qos/logback/logback-core/1.0.13/logback-core-1.0.13.pom from central
Retrieving org/slf4j/slf4j-api/1.7.5/slf4j-api-1.7.5.pom from central
Retrieving org/slf4j/slf4j-parent/1.7.5/slf4j-parent-1.7.5.pom from central
Retrieving org/slf4j/log4j-over-slf4j/1.6.6/log4j-over-slf4j-1.6.6.pom from central
Retrieving org/slf4j/slf4j-parent/1.6.6/slf4j-parent-1.6.6.pom from central
Retrieving org/slf4j/slf4j-api/1.6.6/slf4j-api-1.6.6.pom from central
Retrieving jline/jline/2.11/jline-2.11.pom from central
Retrieving com/parsely/streamparse/0.0.4-SNAPSHOT/streamparse-0.0.4-20160314.185928-7.pom from clojars
Retrieving org/clojure/data.json/0.2.6/data.json-0.2.6.pom from central
Retrieving org/apache/storm/storm-core/0.9.4/storm-core-0.9.4.pom from central
Retrieving org/apache/storm/storm/0.9.4/storm-0.9.4.pom from central
Retrieving org/clojure/tools.nrepl/0.2.12/tools.nrepl-0.2.12.pom from central
Retrieving clojure-complete/clojure-complete/0.2.4/clojure-complete-0.2.4.pom from clojars
Retrieving org/apache/storm/storm-core/0.9.5/storm-core-0.9.5.jar from central
Retrieving org/clojure/clojure/1.5.1/clojure-1.5.1.jar from central
Retrieving joda-time/joda-time/2.0/joda-time-2.0.jar from central
Retrieving org/clojure/core.incubator/0.1.0/core.incubator-0.1.0.jar from central
Retrieving org/clojure/tools.macro/0.1.0/tools.macro-0.1.0.jar from central
Retrieving commons-fileupload/commons-fileupload/1.2.1/commons-fileupload-1.2.1.jar from central
Retrieving javax/servlet/servlet-api/2.5/servlet-api-2.5.jar from central
Retrieving org/mortbay/jetty/jetty/6.1.26/jetty-6.1.26.jar from central
Retrieving org/mortbay/jetty/jetty-util/6.1.26/jetty-util-6.1.26.jar from central
Retrieving org/clojure/tools.logging/0.2.3/tools.logging-0.2.3.jar from central
Retrieving org/clojure/math.numeric-tower/0.0.1/math.numeric-tower-0.0.1.jar from central
Retrieving org/clojure/tools.cli/0.2.4/tools.cli-0.2.4.jar from central
Retrieving commons-io/commons-io/2.4/commons-io-2.4.jar from central
Retrieving org/apache/commons/commons-exec/1.1/commons-exec-1.1.jar from central
Retrieving commons-lang/commons-lang/2.5/commons-lang-2.5.jar from central
Retrieving com/googlecode/json-simple/json-simple/1.1/json-simple-1.1.jar from central
Retrieving com/esotericsoftware/reflectasm/reflectasm/1.07/reflectasm-1.07-shaded.jar from central
Retrieving com/esotericsoftware/kryo/kryo/2.21/kryo-2.21.jar from central
Retrieving org/ow2/asm/asm/4.0/asm-4.0.jar from central
Retrieving com/esotericsoftware/minlog/minlog/1.2/minlog-1.2.jar from central
Retrieving org/objenesis/objenesis/1.2/objenesis-1.2.jar from central
Retrieving com/twitter/chill-java/0.3.5/chill-java-0.3.5.jar from central
Retrieving org/yaml/snakeyaml/1.11/snakeyaml-1.11.jar from central
Retrieving commons-logging/commons-logging/1.1.3/commons-logging-1.1.3.jar from central
Retrieving commons-codec/commons-codec/1.6/commons-codec-1.6.jar from central
Retrieving com/googlecode/disruptor/disruptor/2.10.1/disruptor-2.10.1.jar from central
Retrieving org/jgrapht/jgrapht-core/0.9.0/jgrapht-core-0.9.0.jar from central
Retrieving ch/qos/logback/logback-classic/1.0.13/logback-classic-1.0.13.jar from central
Retrieving ch/qos/logback/logback-core/1.0.13/logback-core-1.0.13.jar from central
Retrieving org/slf4j/slf4j-api/1.7.5/slf4j-api-1.7.5.jar from central
Retrieving org/slf4j/log4j-over-slf4j/1.6.6/log4j-over-slf4j-1.6.6.jar from central
Retrieving jline/jline/2.11/jline-2.11.jar from central
Retrieving org/clojure/data.json/0.2.6/data.json-0.2.6.jar from central
Retrieving org/clojure/tools.nrepl/0.2.12/tools.nrepl-0.2.12.jar from central
Retrieving clj-time/clj-time/0.4.1/clj-time-0.4.1.jar from clojars
Retrieving compojure/compojure/1.1.3/compojure-1.1.3.jar from clojars
Retrieving clout/clout/1.0.1/clout-1.0.1.jar from clojars
Retrieving ring/ring-devel/0.3.11/ring-devel-0.3.11.jar from clojars
Retrieving hiccup/hiccup/0.3.6/hiccup-0.3.6.jar from clojars
Retrieving ring/ring-core/1.1.5/ring-core-1.1.5.jar from clojars
Retrieving clj-stacktrace/clj-stacktrace/0.2.2/clj-stacktrace-0.2.2.jar from clojars
Retrieving ring/ring-jetty-adapter/0.3.11/ring-jetty-adapter-0.3.11.jar from clojars
Retrieving ring/ring-servlet/0.3.11/ring-servlet-0.3.11.jar from clojars
Retrieving com/twitter/carbonite/1.4.0/carbonite-1.4.0.jar from clojars
Retrieving com/parsely/streamparse/0.0.4-SNAPSHOT/streamparse-0.0.4-20160314.185928-7.jar from clojars
Retrieving clojure-complete/clojure-complete/0.2.4/clojure-complete-0.2.4.jar from clojars



[root@ip-172-31-57-217 EX2Tweetwordcount]# pwd
/root/EX2Tweetwordcount
[root@ip-172-31-57-217 EX2Tweetwordcount]# cd topologies
[root@ip-172-31-57-217 topologies]# ls
tweetwordcount.clj
[root@ip-172-31-57-217 topologies]# vi tweetwordcount.clj
[root@ip-172-31-57-217 topologies]# cd ..
[root@ip-172-31-57-217 EX2Tweetwordcount]# cd src/bolts
[root@ip-172-31-57-217 bolts]# ls
__init__.py  parse.py  wordcount.py
[root@ip-172-31-57-217 bolts]# cd ..
[root@ip-172-31-57-217 src]# cd ..
[root@ip-172-31-57-217 EX2Tweetwordcount]# vi finalresults.py
[root@ip-172-31-57-217 EX2Tweetwordcount]# vi histogram.py
[root@ip-172-31-57-217 EX2Tweetwordcount]# vi finalresults.py
[root@ip-172-31-57-217 EX2Tweetwordcount]# vi histogram.py
[root@ip-172-31-57-217 EX2Tweetwordcount]# git *.py  push https://github.com/al-arsenault/exercise_2
git: 'create_table.py' is not a git command. See 'git --help'.
[root@ip-172-31-57-217 EX2Tweetwordcount]# git push *.py https://github.com/al-arsenault/exercies_2
fatal: Not a git repository (or any of the parent directories): .git
[root@ip-172-31-57-217 EX2Tweetwordcount]# git push https://github.com/al-arsenault/exercise_2 *.py
fatal: Not a git repository (or any of the parent directories): .git
[root@ip-172-31-57-217 EX2Tweetwordcount]# git add .
fatal: Not a git repository (or any of the parent directories): .git
[root@ip-172-31-57-217 EX2Tweetwordcount]# git clone https://github.com/al-arsenault/exercise_2
Initialized empty Git repository in /root/EX2Tweetwordcount/exercise_2/.git/
remote: Counting objects: 13, done.
remote: Compressing objects: 100% (9/9), done.
remote: Total 13 (delta 3), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (13/13), done.
[root@ip-172-31-57-217 EX2Tweetwordcount]# cd exercise_2/.git
[root@ip-172-31-57-217 .git]# cp ../../*.py
cp: target `../../Twittercredentials.py' is not a directory
[root@ip-172-31-57-217 .git]# cd ..
[root@ip-172-31-57-217 exercise_2]# cd ..
[root@ip-172-31-57-217 EX2Tweetwordcount]# pwd
/root/EX2Tweetwordcount
[root@ip-172-31-57-217 EX2Tweetwordcount]# ls
_build                   histogram.py       tasks.py
config.json              logs               topologies
create_table.py          project.clj        Twittercredentials.py
exercise_2               psycopg-sample.py  Twittercredentials.pyc
fabfile.py               README.md          virtualenvs
finalresults.py          _resources
hello-stream-twitter.py  src
[root@ip-172-31-57-217 EX2Tweetwordcount]# cp *.py exercise_2/.git
[root@ip-172-31-57-217 EX2Tweetwordcount]# cd exercise_2/.git
[root@ip-172-31-57-217 .git]# ls
branches         finalresults.py          index        psycopg-sample.py
config           HEAD                     info         refs
create_table.py  hello-stream-twitter.py  logs         tasks.py
description      histogram.py             objects      Twittercredentials.py
fabfile.py       hooks                    packed-refs
[root@ip-172-31-57-217 .git]# git add .
fatal: This operation must be run in a work tree
[root@ip-172-31-57-217 .git]# cd ..
[root@ip-172-31-57-217 exercise_2]# mv .git/*.py 
mv: target `.git/Twittercredentials.py' is not a directory
[root@ip-172-31-57-217 exercise_2]# ls
Architecture  README.md  screenshots
[root@ip-172-31-57-217 exercise_2]# cd .git
[root@ip-172-31-57-217 .git]# ls
branches         finalresults.py          index        psycopg-sample.py
config           HEAD                     info         refs
create_table.py  hello-stream-twitter.py  logs         tasks.py
description      histogram.py             objects      Twittercredentials.py
fabfile.py       hooks                    packed-refs
[root@ip-172-31-57-217 .git]# mv *.py ..
[root@ip-172-31-57-217 .git]# cd ..
[root@ip-172-31-57-217 exercise_2]# ls
Architecture     hello-stream-twitter.py  screenshots
create_table.py  histogram.py             tasks.py
fabfile.py       psycopg-sample.py        Twittercredentials.py
finalresults.py  README.md
[root@ip-172-31-57-217 exercise_2]# git add .
[root@ip-172-31-57-217 exercise_2]# git commit -m "First commit"
[master e198c0a] First commit
 Committer: root <root@ip-172-31-57-217.ec2.internal>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

If the identity used for this commit is wrong, you can fix it with:

    git commit --amend --author='Your Name <you@example.com>'

 8 files changed, 216 insertions(+), 0 deletions(-)
 create mode 100644 Twittercredentials.py
 create mode 100644 create_table.py
 create mode 100644 fabfile.py
 create mode 100644 finalresults.py
 create mode 100644 hello-stream-twitter.py
 create mode 100644 histogram.py
 create mode 100644 psycopg-sample.py
 create mode 100644 tasks.py
[root@ip-172-31-57-217 exercise_2]# git push origin master
error: The requested URL returned error: 403 Forbidden while accessing https://github.com/al-arsenault/exercise_2/info/refs

fatal: HTTP request failed
[root@ip-172-31-57-217 exercise_2]# git bash
git: 'bash' is not a git command. See 'git --help'.

Did you mean this?
	stash
[root@ip-172-31-57-217 exercise_2]# ssh-keygen -t rsa -b 4096 -C a.arsenault81@gmail.com
Generating public/private rsa key pair.
Enter file in which to save the key (/root/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /root/.ssh/id_rsa.
Your public key has been saved in /root/.ssh/id_rsa.pub.
The key fingerprint is:
27:df:37:12:8d:0f:f6:b9:18:28:c8:5e:aa:a7:1a:62 a.arsenault81@gmail.com
The key's randomart image is:
+--[ RSA 4096]----+
|                 |
|                 |
|                 |
|             o   |
|        S . = .  |
|     . . + + = . |
|.E.   o o o + *  |
|.. . ..o .   = o |
|  ..o+o     . .  |
+-----------------+
[root@ip-172-31-57-217 exercise_2]# eval "$(ssh-agent -s)"
Agent pid 6869
[root@ip-172-31-57-217 exercise_2]# ssh-add ~/.ssh/id_rsa
Identity added: /root/.ssh/id_rsa (/root/.ssh/id_rsa)
[root@ip-172-31-57-217 exercise_2]# clip < ~/.ssh/id_rsa.pub
-bash: clip: command not found
[root@ip-172-31-57-217 exercise_2]# cd /root/.ssh
[root@ip-172-31-57-217 .ssh]# ls
authorized_keys      dan_oracle_mbp.pub   id_rsa
dan_mcclary_mba.pub  Exercise_2_keys.pub  id_rsa.pub
[root@ip-172-31-57-217 .ssh]# vi id_rsa.pub
[root@ip-172-31-57-217 .ssh]# cd /root/EX2*
[root@ip-172-31-57-217 EX2Tweetwordcount]# ls
_build                   histogram.py       tasks.py
config.json              logs               topologies
create_table.py          project.clj        Twittercredentials.py
exercise_2               psycopg-sample.py  Twittercredentials.pyc
fabfile.py               README.md          virtualenvs
finalresults.py          _resources
hello-stream-twitter.py  src
[root@ip-172-31-57-217 EX2Tweetwordcount]# cd exercise_2
[root@ip-172-31-57-217 exercise_2]# 
[root@ip-172-31-57-217 exercise_2]# ls
Architecture     hello-stream-twitter.py  screenshots
create_table.py  histogram.py             tasks.py
fabfile.py       psycopg-sample.py        Twittercredentials.py
finalresults.py  README.md
[root@ip-172-31-57-217 exercise_2]# git add .
[root@ip-172-31-57-217 exercise_2]# git commit -m "First Commit"
# On branch master
# Your branch is ahead of 'origin/master' by 1 commit.
#
nothing to commit (working directory clean)
[root@ip-172-31-57-217 exercise_2]# git push origin master
error: The requested URL returned error: 403 Forbidden while accessing https://github.com/al-arsenault/exercise_2/info/refs

fatal: HTTP request failed
[root@ip-172-31-57-217 exercise_2]# git push origin master
error: The requested URL returned error: 403 Forbidden while accessing https://github.com/al-arsenault/exercise_2/info/refs

fatal: HTTP request failed
[root@ip-172-31-57-217 exercise_2]# git push origin
error: The requested URL returned error: 403 Forbidden while accessing https://github.com/al-arsenault/exercise_2/info/refs

fatal: HTTP request failed
[root@ip-172-31-57-217 exercise_2]# ls
Architecture     hello-stream-twitter.py  screenshots
create_table.py  histogram.py             tasks.py
fabfile.py       psycopg-sample.py        Twittercredentials.py
finalresults.py  README.md
[root@ip-172-31-57-217 exercise_2]# cd ..
[root@ip-172-31-57-217 EX2Tweetwordcount]# rm exercise_2
rm: cannot remove `exercise_2': Is a directory
[root@ip-172-31-57-217 EX2Tweetwordcount]# git clone https://github.com/al-arsenault
Initialized empty Git repository in /root/EX2Tweetwordcount/al-arsenault/.git/
error: The requested URL returned error: 403 Forbidden while accessing https://github.com/al-arsenault/info/refs

fatal: HTTP request failed
[root@ip-172-31-57-217 EX2Tweetwordcount]# cd root
-bash: cd: root: No such file or directory
[root@ip-172-31-57-217 EX2Tweetwordcount]# cd ..
[root@ip-172-31-57-217 ~]# mkdir trial
[root@ip-172-31-57-217 ~]# cd trial
[root@ip-172-31-57-217 trial]# git clone https://github.com/al-arsenault/exercise_2
Initialized empty Git repository in /root/trial/exercise_2/.git/
remote: Counting objects: 13, done.
remote: Compressing objects: 100% (9/9), done.
remote: Total 13 (delta 3), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (13/13), done.
[root@ip-172-31-57-217 trial]# cp /root/EX2Tweetcount/exercise_2/*.py 
cp: missing destination file operand after `/root/EX2Tweetcount/exercise_2/*.py'
Try `cp --help' for more information.
[root@ip-172-31-57-217 trial]# cp /root/EX2Tweetcount/exercise_2/*.py *
cp: cannot stat `/root/EX2Tweetcount/exercise_2/*.py': No such file or directory
[root@ip-172-31-57-217 trial]# cd /root/EX2Tweetcount/exercise_2
-bash: cd: /root/EX2Tweetcount/exercise_2: No such file or directory
[root@ip-172-31-57-217 trial]# cd /root
[root@ip-172-31-57-217 ~]# cd EX2*
[root@ip-172-31-57-217 EX2Tweetwordcount]# cd /root/trial
[root@ip-172-31-57-217 trial]# cp /root/EX2Tweetwordcount/exercise_2/* 
cp: target `/root/EX2Tweetwordcount/exercise_2/Twittercredentials.py' is not a directory
[root@ip-172-31-57-217 trial]# ls
exercise_2
[root@ip-172-31-57-217 trial]# cd exercise_2
[root@ip-172-31-57-217 exercise_2]# ls
Architecture  README.md  screenshots
[root@ip-172-31-57-217 exercise_2]# cp /root/EX2Tweetwordcount/exercise_2/* 
cp: target `/root/EX2Tweetwordcount/exercise_2/Twittercredentials.py' is not a directory
[root@ip-172-31-57-217 exercise_2]# ls
Architecture  README.md  screenshots
[root@ip-172-31-57-217 exercise_2]# man cp
Formatting page, please wait...
[root@ip-172-31-57-217 exercise_2]# cd ..
[root@ip-172-31-57-217 trial]# cop /root/EX2Tweetwordcount/exercise_2/* exercise_2
-bash: cop: command not found
[root@ip-172-31-57-217 trial]# cp /root/EX2Tweetwordcount/exercise_2/* exercise_2
cp: omitting directory `/root/EX2Tweetwordcount/exercise_2/Architecture'
cp: omitting directory `/root/EX2Tweetwordcount/exercise_2/screenshots'
[root@ip-172-31-57-217 trial]# cd exercise_2
[root@ip-172-31-57-217 exercise_2]# ls
Architecture     hello-stream-twitter.py  screenshots
create_table.py  histogram.py             tasks.py
fabfile.py       psycopg-sample.py        Twittercredentials.py
finalresults.py  README.md
[root@ip-172-31-57-217 exercise_2]# git add .
[root@ip-172-31-57-217 exercise_2]# git commit -m "Second commit"
[master 2716551] Second commit
 Committer: root <root@ip-172-31-57-217.ec2.internal>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:

    git config --global user.name "Your Name"
    git config --global user.email you@example.com

If the identity used for this commit is wrong, you can fix it with:

    git commit --amend --author='Your Name <you@example.com>'

 8 files changed, 216 insertions(+), 0 deletions(-)
 create mode 100644 Twittercredentials.py
 create mode 100644 create_table.py
 create mode 100644 fabfile.py
 create mode 100644 finalresults.py
 create mode 100644 hello-stream-twitter.py
 create mode 100644 histogram.py
 create mode 100644 psycopg-sample.py
 create mode 100644 tasks.py
[root@ip-172-31-57-217 exercise_2]# git push origin master
error: The requested URL returned error: 403 Forbidden while accessing https://github.com/al-arsenault/exercise_2/info/refs

fatal: HTTP request failed
[root@ip-172-31-57-217 exercise_2]# cd /root/EX2T*
[root@ip-172-31-57-217 EX2Tweetwordcount]# ls
_build                   histogram.py       tasks.py
config.json              logs               topologies
create_table.py          project.clj        Twittercredentials.py
exercise_2               psycopg-sample.py  Twittercredentials.pyc
fabfile.py               README.md          virtualenvs
finalresults.py          _resources
hello-stream-twitter.py  src
[root@ip-172-31-57-217 EX2Tweetwordcount]# vi Twittercredentials.py
[root@ip-172-31-57-217 EX2Tweetwordcount]# 
