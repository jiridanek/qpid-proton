# Development

Uses CFFI to wrap the c proton-core library.

Python c-extension development  

- the docs for extension development

- Install debug version of Python
- Use the [GDB Python integration](https://fedoraproject.org/wiki/Features/EasierPythonDebugging) (`py-bt`, ...)

## Fedora

The `python3-debuginfo` package contains the GDB integration.
In Fedora it would activate automatically when the package is installed.
Commands such as `py-bt` then become available.

```shell
sudo dnf debuginfo-install python3
```