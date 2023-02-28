cmake_minimum_required(VERSION 3.24)
project(CPP)

set(CMAKE_CXX_STANDARD 17)

add_executable(CPP main.cpp utils/Searching.h utils/Searching.cpp utils/Utilities.h utils/Utilities.cpp utils/Sorting.h utils/Sorting.cpp utils/Graphs.h utils/Graphs.cpp)
