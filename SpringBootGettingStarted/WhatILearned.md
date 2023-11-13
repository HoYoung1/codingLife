# What I Learned Today

- target : The target directory is used to house all output of the build.

https://maven.apache.org/guides/introduction/introduction-to-the-standard-directory-layout.html

- classpath :  https://en.wikipedia.org/wiki/Classpath


## Maven

```bash
$ mvn dependency:tree

$ mvn spring-boot:run
```


### groupId, artifactId, version

For exmaple : 

```xml
    <groupId>com.example</groupId>
    <artifactId>myproject</artifactId>
    <version>0.0.1-SNAPSHOT</version>
```

Meaning : https://maven.apache.org/guides/mini/guide-naming-conventions.html

## Gradle 

```bash
$ gradle init

$ gradle dependencies

```

## Spring Cli

```bash
$ spring init --build=maven --dependencies=web my-project
```