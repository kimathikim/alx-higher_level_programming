#!/usr/bin/python3
for i in range(48, 58):
    for j in range(48, 58):
        if j > i and i < 56:
            print(f"{i:c}{j:c}", end=", ")
print(f"{89}")
