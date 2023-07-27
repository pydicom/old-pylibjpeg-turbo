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