## Finding Basic Buffer Overflow using Angr

Major reference: https://breaking-bits.gitbook.io/breaking-bits/vulnerability-discovery/automated-exploit-development/buffer-overflows

Permissions of binary can be checked by executing command ```checksec bug``` in the terminal window.
```
Canary   : No --> no stack cookie
NX       : Yes
PIE      : No --> address of all symbols remain the same (i.e. main()'s address will be same always on loading)
Fortify  : No
RelRO    : Partial
```
