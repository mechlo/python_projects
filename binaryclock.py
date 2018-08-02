#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time


# Hide cursor to eliminate artifacts
cursor.hide()


def hours(hrs1, hrs2):
    display = cr.Fore.RED

    h_10 = cr.Cursor.POS(5, 13)    # 0
    h_11 = cr.Cursor.POS(5, 11)    # 2^0
    h_12 = cr.Cursor.POS(5, 9)     # 2^1

    h_00 = cr.Cursor.POS(8, 13)    # 0
    h_01 = cr.Cursor.POS(8, 11)    # 2^0
    h_02 = cr.Cursor.POS(8, 9)     # 2^1
    h_04 = cr.Cursor.POS(8, 7)     # 2^2
    h_08 = cr.Cursor.POS(8, 5)     # 2^3

    # Hours 10's
    if hrs1 == "0":
        print(display + h_10 + "0")
    if hrs1 == "1":
        print(display + h_11 + "1")
    if hrs1 == "2":
        print(display + h_12 + "2")

    # Hours units
    if hrs2 == "0":
        print(display + h_00 + "0")
    if hrs2 == "1":
        print(display + h_01 + "1")
    if hrs2 == "2":
        print(display + h_02 + "2")
    if hrs2 == "3":
        print(display + h_01 + "1")
        print(display + h_02 + "2")
    if hrs2 == "4":
        print(display + h_04 + "4")
    if hrs2 == "5":
        print(display + h_01 + "1")
        print(display + h_04 + "4")
    if hrs2 == "6":
        print(display + h_02 + "2")
        print(display + h_04 + "4")
    if hrs2 == "7":
        print(display + h_01 + "1")
        print(display + h_02 + "2")
        print(display + h_04 + "4")
    if hrs2 == "8":
        print(display + h_08 + "8")
    if hrs2 == "9":
        print(display + h_01 + "1")
        print(display + h_08 + "8")

    return


def minutes(min1, min2):
    display = cr.Fore.RED

    m_10 = cr.Cursor.POS(13, 13)   # 0
    m_11 = cr.Cursor.POS(13, 11)   # 2^0
    m_12 = cr.Cursor.POS(13, 9)    # 2^1
    m_13 = cr.Cursor.POS(13, 7)    # 2^2

    m_00 = cr.Cursor.POS(16, 13)   # 0
    m_01 = cr.Cursor.POS(16, 11)   # 2^0
    m_02 = cr.Cursor.POS(16, 9)    # 2^1
    m_04 = cr.Cursor.POS(16, 7)    # 2^2
    m_08 = cr.Cursor.POS(16, 5)    # 2^3

    # Minutes 10's
    if min1 == "0":
        print(display + m_10 + "0")
    if min1 == "1":
        print(display + m_11 + "1")
    if min1 == "2":
        print(display + m_12 + "2")
    if min1 == "3":
        print(display + m_11 + "1")
        print(display + m_12 + "2")
    if min1 == "4":
        print(display + m_13 + "4")
    if min1 == "5":
        print(display + m_11 + "1")
        print(display + m_13 + "4")

    # Minutes units
    if min2 == "0":
        print(display + m_00 + "0")
    if min2 == "1":
        print(display + m_01 + "1")
    if min2 == "2":
        print(display + m_02 + "2")
    if min2 == "3":
        print(display + m_01 + "1")
        print(display + m_02 + "2")
    if min2 == "4":
        print(display + m_04 + "4")
    if min2 == "5":
        print(display + m_01 + "1")
        print(display + m_04 + "4")
    if min2 == "6":
        print(display + m_02 + "2")
        print(display + m_04 + "4")
    if min2 == "7":
        print(display + m_01 + "1")
        print(display + m_02 + "2")
        print(display + m_04 + "4")
    if min2 == "8":
        print(display + m_08 + "8")
    if min2 == "9":
        print(display + m_01 + "1")
        print(display + m_08 + "8")

    return


def seconds(sec1, sec2):
    display = cr.Fore.RED

    s_10 = cr.Cursor.POS(21, 13)    # 0
    s_11 = cr.Cursor.POS(21, 11)    # 2^0
    s_12 = cr.Cursor.POS(21, 9)     # 2^1
    s_13 = cr.Cursor.POS(21, 7)     # 2^2

    s_00 = cr.Cursor.POS(24, 13)    # 0
    s_01 = cr.Cursor.POS(24, 11)    # 2^0
    s_02 = cr.Cursor.POS(24, 9)     # 2^1
    s_04 = cr.Cursor.POS(24, 7)     # 2^2
    s_08 = cr.Cursor.POS(24, 5)     # 2^3

    # Seconds 10's
    if sec1 == "0":
        print(display + s_10 + "0")
    if sec1 == "1":
        print(display + s_11 + "1")
    if sec1 == "2":
        print(display + s_12 + "2")
    if sec1 == "3":
        print(display + s_11 + "1")
        print(display + s_12 + "2")
    if sec1 == "4":
        print(display + s_13 + "4")
    if sec1 == "5":
        print(display + s_11 + "1")
        print(display + s_13 + "4")

    # Seconds units
    if sec2 == "0":
        print(display + s_00 + "0")
    if sec2 == "1":
        print(display + s_01 + "1")
    if sec2 == "2":
        print(display + s_02 + "2")
    if sec2 == "3":
        print(display + s_01 + "1")
        print(display + s_02 + "2")
    if sec2 == "4":
        print(display + s_04 + "4")
    if sec2 == "5":
        print(display + s_01 + "1")
        print(display + s_04 + "4")
    if sec2 == "6":
        print(display + s_02 + "2")
        print(display + s_04 + "4")
    if sec2 == "7":
        print(display + s_01 + "1")
        print(display + s_02 + "2")
        print(display + s_04 + "4")
    if sec2 == "8":
        print(display + s_08 + "8")
    if sec2 == "9":
        print(display + s_01 + "1")
        print(display + s_08 + "8")

    time.sleep(1)    # Needed to cut down "flicker" as best as possible

    return

##########################################


def main():
    try:
        for c in range(60):    # Currently set for 1 min. (1 hr = 3600, 24 hrs = 86400)
            os.system('cls' if os.name == 'nt' else 'clear')

            # Get current time: hours (24 hour clock), minutes, seconds) and put in a list
            t_now = [time.strftime("%H"), time.strftime("%M"), time.strftime("%S")]
            str_t = "".join(t_now)

            # Initialize and set some colors for colorama
            cr.init()
            off = cr.Back.BLACK
            on = cr.Fore.RED

            # Print Header
            tab = " " * 4
            print(off)
            print(on + tab + 'HRS' + tab + ' MIN' + tab + ' SEC' + "\n")

            # Run clock
            hours(str_t[0], str_t[1])
            minutes(str_t[2], str_t[3])
            seconds(str_t[4], str_t[5])
    except KeyboardInterrupt:
        print("\n" * 8)
        print("Program stopped")
        print(cr.deinit())
        cursor.show()  # Show cursor again
        exit(0)

    print("\n" * 8)
    print(cr.deinit())
    cursor.show()    # Show cursor again

if __name__ == "__main__":
    main()
