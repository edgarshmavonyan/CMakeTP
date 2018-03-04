cmake_minimum_required(VERSION 3.8)
project(TP)

set(CMAKE_CXX_STANDARD 14)

find_package(PythonInterp 3.2 REQUIRED)

add_subdirectory(A)
add_subdirectory(B)

set(SOURCE_LIST C/main.cpp)

add_executable(${PROJECT_NAME} ${SOURCE_LIST})
add_dependencies(${PROJECT_NAME} python_script)

target_include_directories(${PROJECT_NAME} PUBLIC ${PROJECT_SOURCE_DIR})
target_link_libraries(${PROJECT_NAME} A B)
