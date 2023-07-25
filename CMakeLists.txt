cmake_minimum_required(VERSION 3.4)

include(ExternalProject)

project(
    ${SKBUILD_PROJECT_NAME}
    VERSION ${SKBUILD_PROJECT_VERSION}
)


# Modeled on clang-format-wheel for some params here
ExternalProject_Add(libjpeg-turbo
    SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/extern/libjpeg-turbo
    PREFIX ${CMAKE_CURRENT_SOURCE_DIR}/extern/build
    CMAKE_ARGS -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=OFF
    BUILD_COMMAND ${CMAKE_COMMAND} --build . --target turbojpeg
    INSTALL_COMMAND ""
)

set(MYBUILD "${CMAKE_CURRENT_SOURCE_DIR}/extern/build/src/libjpeg-turbo-build/")
install(
  DIRECTORY ${MYBUILD}
  DESTINATION ${CMAKE_CURRENT_SOURCE_DIR}/build/lib
  FILES_MATCHING 
    PATTERN "libturbo*"
    PATTERN "CMakeFiles" EXCLUDE
    PATTERN "md5" EXCLUDE
    PATTERN "pkgscripts" EXCLUDE
    PATTERN "sharedlib"  EXCLUDE
    PATTERN "simd" EXCLUDE
 )
