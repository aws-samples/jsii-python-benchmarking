# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

from aws_jsiisamples.jsii_code_samples import *


def my_function():
    hw = HelloWorld()
    print(hw.say_hello('World'))
    for i in range(0, 25):
        print(str(i) + ': ' + str(hw.fibonacci(i)))
