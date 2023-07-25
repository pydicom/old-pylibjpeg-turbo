cmake_minimum_required(VERSION 3.4)

include(ExternalProject)

project(
    ${SKBUILD_PROJECT_NAME}
    VERSION ${SKBUILD_PROJECT_VERSION}
)


# Modeled on clang-format-wheel for some params here
ExternalProject_Add(libjpeg-turbo
    GIT_REPOSITORY https://github.com/libjpeg-turbo/libjpeg-turbo.git
    GIT_TAG 3.0.0
    GIT_SHALLOW
    # SOURCE_DIR ${CMAKE_BINARY_DIR}/libjpeg-turbo
    BINARY_DIR ${CMAKE_BINARY_DIR}/turbo
    UPDATE_COMMAND ""
    INSTALL_COMMAND ""
    USES_TERMINAL_DOWNLOAD 1
    USES_TERMINAL_CONFIGURE 1
    USES_TERMINAL_BUILD 1
    CMAKE_ARGS -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=OFF
    INSTALL_COMMAND ${CMAKE_COMMAND} --build . --target turbojpeg
)

install(
  TARGETS
    turbojpeg
  DESTINATION dist
)