# Reimplemented mxos-cube as Python3
 
Reimplemented [MXCHIP](https://github.com/MXCHIP)'s mxos-cube as Python3. <br>
[MXCHIP](https://github.com/MXCHIP)'s mxos-cube can be found [here](https://github.com/MXCHIP/mxos-cube). <br>


## Introduction

MXOS cube is the name of the MXCHIP MXOS command-line tool for python3, packaged as `mxos-cube3`. 

MXOS Cube enables Git-based version control, dependencies management, code publishing, support for remotely hosted repositories, use of the MXCHIP MXOS build system and export functions and other operations.


## For Python2
[MXCHIP](https://github.com/MXCHIP)'s mxos-cube can be found [here](https://github.com/MXCHIP/mxos-cube).


## Command List
| Command | Description |
| --- | --- |
| `new` | Creates a new mxos program if executed within a non-program location. Alternatively creates a mico component if executed within an existing program. |
| `import` | Import program from URL |
| `add` | Add component from URL |
| `remove` | Remove component |
| `deploy` | Find and add missing components and source codes |
| `source` | Get the source code of one library |	 
| `publish` | Publish program or component |
| `update` | Update to branch, tag, revision or latest |
| `sync` | Synchronize mico component references |
| `ls` | View dependency tree |
| `status` | Show version control status |
| `make` | Make mico program/component |
| `config` | Tool configuration |
| `lib` | Compile library in current directory |
| `help` | Help screen |
| `upgrade` | Upgrade mxos-Cube |


## Example

Micoder Setting : <br>
```
d:\> mxos config --global MICODER D:\MiCoder
```

config list confirm : <br>
```
d:\> mxos config --list
```

compile : <br>
```
d:\> mxos make ....
```

# License
SPDX-License-Identifier: Apache-2.0

## Author
email : jams7777@gmail.com <br>
Github : [JiamSeo](https://github.com/jams777/) <br>
facebook : [Jiam Seo](https://www.facebook.com/jiam.seo) <br>
linkedin : [JIAM SEO](https://www.linkedin.com/in/jams777/) <br>

 