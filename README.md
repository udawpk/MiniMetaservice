What is it?
=======================
Simple rest service.

Returns files by request.
Files locate in conf/SomeDir/Some.file

If conf/SomeDir contain file `authKey` (`conf/SomeDir/authKey`), authentication key from `authKey` file is requered for access to `conf/SomeDir`

Example requests:
----------------------
     htttp://metaservice.host:PORT/SomeDir/Some.file - with no authKey
     htttp://metaservice.host:PORT/SomeDir/Some.file/someSecretKey - with authKey
