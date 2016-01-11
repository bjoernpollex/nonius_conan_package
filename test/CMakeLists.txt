cmake_minimum_required(VERSION 2.8)
project(nonius_package_test)

include(conanbuildinfo.cmake)
conan_basic_setup()

add_executable(test test.cpp)
target_link_libraries(test ${CONAN_LIBS})
target_compile_options(test PRIVATE -std=c++11)
