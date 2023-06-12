import json
import logging
import os
from argparse import Namespace
from enum import Enum
from typing import Union

from ParserHelpers import ByteBuffer
from PZParseExceptions import InvalidBinFileError


class OptionsParsingMode(Enum):
    DUMP = 0
    SAVE = 1
    GET_VERSION = 2

class SandboxOptionsParser:
    def __init__(self, mode: OptionsParsingMode, file: str, output: str, _logger: logging.Logger, argv: Namespace):
        self._log = _logger.getChild("Parser")
        self._output_file = output
        self._input_file = file
        self._mode = mode
        self._argv = argv

    def getVersion(self):
        if os.path.exists(self._input_file):
            self._log.info("Reading bin_sand data from file '%s'", self._input_file)
            file_data: bytes
            with open(self._input_file, "rb") as f:
                file_data = bytes(f.read())
            sb_data: ByteBuffer = ByteBuffer(file_data)
            #value == 83 && value2 == 65 && value3 == 78 && value4 == 68
            magic: bytes = b'SAND'
            magic_challenge = sb_data.get(4)
            if magic_challenge != magic: # Check if the first 4 bytes of the file == "SAND"
                _str = "The file specified does not appear to be a valid map_sand.bin file. Expected \"{}\", got \"{}\"".format(magic, magic_challenge) # pylint: disable=consider-using-f-string
                self._log.error(_str)
                raise InvalidBinFileError(_str)

            self._log.debug("File magic is valid")
            major_version: int = sb_data.getInt()
            minor_version: int = sb_data.getInt()

            self._log.info("World version is %i", major_version)
            self._log.info("map_sand.bin version is %i", minor_version)

    def dump(self):
        if self._mode != OptionsParsingMode.DUMP:
            self._log.error("Attempted to dump file when not in dump mode")
            raise RuntimeError("Attempted to dump file when not in dump mode")

        sandboxOptions: dict[str, Union[int, str, float, bool]] = {}

        if os.path.exists(self._input_file):
            self._log.info("Reading bin_sand data from file '%s'", self._input_file)
            file_data: bytes
            with open(self._input_file, "rb") as f:
                file_data = bytes(f.read())
            sb_data: ByteBuffer = ByteBuffer(file_data)
            #value == 83 && value2 == 65 && value3 == 78 && value4 == 68
            magic: bytes = b'SAND'
            magic_challenge = sb_data.get(4)
            if magic_challenge != magic: # Check if the first 4 bytes of the file == "SAND"
                _str = "The file specified does not appear to be a valid map_sand.bin file. Expected \"{}\", got \"{}\"".format(magic, magic_challenge) # pylint: disable=consider-using-f-string
                self._log.error(_str)
                raise InvalidBinFileError(_str)

            self._log.debug("File magic is valid")
            worldVersion: int = sb_data.getInt()
            if worldVersion >= 88:
                if worldVersion >= 131:
                    # There is an int here we need to skip over, if it's later needed unquote the second line and quote the first
                    sb_data.skip(4)
                    #int2: int = sb_data.getInt() # we need to read another int here to get the buffer in the right place
                    check3: int = sb_data.getInt()
                    for i in range(0, check3, 1):
                        if i > check3:
                            break
                        # Read string which I can't be arsed to do here
                        optionName: str = sb_data.readPZString()
                        optionValue: Union[str, int, bool, float] = self.getAsCorrectType(sb_data.readPZString())

                        sandboxOptions.update({optionName: optionValue})
            os.makedirs("./output", exist_ok=True)
            with open("./output/map_sand.json", "w", encoding="UTF-8") as f:
                json.dump(sandboxOptions, f, indent=4)
            self._log.info("Dump complete. Contents dumped to '/output/map_sand.json'. Make edits and then use --save to compile to something the game can use.")
            self._log.warning("PLEASE BACK UP YOUR EXISTING map_sand.bin FILE BEFORE APPLYING ONE CREATED BY THIS TOOL. IF YOU LOSE YOUR SAVE, IT'S NOT MY FAULT.")

        else:
            _str = f"Specified input file {self._input_file} doesn't exist!"
            self._log.error(_str)
            raise FileNotFoundError(_str)

    def getAsCorrectType(self, _input: Union[str, int, float, bool]) -> Union[str, int, float, bool]:
        if _input.lower() in ("true", "false"):
            return _input.lower() == "true"

        try:
            return int(_input)
        except: # pylint: disable=bare-except
            pass

        try:
            return float(_input)
        except: # pylint: disable=bare-except
            return str(_input)

    def save(self):
        if self._mode != OptionsParsingMode.SAVE:
            self._log.error("Attempted to save file when not in save mode")
            raise RuntimeError("Attempted to save file when not in save mode")

        if os.path.exists(self._input_file):
            jsonData: dict[str, Union[str, int, float, bool]]
            with open(self._input_file, "r", encoding="utf-8") as f:
                jsonData = json.load(f)

            byteBuffer = ByteBuffer(bytearray())
            # write the header
            byteBuffer.put(b'SAND') # File magic header
            byteBuffer.putInt(self._argv.forced_major_version) # world version
            byteBuffer.putInt(self._argv.forced_minor_version) # also a version identifier
            byteBuffer.putInt(len(jsonData))
            for k,v in jsonData.items():
                byteBuffer.writePZString(k)
                byteBuffer.writePZString(str(v).lower() if isinstance(v, bool) else str(v)) # Make sure to convert bools to lower-cased first letters, but not other strings

            with open(self._output_file, "wb") as f:
                f.write(byteBuffer.getbytes)

            self._log.info(f"Output saved to {self._output_file}. Copy to save directory to use, back up existing first.")
            self._log.warning("PLEASE BACK UP YOUR EXISTING map_sand.bin FILE BEFORE APPLYING ONE CREATED BY THIS TOOL. IF YOU LOSE YOUR SAVE, IT'S NOT MY FAULT.")

        else:
            _str = f"Specified input file {self._input_file} doesn't exist!"
            self._log.error(_str)
            raise FileNotFoundError(_str)
