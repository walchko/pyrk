cmake_minimum_required(VERSION 3.25)
PROJECT(rk45 VERSION "2023.08.24.0")

include(FetchContent)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

if(PROJECT_IS_TOP_LEVEL)
    cmake_host_system_information(RESULT HOST QUERY HOSTNAME)
    # cmake_host_system_information(RESULT CORES QUERY NUMBER_OF_LOGICAL_CORES)
    cmake_host_system_information(RESULT OSN QUERY OS_NAME)
    cmake_host_system_information(RESULT OS_VERSION QUERY OS_RELEASE)
    cmake_host_system_information(RESULT PROC QUERY PROCESSOR_DESCRIPTION)

    message(STATUS "-------------------------------------")
    message(STATUS "  Project: ${PROJECT_NAME}")
    message(STATUS "  C++ ${CMAKE_CXX_STANDARD}")
    message(STATUS "-------------------------------------")
    message(STATUS " ${HOST}")
    message(STATUS " ${OSN}: ${OS_VERSION}")
    message(STATUS " ${PROC}")
    message(STATUS "-------------------------------------")

    set(BUILD_EXAMPLES ON)
    set(BUILD_GTESTS ON)

    # GTest -----------------
    FetchContent_Declare(gtest
        # GIT_REPOSITORY "https://github.com/google/googletest"
        # GIT_TAG "origin/main"
        URL https://github.com/google/googletest/archive/refs/tags/v1.14.0.zip
    )
    list(APPEND libs gtest)
else()
    message(STATUS "-> ${PROJECT_NAME} is submodule")
    set(BUILD_EXAMPLES OFF)
    set(BUILD_GTESTS OFF)
endif()

# if other fetched content, append them to libs too
# list(APPEND libs)

FetchContent_MakeAvailable( ${libs} )

add_library(${PROJECT_NAME} INTERFACE)
target_include_directories(${PROJECT_NAME} INTERFACE src/)
# target_link_libraries(${PROJECT_NAME} INTERFACE library1 library2 ... ) # don't add gtest here

# Examples -----------------------------------------------------------
message(STATUS "Building ${PROJECT_NAME} examples is ${BUILD_EXAMPLES}")
if(${BUILD_EXAMPLES})
    add_subdirectory(examples)
endif()

# Tests --------------------------------------------------------------
message(STATUS "Building ${PROJECT_NAME} gtests is ${BUILD_GTESTS}")
if(${BUILD_GTESTS})
    add_subdirectory(gtests)
endif()