# stub
import os.path
import shutil
import sys
import argparse
from argparse import BooleanOptionalAction, ArgumentParser
from email.policy import default

from src.ostools.systools import OSLabel, get_os
from PyInstaller import __main__ as pyinst

import platform

# TODO: maybe add flags for configuring the output directories and whatnot
# see https://pyinstaller.org/en/stable/usage.html

class Flags:
    """
    The flags that define how the building process should undergo.

    Script Arguments
    :param bool auto: Specifies whether the script should interactively prompt the user for each flag.
    :param bool clean: Deletes the build and dist cache folders.
    :param str target: Target file to pass to PyInstaller - either "release" (pesterchum.py), "dev" (__main__.py), or the path to a custom target.
    :param str output: Name of the executable to create.

    Legacy Arguments
    :param bool windowed:
    :param bool crt: Whether Universal CRT should be bundled with the build.
    :param bool upx_enabled: Whether the executable should be built with UPX (https://pyinstaller.org/en/stable/usage.html#using-upx).
    """

    #### Default arguments
    auto: bool = False
    clean: bool = True
    standalone: bool = False
    output: str = "pesterchum"
    target: str = "dev"


    #### Legacy flags - unused,
    windowed: bool = False ## seems to change nothing?
    upx_enabled: bool = False
    crt: bool = False


class PyinstData:
    FLAGS = Flags()

    arg_parser: ArgumentParser
    args: list[str]


PYINST_DATA = PyinstData()


def parse_args(data: PyinstData) -> None:

    args = argparse.ArgumentParser(
        description="Pesterchum Rewritten's build script to create an executable file.\n"
                    f"OS: {get_os().name.capitalize()} - [{platform.system()}, {platform.node()} @ {platform.release()}]",
        epilog="copyleft (c) 2026 maloryware - all wrongs reserved",
        formatter_class=argparse.RawTextHelpFormatter
    )

    args.add_argument(
        "-a", "--auto", default=data.FLAGS.auto, action=BooleanOptionalAction,
        help="Do not prompt for each build argument (aka non-interactive mode)."
    )
    args.add_argument(
        "-c", "--clean", default=data.FLAGS.clean, action=BooleanOptionalAction,
        help="Remove build+dist cache directories with shutil before building."
    )
    args.add_argument(
        "-t", "--target", default=data.FLAGS.target, action='store',
        help="Target .py file to pass to PyInstaller."
    )
    args.add_argument(
        "-o", "--output", default=data.FLAGS.output, action='store',
        help="Name of the executable to create."
    )
    args.add_argument(
        "-s", "--standalone", default=data.FLAGS.standalone, action=BooleanOptionalAction,
        help="Instead of a folder, create a single standalone executable."
    )
    ### Legacy ###
    # args.add_argument(
    #     "--windowed", default=data.FLAGS.windowed, action=BooleanOptionalAction,
    #     help="Build without console."
    # )
    # args.add_argument(
    #     "--crt", default=data.FLAGS.crt, action=BooleanOptionalAction,
    #     help="Try to bundle Universal CRT with the build"
    # )
    # args.add_argument(
    #     "-w", "--windowed", default=data.FLAGS.windowed, action=argparse.BooleanOptionalAction,
    #     help="Build without console."
    # )
    ##############

    args.parse_args(namespace=data.FLAGS)
    data.arg_parser = args

def build_flags(data: PyinstData) -> None:
    flags = data.FLAGS

    match flags.target:
        case "release": flags.target = "src/pesterchum.py"
        case "dev": flags.target = "src/__main__.py"

    if flags.output == "pesterchum" and get_os() in [OSLabel.WINDOWS, OSLabel.MACOS]:
            flags.output.capitalize()
    data.args = [
        f"{flags.target}", # Target file
        f"--name={flags.output}", # Executable name
        f"--icon={os.path.join("assets", "icon", "pesterchum.ico")}",
        "--clean",
    ]

    if flags.clean:
        data.args.append("-y")

    if flags.standalone:
        data.args.append("--onefile")
        for file in ["README.md", "LICENSE"]:
            data.args.append(f"--add-data {file}:.")
        data.args.append(f"--add-data assets:assets")
    else:
        data.args.append("--onedir")

    print("=== PyInstaller flags ===")
    print(data.args)
    print("=========================\n")


def append_data_files(data: PyinstData) -> None:
    if data.FLAGS.standalone: return
    print("finished building executable; copying assets...")
    for file in ["README.md", "LICENSE"]:
        shutil.copy(file, os.path.join("dist", f"{data.FLAGS.output}", file))
        print(f"- copied {file} to {os.path.join("dist", f"{data.FLAGS.output}", file)}")
    shutil.copytree("assets", os.path.join("dist", f"{data.FLAGS.output}", "assets"))
    print(f"- copied assets/ to {os.path.join("dist", f"{data.FLAGS.output}", "assets/")}")
    print("done!")


if __name__ == "__main__":
    print("Executing PyInstaller build...")
    parse_args(PYINST_DATA)

    # PYINST_DATA.arg_parser.print_help()
    # print()

    build_flags(PYINST_DATA)
    pyinst.run(PYINST_DATA.args)
    append_data_files(PYINST_DATA)
    # print(PYINST_DATA.args)
