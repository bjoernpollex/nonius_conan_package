from os import unlink
from conans import ConanFile
from conans.tools import download, unzip


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
        download(release_url, zipfile_name)
        unzip(zipfile_name)
        unlink(zipfile_name)

    def config(self):
        if self.settings.compiler != "Visual Studio":
            self.options["Boost"].header_only = True
                
    def package(self):
        self.copy("nonius.h++", dst="include", src=".")

    def package_info(self):
        self.cpp_info.libdirs = []
        self.cpp_info.resdirs = []
