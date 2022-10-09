#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 19:11:45 2021

@author: josephleighton
"""
import random
import math

def egcd(a, b):
    s, t = 1, 0
    x, y = 0, 1
    q, r = divmod(a, b)
    while r > 0:
        a, b = b, r
        o_x, o_y = x, y
        x, y = s - q*x, t - q*y
        s, t = o_x, o_y
        q, r = divmod(a, b)
    
    return b, x, y

def Pollard(n):
    """This is the main function of this project,
    it takes a number, and determines if it factors"""
    
    def F(x):
        return (x**2 + 1) % n
    
    p = 1
    l = 1
    
    T = random.randint(1, n-1)
    H = T
    d = 1
    
    while d == 1:
        if p == l:
            T = H
            p *= 2
            l = 0
        H = F(H)
        l += 1
        d = math.gcd(T - H, n)
    
    return d

def RSA_encrypt(m, e, n):
    """This is a function to test the given primes"""
    return pow(m, e, n)

def RSA_decrypt(c, d, n):
    """This is a function to test the given primes"""
    return pow(c, d, n)

def get_values():
    """"This is a function to calculate two prime numbers,
    and give you the primes, along with
    the corrisponding publc and private keys for RSA"""
    p = random.randint(2, 2**1023) * 2 - 1
    while p != Pollard(p):
        p = random.randint(2, 2**1023) * 2 - 1
    
    q = random.randint(2, 2**1023) * 2 - 1
    while q != Pollard(q):
        q = random.randint(2, 2**1023) * 2 - 1
    
    n = p*q
    phi = (p-1)*(q-1)
    
    e = random.randint(3, phi-1)
    N, d, X = egcd(e, phi)
    while N != 1:
        e = random.randint(3, phi-1)
        N, d, X = egcd(e, phi)
    
    if d <= 0:
        d = phi + d
    
    print('values for RSA encryption:')
    print('p: ' + str(p))
    print('q: ' + str(q))
    print('n: ' + str(n))
    print('e: ' + str(e))
    print('d: ' + str(d))