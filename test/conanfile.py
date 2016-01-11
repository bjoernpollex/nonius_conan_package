from os.path import join
from conans import ConanFile, CMake


class NoniusPackageTest(ConanFile):
    settings = "compiler", "arch", "os"
    requires = "nonius/1.1.2@demo/testing"
    generators = "cmake"

    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake . %s' % cmake.command_line)
        self.run("cmake --build . %s" % cmake.build_config)

    def test(self):
        self.run(join(".", "bin", "test"))
