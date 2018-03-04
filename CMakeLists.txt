# cmake_minimum_required(VERSION 3.8)
# project(CMakeTP)

# set(CMAKE_CXX_STANDARD 14)

# add_subdirectory(A)
# add_subdirectory(B)
# include_directories(B)
# target_include_directories(B PUBLIC B/)

# set(MAIN_SOURCES C/main.cpp)

# add_executable(${PROJECT_NAME} ${MAIN_SOURCES})
# target_link_libraries(${PROJECT_NAME} B)


cmake_minimum_required(VERSION 3.8)
project(TP)

add_custom_target(run ALL COMMAND ${PYTHON_EXECUTABLE} ${PROJECT_SOURCE_DIR}/A/generating.py ${PROJECT_SOURCE_DIR} BYPRODUCTS index.h)
add_dependencies(index_generating run)
add_subdirectory(B)
add_subdirectory(C)