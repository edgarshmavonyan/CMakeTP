cmake_minimum_required(VERSION 3.8)
project(A)

add_library(${PROJECT_NAME} INTERFACE)

find_package(PythonInterp 3.2 REQUIRED)

add_custom_target(python_script ALL DEPENDS index.h)

include_directories(${PROJECT_SOURCE_DIR})

add_custom_command(
	OUTPUT "index.h"
	COMMAND python3 generating.py
	COMMENT "generating index.h"
)