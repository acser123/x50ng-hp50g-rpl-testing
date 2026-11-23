# Source release candidate

This project packages modified x50ng emulator source and User RPL test tooling.

Upstream: https://codeberg.org/gwh/x50ng

The source archive was prepared locally, but **the complete modified emulator source has not yet been committed to this repository**. This repository is not a functional standalone release.

Firmware, ROM images, calculator runtime state, and prebuilt binaries are excluded. Obtain firmware separately from lawful sources.

The original local testing setup used RPN mode, virtual SD .49G string imports, →OBJ conversion, and keyboard-driven execution. Verified examples included `1 1 + = 2`, Fibonacci(15) = 610, and the NiMH battery tester 80 mOhm GOOD. These results do not constitute a clean-build test of a published source release.

Before a full public source release, review source and scripts for hard-coded private paths, third-party licenses, and reproducibility.
