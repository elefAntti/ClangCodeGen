# Code generation with libClang


Generates visitor code automatically for structs. Can be used eg. for serialization

Example:

```C++
VisitStruct(my_struct, [](const char* name, auto& data){ 
	std::cout << name << ": " << data << std::endl;
});
```

## How to use

Build the Docker image with

```
./build_docker.sh
```

Run code generator inside Docker

```
./run_docker.sh /app/gen_struct.py /app/data/example.h /app/data/output.h
```

Dump the AST for debug purposes

```
./run_docker.sh /app/dump.py /app/data/example.h
```

