#!/usr/bin/env python3
"""Package HP 50g User RPL source as a .49G string object.

Based on the x50ng HP 50g testing project's binary string-object builder.
Input must be encoded using the calculator's 8-bit character encoding;
ASCII source without special glyphs is supported directly.
"""
import argparse
from pathlib import Path

def pack_string(data: bytes) -> bytes:
    nibbles = []
    def append_five(value):
        nibbles.extend((value >> (4 * i)) & 15 for i in range(5))
    append_five(0x02A2C)
    append_five(5 + len(data) * 2)
    for byte in data:
        nibbles.extend((byte & 15, byte >> 4))
    if len(nibbles) % 2:
        nibbles.append(0)
    return b"HPHP49-C" + bytes(
        nibbles[i] | (nibbles[i + 1] << 4)
        for i in range(0, len(nibbles), 2)
    )

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path, help="Input file in HP 50g-compatible 8-bit encoding")
    parser.add_argument("output", type=Path, help="Output .49G string object")
    args = parser.parse_args()
    args.output.write_bytes(pack_string(args.source.read_bytes()))
    print(f"Wrote {args.output}")

if __name__ == "__main__":
    main()
