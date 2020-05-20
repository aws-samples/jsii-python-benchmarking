# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

from hello_world import hello_world

def my_function():
    hw = hello_world.HelloWorld()
    print(hw.say_hello('World'))
    for i in range(0, 25):
        print(str(i) + ': ' + str(hw.fibonacci(i)))
