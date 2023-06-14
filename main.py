import argparse
import logging
import logging.handlers
import os

from SandboxOptionsParser import OptionsParsingMode, SandboxOptionsParser

handler = logging.handlers.RotatingFileHandler(
    filename='./parser.log',
    encoding='utf-8',
    backupCount=1,
)
dt_fmt = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter('{asctime} {levelname:<8} {name}: {message}', dt_fmt, style='{')
handler.setFormatter(formatter)

log = logging.getLogger("Main")
log.setLevel(logging.INFO)
log.addHandler(handler)
consoleHandler = logging.StreamHandler()

consoleHandler.setFormatter(formatter)
log.addHandler(consoleHandler)

argp = argparse.ArgumentParser()
argp.add_argument("--file", "--bin", "-f", "-b", dest="sandbox_file", required=True, help="With --dump: The path the the map_sand.bin files. With --save: The path to the modified map_sand.json file.")
argp.add_argument("--output", "-o", dest="sand_out", default="map_sand.bin", help="The output file name for the saved map_sand.bin file. Defaults to map_sand.bin. No effect if --dump is specified.")
argp.add_argument("--dump", "-d", action="store_true", dest="is_dump", help="Are we DUMPING the map_sand.bin file (ie. making it editable)?")
argp.add_argument("--save", "-s", action="store_true", dest="is_save", help="Are we SAVING the map_sand.bin file (ie. making it usable by the game)?")
argp.add_argument("--worldversion", "--forceworldversion", "-fwv", dest="world_version", default=195, type=int, help="Force the world version for the file to be a specific value. DO NOT USE THIS UNLESS YOU KNOW WHAT YOU'RE DOING.")
argp.add_argument("--sandboxversion", "--forcesandboxversion", "-fsv", dest="sandbox_version", default=5, type=int, help="Force the sandbox version for the file to be a specific value. DO NOT USE THIS UNLESS YOU KNOW WHAT YOU'RE DOING.")
argp.add_argument("--verbose", action="store_true", dest="verbose", help="Enabled version (debug) logging")
argp.add_argument("--getversion", "--getfileversion", action="store_true", dest="should_test_version", help="Check the world and sandbox versions of the provided map_sand.bin file. Useful if you need to export for an older/newer game version.")

args: argparse.Namespace = argp.parse_args()

if args.verbose:
    log.setLevel(logging.DEBUG)

MAP_SAND: str = args.sandbox_file
DUMPING = args.is_dump
SAVING = args.is_save
OUTPUT_NAME = os.path.join("./output/", args.sand_out)

VERSION_ONLY = args.should_test_version

if VERSION_ONLY:
    parser: SandboxOptionsParser = SandboxOptionsParser(mode=OptionsParsingMode.GET_VERSION, file=MAP_SAND, output=OUTPUT_NAME, _logger=log, argv=args)
    parser.getVersion()

if DUMPING and SAVING:
    log.error("Attempted to read and write map_sand.bin file at the same time")
    raise RuntimeError("Cannot dump and save map_sand.bin at the same time (that would be pointless)")

if DUMPING:
    log.info("Parsing map_sand file from file '%s'...", MAP_SAND)
    parser: SandboxOptionsParser = SandboxOptionsParser(mode=OptionsParsingMode.DUMP, file=MAP_SAND, output=OUTPUT_NAME, _logger=log, argv=args)
    parser.dump()

if SAVING:
    log.info("Writing map_sand file to file '%s'...", OUTPUT_NAME)
    parser: SandboxOptionsParser = SandboxOptionsParser(mode=OptionsParsingMode.SAVE, file=MAP_SAND, output=OUTPUT_NAME, _logger=log, argv=args)
    parser.save()
