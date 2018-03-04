cmake_minimum_required(VERSION 3.8)
project(B)

# set(CMAKE_CXX_STANDARD 14)

add_library(${PROJECT_NAME} INTERFACE)
# add_library(B ALIAS ${PROJECT_NAME})
# add_executable(B ${SOURCE_FILES})
target_include_directories(${PROJECT_NAME} INTERFACE ${PROJECT_SOURCE_DIR}/include)