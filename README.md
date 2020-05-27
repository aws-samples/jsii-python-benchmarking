# jsii-python-benchmarking

> Benchmark jsii Python module vs native counterpart

## Benchmark native Python [![](https://img.shields.io/pypi/v/aws-jsiisamples.jsii-native-python)](https://pypi.org/project/aws-jsiisamples.jsii-native-python/)

1. run `cd native-python`
2. run `pip install -r requirements.txt`
3. run `python -m timeit "import benchmark; benchmark.my_function()"`

native module timeit results:

1. From an AWS Workspaces VM with 4 Cores and 8 GiB RAM running Windows 10 (and Ubuntu 19.10 WSL).

```text
2000 loops, best of 5: 117 usec per loop
```

2. From a 2019 MacBook Pro with 2.8 GHz Intel Core i7 and 16GiB RAM running macOS Mojave.

```text
5000 loops, best of 5: 69.4 usec per loop
```

## Benchmark jsii Python [![](https://img.shields.io/pypi/v/aws_jsiisamples.jsii_code_samples)](https://pypi.org/project/aws-jsiisamples.jsii-code-samples/)

1. run `cd jsii-python`
2. run `pip install -r requirements.txt`
3. run `python -m timeit "import benchmark; benchmark.my_function()"`

jsii module timeit results:

1. From an AWS Workspaces VM with 4 Cores and 8 GiB RAM running Windows 10 (and Ubuntu 19.10 WSL).

```text
1 loop, best of 5: 14 msec per loop
```

2. From a 2019 MacBook Pro with 2.8 GHz Intel Core i7 and 16GiB RAM running macOS Mojave.

```text
50 loops, best of 5: 6.7 msec per loop
```

P.S.:  Thanks to [this detailed article](https://www.blog.pythonlibrary.org/2016/05/24/python-101-an-intro-to-benchmarking-your-code/) for the help with benchmarking Python code

## License

This library is licensed under the MIT-0 License. See the LICENSE file.
