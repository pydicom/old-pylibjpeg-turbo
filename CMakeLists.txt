cmake_minimum_required(VERSION 3.4...3.22)

include(ExternalProject)

project(
    ${SKBUILD_PROJECT_NAME}
    VERSION ${SKBUILD_PROJECT_VERSION}
)

set(BUILD_SHARED_LIBS "On")
set(CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS ON)

# Rpath from https://duerrenberger.dev/blog/2021/08/04/understanding-rpath-with-cmake/
# use, i.e. don't skip the full RPATH for the build tree
set(CMAKE_SKIP_BUILD_RPATH FALSE)
 
# when building, don't use the install RPATH already
# (but later on when installing)
set(CMAKE_BUILD_WITH_INSTALL_RPATH FALSE)
set(CMAKE_INSTALL_RPATH "${CMAKE_INSTALL_PREFIX}/lib")
 
# add the automatically determined parts of the RPATH
# which point to directories outside the build tree to the install RPATH
set(CMAKE_INSTALL_RPATH_USE_LINK_PATH TRUE)

find_program(MAKE_EXE NAMES gmake nmake make)
ExternalProject_Add(
    libjpeg-turbo
    GIT_REPOSITORY https://github.com/libjpeg-turbo/libjpeg-turbo.git
    GIT_TAG 3.0.0
    GIT_SHALLOW
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=turbo
    INSTALL_COMMAND ${CMAKE_COMMAND} --build . --target install
)
