from os.path import join
from conans import ConanFile, CMake


class NoniusPackageTest(ConanFile):
    settings = "compiler", "arch", "os"
    requires = "nonius/1.2.0-beta.1@demo/testing"
    generators = "cmake"

    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake {0} {1}'.format(self.conanfile_directory, cmake.command_line))
        self.run("cmake --build . {0}".format(cmake.build_config))

    def test(self):
        self.run(join(".", "bin", "test"))
