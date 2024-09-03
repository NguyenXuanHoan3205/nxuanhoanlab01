# -*- coding: utf-8 -*-
"""
Created on Mon Sep 2 18:55:04 2024

@author: Nguyễn Xuân Hoan - 23694771
"""

def format_date(day, month, year):
    print(f"a. {day}/{month}/{year}")
    print(f"b. {day}/{month}/{year:02d}")
    print(f"c. {year}/{month}/{day}")
day=int(input("Nhap vao ngay sinh: "))
month=int(input("Nhap vao thang sinh: "))
year=int(input("Nhap vao nam sinh: "))
format_date(day, month, year)

    