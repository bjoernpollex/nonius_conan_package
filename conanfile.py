from os import unlink
from conans import ConanFile
from conans.tools import check_sha256, download, unzip


class Nonius(ConanFile):
    name = "nonius"
    version = "1.2.0-beta.1"
    url = "https://github.com/bjoernpollex/nonius_conan_package"
    license = "CC0 1.0"
    requires = "Boost/1.60.0@lasote/stable"
    settings = "compiler"

    def source(self):
        zipfile_name = "nonius-{0}.zip"
        release_url = "https://github.com/libnonius/nonius/releases/download/v{0}/nonius-{0}.zip".format(self.version)
        sha256 = "d7542740b438725409f43f49949c98093d7d655b36c13077be4a20007d0585c0"
        download(release_url, zipfile_name)
        check_sha256(zipfile_name, sha256)
        unzip(zipfile_name)
        unlink(zipfile_name)

    def config_options(self):
        if self.settings.compiler != "Visual Studio":
            self.options["Boost"].header_only = True
                
    def package(self):
        self.copy("nonius.h++", dst="include", src=".")

    def package_info(self):
        self.cpp_info.libdirs = []
        self.cpp_info.resdirs = []
