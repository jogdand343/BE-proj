#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hotel as h
import predict as p
import tweetsFinal as t
x=input("Enter the City Name ")
d=int(input("Enter the week number "))
h.search(x)
p.predict(x,d)
t.tweetsFinal(x)