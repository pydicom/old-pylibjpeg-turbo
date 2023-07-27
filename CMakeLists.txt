# Modeled after https://github.com/tttapa/py-build-cmake/issues/11
# except need ExternalProject

include(ExternalProject)


cmake_minimum_required(VERSION 3.3)
project(pylibjpeg_turbo)
find_package(Python3 REQUIRED COMPONENTS Development)

set(PROJECT_INSTALL_STEPS_FILE project_install_steps.cmake)
set(BUILD_SHARED_LIBS On)
set(LIB_INSTALL_DIR ${PY_BUILD_CMAKE_MODULE_NAME})


# Modeled on clang-format-wheel for some params here
# for install command from https://stackoverflow.com/questions/30205379/
ExternalProject_Add(libjpeg-turbo
    SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/extern/libjpeg-turbo
    BUILD_COMMAND ${CMAKE_COMMAND} --build . --target turbojpeg
    INSTALL_COMMAND ""
)

# Install the module
if (WIN32)
    install(TARGETS turbojpeg
            EXCLUDE_FROM_ALL
            RUNTIME DESTINATION ${PY_BUILD_CMAKE_MODULE_NAME}
            COMPONENT python_module)
else()
    install(TARGETS turbojpeg
            EXCLUDE_FROM_ALL
            LIBRARY DESTINATION ${PY_BUILD_CMAKE_MODULE_NAME}
            COMPONENT python_module)
endif()
